from django.urls import path
from app_crud import views

urlpatterns = [
    path("", views.home, name='home'),
    path("create/", views.create, name="create"),
    path("store", views.store, name='store product'),
    path('edit/<int:pk>', views.edit, name="edit"),
    path("store-edit/<int:pk>", views.store_edit, name='store_edit'),
    path("delete/<int:pk>", views.delete, name="delete")
]
