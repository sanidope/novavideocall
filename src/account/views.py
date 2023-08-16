from . models import Profile
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from . forms import UserRegistrationForm, RegistrationForm2


class Register(FormView):
    template_name = 'account/signup.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy("account:signup2")

    def form_valid(self, form):
        self.request.session['user_data'] = self.request.POST
        return super().form_valid(form)


class Register2(FormView):
    custom_text_value = str()
    form_class = RegistrationForm2
    template_name = 'account/signup2.html'
    success_url = reverse_lazy("account:signup_completed")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email'] = self.request.session['user_data'].get('email')
        context['account_type'] = self.request.session['user_data'].get('account_type')
        context['form'] = self.get_form()
        context['custom_text_value'] = self.custom_text_value
        return context


    def form_valid(self, form):
        email = self.request.session['user_data'].get('email')
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = User.objects.create_user(username, email, password)
        user.first_name = self.request.session['user_data'].get('first_name')
        user.last_name = self.request.session['user_data'].get('last_name')
        user.is_active = True
        user.save()
        return super().form_valid(form)
       # self.init_email_activation(email)
       # self.send_activation_mail()


class  SignUpCompleted(TemplateView):
    template_name = 'account/signup_completed.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email'] = self.request.session['user_data'].get('email')
        return context


@login_required
def dashboard(request):
    profile = get_object_or_404(Profile, user=request.user)

    if profile.account_type == 'supervisor':
        return render(request, 'core/supervisor_admin_dashboard.html', {
            'profile' : profile
        })

    else:
        return render(request, 'core/cadet_admin_dashboard.html', {
            'profile' : profile
        })


@login_required
def settings(request):
    user = User.objects.get(username=request.user.username)
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        print(request.POST)
        if 'general' in request.POST:
            user_form = UserModelForm(instance=user, data=request.POST)
            if user_form.is_bound and user_form.is_valid():
                user_form.save()
                messages.success(request, "Successfully Updated")
                return HttpResponseRedirect("/dashboard/settings/")
            
            else:
                messages.error(request, user_form.errors)


        if 'authentication' in request.POST:
            update_password_form = UpdatePasswordForm(request.POST) 
            
            if update_password_form.is_bound and update_password_form.is_valid():
                current_password = update_password_form.cleaned_data.get("current_password")
                if user.check_password(current_password):
                    password = update_password_form.cleaned_data.get("password")
                    user.set_password(password)
                    user.save()
                    messages.success(request, 'Your password was successfully updated!')
                    return HttpResponseRedirect("/dashboard/settings/")
                else:
                    messages.error(request, "Your current password is incorrect!")
        
            else:
                messages.error(request, update_password_form.errors)


        if 'supplementary' in request.POST:
            settings_form = SettingModelForm(instance=profile, data=request.POST)
            
            if settings_form.is_bound and settings_form.is_valid():
                settings_form.save()
                messages.success(request, "Successfully Updated")
                return HttpResponseRedirect("/dashboard/settings/")
            
            else:
                messages.error(request, settings_form.errors)

        
        if 'profilepic' in request.POST:
            profilepic_form = ProfilePicForm(instance=profile, files=request.FILES)
            
            if profilepic_form.is_bound and profilepic_form.is_valid():
                profilepic_form.save()
                messages.success(request, "Profile Pictured Successfully Updated")
                return HttpResponseRedirect("/dashboard/settings/")
            
            else:
                messages.error(request, profilepic_form.errors)
        
        
    user_form = UserModelForm(instance=user)
    profile_pic_form = ProfilePicForm(instance=profile)
    settings_form = SettingModelForm(instance=profile)
    update_password_form = UpdatePasswordForm()

    return render(request, 'core/settings.html', {
        'profile': profile,
        'user_form' : user_form,
        'profile_pic_form' : profile_pic_form,
        'settings_form' : settings_form,
        'update_password_form' : update_password_form
    })


