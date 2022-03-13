from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from articles import views
from blog.settings import MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),

    #account
    path('', include('account.urls')),

    #articles
    path('create/', views.create, name='create'),
    path('article/<int:article_pk>/', views.articleview, name='articleview'),
    path('myarticles/', views.myarticles, name='myarticles'),
    path('update/<int:article_pk>/', views.update, name='update'),
    path('delete/<int:article_pk>/', views.delete, name='delete'),
    path('deletecomment/<int:comment_pk>/', views.deletecomment, name='deletecomment'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
