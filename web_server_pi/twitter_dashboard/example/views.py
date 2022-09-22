from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Order


class Example():

    def order(*args):
        print(args)
        orders = Order.objects.all()

        for order in orders:
            temp = order.customer
        return HttpResponse(temp)

def order(*args):
    orders = Order.objects.all()

    for order in orders:
        temp = order.customer

    return HttpResponse(temp)