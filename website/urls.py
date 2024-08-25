from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  # home page
    path('suggest/', views.suggest, name='suggest'),  # suggest page
    path('login/', views.login_user, name='login'),  # login page
    path('logout/', views.logout_user, name='logout'),  # logout page
    path('register/', views.register_user, name='register'),  # register page
    path('past', views.past, name='past'),  # past page
    path('delete_past/<Past_id>', views.delete_past,
         name='delete_past'),  # delete past page
]
