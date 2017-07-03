* Làm việc với JSON trong Python
* Làm việc với Facebook Graph API thông qua *requests*
* *Debug* trong Python

## 1. Làm việc với JSON

```javascript
{
      "message": "Looking forward to 2010!",
      "actions": [
        {
          "name": "Comment",
          "link": "http://www.facebook.com/X999/posts/Y999"
        },
        {
          "name": "Like",
          "link": "http://www.facebook.com/X999/posts/Y999"
        }
      ],
      "type": "status",
      "created_time": "2010-08-02T21:27:44+0000",
      "updated_time": "2010-08-02T21:27:44+0000"
}
```

### 1.1. Module [*json*](https://docs.python.org/3/library/json.html)

*json* cung cấp phương thức cho phép convert data với định dạng JSON sang Python object và ngược lại

* *load/loads*: JSON data -> Python object
* *dump/dumps*: Python object -> JSON data

Chạy các đoạn code sau

```python
import json

s = '{"name":"Nguyen Van A", "age":30}'
obj = json.loads(s)
print(obj.get('name'))

```

và

```python
import json

obj = {'name': 'Nguyen Van A', 'age':30}
print(json.dumps(obj))
```

**__Bài tập 1:__**

*Dùng *json* module convert **fb_sample.json** sang Python object rồi in ra màn hình các Facebook messages có trong nội dung file **fb_sample.json***

**__Bài tập 2:__**

*Dùng *json* module để fork nội dung file **fb_sample.json** sang file **fb_sample_bis.json**, trong đó các trường **actions** được lược bỏ*

## 2. Facebook Graph API

![](https://raw.githubusercontent.com/mto/python-course/master/Session5/material/fb_graph_api.png)

* RESTful API cho phép tương tác với dữ liệu Facebook
* Authorization với *access_token*

```python
import requests

atoken = '.......'

res = requests.get('https://graph.facebook.com/me', params={'access_token':atoken})
```


__NOTE:__

*Việc tích hợp **Login Flow** với ứng dụng desktop sẽ được xử lý trong các buổi học sau. Trong buổi học này ta sẽ tạo **access_token** thông qua **Facebook Graph Explorer***

### 2.1. Lấy *access_token*

Truy cập vào trang *Graph API Explorer* với link

![](https://raw.githubusercontent.com/mto/python-course/master/Session5/material/fb_graph_api.png)

* Click *Get Token*
* Chọn *Get User Access Token*
* Chọn các options về permissions như trong screenshot dưới đây
* Click *Get Access Token*

![](https://raw.githubusercontent.com/mto/python-course/master/Session5/material/permissions.png)

**__Bài tập 3:__**

*Tạo access token thông qua công cụ **Facebook Graph Explorer***

### 2.2. Thông tin cá nhân

```curl
GET https://graph.facebook.com/me?access_token=...
```

**__Bài tập 4:__**

*In ra màn hình Facebook ID của tài khoản Facebook đã dùng để tạo access token*

### 2.3. Danh sách friends

```curl
GET https://graph.facebook.com/{FACEBOOK_ID}/friends?access_token=
```

**__Bài tập 5:__**

*In ra màn hình danh sách 10 Facebook friends đầu tiên trong list friends*


### 2.4. Danh sách groups

```curl
GET https://graph.facebook.com/{FACEBOOK_ID}/groups?access_token=...
```

**__Bài tập 6:__**

*In ra màn hình danh sách các Facebook groups mà tài khoản FB hiện tại đang manage*

### 2.5. Danh sách posts

```curl
GET https://graph.facebook.com/{FACEBOOK_ID}/posts?access_token=...
```

**__Bài tập 7:__**

*In ra màn hình danh sách các bài posts được tạo ra từ tài khoản hiện tại*

## 3. Facebook Console

Tạo tài khoản GitHub và Git repository *fbcli* theo hướng dẫn trong bài học trước. Tiếp theo chạy command sau

```shell
git clone git@github.com:{GITHUB_ACCOUNT}/fbcli.git

cd fbcli
```


**__Bài tập 8:__**

*Tạo file **fb_sdk.py** trong thư mục **fbcli** và implement các method như dưới đây, sau đó commit code và push lên GitHub*

```python
import requests

class FacebookSDK(object):

    def __init__(self, access_token):
        self.atoken = access_token

    def me(self):
        pass

    def friends(self):
        pass

    def groups(self):
        pass

    def posts(self):
        pass

```

## 4. *Debug* trong Python

*Debug*: Phương pháp *nội soi* tiến trình chạy của chương trình

* Cho phép **treo tạm thời** chương trình ở các **vị trí** mong muốn
* Cho phép lấy thông tin chi tiết và điều khiển tiến trình chạy của chương trình khi **treo tạm thời**
* Công cụ không thể thiếu để **reproduce** các vấn đề **concurrency**

![](https://raw.githubusercontent.com/mto/python-course/master/Session5/material/debug_pycharm.png)
