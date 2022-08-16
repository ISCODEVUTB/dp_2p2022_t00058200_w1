

from django.http import JsonResponse
import json
def Package(request):
  body = request.body.decode('utf-8')
  if body:
    bd = json.loads(body)
    print(bd['hola'])
  return JsonResponse({
    "name":"ha"
  })