
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Land),
    path('Password_Generator/', include('Password_Generator.urls'))
]
