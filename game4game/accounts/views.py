from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreateForm, UserProfileInfoForm
from django.contrib import messages


def signup(request):

    registered = False

    if request.method == 'POST':
        user_form = UserCreateForm(request.POST, request.FILES)
        profile_form = UserProfileInfoForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            messages.warning(self.request, f"{user_form.errors}, {profile_form.errors}")

    else:
        user_form = UserCreateForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'accounts/signup.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})
