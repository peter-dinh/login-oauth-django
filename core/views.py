from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse, Http404, JsonResponse
import json
from datetime import datetime
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
def login(request):
    
    return render(request, 'login.html')
  
def register(request):
    return render(request, 'register.html')

# @login_required
def profile(request, **kw):
    profile = Profile.objects.filter(account=request.user)
    extra_data = request.user.social_auth.filter(provider='facebook')[0].extra_data
    if not profile.exists():
        profile = Profile.objects.create(
            name=request.user.first_name + ' ' + request.user.last_name,
            account=request.user,
            email=extra_data['email'],
        )
    activities = Activity.objects.filter(account=request.user).order_by('-date')
    return render(request, 'profile.html', {
        'profile': profile[0],
        'activities': activities,
    })

def update_profile(request, **kw):
    if request.method == 'POST':
        profiles = Profile.objects.filter(account=request.user)
        if profiles.exists():
            profile = profiles[0]
            log = 'Update Data<br /><br />'
            if profile.name != request.POST.get('inputName'):
                log += 'Name: %s  ->  %s<br />' % (profile.name, request.POST.get('inputName'))
                profile.name = request.POST.get('inputName')
            if profile.job != request.POST.get('inputJob'):
                log += 'Job: %s  ->  %s<br />' % (profile.job, request.POST.get('inputJob'))
                profile.job = request.POST.get('inputJob')
            if profile.location != request.POST.get('inputLocation'):
                log += 'Location: %s  ->  %s<br />' % (profile.location, request.POST.get('inputLocation'))
                profile.location = request.POST.get('inputLocation')
            if profile.education != request.POST.get('inputEducation'):
                log += 'Education: %s  ->  %s<br />' % (profile.education, request.POST.get('inputEducation'))
                profile.education = request.POST.get('inputEducation')
            if profile.skills != request.POST.get('inputSkills'):
                log += 'Skills: %s  ->  %s<br />' % (profile.skills, request.POST.get('inputSkills'))
                profile.skills = request.POST.get('inputSkills')
            if profile.experience != request.POST.get('inputExperience'):
                log += 'Experience: %s  ->  %s<br />' % (profile.experience, request.POST.get('inputExperience'))
                profile.experience = request.POST.get('inputExperience')

            profile.save()
            activity = Activity.objects.create(
                account=request.user,
                profile=profile,
                data=log,
                date=datetime.now()
            )
            data_response = activity.__dict__
            del data_response['_state']
            return  HttpResponse(json.dumps(data_response, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json")
        return Http404
    return Http404