from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),

    path('classes/', include(('classes.urls', 'classes'), namespace='classes')),

    path('mongo-practice/', include(('mongodb_practice.urls', 'mongodb_practice'), namespace='mongodb_practice'))

]
