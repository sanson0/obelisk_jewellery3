from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def contact(request):
    return render(request, 'home/contact.html')


def deliver(request):
    return render(request, 'home/deliver.html')


def manufacture(request):
    return render(request, 'home/manufacture.html')


def payment(request):
    return render(request, 'home/payment.html')


def refund(request):
    return render(request, 'home/refund.html')


def ring_sizes(request):
    return render(request, 'home/ring_sizes.html')


def ts_and_cs(request):
    return render(request, 'home/ts_and_cs.html')