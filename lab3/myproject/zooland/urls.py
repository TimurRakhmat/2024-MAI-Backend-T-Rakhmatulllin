from django.urls import path
from . import views

urlpatterns = [
    path('zones', views.all_zones, name='zones'),
    path('zones/<uuid:zone_id>', views.zone, name='zone'),
    path('visitors', views.all_visitors, name='visitors'),
    path('visitors/<uuid:visitor_id>', views.visitor, name='visitor'),
    path('visitors/tickets/<uuid:visitor_id>', views.visitor_tickets, name='visitor_tickets'),
    path('tickets', views.all_tickets, name='tickets'),
    path('tickets/<uuid:ticket_id>', views.ticket, name='ticket'),
    path('tickets/<uuid:ticket_id>', views.ticket_zones, name='ticket_zones'),
    path('zones/create', views.create_zone, name='zone_create'),
    path('visitors/create', views.create_visitor, name='visitor_create'),
    path('tickets/create', views.create_ticket, name='tickets_create'),
]
