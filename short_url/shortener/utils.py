from hashlib import md5

def create_hash_url(url):
    hash_url = md5(url.encode()).hexdigest()[:10]
    return hash_url

def create_short_url(hash_url):
    short_url = f'http://localhost:8000/{hash_url}/'
    return short_url