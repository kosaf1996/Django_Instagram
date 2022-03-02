from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .models import Feed

class Main(APIView):
    def get(self, request):
        # Feed 모든 데이터를 가져옴 -> select * from content_feed -> feed 를 최신부터 보여주기위해 order_by 사용
        feed_list = Feed.objects.all().order_by('-id')

        for feed in feed_list:
            pass
        return render(request, "instagram/main.html", context=dict(feed=feed_list))

    def post(self, request):
        return render(request, "instagram/main.html")