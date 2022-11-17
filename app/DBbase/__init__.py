from sqlalchemy import create_engine
import redis

sql_engine = create_engine(
    "mysql+pymysql://root:yangGE926443yang@112.124.19.21:3306/ball?charset=utf8mb4",
    echo=True,
    max_overflow=5
)
pool = redis.ConnectionPool(host='112.124.19.21', port=6379, decode_responses=True)
redis_engine = redis.Redis(connection_pool=pool)

