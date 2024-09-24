from django.shortcuts import render # 템플릿 엔진을 이용해서 HTML 출력 사용
from rest_framework.decorators import api_view
from rest_framework.response import Response #데이터 생성에 사용

from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializer import BookSerializer

# 하나의 함수를 통해 GET과 POST 구분 처리
@api_view(['GET', 'POST'])
def booksAPI(request):
    if request.method == 'GET':
        # 전체 데이터 조회
        books = Book.objects.all()
        # 가져온 데이터 JSON 문자열로 변환
        serializer = BookSerializer(books, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer
        if serializer.is_valie():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# 기본키 값 받아서 하나의 데이터를 찾아서 출력하는 함수
@api_view(['GET'])
def bookAPI(request, bid):
    book = get_object_or_404
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def helloAPI(request):
    return Response("Hello REST API") 