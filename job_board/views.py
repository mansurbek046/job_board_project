from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import unauthenticated_user

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Job, Company
from django.contrib.auth.models import User
from .forms import UserRegistrationForm



def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data["username"]
            # email = form.cleaned_data["email"]
            # password = form.cleaned_data["password"]
            # user = User.objects.create_user(email=email, password=password, username=username)
            # Redirect to a success page or any other desired page
            return redirect("home")
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("home")

class homePageView(TemplateView):
    template_name='base.html'

class jobListView(ListView):
    model=Job
    template_name='job_list.html'

class jobDetailView(DetailView):
    model=Job
    template_name='job_detail.html'

class jobCreateView(CreateView):
    model=Job
    fields=['jobTitle','jobDescription','jobCompany','jobSalary','jobWorkTime','jobType','jobSkills']
    template_name='job_form.html'
    success_url=reverse_lazy('job-list')
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['jobCompany'].queryset = Company.objects.filter(created_by=self.request.user)
        return form

class jobUpdateView(UpdateView):
    model=Job
    fields=['jobTitle','jobDescription','jobCompany','jobSalary','jobWorkTime','jobType','jobSkills']
    template_name='job_form.html'
    success_url=reverse_lazy('job-list')
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class jobDeleteView(DeleteView):
    model=Job
    success_url=reverse_lazy('job-list')
    template_name='job_delete_confirm.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class companyCreateView(CreateView):
    model=Company
    fields=['companyName','companyDescription','companyIndustry','companyLocation']
    template_name='company_form.html'
    success_url=reverse_lazy("company-list")
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class companyUpdateView(UpdateView):
    model=Company
    fields=['companyName','companyDescription','companyIndustry','companyLocation']
    template_name='company_form.html'
    success_url=reverse_lazy("company-list")
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class companyDeleteView(DeleteView):
    model=Company
    success_url=reverse_lazy('company-list')
    template_name='company_delete_confirm.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    

class companyListView(ListView):
    model=Company
    template_name='company_list.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)



