from django.contrib import admin
from django.urls import path, include

app_name = 'app'
urlpatterns = [
  path('app/', include('app.urls')),
  path('admin/', admin.site.urls),
]