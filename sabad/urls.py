from . import views
from django.urls import path

app_name = 'sabad'


urlpatterns = [
    path('', views.sabad_detail, name='sabad_detail'),
    path('add/<int:product_id>/', views.sabad_add, name='sabad_add'),
    path('remove/<int:product_id>/', views.sabad_remove, name='sabad_remove'),
 ]
