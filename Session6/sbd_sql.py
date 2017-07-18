from sqlalchemy import create_engine
from sqlalchemy.engine.base import Connection

MYSQL_DB_URL = 'mysql+pymysql://test:123456@localhost:3306/sbd'
engine = create_engine(MYSQL_DB_URL, echo=True)

conn = engine.connect()

q = 'SELECT * FROM employees;'
result = conn.execute(q)
for row in result:
    print(row)