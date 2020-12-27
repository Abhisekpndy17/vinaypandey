from django.urls import path
from blog.views import blog, post_deatils


urlpatterns = [
    path('', blog, name='blog'),
    path('<slug:slug>/', post_deatils, name='post_details' ),
]

