from django.contrib import admin
from . import views

urlpatterns=[
    url(r'^admin/',admin.site.urls)
]