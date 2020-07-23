from . import views as acc_views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name="accounts"

urlpatterns=[
	path('login/',acc_views.User_Login.as_view(template_name="accounts/login.html"),name="login"),
	path('logout/',auth_views.LogoutView.as_view(template_name="accounts/logout.html"),name="logout"),
	path('register/',acc_views.register,name="register"),
	path('<slug:username>/delete/',acc_views.delete_acc,name='delete_acc'),
]
