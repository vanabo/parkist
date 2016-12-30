from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.template import loader

from .forms import Order
from .forms import CallBack
from .forms import CallBack2

def index(request):
    form = Order(request.POST or None)

    success = {}

    if form.is_valid():
        form_current_point = form.cleaned_data.get('current_point')
        form_current_date = form.cleaned_data.get('current_date')
        form_current_time = form.cleaned_data.get('current_time')
        form_phone3 = form.cleaned_data.get('phone3')
        #print(form_current_point, form_current_date, form_current_time, form_phone3)
        subject = 'Parkist Заказ'
        from_email = settings.EMAIL_HOST_USER
        to_email = ['nv@alltargets.ru', 'vanabo@mail.ru']
        contact_message = '{0} {1} {2} {3}'.format(form_current_point, form_current_date, form_current_time, form_phone3)
        send_mail(
            subject,
            contact_message,
            from_email,
            to_email,
            fail_silently=True,
        )
        success = 'Ваша заявка успешно отправлена'
        return HttpResponseRedirect('/#order')

    form1 = CallBack(request.POST or None)

    if form1.is_valid():
        form1_name = form1.cleaned_data.get('name2')
        form1_phone = form.cleaned_data.get('phone2')
        subject2 = 'Parkist Обратный звонок'
        from_email = settings.EMAIL_HOST_USER
        to_email = ['nv@alltargets.ru', 'vanabo@mail.ru']
        contact_message2 = '{0} {1}'.format(form1_name, form1_phone)
        send_mail(
            subject2,
            contact_message2,
            from_email,
            to_email,
            fail_silently=True,
        )
        success = 'Ваша заявка успешно отправлена'
        return HttpResponseRedirect('/#callback')


    form2 = CallBack2(request.POST or None)

    if form2.is_valid():
        form2_name = form1.cleaned_data.get('name3')
        form2_phone = form.cleaned_data.get('phone3')
        subject3 = 'Parkist Обратный звонок'
        from_email = settings.EMAIL_HOST_USER
        to_email = ['nv@alltargets.ru', 'vanabo@mail.ru']
        contact_message3 = '{0} {1}'.format(form2_name, form2_phone)
        send_mail(
            subject3,
            contact_message3,
            from_email,
            to_email,
            fail_silently=True,
        )
        success = 'Ваша заявка успешно отправлена'
        return HttpResponseRedirect('/#home')

    context = {
        "form": form,
        "form1": form1,
        "form2": form2
    }

    return render(request, 'main/index.html', context)
