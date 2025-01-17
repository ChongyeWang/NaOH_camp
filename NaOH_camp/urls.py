"""NaOH_camp URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("projects.urls")),
    path("blog/", include("blog.urls")),
    path('auth/', include('allauth.urls')),
    path("accounts/", include("accounts.urls")),
    path("info/", include("info.urls")),
    path("data/", include("data.urls")),
    path("essays/", include("essays.urls")),
    path("videos/", include("videos.urls")),
    path("chat/", include("chat.urls")),
    path("news/", include("news.urls")),
    path("shop/", include("shop.urls")),
    path("cart/", include("cart.urls")),
    path("order/", include("order.urls")),
    path("ranking/", include("ranking.urls")),
    path("photo/", include("face.urls")),
    path("auth/", include("face_auth.urls")),
    path("links/", include("links.urls")),
    path("", include('social_django.urls', namespace='social')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

