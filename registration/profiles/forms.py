from django import forms
from profiles.models import Users


class UserCreateForm(forms.ModelForm):
    class Meta:
        model=Users
        fields="__all__"

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "phone":forms.TextInput(attrs={"class":"form-control"}),
            "qualification":forms.TextInput(attrs={"class":"form-control"}),
            "job":forms.TextInput(attrs={"class":"form-control"}),
            "address":forms.Textarea(attrs={"class":"form-control","rows":3}),
            "age":forms.TextInput(attrs={"class":"form-control"}),
            "gender":forms.Select(attrs={"class":"form-select"})}



        