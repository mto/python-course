
* Cài đặt môi trường làm việc
* Bài tập làm quen với syntax
* Cấu trúc dữ liệu *list*


## 1. Cài đặt môi trường làm việc

### 1.1 Cài đặt Python

(cho Windows)

*Step 1:*

Tải Python 3.6.1 từ https://www.python.org/downloads/ và chạy chương trình cài đặt

*Step 2:*

Chọn 'Customize installation' và 'Add Python 3.6 to PATH'

![](https://raw.githubusercontent.com/mto/python-course/master/Session1/install_python_1.png)

*Step 3:*

Chọn thư mục cài đặt C:\Python3.6

![](https://raw.githubusercontent.com/mto/python-course/master/Session1/install_python_2.png)

*Step 4:*

Kiểm tra cài đặt bằng cách mở cửa sổ **cmd** và gõ lệnh

```shell
python --version
```

Nếu cài đặt thành công thì màn hình sẽ in ra

```shell
Python 3.6.1
```

### 1.2 Tạo working directory

Tạo thư mục C:\python-course làm thư mục gốc cho toàn bộ khoá học

## 2. Bài tập làm quen với syntax

File mã nguồn của Python là một file có đuôi *.py*. Để chạy một file *test.py* trên cửa sổ **cmd** ta dùng lệnh

```shell
python test.py
```

Với mỗi bài tập sau đây, yêu cầu học viên tạo file Python có tên 'ex_k.py' trong đó k là số thứ tự của bài tập


### 2.1 Hàm *print* trong Python

https://docs.python.org/3/library/functions.html#print

Hàm *print* nhận tham số đầu vào là chuỗi ký tự và in chuỗi ký tự ra output của chương trình

Ví dụ:

```python
print('ABCXYZ')
```

sẽ in ra

```shell
ABCXYZ
```

__**Bài tập 1:**__

*Tạo file Python (ex_1.py) in ra tên, tuổi, nghề nghiệp và email của học viên tương tự như đoạn code dưới đây và chạy file Python trên cửa sổ* **cmd**

```python
print('Minh Hoang TO')
print('35')
print('Engineer')
print('hoang281283@gmail.com')
```

### 2.2 Method trong Python

Để tránh việc phải viết lặp lại nhiều đoạn code giống/tương tự nhau thì ta có thể gom một số đoạn code vào trong *method* và sử dụng lại method.

Cấu trúc của method trong Python có dạng

```python
def method_name(arg1[,arg2[,arg3[...]]]):
    ...
    return return_statement (optional)

```

__**Bài tập 2:**__

*Tạo file Python ex_2.py có chứa method *print_user* nhận 4 tham số đầu vào *name, age, job, email* và in ra màn hình các tham số này*

```python
def print_user(name, age, job, email):

```

Thêm vào file ex_2.py đoạn mã dưới đây và chạy ex_2.py trên cửa sổ **cmd**

```
print_user('TÊN_HỌC VIÊN', 'TUỔI', 'NGHỀ NGHIỆP', 'EMAIL')
```

### 2.3 *for* loop trong Python

Cấu trúc vòng lặp *for* trong Python

```python
for ITERATING_VARIABLE in SEQUENCES:
    ...
```

Ví dụ:

```python
for i in range(0,10):
    print('Hello World')
```

__**Bài tập 3:**__

*Tạo file ex_3.py in ra màn hình tất cả các số nguyên từ 1->100*

### 2.4 *if/else* trong Python

Cấu trúc *if/else*

```python
if CONDITION_CHECK:
   ...
```

hoặc

```python
if CONDITION_CHECK:
   ...
else:
   ...
```

hoặc

```python
if CONDITION_CHECK:
   ...
elif SECOND_CONDITION_CHECK:
   ...
elif THIRD_CONDITION_CHECK:
   ...
else:
   ...
```

__**Bài tập 4:**__

*Tạo file ex_4.py in ra màn hình các số nguyên lẻ nằm trong khoảng từ 1->100, nằm trên cùng 1 dòng và cách nhau bởi dấu ','*

__**Bài tập 5:**__

*Tạo file ex_5.py in **từ từ** 100 ký tự '|' ra màn hình và nằm trên cùng 1 dòng*

__Chú ý__:

Python cung cấp hàm *sleep* trong module *time* cho phép dừng tạm thời *execution* của chương trình trong một khoảng thời gian xác định. Để làm bài tập 5 ta cần đoạn mã sau

```python
import time

for i in range(0,100):
    ...
    time.sleep(0.2)
```

## 3. Cấu trúc dữ liệu *list*

### 3.1 Hình dung khái niệm *list* qua code mẫu

Copy/paste và chạy các đoạn mã sau đây

```python
l = [1,2,3,4,5,6]
print(l)
```

```python
l = [1,2,3,4,5,6]
l.append('abc')
l.append('def')
print(l)
```

```python
l = []
for i in range(1,7):
    l.append(i)
print(l)
```

__**Bài tập 6:**__

*Tạo file ex_6.py có khai báo một list rỗng và thêm vào trong list các số chia hết cho 5 nằm trong khoảng từ 1->100. Sau đó in list ra màn hình*

### 3.6 Vòng lặp trên *list*

```python
l = [1,3,5,'abc',9]

for x in l:
    print(x)
```

__**Bài tập 7:**__

*Tạo file ex_7.py có chứa hàm filter(l, rex) nhận đầu vào là list các chuỗi ký tự và trả về
list các chuỗi ký tự có prefix là chuỗi rex*

Ví dụ:

filter(['abc', 'aabc', 'aaab'], 'aa') trả về list ['aabc', 'aaab']

__**Bài tập 8:**__

*Tạo file ex_8.py trả về list các file Python trong thư mục hiện tại*

__Chú ý:

Cần dùng đoạn mã sau để lấy danh sách các file nằm trong thư mục hiện tại

```python
import os

os.listdir('.')
```