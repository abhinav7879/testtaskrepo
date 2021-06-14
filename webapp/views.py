from rest_framework.views import APIView
import requests
from django.http import JsonResponse
import urllib.request,json
#from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, response
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status


class Ping(APIView):
    def get (self, request):
        with urllib.request.urlopen("https://www.foobar.com") as url:
            data = json.loads(url.read().decode())
            print(data)
            return JsonResponse(data, safe=False)

@api_view(["GET"])
def welcome(request):
    status = {"Receiver:": "Cisco is the best!"}
    return JsonResponse(status)

'''also we can use this api for ping method and to get url from github
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def deploy(request):
    # Verify if request came from GitHub.
    forwarded_for = u'{}'.format(request.META.get('HTTP_X_FORWARDED_FOR'))
    client_ip_address = ip_address(forwarded_for)
    whitelist = requests.get('https://www.foobar.com').json()['hooks']

    for valid_ip in whitelist:
        if client_ip_address in ip_network(valid_ip):
            break
        else:
            return HttpResponseForbidden('Permission denied.')

    # If request reached this point we are in a good shape
    # Process the GitHub events
    event = request.META.get('HTTP_X_GITHUB_EVENT', 'ping')
    print('the event is ', event)
    if event == 'ping':
        return HttpResponse(event)
    elif event == 'push':
        print('hello world')
        bash_file_location = os.path.join(settings.BASE_DIR, 'deploy.sh')
        process = subprocess.Popen(bash_file_location, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = process.communicate()[0]
        return HttpResponse('the output is ', output)

    # In case we receive an event that's not ping or push.
    return HttpResponse(event)  # HttpResponse(status=204)'''


