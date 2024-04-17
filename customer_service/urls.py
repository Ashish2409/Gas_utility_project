from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_request_list, name='service_request_list'),
    path('request/<int:id>/', views.service_request_detail, name='service_request_detail'),
    path('create/', views.create_service_request, name='create_service_request'), 
    path('<int:id>/change-status/', views.change_status, name='change_status'),   
]
