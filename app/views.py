from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from . import models
from .models import Profile, User_uuid, Rom
from .forms import ProfileForm, UserForm, User_uuidForm, Device_name_Form
from django.db.models import Count, Max, Min, Avg




#------------------------------------------------------------------------------
@login_required(login_url="/login/")
def index(request):
    uuid = models.User_uuid.objects.filter(user=request.user).values('UUID')
    devices = models.Rom.objects.filter(UUID__in=uuid, family_id='01')

    context = {'devices':devices}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))




#------------------------------------------------------------------------------

@login_required(login_url="/login/")
def profile(request):
    uuid = models.User_uuid.objects.filter(user=request.user).values('UUID')
    devices = models.Rom.objects.filter(UUID__in=uuid, family_id='01')

    profile = models.Profile.objects.filter(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            username = user_form.cleaned_data['username']
            first_name = user_form.cleaned_data['first_name']
            last_name = user_form.cleaned_data['last_name']
            email = user_form.cleaned_data['email']
            password1 = user_form.cleaned_data['password1']
            password2 = user_form.cleaned_data['password2']
            phone = profile_form.cleaned_data['phone']
            address = profile_form.cleaned_data['address']
            user_photo = profile_form.cleaned_data['user_photo']
            user_form.save()
            profile_form.save()
            context = {'user_form':user_form, 'profile_form':profile_form, 'devices':devices}
            context['segment'] = 'profile'

            html_template = loader.get_template( 'accounts/profile.html' )
            return HttpResponse(html_template.render(context, request))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {'user_form':user_form, 'profile_form':profile_form, 'devices':devices}
    context['segment'] = 'profile'

    html_template = loader.get_template( 'accounts/profile.html' )
    return HttpResponse(html_template.render(context, request))





#------------------------------------------------------------------------------

@login_required(login_url="/login/")
def nodes(request):
    uuid = models.User_uuid.objects.filter(user=request.user).values('UUID')
    devices = models.Rom.objects.filter(UUID__in=uuid, family_id='01')
    device_name_Form = Device_name_Form(request.POST)
    user_uuid_Form = User_uuidForm(request.POST, instance=request.user)

    if request.method == 'POST':

        if device_name_Form.is_valid():
            uuid = device_name_Form.cleaned_data['Device_UUID']
            obj = get_object_or_404(models.Rom, UUID=uuid, family_id='01')
            obj.name = device_name_Form.cleaned_data['Device_name']
            obj.save()
            context = {'user_uuid_Form': user_uuid_Form, 'devices':devices, 'device_name_Form':device_name_Form}
            return render(request, 'nodes.html', context)

        if user_uuid_Form.is_valid():
            obj = User_uuid()
            obj.UUID = user_uuid_Form.cleaned_data['UUID']
            obj.user = user_uuid_Form.created_by=request.user
            obj.save()
            context = {'user_uuid_Form': user_uuid_Form, 'devices':devices, 'device_name_Form':device_name_Form}
            return render(request, 'nodes.html', context)
    else:
        user_uuid_Form = User_uuidForm(request.POST)

    context = {'user_uuid_Form':user_uuid_Form, 'devices':devices, 'device_name_Form':device_name_Form}
    context['segment'] = 'nodes'
    html_template = loader.get_template( 'nodes.html' )
    return HttpResponse(html_template.render(context, request))




@login_required(login_url="/login/")
def nodes_detail(request, id):
    uuid = models.User_uuid.objects.filter(user=request.user).values('UUID')
    devices = models.Rom.objects.filter(UUID__in=uuid, family_id='01')

    node = get_object_or_404(models.Rom, id=id)
    sensors = models.Rom.objects.filter(node_id=node.node_id)
    sensors_uuid = models.Rom.objects.filter(node_id=node.node_id).values('UUID')

    temp12 = models.Temp12.objects.filter(UUID__in=sensors_uuid)

    temp_uuid = models.Temp12.objects.filter(UUID__in=sensors_uuid).values('UUID').distinct()
    temp_just_uuid=list(temp_uuid.values_list('UUID', flat=True))

    i = 0
    last_temp = []
    while i < len(temp_just_uuid):
        Temp12_value = models.Temp12.objects.filter(UUID=temp_just_uuid[i]).values('UUID', 'temp').latest('created_on')
        last_temp.append(Temp12_value)
        i+=1




    ss = [
        { 'UUID':'FC412F2B2CBB', 'last_temp':'45', 'max_temp':'60', 'min_temp':'34', 'avg_temp':'48' },
        { 'UUID':'FC412F2B2CBB', 'last_temp':'45', 'max_temp':'60', 'min_temp':'34', 'avg_temp':'48' }
    ]





    #max = models.Temp12.objects.filter(UUID=temp_just_uuid[0]).aggregate(Max('temp'))
    #min = models.Temp12.objects.filter(UUID=temp_just_uuid[0]).aggregate(Min('temp'))
    #avg = models.Temp12.objects.filter(UUID=temp_just_uuid[0]).aggregate(Avg('temp'))
    #print(max)
    #print(min)
    #print(avg)



    context = {
    'devices':devices,
    'node':node,
    'sensors':sensors,
    'temp12':temp12,
    'last_temp':last_temp,
    'ss':ss
    }
    context['segment'] = 'nodes_detail'
    html_template = loader.get_template( 'nodes_detail.html' )
    return HttpResponse(html_template.render(context, request))

#------------------------------------------------------------------------------




@login_required(login_url="/login/")
def sensors(request):
    uuid = models.User_uuid.objects.filter(user=request.user).values('UUID')
    devices = models.Rom.objects.filter(UUID__in=uuid, family_id='01')

    device_node_id = models.Rom.objects.filter(UUID__in=uuid, family_id='01').values('node_id')
    sensor_temp = models.Temp12.objects.filter(UUID__in=device_node_id)

    context = {'devices':devices, 'sensor_temp':sensor_temp}
    context['segment'] = 'sensors'
    html_template = loader.get_template( 'sensors.html' )
    return HttpResponse(html_template.render(context, request))









# End
