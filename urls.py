from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import main.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", main.views.index, name="index"),
    path("auth/", main.views.auth, name="auth"),
    path("dashboard/", main.views.dashboard, name="dashboard"),
    path("connect/", main.views.connect, name="connect"),
    path("private/", main.views.private, name="private"),
    path("admin/", admin.site.urls),
]
