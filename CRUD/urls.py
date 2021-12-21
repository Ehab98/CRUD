
from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home ,name='home'),
    path('add/',views.add_emp,name='add_emp'),
    path('delete/<int:id>', views.delete_emp,name='delete_emp'), 
    path('update/<int:id>', views.update_emp,name='update_emp'), 
]
