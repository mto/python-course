* Module *os* & *sys*
* Đọc & ghi file
* Regular expression

## 1. Module *sys* & *os*

* *sys*: Cung cấp method cho phép tương tác với Python intepreter
* *os*: Cung cấp *portable* method cho phép tương tác với Operating System


### 1.1 Module *sys*

https://docs.python.org/3.6/library/sys.html

Chạy đoạn code sau đây

```python
import os
import os.path
import gzip
import zipfile

print(sys.path)
print(sys.modules)

sys.stdout.write('Hello')
```

__**Bài tập 1:**__

*In ra màn hình thông tin về phiên bản Python đang dùng để chạy chương trình trên máy*

__**Bài tập 2:**__

*In ra màn hình các tham số *flags* mà Python interpreter hỗ trợ*

### 1.3 Module *os*

https://docs.python.org/3.6/library/os.html

```python
import os

print(os.environ)
```

__**Bài tập 3:**__

*In ra màn hình tên tài khoản người dùng đang dùng Operating System*

__**Bài tập 4:**__

*In ra màn hình danh sách các file/folder nằm trong thư mục HOME*


## 2. Đọc & ghi file

![](https://raw.githubusercontent.com/mto/python-course/master/Session3/maria_ozawa.jpg)

Chạy thử đoạn code sau đây

```python
f = open('./maria_ozawa.jpg', mode='r')
print(f.read())
```

và

```python
f = open('./maria_ozawa.jpg', mode='rb')
print(f.read())
```

### 2.1 Đọc & ghi file binary

```python
fr = open('FILE_PATH', mode='rb')
fw = open('FILE_PATH', mode='wb')
```

*Chú ý:*

Khi đọc/ghi file binary (mà không phải file text) thì chỉ có thao tác trên *bytes*

__**Bài tập 5:**__

*Tạo file ex_5.py copy file ảnh maria_ozawa.jpg sang file maria_ozawa_bis.jpg*


### 2.2 Biểu diễn file binary dưới dạng text

![](https://raw.githubusercontent.com/mto/python-course/master/Session3/material/pk_base64.png)

Cách phổ biến để biểu diễn file binary dưới dạng text (ví dụ cho bài toán tìm kiếm) là dùng *base64*

__**Bài tập 6:**__

*Tạo file Python ex_6.py encode nội dung của maria_ozawa.jpg sang dạng text dùng base64 và lưu vào file maria_ozawa_b64.txt*

### 2.3 File checksum

![](https://raw.githubusercontent.com/mto/python-course/master/Session3/material/md5_checksum.png)

So sánh MD5 checksum là cách làm phổ biến để kiểm tra tính toàn vẹn của file trong quá trình download

__**Bài tập 7:**__

*Tạo file ex_7.py có chứa method *md5_checksum(fn)* nhận tham số đầu vào là đường dẫn đến file binary và trả về giá trị MD5 checksum*

```python

def md5_checksum(fn):
    pass

cks1 = md5_checksum('./maria_ozawa.jpg')
cks2 = md5_checksum('./maria_ozawa_bis.jpg')
print(cks1)
print(cks2)
print(cks1 == cks2)
```

### 2.4 Phương pháp tra cứu Python doc cho đọc & ghi file

Đọc & ghi file bắt đầu với đoạn code

```
f = open(fn[, mode])
```

Tuy nhiên các *operation* có thể thực thi trên đối tượng *file object* **f** có thể thay đổi theo giá trị của *mode*

Để biết thông tin về f cho việc tra cứu Python doc ta dùng method *type*

```
type(f)
```


## 3. Regular Expression

```python
import re

rex = '[0-9]+'
pattern = re.compile(rex)

s = 'John was born in 1970, he joined SEAL force at the age of 30. John was killed in action in 2016.'
print(pattern.findall(s))
```

### 3.1 Tìm kiếm các *cấu trúc* trong một đoạn text

https://docs.python.org/3/library/re.html


```python
import re

rex = 'Regular expression'
pattern = re.compile(rex)

s = 'input string'

pattern.search(s)
pattern.match(s)
pattern.findall(s)
```

__**Bài tập 8:**__

*Viết chương trình đọc nội dung file [evnexpress.txt](https://raw.githubusercontent.com/mto/python-course/master/Session3/evnexpress.txt) và in ra màn hình các số nằm trong nội dung của file*

### 3.2 Thay thế các *cấu trúc* trong một đoạn text

Chạy các đoạn code sau đây

```python
import re

rex = '[0-9]+'
pattern = re.compile(rex)

s = 'John was born in 1970, he joined SEAL force at the age of 30. John was killed in action in 2016.'
print(pattern.sub('dd-mm-yyyy', s))

```

và

```python
import re

rex = '[0-9]+'
pattern = re.compile(rex)

def replace(matchobj):
    return '[%s]' % matchobj.group(0)

s = 'John was born in 1970, he joined SEAL force at the age of 30. John was killed in action in 2016.'

print(pattern.sub(replace, s))

```

__**Bài tập 9:**__

*Viết chương trình đọc nội dung file ![frozen.srt](https://raw.githubusercontent.com/mto/python-course/master/Session3/frozen.srt) và thay thế các từ *snow*, *frozen*, *icy* bằng từ viết hoa. Sau đó ghi nội dung mới này ra file khác*

### 3.3 Capturing group

https://docs.python.org/3.6/library/re.html

Xem cách dùng metho *match.group()*