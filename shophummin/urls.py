from . import views
from django.urls import path

app_name = 'shophummin'


urlpatterns = [
    path('', views.index, name='index'),
    # path('checkout/', views.checkout, name='checkout'),
    path('product/<int:pk>/', views.product, name='product'),
    path('store/', views.store, name='store'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('aboutteam/', views.aboutteam, name='aboutteam'),
    path('to-bank/<int:order_id>/', views.to_bank, name='to_bank'),
    path('callback/', views.callback, name='callback'),
    path('ordercompletion/', views.ordercompletion, name='ordercompletion'),
    path('abouttelesk/', views.abouttelesk, name='abouttelesk'),
 ]