from django import forms
from django.forms import MultiValueField, CharField, ChoiceField, MultiWidget, TextInput, Select
from django.forms.extras.widgets import SelectDateWidget
from django.forms import widgets
from django.conf import settings
from django.template.defaultfilters import safe
import floppyforms
from floppyforms import gis


import datetime

d = datetime.date.today()
s = datetime.datetime.now()
tv1 = s.time
td = datetime.timedelta(minutes=30)
tv = s + td

td2 = datetime.timedelta(days=7)

date1 = d
date2 = d + td2
yy = d.year
dd = d.day
mm = d.month

class PhoneNumberInput(floppyforms.PhoneNumberInput):
    template_name = 'floppyforms/phonenumber.html'

class GMapPolygonWidget(floppyforms.gis.BaseGMapWidget, floppyforms.gis.PolygonWidget):

    class Media:
        js = (
            'floppyforms/openlayers/OpenLayers.js',
            'floppyforms/js/MapWidget.js',

            # Needs safe() because the ampersand (&):
            safe('http://maps.google.com/maps/api/js?'
                 'v=3&key=AIzaSyDLqdgdRPeKm-bfgXtaOQqQFsCH1FXHVPk'),
        )
        css = {
            'all': ('https://openlayers.org/en/v3.20.1/css/ol.css')
        }


class Order(floppyforms.Form):
    current_point = floppyforms.gis.PolygonField(widget=GMapPolygonWidget(attrs={}), required = False)
    current_date = floppyforms.DateField(label='Дата*', widget=SelectDateWidget(attrs={'class':'form-control-date'}), initial=d, required = True)
    current_time = floppyforms.TimeField(label='Время*', widget=floppyforms.TimeInput(attrs={'class':'form-control-time', 'size':'8'}), initial=tv, required = True)
    phone3 = floppyforms.CharField(label='Телефон*', widget=floppyforms.PhoneNumberInput(attrs={'class':'form-control', 'placeholder':'Введите номер телефона'}), required=True)

    def clean_current_time(self, *args, **kwargs):
        current_time = self.cleaned_data.get('current_time')
        if current_time < datetime.time(hour=9, minute=0, second=0, microsecond=0, tzinfo=None) or current_time > datetime.time(hour=21, minute=0, second=0, microsecond=0, tzinfo=None):
            raise forms.ValidationError('Введите, пожалуйста, требуемое время парковки в рабочие часы с 9:00 до 21:00')
        return current_time

    def clean_current_date(self, *args, **kwargs):
        current_date = self.cleaned_data.get('current_date')
        if current_date < d:
            raise forms.ValidationError('Введите, пожалуйста, дату сегодня или позднее')
        elif current_date.weekday() == 5:
            raise forms.ValidationError('Выберите, пожалуйста, будний день')
        elif current_date.weekday() == 6:
            raise forms.ValidationError('Выберите, пожалуйста, будний день')
        return current_date

    class Media:
        js = (
            'floppyforms/openlayers/OpenLayers.js',
            'floppyforms/js/MapWidget.js',

            # Needs safe() because the ampersand (&):
            safe('http://maps.google.com/maps/api/js?'
                 'v=3&key=AIzaSyDLqdgdRPeKm-bfgXtaOQqQFsCH1FXHVPk'),
        )
        css = {
            'all': ('https://openlayers.org/en/v3.20.1/css/ol.css')
        }

class CallBack2(forms.Form):
    name = forms.CharField(label='Ваше Имя', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ваше имя'}), max_length=100, required=False)
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите номер телефона'}), max_length=11, required = True)