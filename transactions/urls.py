from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("transactions/", views.transactions, name="transactions"),
    path("transaction/<int:pk>/update/", views.update_transaction, name="update-transaction"),
    path("transaction/<int:pk>/delete/", views.delete_transaction, name="delete-transaction"),
]