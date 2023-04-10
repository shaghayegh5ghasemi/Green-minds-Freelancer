from django.shortcuts import render


from jobs.models import Freelancer, Business

def home(request):
    if request.user.is_authenticated:
        if request.user.get_freelancer():
            f_id = request.user.get_freelancer().id
            freelancers = Freelancer.objects.all().exclude(id=f_id)[:3]
            businesses = Business.objects.all()[:3]
        elif request.user.get_business():
            b_id = request.user.get_business().id
            freelancers = Freelancer.objects.all()[:3]
            businesses = Business.objects.all().exclude(id=b_id)[:3]
        context = {
            'freelancers': freelancers,
            'businesses': businesses
        }
        return render(request, 'jobs/home.html', context)
    else:
        freelancers = Freelancer.objects.all()[:3]
        businesses = Business.objects.all()[:3]
        context = {
            'freelancers': freelancers,
            'businesses': businesses
        }
        return render(request, 'jobs/home.html', context)
