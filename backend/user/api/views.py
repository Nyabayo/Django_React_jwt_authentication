# In views.py create a new view that returns all the possible routes, here,
# we are going to have two routes: one for sending user login details
# and receiving authentication tokens / api / token, and one for sending
# a refresh token and receiving new authentication tokens /api/token/refresh.

from django.http import JsonResponse

def get_routes(request):
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]
    return JsonResponse(routes, safe=False) #The safe=False allows us to receive and display non-Json data

