from __future__ import print_function
from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/admin.directory.device.chromeos.readonly']
BASE_URL = 'https://www.googleapis.com/admin/directory/v1/customer/my_customer/devices/chromeos'


def main():
    """
    See: https://google-api-client-libraries.appspot.com/documentation/admin/directory_v1/python/latest/admin_directory_v1.chromeosdevices.html
    for service
    """
    # --------------------------------------Authentication--------------------------
    # Cria as credênciais do escopo
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'token.json', scopes=SCOPES)

    # Faz o login com a conta informada
    dc = credentials.create_delegated('dev@gedu.demo.bedu.tech')

    # --------------------------------------Service----------------------------------

    admin_service = build('admin', 'directory_v1',
                          http=dc.authorize(Http()), cache_discovery=False)
    results = admin_service.chromeosdevices().list(customerId='my_customer', projection='BASIC').execute() 
    # In 'projection', full will bring a lot of new fields

    print(results)


if __name__ == '__main__':
    main()
