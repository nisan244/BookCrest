from django.contrib import admin
from django.urls import path, include
from . views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name= 'home'),
    path('account/', include('accounts.urls')),
    path('book/', include('books.urls')),
    path('categories/', include('categories.urls')),
    path('transactions/', include('transactions.urls')),
    path('', all_categories, name= 'all_categories'),
    path('category/<slug:category_slug>/', home, name= 'category_wise'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

