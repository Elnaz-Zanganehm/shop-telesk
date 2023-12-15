from . import views
from django.urls import path

app_name = 'shophummin'


urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/', views.index, name='checkout'),
    path('product/', views.index, name='product'),
    path('store/', views.index, name='store'),
    path('login/', views.user_login, name='login'),
    path('login/', views.user_logout, name='logout')

 ]