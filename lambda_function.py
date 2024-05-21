import re

import requests

from s3_daily_cache import s3_daily_cache


def redirect(redirect_url):
    response = {
        'statusCode': 302,  # Redirect status code
        'headers': {
            'Location': redirect_url,  # URL to redirect to
        },
        'body': '',  # Empty body for redirects
    }
    return response


@s3_daily_cache('wilby-url')
def get_wilby_url():    
    response = requests.get('https://wiby.me/surprise')
    lines = [line.decode('utf-8').strip() for line in response.iter_lines()]
    meta_line, = [line for line in lines if '<meta http-equiv="refresh"' in line]
    
    pattern = r"URL='(.*?)'"
    match = re.search(pattern, meta_line)
    wilby_url = match.group(1)
    return wilby_url


def lambda_handler(event, context):
    wilby_url = get_wilby_url()
    return redirect(wilby_url)

