from django.shortcuts import render, redirect
from django.conf import settings
from django.db.models import Count
from django.views.decorators.http import require_http_methods
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import Http404, HttpResponseRedirect, HttpResponse, JsonResponse
from .models import *
from accounts.models import User
import decimal
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.utils.text import slugify
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

@csrf_exempt
@require_http_methods(["GET", "POST"])
def add_mycvs(request):
    user = request.user  
    postedPlace=json.loads(request.POST.get("place",""))
    place_name=postedPlace['place_name']
    postedCvs=CVS.objects.filter(name=place_name)
    if(len(postedCvs)!=0): #try except로 바꿀 예정
        postedCvs=CVS.objects.get(name=place_name)
        postedCvs.user.add(user)
    else:
        mycvs=CVS()
        mycvs.name=place_name
        mycvs.slug=slugify(place_name, allow_unicode=True)
        mycvs.latitude=postedPlace['x']
        mycvs.longitude=postedPlace['y']
        mycvs.brand, mycvs.brand_logo=find_brand(place_name)
        mycvs.save()
        mycvs.user.add(user)
    message = "좋아요"
    context = {'message': message }
    return HttpResponse(json.dumps(context), content_type="application/json")  

def find_brand( name):
    if "이마트24" in name:
        return "이마트24", "brand/이마트24.jpg"
    elif "CU" in name:
        return "CU", "brand/씨유.jpg"
    elif "세븐일레븐" in name:
        return "세븐일레븐", "brand/세븐일레븐.jpg"
    elif "스토리웨이" in name:
        return "스토리웨이", "brand/스토리웨이.jpg"
    elif "GS25" in name:
        return "GS25", "brand/GS25.jpg"
    elif "미니스톱" in name:
        return "미니스톱", "brand/미니스톱.jpg"
    elif "IGA" in name:
        return "IGA", "brand/IGA.jpg"
    elif "로그인" in name:
        return "로그인", "brand/로그인.jpg"
    elif "씨스페이스" in name:
        return "씨스페이스", "brand/씨스페이스.jpg" 
    else :
        return "기타"  

@csrf_exempt
@require_http_methods(["GET", "POST"])
def delete_mycvs(request):
    user = request.user  
    postedPlace=json.loads(request.POST.get("place",""))
    postedCvs=CVS.objects.get(name=postedPlace)
    postedCvs.user.remove(user)
    if (postedCvs.user.count()==0):
        postedCvs.delete()
    message = "좋아요 취소"
    context = {'message': message }
    return HttpResponse(json.dumps(context), content_type="application/json")  