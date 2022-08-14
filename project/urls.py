"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from repo.views import delete_repo, new_repo,all_repo,single_repo,home,edit_repo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('repo/',all_repo,name="all_repo"),
    path('repo/<int:id>',single_repo,name="single_repo"),
    path('repo/<int:id>/edit', edit_repo, name="edit_repo"),
    path('repo/new', new_repo, name="new_repo"),
    path('repo/<int:id>/delete', delete_repo, name="delete_repo")


]
