from django.shortcuts import render



def settings(request):
    return render(request, 'dashboard/settings.html', {})