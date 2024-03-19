from django.urls import path
from . import views



urlpatterns = [
    path("", views.getAccountsRoutes.as_view(), name="accounts-routes"),
    path("register/", views.RegisterView.as_view(), name="user-register"),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path("current/",views.UserView.as_view(), name="user-current"),
    
]


