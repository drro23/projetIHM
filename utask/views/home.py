from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from utask.models import Profile
from django.http import JsonResponse
from django.http import HttpResponse
import json


class HomeView(TemplateView):
    template_name = 'page/home.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            profile = Profile.objects.get(user_id=user.id)
            data = json.dumps(profile.skills)
            a = json.loads(data)
            return render(request, self.template_name, {'profile': profile, 'data': a})
        else:
            return redirect('/accounts/login/')
