from django.urls import path
from .views import home, view_business_profile, view_freelancer_profile, search, freelancer_report, business_report, FreelancerListViews, BusinessListViews

urlpatterns = [
    path('', home),
    path('freelancers/', FreelancerListViews.as_view(), name='freelancers-list'),
    path('business/', BusinessListViews.as_view(), name='business-list'),
    path('business/<int:pk>', view_business_profile, name='view-business-profile'),
    path('freelancer/<int:pk>', view_freelancer_profile, name='view-freelancer-profile'),
    path('search-results/', search, name='search-results'),
    path('freelancer-report/<int:pk>', freelancer_report, name='freelancer-report'),
    path('business-report/<int:pk>', business_report, name='business-report'),
]
