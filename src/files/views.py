from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TeacherFileForm
from .models import TeacherFile
from django.contrib import messages


@login_required
def upload_file(request):
    form = TeacherFileForm()
    if request.user.userprofile.account_type == 'teacher':
        if request.method == "POST":
            form = TeacherFileForm(request.POST, request.FILES)
            if form.is_valid():
                the_file = form.save(commit=False)
                the_file.user = request.user
                the_file.save()
                return redirect('account:profile', username=request.user.username)

            else:
                form = form()
    else:
        messages.info(request, 'only teachers can upload files')
        return redirect('account:profile', username=request.user.username)

    template_name = 'files/upload_file.html'
    context = {'form': form}

    return render(request, template_name, context)


def delete_file(request, name):
    context = {}
    template_name = 'files/delete_file.html'
    try:
        the_file = TeacherFile.objects.get(user=request.user, name=name)
        context['file'] = the_file

    except:
        messages.info(request, 'you don\t have file with this name')
        return redirect('account:profile', username=request.user.username)

    if request.method == "POST":
        the_file.delete()
        messages.info(request, 'deleted')
        return redirect('account:profile', username=request.user.username)

    return render(request, template_name, context)
