from django.urls import path, include
from django.conf.urls.static import static
from trippin import settings

from rest_framework_simplejwt.views import (
     TokenObtainPairView,
     TokenRefreshView,
   )

from .views_queries import queries, query
from .views import index
urlpatterns = [
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('login', views.login_view),

        # get or post queries
    path('api/queries/', queries),
    
    # get, put or delete query by id
    path('api/queries/<int:query_id>/', query),
    
    path('', index),
]
