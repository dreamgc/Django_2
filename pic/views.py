import os
import re
from urllib.request import urlopen

import MySQLdb
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from pic.models import Infor, Type
# Create your views here.


def get_pic(request):
    picture_all = {}

    response = {
        "data": picture_all
    }

    if request.method == "GET":
        pic_types = Type.objects.all()
        for pic_type in pic_types:
            picture_all[pic_type.type] = []
            pics_infor = Infor.objects.filter(type=pic_type.type).values()
            for pic_infor in pics_infor:
                # pic_infor["url"] = "http://10.10.0.192:1523/static/pic/images/%s/%s" % (pic_infor["type"], pic_infor["url"])
                pic_infor["url"] = "http://www.vicgee.top:1523/static/pic/images/%s/%s" % (pic_infor["type"], pic_infor["url"])
                picture_all[pic_type.type].append(pic_infor)
        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})


def add_pic(request):
    # local_public_ip = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", requests.get('http://myip.ipip.net', timeout=5).text)[0]

    if request.META.get("REMOTE_ADDR") == "10.10.0.192":
        pic_path = "pic/static/pic/images"
        for i in os.listdir(pic_path):
            Type.objects.get_or_create(type=i)

            for j in os.listdir(pic_path + "/" + i):
                Infor.objects.get_or_create(name=j.split(".")[0], type=i, url=j)

        return HttpResponse("添加成功")
    else:
        print("拒绝访问: %s" % request.META.get("REMOTE_ADDR"))
        return HttpResponse("拒绝访问")



