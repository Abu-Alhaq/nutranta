from django.shortcuts import render,redirect
from django.views import View
from .models import Product , Cart , OrderPlaced , Address , Customer , Contact
from .api_call import dailycalorie, get_diet_plan
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from .forms import UserRegisterForm,Contact_Us,ProfileForm

# Create your views here.
class ProductView(View):
 def get(self, request):
  all_Products = Product.objects.all()
  print(all_Products.count())
  return render(request, 'nutranta/home.html' , {'all_Products' : all_Products})


class ProductDetailView(View):
  def get(self, request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'nutranta/productdetail.html' , {'product' : product})


def all_products(request,data=None):
 if data == None:
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
      print("title_summary: ",title_summary)
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

# @login_required
# def Profile(request):
#     return render(request, 'nutranta/profile.html')


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
    

def add_to_cart(request):
 return render(request, 'nutranta//addtocart.html')

def buy_now(request):
 return render(request, 'nutranta/buynow.html')

def profile(request):
 return render(request, 'nutranta/profile.html')

def address(request):
 return render(request, 'nutranta/address.html')

def orders(request):
 return render(request, 'nutranta/orders.html')

# def change_password(request):
#  return render(request, 'nutranta/changepassword.html')

def mobile(request):
 return render(request, 'nutranta/mobile.html')

# def login(request):
#  return render(request, 'nutranta/login.html')

# def customerregistration(request):
#  return render(request, 'nutranta/customerregistration.html')

def checkout(request):
 return render(request, 'nutranta/checkout.html')



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