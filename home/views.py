from django.shortcuts import render
from .models import Contact, Refunds, Tandcs, Home_image
from bag.models import Bag


def index(request):
    """ A view to return the index page """

    home_images = Home_image.objects.all()
    bags = Bag.objects.all()

    context = {
        'home_images': home_images,
        'bags': bags,
    }

    return render(request, 'home/index.html', context)


def contact(request):
    """ A view to return the contacts page """

    contacts = Contact.objects.all()

    context = {
        'contacts': contacts,
    }
    return render(request, 'home/contact.html', context)


def deliver(request):
    """ A view to return the delivery page """
    return render(request, 'home/deliver.html')


def manufacture(request):
    """ A view to return the manufacture page """
    return render(request, 'home/manufacture.html')


def payment(request):
    """ A view to return the payment page """
    return render(request, 'home/payment.html')


def refund(request):
    """ A view to return the returns and refunds page """

    refunds = Refunds.objects.all()

    context = {
        'refunds': refunds,
    }
    return render(request, 'home/refund.html', context)


def ring_sizes(request):
    """ A view to return the ring sizes page """
    return render(request, 'home/ring_sizes.html')


def ts_and_cs(request):
    """ A view to return the terms and conditions page """

    tsandcs = Tandcs.objects.all()

    context = {
        'tsandcs': tsandcs,
    }
    return render(request, 'home/ts_and_cs.html', context)
