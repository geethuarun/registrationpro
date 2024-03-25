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
            "qualification":forms.Textarea(attrs={"class":"form-control","rows":3}),
            "job":forms.Select(attrs={"class":"form-select"}),
            "address":forms.Select(attrs={"class":"form-select"}),
            "age":forms.Select(attrs={"class":"form-select"}),
            "gender":forms.Select(attrs={"class":"form-select"})}



        