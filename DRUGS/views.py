from django.shortcuts import render


def home(request):
    return render(request, 'DRUGS/pages/home.html', context={
        'drug': 'Dipirona 1g/2ml',
    })
