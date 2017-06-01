'''

Làm việc với các cấu trúc dữ liệu list

l = [1,2,3,4,5,6]

'''

'''
1. Chạy đoạn mã sau và xem kết quả trên màn hình

l = [1,2,3,4,5,6]
print(l)

l.append(7)
print(l)

'''



'''
Syntax cho vòng lặp trên list

l = [1,2,3,7,9,11]

for i in l:
    print(i)
    
'''

# 2. Viết method compute_sum trả về tổng tất cả các số trong list số nguyên cho trước


def compute_sum(l):
    pass


# 3. Viết method filter_even_number nhận một list các số nguyên và trả về một list các số chẵn trong list ban đầu

def filter_even_number(l):
    pass

'''

List Comprehension trong Python cho phép thực hiện các thao tác cơ bản filter/map trên list trong Python
một cách ngắn gọn và không cần trực tiếp sử dụng vòng lặp for

l = [1,2,3,4,5,6,7,8,9]

el = [ x in l if x %2 == 0]

'''

'''
4. Chạy đoạn code sau đây và xem kết quả trên màn hình


l = [1,2, 7,9, 0]
sl = [x*x for x in l]

print(sl)


l=['a', 'b', 'c', 'd']
dl = [ x + x for x in l]

print(dl)

'''

'''
5. Chạy đoạn mã liệt kê danh sách các file nằm trong thư mục 'PATH_TO_FOLDER'

import os

print(os.listdir(PATH_TO_FOLDER))

'''

'''
6. Hàm listdir trong module os trả về list các file/folders trong thư mục có tên trong tham số đầu vào.

Hãy viết đoạn mã DÙNG VÒNG LẶP in ra danh sách các folder trong thư mục đầu vào

'''

'''
7. Yêu cầu kết quả tương tự 6, với điều kiện dùng LIST COMPREHENSION
'''

'''
8. Viết method find(path, pattern) nhận tham số đầu vào là đường dẫn đến thư mục và từ khoá tìm file. In ra màn hình
danh sách các file có tên file bắt đầu với pattern

'''