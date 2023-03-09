from django.shortcuts import render
from .models import Profile

def home(request):
    return render(request, 'greenMinds/index.html')

def logIn(request):
    return render(request, 'greenMinds/login.html')

def signUp(request):
    return render(request, 'greenMinds/signup.html')

def profile(request):
    return render(request, 'greenMinds/profile.html')

def about(request):
    return render(request, 'greenMinds/AboutUs.html')

def browseJobs(request):
    return render(request, 'greenMinds/BrowseJobs.html')

def employer(request):
    return render(request, 'greenMinds/employer.html')

def freelancer(request):
    context = {
        'profile': Profile.objects.first()
    }
    return render(request, 'greenMinds/freelancer.html', context)

def update_freelancer(request, id):
  context = {
    'profile': Profile.objects.first()
  }
  return render(request, 'greenMinds/freelancer.html', context)

def howItWorks(request):
    return render(request, 'greenMinds/howItWorks.html')

def reportFreelancer(request):
    return render(request, 'greenMinds/customer_report_page.html')

def reportEmoloyer(request):
    return render(request, 'greenMinds/provider_report_page.html')







    