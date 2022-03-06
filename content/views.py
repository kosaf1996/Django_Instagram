import os
from uuid import uuid4

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from instagram.settings import MEDIA_ROOT
from user.models import User
from .models import Feed


class Main(APIView):
    def get(self, request):
        # Feed 모든 데이터를 가져옴 -> select * from content_feed -> feed 를 최신부터 보여주기위해 order_by 사용
        feed_list = Feed.objects.all().order_by('-id')

        #TODO 세션을 활용해 로그인한 사용자 데이터 받기
        email = request.session['email']

        #TODO 세션에 이메일이 존재하지않을떄
        if email is None:
            render(request,"user/login.html")

        user = User.objects.filter(email=email).first()

        #TODO 이메일 주소가 회원이 아닐떄
        if user is None:
            render(request, "user/login.html")


        return render(request, "instagram/main.html", context=dict(feed=feed_list, user=user))


class UploadFeed(APIView):
    def post(self, request):

        #파일 저장 기능
        file = request.FILES['file']
        uuid_name = uuid4().hex #이미지가 특수문자등 난해 할수 있어 uuid 로 생성된 이름 사용
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        #main.html의 AJAX 로 부터 데이터 받기
        image = uuid_name
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.get('profile_image')

        Feed.objects.create(image=image,content=content,user_id=user_id,profile_image=profile_image,like_count=0)

        return Response(status=200)

class Profile(APIView):
    def get(self, request):
        #TODO 세션을 활용해 로그인한 사용자 데이터 받기
        email = request.session['email']

        #TODO 세션에 이메일이 존재하지않을떄
        if email is None:
            render(request,"user/login.html")

        user = User.objects.filter(email=email).first()

        #TODO 이메일 주소가 회원이 아닐떄
        if user is None:
            render(request, "user/login.html")

        return render(request, 'content/profile.html', context=dict(user=user))