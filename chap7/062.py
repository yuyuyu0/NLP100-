import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

print((r.get('Harpbeat')).decode('utf-8'))
