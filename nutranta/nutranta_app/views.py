from django.shortcuts import render,redirect
from django.views import View
from .models import Product , Cart , OrderPlaced , Address , Customer , Contact
from .api_call import dailycalorie, get_diet_plan
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.contrib import messages
from .forms import UserRegisterForm,Contact_Us,ProfileForm
from django.http import HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.
class ProductView(View):
 def get(self, request):
  all_Products = Product.objects.all()
  print(all_Products.count())
  return render(request, 'nutranta/home.html' , {'all_Products' : all_Products})


class ProductDetailView(View):
  def get(self, request, pk):
    product = Product.objects.get(pk=pk)
    item_already_in_cart = False
    if request.user.is_authenticated:
        item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
    return render(request, 'nutranta/productdetail.html' , {'product' : product, 'item_already_in_cart': item_already_in_cart})


def all_products(request,data=None):
 if data == None:
  all_Products = Product.objects.all()
 elif data == 'Fruits':
    all_Products = Product.objects.filter(category='f')
 elif data == 'Vegetables':
  all_Products = Product.objects.filter(category='v')
 elif data == 'Dairy':
  all_Products = Product.objects.filter(category='d')
 elif data == 'Fish':
  all_Products = Product.objects.filter(category='fi')
 else:
    all_Products = Product.objects.all()
 return render(request, 'nutranta/products.html', {'all_Products' : all_Products})


def diet_recommandation(request):
 if request.method == 'POST':
      weight = int(request.POST['weight'])
      height = int(request.POST['height'])
      age = request.POST['age']
      gender = request.POST['gender']
      activity = request.POST['activity']
      plan = request.POST['plan']
      print("weight: ",weight)
      print("height: ",height)
      print("age: ",age)
      print("gender",gender)
      print("activity: ",activity)
      print("plan: ",plan)

      # Calculate BMI
      bmi = calculate_bmi(weight, height)
      bmi = round(bmi, 2)
      interpretation = interpret_bmi(bmi)
      result_dict = {'bmi': bmi, 'interpretation': interpretation}
      # call api
      main_tain, mild_weight_loss_week, mild_weight_loss_cal, weight_loss_week, weight_loss_cal, extream_calory, extream_loss_weight = dailycalorie(age, gender, height, weight, activity)

      title_summary,  breakfast_title, lunch_title, dinner_title = get_diet_plan(plan)
      brakfast_title_summary = title_summary[0]
      lunch_title_summary = title_summary[1]
      dinner_title_summary = title_summary[2]
      context = {
        'result': result_dict,
        'main_tain': main_tain,
        'mild_weight_loss_week': mild_weight_loss_week,
        'mild_weight_loss_cal': mild_weight_loss_cal,
        'weight_loss_week': weight_loss_week,
        'weight_loss_cal': weight_loss_cal,
        'extream_calory': extream_calory,
        'extream_loss_weight': extream_loss_weight,
        'breakfast_title': breakfast_title,
        'lunch_title': lunch_title,
        'dinner_title': dinner_title,
        'brakfast_title_summary': brakfast_title_summary,
        'lunch_title_summary': lunch_title_summary,
        'dinner_title_summary': dinner_title_summary,

      }

      return render(request, 'nutranta/dietrecommandation.html', context)
 return render(request, 'nutranta/dietrecommandation.html')


class User_Registration_view(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'nutranta/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created succassfuly {username}!')
            return redirect('login')
        else:
            return render(request, 'nutranta/register.html', {'form': form})


def AboutUS(request):
    return render(request, 'nutranta/about.html')

class ContactUS(View):
    def get(self, request):
        form = Contact_Us()
        return render(request, 'nutranta/contact.html', {'form': form})

    def post(self, request):
        form = Contact_Us(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            customer = Contact(name=name, email=email, phone=phone, message=message)
            customer.save()
            sender_email = 'musadiqzahid815@gmail.com'
            recipient_email = email
            message = 'Thank you for contacting us. We will get back to you soon. Nutranta Team'

            send_mail('Subject', message, sender_email, [recipient_email])
            return render(request, 'nutranta/success.html')
        else:
            return render(request, 'nutranta/contact.html', {'form': form})
        
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = ProfileForm()

        return render(request, 'nutranta/profile.html', {'form': form, 'active': 'btn-primary'})
    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user, name=name, email=email, mobile=mobile, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, f'Profile Updated Succassfuly!')
        return render(request, 'nutranta/profile.html', {'form': form, 'active': 'btn-primary'}) 
    


@login_required
def add_to_cart(request):
    user = request.user
    product_id_str = request.GET.get('product_id')
    try:
        # Extract the numeric part from the string
        product_id = int(product_id_str.split()[0])
    except (ValueError, IndexError):
        return HttpResponseBadRequest("Invalid product_id")

    try:
        product = Product.objects.get(id=product_id)
    except ObjectDoesNotExist:
        return HttpResponseBadRequest("Product does not exist")

    Cart(user=user, product=product).save()
    return redirect('showcart')

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart_count = Cart.objects.filter(user=user).count()
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 120.0
        total_cal = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        print(cart_product)

        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.selling_price)
                cal = (p.quantity * p.product.total_calroes)
                total_cal += cal
                amount += tempamount
            totalamount = amount + shipping_amount
            return render(request, 'nutranta/addtocart.html', {'carts': cart, 'totalamount': totalamount, 'amount': amount, 'cal': total_cal, 'cart_count': cart_count})
        else:
            totalamount = 0.0
            return render(request, 'nutranta/emptycart.html', {'totalamount': totalamount})
        
def cartcount(request):
    cart_count = Cart.objects.filter(user=request.user).count()
    return render(request, 'nutranta/base.html', {'cart_count': cart_count})
         
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        print(c)
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 120.0
        total_cal = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        print(cart_product)

        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.selling_price)
                cal = (p.quantity * p.product.total_calroes)
                total_cal += cal
                amount += tempamount

            data = {
                'quantity': c.quantity,
                'amount': amount,
                'cal': total_cal,
                'totalamount': amount + shipping_amount
            }
            return JsonResponse(data)
        else:
            totalamount = 0.0
            data = {
                'quantity': c.quantity,
                'amount': amount,
                'cal': total_cal,
                'totalamount': amount + shipping_amount
            }
            return JsonResponse(data)
        
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        print(c)
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 120.0
        total_cal = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        print(cart_product)

        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.selling_price)
                cal = (p.quantity * p.product.total_calroes)
                total_cal += cal
                amount += tempamount

            data = {
                'quantity': c.quantity,
                'amount': amount,
                'cal': total_cal,
                'totalamount': amount + shipping_amount
            }
            return JsonResponse(data)
        else:
            totalamount = 0.0
            data = {
                'quantity': c.quantity,
                'amount': amount,
                'cal': total_cal,
                'totalamount': amount + shipping_amount
            }
            return JsonResponse(data)

# remove item from cart
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        print(c)
        c.delete()
        amount = 0.0
        shipping_amount = 120.0
        total_cal = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        print(cart_product)

        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.selling_price)
                cal = (p.quantity * p.product.total_calroes)
                total_cal += cal
                amount += tempamount

            data = {
                'amount': amount,
                'cal': total_cal,
                'totalamount': amount + shipping_amount
            }
            return JsonResponse(data)
        else:
            totalamount = 0.0
            data = {
                'amount': amount,
                'cal': total_cal,
                'totalamount': amount + shipping_amount
            }
            return JsonResponse(data)
      

def buy_now(request):
 return render(request, 'nutranta/buynow.html')

@login_required
def address(request):
 add = Customer.objects.filter(user=request.user)
 return render(request, 'nutranta/address.html', {'add': add, 'active': 'btn-primary'})

@login_required
def orders(request):
 op = OrderPlaced.objects.filter(user=request.user)
 return render(request, 'nutranta/orders.html', {'order_placed': op})

@login_required
def checkout(request):
    # check out Cart
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 120.0
    total_cal = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    print(cart_product)
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            cal = (p.quantity * p.product.total_calroes)
            total_cal += cal
            amount += tempamount
        totalamount = amount + shipping_amount
        return render(request, 'nutranta/checkout.html', {'add': add, 'totalamount': totalamount, 'cart_items': cart_items, 'amount': amount, 'cal': total_cal})

    else:
        return redirect('showcart')
 
# payment done
@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer , product=c.product, total_cost = c.product.selling_price,  quantity=c.quantity, total_calroes=c.product.total_calroes).save()
        c.delete()
    return redirect("orders")


def calculate_bmi(weight, height):
    height = height / 100
    # Calculate BMI
    bmi = weight / (height ** 2)

    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"