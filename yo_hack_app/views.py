import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import requests
from yo_hack.settings import YO_API
from yo_hack_app.forms import ProfileForm, ActionForm, CreateWordForm
from yo_hack_app.models import Family, Action, Profile


def index(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'profile.html')


def register(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password1"]
            form.save()
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect("index")
    else:
        form = ProfileForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

@login_required
def dashboard(request):
    wordForm = CreateWordForm(initial={
        'word1': request.user.word1,
        'word2': request.user.word2})

    familys = Family.objects.filter(me=request.user)

    action_collection = []
    for family in familys:
        received_hellos = Action.objects.filter(sender=family, action=0)
        received_helps = Action.objects.filter(sender=family, action=1)
        received_locations = Action.objects.filter(sender=family, action=2)
        action_collection.append([received_hellos, received_helps, received_locations])

    return render(request, 'dashboard.html', {
        'wordForm': wordForm,
        'familys': familys,
        'action_collection': action_collection
    })

@csrf_exempt
def hello(request):
    data = json.loads(request.body)
    users = data['name_list']
    action= Action.objects.create(
        text=data['text'],
        sender=request.user,
        action=0,
    )
    for user in users:
        action.receiver.add(Profile.objects.get(username=user))
        response = requests.post(
            YO_API,
            data={'api_token': request.user.api_token, 'username': user, 'link': request.META['HTTP_ORIGIN'] + '/hello/'+str(action.pk) })

    return HttpResponse(
                serializers.serialize('json', [action], indent=2,
                                      use_natural_foreign_keys=True,
                                      use_natural_primary_keys=True),
                content_type='application.json'
    )

@csrf_exempt
def emergency(request):
    data = json.loads(request.body)
    # latlon = str(data['userLat'])+";"+str(data['userLon'])
    users = data['name_list']
    action= Action.objects.create(
            sender=request.user,
            action=1,
            latitude = data['userLat'],
            longitude = data['userLon']
        )
    for user in users:
        action.receiver.add(Profile.objects.get(username=user))
        response = requests.post(
            YO_API,
            data={'api_token': request.user.api_token, 'username': user, 'link': request.META['HTTP_ORIGIN'] + '/emergency/'+str(action.pk) })

        # collection = {'response': response.status_code,
        #               'api': YO_API,
        #               'token': request.user.api_token,
        #               'link': request.META['HTTP_ORIGIN'] + '/emergency/'+str(action.pk),
        #               'receiver': receiver}
    # return HttpResponse(
    #             json.dumps(collection),
    #             content_type='application.json'
    # )
    return HttpResponse(
                serializers.serialize('json', [action], indent=2,
                                      use_natural_foreign_keys=True,
                                      use_natural_primary_keys=True),
                content_type='application.json'
    )

@csrf_exempt
def im_lost(request):
    data = json.loads(request.body)
    users = data['name_list']
    action= Action.objects.create(
            sender=request.user,
            action=2,
            latitude = data['userLat'],
            longitude = data['userLon']
        )
    for user in users:
        action.receiver.add(Profile.objects.get(username=user))
        response = requests.post(
            YO_API,
            data={'api_token': request.user.api_token, 'username': user, 'link': request.META['HTTP_ORIGIN'] + '/lost/'+str(action.pk) })

    return HttpResponse(
                serializers.serialize('json', [action], indent=2,
                                      use_natural_foreign_keys=True,
                                      use_natural_primary_keys=True),
                content_type='application.json'
    )

@csrf_exempt
def save_words(request):
    data = json.loads(request.body)
    user = request.user
    user.word1 = data['word1']
    user.word2 = data['word2']
    user.save()

    return JsonResponse({'success':'True'})



def emergency_url(request, emergency_id):
    emergency = Action.objects.get(pk=emergency_id)
    # data={}
    return render_to_response('emergency_url.html', {
        'emergency': emergency
    })


def lost_url(request, lost_id):
    lost = Action.objects.get(pk=lost_id)
    return render_to_response('lost_url.html', {
        'lost': lost
    })


def action(request):
    familys = Family.objects.filter(me=request.user)
    return render(request, 'action.html', {
        'familys': familys
    })


def hello_url(request, hello_id):
    hello = Action.objects.get(pk=hello_id)
    return render_to_response('hello_url.html', {
        'hello': hello
    })