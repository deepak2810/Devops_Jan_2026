from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect to Redis using the hostname 'redis' (we will define this later in AWS)
r = redis.Redis(host='redis-service', port=6379, decode_responses=True)

@app.route('/')
def hello():
    try:
        # Increment a counter in Redis
        count = r.incr('hits')
        return f"Hello from ECS! This page has been viewed {count} times.\n"
    except Exception as e:
        return f"Error connecting to Redis: {str(e)}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)