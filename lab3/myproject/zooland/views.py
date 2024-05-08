from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.forms import model_to_dict

import json

from .models import Zone, VisitorProfile, Ticket, TicketZone


# Create your views here.


@csrf_exempt
@require_http_methods(["GET"])
def all_visitors(request):
    return JsonResponse(list(VisitorProfile.objects.all().values()),
                        safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
@require_http_methods(["GET"])
def visitor(request, visitor_id):
    visitor_profile = VisitorProfile.objects.get(login=visitor_id)
    context = {'visitor': model_to_dict(visitor_profile)}
    return JsonResponse(context)


@csrf_exempt
@require_http_methods(["GET"])
def visitor_tickets(request, visitor_id):
    visitor_profile = VisitorProfile.objects.get(login=visitor_id)
    return JsonResponse(list(Ticket.objects.filter(visitor_id=visitor_profile).values()),
                        safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
@require_http_methods(["GET"])
def all_zones(request):
    return JsonResponse(list(Zone.objects.all().values()), safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
@require_http_methods(["GET"])
def zone(request, zone_id):
    zone_item = Zone.objects.get(title=zone_id)
    context = {'zone': model_to_dict(zone_item)}
    return JsonResponse(context)


@csrf_exempt
@require_http_methods(["GET"])
def all_tickets(request):
    return JsonResponse(list(Ticket.objects.all().values()), safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
@require_http_methods(["GET"])
def ticket(request, ticket_id_post):
    ticket_item = Ticket.objects.get(number=ticket_id_post)
    context = {'ticket': model_to_dict(ticket_item)}
    return JsonResponse(context)


@csrf_exempt
@require_http_methods(["GET"])
def ticket_zones(request, ticket_id_post):
    ticket_item = Ticket.objects.get(ticket_id=ticket_id_post)
    # return JsonResponse({'status': 'ok'})
    return JsonResponse(list(ticket_item.zones.all().values()),
                        safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
@require_http_methods(["POST"])
def create_visitor(request):
    post_data = json.loads(request.body.decode("utf-8"))
    VisitorProfile.objects.create(login=post_data['login'], password=post_data['password'])
    return JsonResponse({'status': 'ok'})


@csrf_exempt
@require_http_methods(["POST"])
def create_zone(request):
    post_data = json.loads(request.body.decode("utf-8"))
    Zone.objects.create(title=post_data['title'], description=post_data['description'])
    return JsonResponse({'status': 'ok'})


@csrf_exempt
@require_http_methods(["POST"])
def create_ticket(request):
    data = json.loads(request.body.decode("utf-8"))
    visitor_profile = VisitorProfile.objects.get(login=data["visitor_id"])
    ticket_impl = Ticket.objects.create(visitor_id=visitor_profile, duration=data["duration"])
    for zone_data in data["zones"]:
        zone_impl = Zone.objects.get(title=zone_data)
        ticket_impl.zones.add(zone_impl)
        # TicketZone.objects.create(ticket_id=ticket_impl, zone_id=zone_impl)
    return JsonResponse({'status': 'ok'})
