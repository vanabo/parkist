from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader

from .forms import Order

def index(request):

    call_back_data = {}
    call_back_data2 = {}
    order_data = {}

    if request.method == 'POST':
        current_point = request.POST.get('current_point')
        current_date = request.POST.get('current_date')
        current_time = request.POST.get('current_time')
        phone3 = request.POST.get('phone3')

        order_data.update({'current_point': current_point, 'current_date': current_date, 'current_time': current_time, 'phone3': phone3})
        send_mail(
            'Parkist Заказ',
            order_data,
            'vanabo@mail.ru',
            ['nv@alltargets.ru'],
            fail_silently=False,
        )
        return HttpResponseRedirect('/#order')

    context = {
        'call_back_data': call_back_data,
        'call_back_data2': call_back_data2,
        'order_data': order_data,
    }

    return render(request, 'main/index.html', context)