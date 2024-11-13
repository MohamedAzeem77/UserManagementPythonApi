from django.urls import path
from . import views

urlpatterns=[
    path('add/', views.create_user, name='create_user'),
    path('update/<int:user_id>/', views.update_user, name='update_user'),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('all/', views.get_users, name='get_users'),
    path('get/<int:user_id>/', views.get_user_by_id, name='get_user_by_id'),
]