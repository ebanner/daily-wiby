import boto3

from datetime import datetime, timedelta


s3 = boto3.client('s3')

BUCKET = 'daily-cache3'


def get_est_now():
    EST_OFFSET = timedelta(hours=-5)
    est_now = datetime.utcnow() + EST_OFFSET
    return est_now


def get_today_key():
    est_now = get_est_now()
    today_key = est_now.strftime("%Y-%m-%d")
    return today_key


def put(key, value):
    s3.put_object(Bucket=BUCKET, Key=key, Body=value)


def get(key):
    """If there is no key entry then return None"""

    try:
        object = s3.get_object(Bucket=BUCKET, Key=key)
    except Exception as e:
        print(e)
        return None

    value = object['Body'].read().decode('utf-8')
    return value


def delete(key):
    s3.delete_object(Bucket=BUCKET, Key=key)


def get_cache_key(resource):
    today_key = get_today_key()
    cache_key = resource+'-'+today_key
    return cache_key


def delete_s3_entry(resource):
    cache_key = get_cache_key(resource)
    delete(cache_key)


#
# Decorator
#
def s3_daily_cache(resource): # bind the value of resource so we can use it in the decorate function body
    def decorator(func):
        def wrapper():
            today_key = get_today_key()
            cache_key = get_cache_key(resource)
            value = get(cache_key)
            if value:
                return value
            value = func()
            put(cache_key, value)
            return value
        return wrapper
    return decorator

