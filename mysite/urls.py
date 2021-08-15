from django.urls import include, path
from mysite.demo.views import user_view_set

urlpatterns = [
    path('user/<int:id>/', user_view_set, name='user_view_set'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
