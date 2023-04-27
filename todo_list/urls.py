from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('delete/<item_id>', views.delete, name='delete'),
    path('Pending/<item_id>', views.Pending, name='Pending'),
    path('Done/<item_id>', views.Done, name='Done'),
    path('edit/<item_id>', views.edit, name='edit'),
]
