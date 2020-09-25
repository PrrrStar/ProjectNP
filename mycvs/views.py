from django.shortcuts import render
from django.conf import settings

# Create your views here.
def mymap(request):

    KAKAO_MAP_API_KEY = getattr(settings, 'KAKAO_MAP_API_KEY', 'KAKAO_MAP_API_KEY')
    print(KAKAO_MAP_API_KEY)
    context = {
        'KAKAO_MAP_API_KEY':KAKAO_MAP_API_KEY
    }
    return render(request, 'mycvs/mymap.html', context)

