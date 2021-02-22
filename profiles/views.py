from django.shortcuts import render


def profile(request):
    # View for users profile
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
