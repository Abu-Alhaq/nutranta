from django.shortcuts import render
from django.views import View
from .models import Product , Cart , OrderPlaced , Address , Customer

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
      weight = request.POST['weight']
      height = request.POST['height']
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
      return render(request, 'nutranta/dietrecommandation.html')
 return render(request, 'nutranta/dietrecommandation.html')


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

def change_password(request):
 return render(request, 'nutranta/changepassword.html')

def mobile(request):
 return render(request, 'nutranta/mobile.html')

def login(request):
 return render(request, 'nutranta/login.html')

def customerregistration(request):
 return render(request, 'nutranta/customerregistration.html')

def checkout(request):
 return render(request, 'nutranta/checkout.html')
