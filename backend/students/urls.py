from django.urls import URLPattern, path
from .views import index

urlspatterns={
    path("students/",index)
}