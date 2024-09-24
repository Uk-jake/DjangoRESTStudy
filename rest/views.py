from django.shortcuts import render # 템플릿 엔진을 이용해서 HTML 출력 사용
from rest_framework.decorators import api_view
from rest_framework.response import Response #데이터 생성에 사용

@api_view(['GET'])
def helloAPI(request):
    return Response("Hello REST API") 