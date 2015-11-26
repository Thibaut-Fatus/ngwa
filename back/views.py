from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def angular_app(request):
    return render(request, 'base.html')

