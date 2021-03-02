from django.shortcuts import render
from ecoverdeapp.models import Announcement, View, Status, District, Region, Type
from django.contrib.auth.models import User
import json
from django.core import serializers
from PIL import Image
from django.core.files.storage import FileSystemStorage


def personal(request, username):
    announcements = Announcement.objects.filter(author=username)
    user = User.objects.filter(username=username)
    return render(request, 'personal_area.html', {'announcements': announcements, 'user': user})


def add(request, username):

    regions = Region.objects.all()
    json_serializer = serializers.get_serializer("json")()
    districts = json_serializer.serialize(District.objects.all(), ensure_ascii=False)
    statuses = Status.objects.all()
    types = Type.objects.all()
    views = View.objects.all()

    
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        region_id = request.POST['region_id']
        district_id = request.POST['district_id']
        address = request.POST['address']
        type_id = request.POST['type_id']
        view_id = request.POST['view_id']
        status_id = request.POST['status_id']
        price = request.POST['price']
        features = request.POST['features']
        image = request.FILES.getlist('image')
        phone = request.POST.get('phone', '')

        announcement = Announcement(
            title=title,
            content=content,
            region_id=region_id,
            district_id=district_id,
            address=address,
            type_id=type_id,
            view_id=view_id,
            status_id=status_id,
            price=price,
            features=features,
            image=image,
            phone=phone,
            author=username
        )
        announcement.save()
    return render(request, 'add.html',
    {
        'regions': regions,
        'districts': districts,
        'statuses': statuses,
        'types': types,
        'views': views
    })

