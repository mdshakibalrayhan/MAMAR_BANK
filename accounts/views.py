from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import UserregistrationForm,UserUpdateForm
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.views import View

# Create your views here.


class UserRegistrationView(FormView):
    template_name = 'accounts/user_registraion.html'
    success_url = reverse_lazy('home')
    form_class = UserregistrationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        print(form.cleaned_data)
        return super().form_valid(form)
    

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    



class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        """Handle logout via GET request."""
        if request.user.is_authenticated:
            logout(request)  # Log the user out
        return redirect(reverse_lazy('home')) 



class UserBankAccountUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})
