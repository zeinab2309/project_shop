from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import ShopUser


class ShopUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=ShopUser
        fields = ('phone','first_name','last_name','address','is_active','is_staff','is_superuser')

    def clean_phone(self):
        phone=self.cleaned_data.get('phone')
        if self.instance.pk:
            if ShopUser.objects.filter(phone=phone).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('Phone already exist')
        else:
            if ShopUser.objects.filter(phone=phone).exists():
                raise forms.ValidationError('Phone already exist')
        if not phone.isdigit():
            raise forms.ValidationError('phone must be numbers')
        if not phone.startswith('09'):
            raise forms.ValidationError('phone must start whit 09 digits')
        if len(phone)!=11:
            raise forms.ValidationError('Phone must have 11 digit.')
        return phone


class ShopUserChangeForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=ShopUser
        fields = ('phone','first_name','last_name','address','is_active','is_staff','is_superuser')

    def clean_phone(self):
        phone=self.cleaned_data.get('phone')
        if self.instance.pk:
            if ShopUser.objects.filter(phone=phone).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('Phone already exist')
        else:
            if ShopUser.objects.filter(phone=phone).exists():
                raise forms.ValidationError('Phone already exist')
        if not phone.isdigit():
            raise forms.ValidationError('phone must be numbers')
        if not phone.startswith('09'):
            raise forms.ValidationError('phone must start whit 09 digits')
        if len(phone)!=11:
            raise forms.ValidationError('Phone must have 11 digit.')
        return phone
