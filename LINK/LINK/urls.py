from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from groups import views as group_views
from journal.views import PostCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('members_group/', user_views.members_group, name='members_group'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('create_group/', group_views.create_group, name='create_group'),
    path('join_group/', group_views.join_group, name='join_group'),
    path('ping/', group_views.ping),
    path('change_group/', user_views.change_group, name='change_group'),
    path('', include('journal.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
