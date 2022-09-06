from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),

    path('classes/', include(('classes.urls', 'classes'), namespace='classes')),

]
