from django.urls import path
from profiles.views import UserCreateView,UserListView,UserDetailView,UserUpdateView,remove_user

urlpatterns=[
    path("register",UserCreateView.as_view(),name="add"),
    path("list",UserListView.as_view(),name="userlist"),
    path("user/<int:pk>",UserDetailView.as_view(),name="userdetail"),
    path("edit/<int:pk>",UserUpdateView.as_view(),name="edituser"),
    path("remove/<int:pk>",remove_user,name="userremove")
    
]