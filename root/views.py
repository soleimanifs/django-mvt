from django.shortcuts import render
from .models import Special,Services,Trainers,Price,Questions


def home(requests):
    service = Services.objects.filter(statue = True)
    specials = Special.objects.filter(statue=True)
    questionss = Questions.objects.filter(statue = True)
    prices = Price.objects.filter(statue=True)
    trainer = Trainers.objects.filter(status=True)
    context = {
        'trainer': trainer,
        'prices' :prices,
        'service' : service ,
        'specials' : specials,
        'questionss':questionss,
    }
    return render(requests,'root/index.html', context=context)