from django.urls import path
from home import views

urlpatterns = [
    path('', views.home_page , name = 'home_page'),
    path('submit_and_process_data', views.submit_and_process_data , name = 'submit_and_process_data'),
   
]
