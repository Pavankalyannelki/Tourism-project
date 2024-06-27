from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static

from django.conf import settings
from .views import booking_success
urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('home/',views.home, name='home'),
    path('gallerypage/',views.gallerypage, name='gallerypage'),
    path('contactus/',views.contactus, name='contactus'),
    path('categories/',views.categories, name='categories'),
    path('araku/',views.araku, name='araku'),
    path('dindi/',views.dindi, name='dindi'),
    path('lepakshi/',views.lepakshi, name='lepakshi'),
    path('lambasingi/',views.lambasingi, name='lambasingi'),
    path('thimmamma/',views.thimmamma, name='thimmamma'),
    path('undavalli/',views.undavalli, name='undavalli'),
    path('ettipothala/',views.ettipothala, name='ettipothala'),
    path('chebrole/',views.chebrole, name='chebrole'),
    path('coringa/',views.coringa, name='coringa'),
    path('annavaram/',views.annavaram, name='annavaram'),
    path('rushikonda/',views.rushikonda, name='rushikonda'),
    path('bheemili/',views.bheemili, name='bheemili'),
    path('manginapudi/',views.manginapudi, name='manginapudi'),
    path('simhachalam/',views.simhachalam, name='simhachalam'),
    path('kanakadurga/',views.kanakadurga, name='kanakadurga'),
    path('vijayawada/',views.kanakadurga, name='vijayawada'),


    path('machilipatnam/',views.machilipatnam,name='machilipatnam'),
    path('kondapalli/',views.kondapalli, name='kondapalli'),
    path('bhavani island/',views.bhavaniisland, name='bhavaniisland'),
    path('gandhihill/',views.gandhihill, name='gandhihill'),
    path('kuchipudi/',views.kuchipudi, name='kuchipudi'),
    path('prakasam barrage/',views.prakasambarrage, name='prakasambarrage'),
    path('papikondalu/',views.papikondalu, name='papikondalu'),
    path('rajahmundry/',views.rajahmundry, name='rajahmundry'),
    path('draksharamam/',views.draksharamam, name='draksharamam'),
    path('maredumilli/',views.maredumilli, name='maredumilli'),
    path('godavari bridge/',views.godavaribridge, name='godavaribridge'),
    path('kailasagiri hills/',views.kailasagirihills, name='kailasagirihills'),
    path('borra caves/',views.borracaves, name='borracaves'),
    path('submarine museum/',views.submarinemuseum, name='submarinemuseum'),
    path('gooty fort/',views.gootyfort, name='gootyfort'),
    
    path('hemavathi temple/',views.hemavathi, name='hemavathi'),
    path('penukonda fort/',views.penukonda, name='penukonda'),
    path('kadiri lakshmi narasimha swamy temple/',views.klns, name='klns'),
    path('Bugga ramalingeswara swamy temple/',views.brs, name='brs'),
    path('chintala venkataramana swamy temple/',views.cvs, name='cvs'),
    path('pedakakani/',views.pedakakani, name='pedakakani'),
    path('mahachaitya amaravathi/',views.amaravathi, name='amaravathi'),
    path('mangalagiri/',views.mangalagiri, name='mangalagiri'),
   
    path('uppalapadu bird scanctuary/',views.uppalapadu, name='uppalapadu'),
    path('dhyana buddha statue/',views.dhyana, name='dhyana'),
    
    

    path('hotel/',views.Hotelbooking,name='hotelbooking'),

    # path('book/',views.book, name='book'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('destinations/',views.destinations, name='destinations'),
]