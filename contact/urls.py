from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    # path('agenda/', views.agenda, name='agenda'),

    # contact (CRUD)
    path('contact/<int:contact_id>/', views.contact, name='contact'),
]
