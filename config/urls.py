"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('Yesterday_map/', include('Yesterday_map.urls')),
    path('Tomorrow_map/', include('Tomorrow_map.urls')),
    path('Goyang/', include('Goyang.urls')),
    path('Ansan/', include('Ansan.urls')),
    path('Anseong/', include('Anseong.urls')),
    path('Anyang/', include('Anyang.urls')),
    path('Bucheon/', include('Bucheon.urls')),
    path('Dongducheon/', include('Dongducheon.urls')),
    path('Gapyeong/', include('Gapyeong.urls')),
    path('Gimpo/', include('Gimpo.urls')),
    path('Gunpo/', include('Gunpo.urls')),
    path('Guri/', include('Guri.urls')),
    path('Gwacheon/', include('Gwacheon.urls')),
    path('Gwangju/', include('Gwangju.urls')),
    path('Gwangmyeong/', include('Gwangmyeong.urls')),
    path('Hanam/', include('Hanam.urls')),
    path('Hwaseong/', include('Hwaseong.urls')),
    path('Icheon/', include('Icheon.urls')),
    path('Namyangju/', include('Namyangju.urls')),
    path('Osan/', include('Osan.urls')),
    path('Paju/', include('Paju.urls')),
    path('Pocheon/', include('Pocheon.urls')),
    path('Pyeongtaek/', include('Pyeongtaek.urls')),
    path('Seongnam/', include('Seongnam.urls')),
    path('Siheung/', include('Siheung.urls')),
    path('Suwon/', include('Suwon.urls')),
    path('Uijeongbu/', include('Uijeongbu.urls')),
    path('Uiwang/', include('Uiwang.urls')),
    path('Yangju/', include('Yangju.urls')),
    path('Yangpyeong/', include('Yangpyeong.urls')),
    path('Yeoju/', include('Yeoju.urls')),
    path('Yeoncheon/', include('Yeoncheon.urls')),
    path('Yongin/', include('Yongin.urls')),
    path('', include('common.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)