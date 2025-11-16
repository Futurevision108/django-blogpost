from django.urls import path
from .import views

urlpatterns = [
<<<<<<< HEAD
    path('', home_page_view),
=======
    path('', views.PostList.as_view(), name='home'),
>>>>>>> workingbranch
]
