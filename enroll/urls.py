from django.urls import path
from enroll import views


# URL patterns

urlpatterns = [
    
    path('', views.UserAddShowView.as_view(), name='addandshow'),
    
    path('delete/<int:id>/', views.UserDeleteView.as_view(), name="deletedata"),
    
    path('<int:id>/', views.UserUpdateView.as_view(), name="updatedata"),
     
]
