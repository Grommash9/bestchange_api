import os
import redis


redis = redis.Redis(decode_responses=True)

MYSQL = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'db': 'bestchange_api_db',
    # 'unix_socket': '/var/run/mysqld/mysqld.sock'
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))