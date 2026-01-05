from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('mentorship/', views.mentorship_list, name='mentorship_list'),
    path('mentorship/create/', views.mentorship_create, name='mentorship_create'),
    path('mentorship/edit/<int:pk>/', views.mentorship_edit, name='mentorship_edit'),
    path('mentorship/disable/<int:pk>/', views.mentorship_disable, name='mentorship_disable'),
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('products/disable/<int:pk>/', views.product_disable, name='product_disable'),
    path('about/', views.about_edit, name='about_edit'),
    path('settings/', views.settings_edit, name='settings_edit'),
]
