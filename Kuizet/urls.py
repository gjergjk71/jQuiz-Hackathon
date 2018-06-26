
from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views



urlpatterns = [
	path("",views.redirectToHome,name="redirectToHome"),
	path("logout/",auth_views.logout,name="logout"),
	path("signup/",views.signup,name="signup"),
	path('home/', views.home,name='home'),
	path('quiz/<ID>',views.quiz,name="quiz"),
	path("result/<ID>",views.result,name="result"),
]
