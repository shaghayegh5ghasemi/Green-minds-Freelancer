from django.shortcuts import render

def home(request):
    return render(request, 'profile/home_profile.html')

def report(request):
    return render(request, 'profile/report.html', {'title': '- Report'})
    