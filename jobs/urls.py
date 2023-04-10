from django.urls import path
from .views import home, handle_login, profile, FreelancerCreateView, BusinessCreateView, FreelancerDetailView, BusinessDetailView

urlpatterns = [
    path('', home),
    path('freelancer/<int:pk>/', FreelancerDetailView.as_view(), name='freelancer-detail'),
    path('business/<int:pk>/', BusinessDetailView.as_view(), name='business-detail'),
    path('freelancer/create/', FreelancerCreateView.as_view(), name='freelancer-create'),
    path('business/create/', BusinessCreateView.as_view(), name='business-create'),
    path('account/setup', handle_login, name='handle-login'),
    path('profile', profile, name='profile'),
]