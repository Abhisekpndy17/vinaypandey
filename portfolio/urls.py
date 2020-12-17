from django.urls import path
from portfolio.views import home, works,about


urlpatterns = [
    path('', home, name='home'),
    path('works/', works, name='works'),
    path('about_us/', about, name='aboutus' )
]

