from __future__ import print_function
import httplib2
from oauth2client.service_account import ServiceAccountCredentials
import json
import pprint
import urllib.parse
from httplib2 import Http

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/cloud-identity.devices']
BASE_URL = 'https://cloudidentity.googleapis.com/v1/'


def main():
    """
    
    """
    # --------------------------------------Authentication--------------------------
    # Cria as credênciais do escopo
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'token.json', scopes=SCOPES)

    # Faz o login com a conta informada
    dc = credentials.create_delegated('dev@gedu.demo.bedu.tech')
    dc.refresh(httplib2.Http())

    # --------------------------------------Service----------------------------------
    # Call the Admin SDK Reports API

    ###############################
    # LIST deviceUsers with filter.
    # Change this filter according to the options here:
    # https://support.google.com/a/answer/7549103
    list_url = BASE_URL + 'devices'
    auth_header = {'Authorization': 'Bearer ' + dc.access_token}
    content = urllib.request.urlopen(
        urllib.request.Request(list_url, headers=auth_header)).read()
    response = json.loads(content)
    pp = pprint.PrettyPrinter(indent=4)

    print(response)

    # loop = True
    # while loop:
    #     if 'nextPageToken' in results:
    #         results = self.report_service.activities().list(userKey='all',
    #                                                         applicationName='meet',
    #                                                         pageToken=results['nextPageToken']).execute()
    #         activities = activities + results.get('items', [])
    #     else:
    #         loop = False

    # if 'deviceUsers' in response:
    #     print('Listed: ' +
    #           str(len(response['deviceUsers'])) + ' deviceUsers\n')

    # for element in response['deviceUsers']:
    #     pp.pprint(element)
    #     print('Next page token: ' + response['nextPageToken'])
    # else:
    #     print('Empty response')


if __name__ == '__main__':
    main()