from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import Home


# Create your views here.
@csrf_exempt
@require_POST
def index(request):
    key = request.POST.get('key', None)

    if key is None:
        return HttpResponseBadRequest()

    home = get_object_or_404(Home, psk=key)
    home.ip = request.META['HTTP_X_REAL_IP']
    home.last_check_date = datetime.now()

    home.save()

    return HttpResponse('OK')
