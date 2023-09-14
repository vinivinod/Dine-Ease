# from django import forms
# from .models import hmenus,menus



# class MenuForm(forms.ModelForm):
#     class Meta:
#         model = menus
#         fields = ['name', 'desc', 'price', 'img']

        # widgets = {
        #     'name': forms.TextInput(attrs={"class": "form-control ",
        #         'placeholder': 'Enter Menu Name'
        #     }),
        #     'desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        #     'price': forms.TextInput(attrs={'class': 'form-control'}),
        #     'img': forms.FileInput(attrs={'class': 'form-control'}),
        # }

from django import forms
from .models import Reservation

class YourForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'phone', 'email', 'num_of_persons', 'table_id', 'reservation_date']