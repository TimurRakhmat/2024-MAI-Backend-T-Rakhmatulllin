from django.urls import path
from . import views

urlpatterns = [
    path('zones', views.all_zones, name='zones'),
    path('zones/<slug:zone_id>', views.zone, name='zone'),
    path('visitors', views.all_visitors, name='visitors'),
    path('visitors/<slug:visitor_id>', views.visitor, name='visitor'),
    path('visitors/tickets/<slug:visitor_id>', views.visitor_tickets, name='visitor_tickets'),
    path('tickets', views.all_tickets, name='tickets'),
    path('tickets/<int:ticket_id>', views.ticket, name='ticket'),
    path('tickets/zone/<int:ticket_id_post>', views.ticket_zones, name='ticket_zones'),
    path('zones_create', views.create_zone, name='zone_create'),
    path('visitors_create', views.create_visitor, name='visitor_create'),
    path('tickets_create', views.create_ticket, name='tickets_create'),
    path('zones_search', views.search_zone, name='search_zones'),
]
