from django.contrib.auth.models import User
import json
from django.core import serializers
from django.http import HttpResponse

def user_view_set(request, id):
    user = User.objects.get(id=id)
    data = serializers.serialize('json', [user,])
    struct = json.loads(data)
    data = json.dumps(struct[0])
    return HttpResponse(data)
