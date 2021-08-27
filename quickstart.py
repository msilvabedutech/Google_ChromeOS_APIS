from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/admin.reports.audit.readonly']


def main():
    """
    Shows basic usage of the Admin SDK Reports API.
    Prints the time, email, and name of the last 10 login events in the domain.
    """
    # --------------------------------------Authentication--------------------------
    # Cria as credênciais do escopo
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'token.json', scopes=SCOPES)

    # Faz o login com a conta informada
    dc = credentials.create_delegated('dev@gedu.demo.bedu.tech')

    service = build('admin', 'reports_v1', http=dc.authorize(
        Http()), cache_discovery=False)

    # --------------------------------------Service----------------------------------
    # Call the Admin SDK Reports API
    results = service.activities().list(userKey='all', applicationName='chrome',
                                        maxResults=10).execute()
    activities = results.get('items', [])

    if not activities:
        print('No results found.')
    else:
        print('Logins:')
        for activity in activities:
            print(u'{0}: {1} ({2})'.format(activity['id']['time'],
                                           activity['actor']['email'], activity['events'][0]['name']))


if __name__ == '__main__':
    main()
