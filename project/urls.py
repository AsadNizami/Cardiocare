"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from app import views as app_view  # test, result, landing_view, history, render_pdf_view
from users import views as user_views
from info import views as info_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_view.landing_view, name='landing'),
    path('test/', app_view.test, name='test'),
    path('result/', app_view.result, name='result'),
    path('history/', app_view.history, name='history'),
    re_path('pdf/(?P<pk>[^/]*)', app_view.render_pdf_view, name='pdf'),
]

urlpatterns += [
    path('register/', user_views.register, name='register'),
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('login/', user_views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('delete/', user_views.delete_user, name='delete'),
]

urlpatterns += [
    path('about/', info_view.about, name='about'),
    path('info/', info_view.info, name='info'),
    path('learnmore/', info_view.learn_more, name='learn_more')
]
# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
