from django.urls import path
from . import views

urlpatterns = [
    path('zones', views.all_zones, name='zones'),
    path('zones/<uuid:zone_id>', views.zone, name='zone'),
    path('visitors', views.all_visitors, name='visitors'),
    path('visitors/<uuid:visitor_id>', views.visitor, name='visitor'),
    path('tickets', views.all_tickets, name='tickets'),
    path('tickets/<uuid:ticket_id>', views.ticket, name='ticket'),
]
