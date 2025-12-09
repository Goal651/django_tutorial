from django.urls import path
from recorder import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("update_record", views.update_record, name="Update Record"),
    path("create_record", views.create_record, name="create record"),
    path("view_records", views.view_records, name="view records"),
]
