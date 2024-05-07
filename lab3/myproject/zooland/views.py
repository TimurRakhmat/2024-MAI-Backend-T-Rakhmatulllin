from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.forms import model_to_dict

import json

from .models import Zone, VisitorProfile, Ticket


# Create your views here.


@require_http_methods(["GET"])
def all_visitors(request):
    return JsonResponse(list(VisitorProfile.objects.all().values()),
                        safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def visitor(request, visitor_id):
    visitor_profile = VisitorProfile.objects.get(title=visitor_id)
    context = {'visitor': model_to_dict(visitor_profile)}
    return JsonResponse(context)


@require_http_methods(["GET"])
def all_zones(request):
    return JsonResponse(list(Zone.objects.all().values()), safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def zone(request, zone_id):
    zone_item = Zone.objects.get(title=zone_id)
    context = {'zone': model_to_dict(zone_item)}
    return JsonResponse(context)


@require_http_methods(["GET"])
def all_tickets(request):
    return JsonResponse(list(Ticket.objects.all().values()), safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def ticket(request, ticket_id):
    ticket_item = Ticket.objects.get(number=ticket_id)
    context = {'ticket': model_to_dict(ticket_item)}
    return JsonResponse(context)

