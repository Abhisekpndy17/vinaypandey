from django.urls import path
from portfolio.views import home, works,about, iprrelated, labour,mcaroc, others, sebi, startup, taxplanning


urlpatterns = [
    path('', home, name='home'),
    path('works/', works, name='works'),
    path('about_us/', about, name='aboutus' ),
    path('iprrelated/', iprrelated, name='iprrelated'),
    path('labour/', labour, name='labour'),
    path('mca&roc/', mcaroc, name='mca&roc'),
    path('others/', others, name='others'),
    path('sebi/', sebi, name='sebi'),
    path('startup/', startup, name='startup'),
    path('taxplanning/', taxplanning, name='taxplanning')
]

