from django.shortcuts import render
from django.views.generic import ListView
from jobs.models import Freelancer, Business



class FreelancerListViews(ListView):
    model = Freelancer

class BusinessListViews(ListView):
    model = Business


def view_business_profile(request, pk):
    business = Business.objects.get(id=pk)
    context = {
        'business': business,
    }

    return render(request, 'jobs/other_business_profile.html', context)

def view_freelancer_profile(request, pk):
    freelancer = Freelancer.objects.get(id=pk)
    context = {
        'freelancer': freelancer,
    }

    return render(request, 'jobs/other_freelancer_profile.html', context)

def search(request):
    searched_query = request.GET.get('searched_query')
    if searched_query:
        freelancers = Freelancer.objects.filter(name=searched_query)
        businesses = Business.objects.filter(name=searched_query)

        context = {
            'freelancers': freelancers,
            'businesses': businesses,
            'searched_query': searched_query,
        }
        return render(request, 'jobs/home.html', context)
    else:
        context = {}
        return render(request, 'jobs/home.html', context)

def freelancer_report(request, pk):
    freelancer = Freelancer.objects.get(id=pk)
    context = {
        'freelancer': freelancer,
        'user': request.user,
    }
    return render(request, 'jobs/freelancer_report.html', context)

def business_report(request, pk):
    business = Business.objects.get(id=pk)
    context = {
        'business': business,
        'user': request.user,
    }
    return render(request, 'jobs/business_report.html', context) # remember to change
