from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import UserLoginForm,UserPasswordChangeForm,UserPasswordResetForm,UserSetPasswordForm

urlpatterns = [
    path('', views.ProductView.as_view() , name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view() , name='product-detail'),

    path('products/', views.all_products, name='product'),
    path('products/<slug:data>', views.all_products, name='productdata'),
    path('dietrecommandation/', views.diet_recommandation, name='dietrecommandation'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='nutranta/login.html',authentication_form=UserLoginForm) , name='login'),
    path('register/', views.User_Registration_view.as_view(), name='register'),
    path('logout/', auth_view.LogoutView.as_view(next_page='home'), name='logout'),
    ############################# End Account Login ###################################
    ############################# Change Password #####################################
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='nutranta/passwordchange.html',form_class=UserPasswordChangeForm,success_url='/passwordchangedone/'), name='password-change'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='nutranta/passwordchangedone.html'), name='password-change-done'),
    ############################# End Change Password ################################
    ############################# Reset Password #####################################

    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='nutranta/password_reset.html',html_email_template_name='nutranta/password_reset_email.html',form_class=UserPasswordResetForm), name='password-reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='nutranta/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='nutranta/password_reset_confirm.html',form_class=UserSetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='nutranta/password_reset_complete.html'), name='password_reset_complete'),
    ############################# End Reset Password #################################
    ############################# Contact Us ########################################
    path('contactus/', views.ContactUS.as_view(), name='contactus'),
    ############################# End Contact Us ####################################
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    # path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    # path('login/', views.login, name='login'),
    # path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)