from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Group, GroupMember
from .forms import GroupForm
from posts.models import Post
from posts.forms import PostForm, CommentForm


@login_required
def create_group(request):
    if request.user.userprofile.account_type == 'teacher':
        if request.method == "POST":
            form = GroupForm(request.POST)
            if form.is_valid():
                try:
                    group = form.save(commit=False)
                    group.auther = request.user
                    group.save()
                    member = GroupMember.objects.create(
                        user=request.user, group=group)
                    member.save()
                    group.members.set = member
                    group.save()

                    return redirect('groups:group_details', group.slug)
                except:
                    messages.info(request, 'name is aready used')
                    return redirect("groups:create_group")

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

    # create posts and comments in group
    else:
        if request.method == 'POST':
            post_like = request.POST.get('post_like')
            post_dislike = request.POST.get('post_dislike')

            post_form = PostForm(request.POST)
            post_content = request.POST.get('content')

            comment_form = CommentForm(request.POST)

            try:
                # the post which come with comment form
                post_id = request.POST.get('post_id')
                the_comment = request.POST.get('comment')
                the_post = Post.objects.get(id=post_id)

            except:
                pass

            # create post
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.user = request.user
                post.group = group
                post.content = post_content
                post.save()

                return redirect('groups:group_details', group.slug)

            # create comment

            elif comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = the_post
                comment.user = request.user
                comment.comment = the_comment
                comment.save()

            # like post

            elif post_like:
                post = get_object_or_404(Post, id=post_like)
                post.likes.add(request.user)

            # dislike post
            elif post_dislike:
                post = get_object_or_404(Post, id=post_dislike)
                post.likes.remove(request.user)

    posts = Post.objects.filter(group=group).order_by('-created_at')

    post_form = PostForm()
    template_name = 'groups/group_details.html'
    context = {
        'group': group,
        'post_form': post_form,
        'posts': posts
    }

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


def join_group(request, slug):
    try:
        group = Group.objects.get(slug=slug)

    except:
        messages.warning(request, 'group not found')
        return redirect('account:profile', request.user.username)

    if request.user not in group.members.all():

        member = GroupMember.objects.create(user=request.user, group=group)
        member.save()
        group.members.set = member
        group.save()
        return redirect('groups:group_details', group.slug)
    else:
        messages.warning(request, 'you already in this group')
        return redirect('groups:group_details', group.slug)


def leave_group(request, slug):
    try:
        group = Group.objects.get(slug=slug)

    except:
        messages.warning(request, 'group not found')
        return redirect('account:profile', request.user.username)

    if request.user in group.members.all():
        member = GroupMember.objects.get(user=request.user, group=group)
        member.delete()
        messages.success(request, 'leaved')
        return redirect('account:profile', request.user.username)
    else:
        messages.warning(request, 'you already not in this group')
        return redirect('account:profile', request.user.username)


def remove_member(request, slug, username):
    try:
        group = Group.objects.get(slug=slug)
        user = User.objects.get(username=username)

    except:
        messages.warning(request, 'group not found')
        return redirect('account:profile', request.user.username)

    if group.auther == request.user and user in group.members.all():
        member = GroupMember.objects.get(user=user, group=group)
        member.delete()
        messages.success(request, 'removed')
        return redirect('groups:group_details', group.slug)

    else:
        messages.success(request, 'can\'t remove')
        return redirect('groups:group_details', group.slug)
