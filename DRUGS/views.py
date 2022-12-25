from django.shortcuts import render

from utils.DRUGS.factory import make_recipe


def home(request):
    return render(request, 'DRUGS/pages/home.html', context={
        'drugs': [make_recipe() for _ in range(10)],
    })


def drugs(request, id):
    return render(request, 'DRUGS/pages/guide-view.html', context={
        'drug': make_recipe(),
        'detail_page': True,
    })
