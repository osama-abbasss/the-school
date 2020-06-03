from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm, ProfileFrom, EditProfileForm
from .models import EmailConfirm, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from files.models import TeacherFile


def signup(request):
    form = SignUpForm()

    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)

            if form.is_valid():
                form.save()
                username = request.POST['username']
                password = request.POST['password1']
                new_user = authenticate(username=username, password=password,)
                login(request, new_user)
                return redirect("account:create_profile")
            else:
                messages.info(request, 'sorry something wrong Plz try again')
    context = {"form": form}
    template_name = 'registration/signup.html'
    return render(request, template_name, context)


@login_required
def create_profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = ProfileFrom(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account:profile', username=request.user.username)
        else:
            messages.info(request, 'sorry something wrong Plz try again')

    else:
        form = ProfileFrom()

    context = {"form": form}
    template_name = 'accounts/profile_form.html'
    return render(request, template_name, context)


@login_required
def edit_profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account:profile', username=request.user.username)
        else:
            messages.info(request, 'sorry something wrong Plz try again')

    else:
        form = EditProfileForm(instance=profile)

    context = {"form": form}
    template_name = 'accounts/edit_profile_form.html'
    return render(request, template_name, context)


@login_required
def profile_view(request, username):
    try:
        user = User.objects.get(username=username)
        profile = UserProfile.objects.get(user=user)
        files = TeacherFile.objects.filter(user=user)

    except:
        messages.info(request, 'not found Try again')
        return redirect("/")

    template_name = 'accounts/profile.html'
    context = {'profile': profile,
               'user': user,
               'files': files}

    return render(request, template_name, context)


def account_activated(request, code):
    print(code)
    print(request.user)
    try:
        email_confirm = EmailConfirm.objects.get(user=request.user, code=code)
        if email_confirm:
            email_confirm.confirmed = True
            email_confirm.save()
            messages.success(request, 'activated')
        return redirect("/")
    except:
        messages.warning(request, 'wrong url try again')
        return redirect("/")
