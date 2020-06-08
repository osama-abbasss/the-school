from django.shortcuts import render
from groups.models import Group
from django.db.models import Q
from accounts.models import UserProfile
from django.contrib.auth.models import User


def search(request):

    if request.method == 'POST':
        q = request.POST.get('q')

        groups = Group.objects.filter(
            Q(auther__username__icontains=q) |
            Q(name__icontains=q) |
            Q(description__icontains=q))

        users = User.objects.filter(
            Q(username__icontains=q) |
            Q(first_name__icontains=q) |
            Q(last_name__icontains=q) |
            Q(email__icontains=q)
        )
        profiles = UserProfile.objects.filter(
            Q(city__icontains=q) |
            Q(address__icontains=q) |
            Q(Mobail__icontains=q) |
            Q(subject__icontains=q) |
            Q(description__icontains=q) |
            Q(school_name__icontains=q) |
            Q(year__icontains=q)
        )

    template_name = 'searches/search_results.html'

    context = {
        'groups': groups,
        'users': users,
        'profiles': profiles,
        'q': q
    }

    return render(request, template_name, context)
