from django.urls import path, include
from .views import home, display, detail

urlpatterns = [path("", home.as_view(), name='home'),
               path("display/", display.as_view(), name='display'),
               path("detail/", detail.as_view(), name='detail'),
]
