from django.shortcuts import render,redirect
from profiles.models import Users
from profiles.forms import UserCreateForm

from django.views.generic import View,CreateView,ListView,DetailView,UpdateView
from django.urls import reverse_lazy



class UserCreateView(CreateView):
    
    template_name="register.html"
    form_class=UserCreateForm
    model=Users
    success_url=reverse_lazy("userlist")

class UserListView(ListView):
    template_name="list.html"
    context_object_name="users"
    model=Users
    def get_queryset(self):
        qs=Users.objects.all().order_by('name')
        return qs
    

class UserDetailView(DetailView):
    template_name="userdetail.html"
    context_object_name="user"
    model=Users


class UserUpdateView(UpdateView):
    template_name="userupdate.html"
    form_class=UserCreateForm
    model=Users
    success_url=reverse_lazy("listuser")

def remove_user(request,*args,**kwargs):
    id=kwargs.get("pk")
    Users.objects.filter(id=id).delete()
    return redirect("listuser")


    
