'''

Làm việc với hàm print() trong Python


print('ABCXYZ', end='MNPQ') in ra màn hình chuỗi 'ABCXYZ' và chuỗi 'MNPQ' ở cuối

print('ABCXYZ') <-> print('ABCXYZ', end='\n')

'''


# 1. Dùng hàm print in ra màn hình tên, tuổi, nghề nghiệp, email

print('Minh Hoang TO')
print('35')
print('Engineer')
print('hoang281283@gmail.com')


'''

Syntax của method trong Python

def my_method(param1, param2, param3,...):
    method_body
    return return_statement (optional)

Ví dụ:    

def print_name(name):
    print(name)
    
def add(x1, x2):
    return x1 + x2
    
'''

# 2. Hoàn thiện method print_user nhận 4 tham số đầu vào gồm name, age, job, email và in ra
# màn hình giá trị của các tham số


def print_user(name, age, job, email):
    pass

# 3. Dùng method print_user với name, age, job, email thật của bạn


'''

Khai báo biến trong Python

MY_VAR_NAME = VALUE_

Ví dụ:

name = 'Hoang'
age = 35
email = 'hoang281283@gmail.com'

'''

# 4. Khai báo các biến name, age, job, email và gọi hàm print_user với các biến này


'''

Vòng lặp for trong Python

for ITERATING_VARIABLE in SEQUENCES:
    DO_SOMETHING
        
Ví dụ:

    for i in range(0,10):
        print(i)
        
    
    seq = [1,2,3,4,5,6]
    for i in seq:
        print(i*i)
        
'''

# 5. In ra màn hình các số nguyên từ 1 -> 100, nằm trên cùng 1 dòng và cách nhau bởi dấu phẩy


'''

if/else statements

if CONDITION_CHECK:
   DO_SOME_THING

hoặc

if CONDITION_CHECK:
   DO_SOME_THING
else:
   DO_SOME_THING_ELSE
   
Ví dụ:

for i in range(0,10):
    if i %2 == 0:
       print(i)
       
for i in range(0,10):
    if i %2 == 0:
       print(i)
    else:
       print(i*i)
       
'''

# 6. In ra màn hình các số nguyên lẻ từ 1 -> 100, nằm trên cùng 1 dòng và cách nhau bởi dấu phẩy

'''

Python cung cấp method sleep cho phép dừng tạm thời execution của chương trình trong một khoảng thời gian xác định

Ví dụ:

import time

for i in range(0,10):
    print(i)
    time.sleep(0.2)

Đoạn mã trên in lần lượt các số từ 0 -> 10 ra màn hình và có khoảng dừng giữa 2 lần in liên tiếp là 0.2 second

'''

# 7. In ra màn hình lần lượt 100 ký tự '|' trên cùng dòng, khoảng cách giữa 2 lần in liên tiếp là 50 milliseconds.
# Sau khi in xong 100 ký tự thì in ra màn hình thông báo 'Download completed'

