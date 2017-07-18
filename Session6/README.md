* Làm việc với Relational DB thông qua *sqlalchemy*

## 1 Cài đặt RDBMS

### 1.1 Cài MySQL

Cài MySQL trên Windows theo hướng dẫn trong link

https://dev.mysql.com/doc/refman/5.7/en/windows-installation.html

### 1.2 Cài MySQL Workbench

Tool cho phép tương tác với dữ liệu lưu trữ trên MySQL

Cài MySQL Workbench trên Windows theo hướng dẫn trong link

https://dev.mysql.com/doc/workbench/en/wb-installing-windows.html


### 1.3 Tạo schema *sbd*

Bật MySQL Workbench, đăng nhập bằng *root* và tạo schema mới *sbd*

![](./material/mysql_workbench.png)

### 1.3 Tạo *user* và *table*


**__Bài tập 1:__**

*Tạo bảng *employees* từ giao diện của MySQL Workbench với các cột như dưới đây*

|first_name|last_name|email|position|phone|

**__Bài tập 2:__**

*Tạo user **test** với password **123456** và gán cho user **test** toàn bộ các quyền trên schema **sbd***

### 1.4 SQL

Các RDBMS (MySQL, Postgres, Oracle,...) nhận và xử lý các command tuân theo syntax của SQL

https://www.tutorialspoint.com/sql/

**__Bài tập 3:__**

*Thực thi các SQL query CREATE/SELECT/UPDATE từ MySQL Workbench để read/write record trong bảng **employees***


## 2 Thư viện *sqlalchemy*

![](./material/sql_alchemy.png)

*sqlalchemy* cho phép ứng dụng Python tương tác *programmatically* với dữ liệu lưu trong RDBMS

Ứng dụng Python tương tác với RDBMS thông qua một trong 2 mô hình:

* __SQLAlchemy Core__: Low-level API, pure SQL queries
* __SQLAlchemy ORM__: High-level API, object-oriented

__Chú ý:__

Trong bài học ta sẽ sử dụng SQLAlchemy Core giúp học viên luyện tập với SQL query language

### 2.1 Cài đặt *dependencies*

 Các dependencies cần cài đặt bao gồm:

 * SQLAlchemy core
 * Driver cho mỗi loại RDBMS (MySQL, Postgres, Oracle,...)

Tạo file requirements.txt với nội dung

```shell
SQLAlchemy==1.1.11
PyMySQL==0.7.1
```

sau đó chạy command

```shell
pip install -r requirements.txt
```

### 2.2 Tạo kết nối tới MySQL

```python
from sqlalchemy import create_engine

MYSQL_DB_URL = 'mysql+pymysql://test:123456@localhost:3306/sbd'
engine = create_engine(MYSQL_DB_URL, echo=True)

conn = engine.connect()
print(conn)

```

### 2.3 Thực thi SQL query

Code mẫu để thực thi SQL query (ví dụ query lấy toàn bộ các record trong bảng *employees*) như sau


```python
from sqlalchemy import create_engine

MYSQL_DB_URL = 'mysql+pymysql://test:123456@localhost:3306/sbd'
engine = create_engine(MYSQL_DB_URL, echo=True)

...

q = 'SELECT * FROM employees;'
conn = engine.connect()
result = conn.execute(q)

for row in result:
    pass

```


__Tương tác DB <-> Tạo SQL query__

https://www.tutorialspoint.com/sql/


**__Bài tập 4:__**

*Viết chương trình in ra màn hình các record có trong bảng **employees***


**__Bài tập 5:__**

*Viết chương trình nhận thông tin **first_name, last_name, email, position** từ console và tạo record mới trong bảng **employees***

**__Bài tập 6:__**

*Viết chương trình in ra màn hình các record trong bảng **employees** có Gmail email*

## 3 Kết nối ứng dụng Facebook Console với MySQL

**__Bài tập 7:__**

*Tạo schema **fbcli** và bảng **posts** trong schema này, tiếp theo kết nối ứng dụng Facebook Console trong bài học 5 với MySQL và lưu trữ dữ liệu **post** từ Facebook về bảng **posts***