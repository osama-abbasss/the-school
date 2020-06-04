from django.shortcuts import render, redirect, get_object_or_404
from .models import Group, GroupMember
from .forms import GroupForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def create_group(request):
    if request.user.userprofile.account_type == 'teacher':
        if request.method == "POST":
            form = GroupForm(request.POST)
            if form.is_valid():
                group = form.save(commit=False)
                group.auther = request.user
                group.save()
                member = GroupMember.objects.create(
                    user=request.user, group=group)
                member.save()
                group.members.set = member
                group.save()
                return redirect('groups:group_details', group.slug)
        else:
            form = GroupForm()

    else:
        messages.info(request, 'only teacher\'s can create groups')
        return redirect("/")

    template_name = 'groups/group_form.html'
    context = {'form': form}

    return render(request, template_name, context)


@login_required
def group_details(request, slug):
    group = get_object_or_404(Group, slug=slug)
    if request.user not in group.members.all():
        messages.warning(request, 'the group private for members only')
        return redirect('/')
    template_name = 'groups/group_details.html'
    context = {'group': group}

    return render(request, template_name, context)


@login_required
def delete_group(request, slug):
    try:
        group = Group.objects.get(auther=request.user, slug=slug)
    except:
        messages.warning(request, 'you don\'t have any groups with this name')
        return redirect('/')

    if request.method == "POST":
        group.delete()
        messages.warning(request, 'deleted')
        return redirect('account:profile', request.user.username)

    template_name = 'groups/group_delete.html'
    context = {'group': group}

    return render(request, template_name, context)
