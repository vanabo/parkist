from django import forms
from django.forms import MultiValueField, CharField, ChoiceField, MultiWidget, TextInput, Select
from django.forms.extras.widgets import SelectDateWidget

import datetime

d = datetime.date.today()
s = datetime.datetime.now()
tv1 = s.time
td = datetime.timedelta(minutes=30)
tv = s + td

class Order(forms.Form):
    current_point = forms.CharField(label='Укажите адрес*', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите адрес Вашего местоположения'}), max_length=100, required = True)
    current_date = forms.DateField(label='Дата*', widget=SelectDateWidget(attrs={'class':'form-control-date'}), initial=d, required = True)
    current_time = forms.TimeField(label='Время*', widget=forms.TimeInput(attrs={'class':'form-control-time', 'size':'8'}), initial=tv, required = True)
    phone3 = forms.CharField(label='Телефон*', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите номер телефона'}), required=True)

class CallBack(forms.Form):
    name2 = forms.CharField(label='Ваше Имя', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ваше имя'}), max_length=100, required=False)
    phone2 = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите номер телефона'}), max_length=11, required = True)

class CallBack2(forms.Form):
    name = forms.CharField(label='Ваше Имя', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ваше имя'}), max_length=100, required=False)
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите номер телефона'}), max_length=11, required = True)
