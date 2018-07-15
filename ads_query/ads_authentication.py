import os


def get_token():
    return 'Bearer {}'.format(os.environ.get('ADS_TOKEN'))
