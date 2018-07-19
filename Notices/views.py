
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Notice
from .update import update_db
from django.core import serializers

def check_new(request):
	latest_key = 0
	all_objects = Notice.objects.order_by('id')
	if len(all_objects) is not 0:
		latest_object = all_objects[0]
		latest_key = latest_object.getKey()
	data = {'latest_key':latest_key}
	return JsonResponse(data)


def get_notices(request, latest_key):
	required_objects = Notice.objects.filter(key__gt=latest_key)
	data = serializers.serialize('json', required_objects, fields=('title','key','content'))
	return HttpResponse(data)


def update_notices(request):
	update_db()
	return HttpResponse("OK")