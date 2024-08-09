
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="todo"),
    
    path('del/<str:item_id>', views.remove, name="del"),
    
    path('admin/', admin.site.urls),
]
