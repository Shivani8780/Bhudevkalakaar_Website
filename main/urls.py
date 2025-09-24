from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('past-events/', views.past_events, name='past-events'),
    path('photos/', views.photos, name='photos'),
    path('contact/', views.contact, name='contact'),
    path('get-tickets/', views.get_tickets, name='get-tickets'),
    path('audience/', views.audience, name='audience'),
    path('participant-form/', views.participant_form, name='participantForm'),
    path('events/', views.event_list, name='event-list'),
    path('submit-ticket/', views.submit_ticket_form, name='submit_ticket_form'),
    path('tickets/', views.ticket_list, name='ticket-list'),
    path('submit-form/', views.submit_form, name='submit_form'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('submit-contact/', views.submit_contact_form, name='submit_contact_form'),
    path('participants/profile/', views.participant_profile, name='participant-profile'),
    path('info/', views.infopage, name='Infopage'),
]
