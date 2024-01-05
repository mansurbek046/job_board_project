from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', homePageView.as_view(), name="home"),
    path('register', register_user, name="register"),
    path('login', auth_views.LoginView.as_view(), name="login"),
    path('logout', logout_view, name="logout"),
    path('job/list', jobListView.as_view(), name="job-list"),
    path('job/list/<int:pk>', jobDetailView.as_view(), name="job-detail"),
    path('job/create', jobCreateView.as_view(), name="job-create"),
    path('job/list/<int:pk>/update', jobUpdateView.as_view(), name="job-update"),
    path('job/list/<int:pk>/delete', jobDeleteView.as_view(), name="job-delete"),
    path('company/create', companyCreateView.as_view(), name="company-create"),
    path('company/list', companyListView.as_view(), name="company-list"),
    path('company/list/<int:pk>/update', companyUpdateView.as_view(), name="company-update"),
    path('company/list/<int:pk>/delete', companyDeleteView.as_view(), name="company-delete"),
]
