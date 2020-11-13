from django.shortcuts import render, redirect
from django.conf import settings
from django.db.models import Count
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import Http404, HttpResponseRedirect, HttpResponse, JsonResponse
from .models import *
from accounts.models import User
import decimal
from django.core import serializers
# Create your views here.
def mymap(request):

    KAKAO_MAP_API_KEY = getattr(settings, 'KAKAO_MAP_API_KEY', 'KAKAO_MAP_API_KEY')
    print(KAKAO_MAP_API_KEY)
    user=request.user
    if not user.is_authenticated:
        return redirect('/') 
    else : 
        mycvses=CVS.objects.filter(user=user)
        mycvs=json.dumps([mycvs.to_json for mycvs in mycvses],ensure_ascii=False, cls=DjangoJSONEncoder)
    print(mycvs)
    context = {
        'KAKAO_MAP_API_KEY':KAKAO_MAP_API_KEY,
        'mycvs':mycvs,
        #'mycvses_js':json.dumps([mycvs.json() for mycvs in mycvses], cls=DjangoJSONEncoder),
    }

    return render(request, 'mycvs/location.html', context)

# def myCvs_create(request):
#     user = request.user
#     if request.method =='POST':
#         asdf=CVS()
#         asdf.user=user
#         asdf.longitude=y
#         asdf.latitude=x
#         asdf.name=name
#         asdf.brand, asdf.brand_logo=find_brand(name)
#         asdf.save()
#         return redirect('location.html')
#     def find_name(name):
#         if "이마트24" in name:
#             return "이마트24", "media/brand/이마트24.jpg"
#         elif "CU" in name:
#             return "CU", "media/brand/씨유.jpg"
#         elif "세븐일레븐" in name:
#             return "세븐일레븐", "media/brand/세븐일레븐.jpg"
#         elif "스토리웨이" in name:
#             return "스토리웨이", "media/brand/스토리웨이.jpg"
#         elif "GS25" in name:
#             return "GS25", "media/brand/GS25.jpg"
#         elif "미니스톱" in name:
#             return "미니스톱", "media/brand/미니스톱.jpg"
#         elif "IGA" in name:
#             return "IGA", "media/brand/IGA.jpg"
#         elif "로그인" in name:
#             return "로그인", "media/brand/로그인.jpg"
#         elif "씨스페이스" in name:
#             return "씨스페이스", "media/brand/씨스페이스.jpg" 
#         else :
#             return "기타"            
