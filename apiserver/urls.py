from django.contrib import admin
from django.urls import path, include

from rest import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/', include("rest.urls")),

    # ajax/ 경로로 요청이오면 views.ajax 함수 호출
    path('ajax/', views.ajax)
]