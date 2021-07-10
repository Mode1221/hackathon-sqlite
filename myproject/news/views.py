from django.shortcuts import render
import json
import urllib.request
from mypage.models import Mypage

# Create your views here.
def search(request):
    if request.method == 'GET':
        client_id = "vmpZnAFJTefT7w29tjHw"
        client_secret = "RyVRnKCQ3B"

        q = request.GET.get('Mypage.keyword')
        encText = urllib.parse.quote("{}".format(q))
        url = "https://openapi.naver.com/v1/search/news.json?query=marketing&display=4&start=1&sort=sim"
        news_api_request = urllib.request.Request(url)
        news_api_request.add_header("X-Naver-Client-Id", client_id)
        news_api_request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(news_api_request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')
            print(result)

            context = {
                'items': items
            }
            return render(request, 'news.html', context=context)