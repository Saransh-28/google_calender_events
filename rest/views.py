from rest_framework.decorators import api_view
from django.http import HttpResponse
from gcsa.google_calendar import GoogleCalendar

# # Create your views here.

import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

events = []

@api_view(['GET'])
def GoogleCalendarInitView(request):
    CURR_DIR = os.path.dirname(os.path.realpath(__file__))
    CLIENT_SECRETS_FILE=str(CURR_DIR)+'\\credentials.json'
    gc = GoogleCalendar(credentials_path=CLIENT_SECRETS_FILE,save_token=True)
    for event in gc:
        events.append(event)
    return HttpResponse('verified')


@api_view(['GET'])
def GoogleCalendarRedirectView(request):
    return HttpResponse(events)

