* Third-party libraries
* *requests* library
* Virtual Environment
* **FB Console**

## 1 Third-party libraries

![](https://raw.githubusercontent.com/mto/python-course/master/Session4/material/pypi_index.png)

### 1.1 *Pip* & *PyPI*

Tạo file *requirements.txt* với nội dung

```shell
requests==2.13.0
```

và chạy command sau trên console

```shell
pip install -r requirements.txt
```


* Pip: Công cụ quản lý third-party dependencies trong Python
* PyPI: Remote repo chứa third-party dependencies


| Programming Language | Dependency Management | DM files |
|---|---|---|
|Python|pip|requirements.txt|
|Java|Maven/Gradle|pom.xml/build.gradle|
|C/C++|CMake/Ninja|Makefile/.ninja|
|JavaScript/NodeJS|npm|package.json|
|PHP|Composer|composer.json|
|Ruby|Bundler|Gemfile|
|C#|Nuget|.csproj|

### 1.2 *site-packages* folder

*Third-party dependencies được cài vào thư mục *site-packages**

### 1.3 Phương pháp lựa chọn libraries

* *Vừa đủ* với nhu cầu dùng
* Tần suất release trên GitHub
* *license* & *pricing*

## 2 Library *requests*

http://docs.python-requests.org/en/master/

Thực thi đoạn code sau đây

```python
import requests

res = requests.get('http://google.com')
print(res.text)
print("Check type")
print(type(res))
```

**Requests: HTTP client library**

__**Bài tập 1:**__

*Viết script dùng *requests* lấy và in ra màn hình content HTML nội dung trang chủ trang VNExpress*

__**Bài tập 2:**__

*Viết script lấy nội dung 1 bài báo trong mục *Thời sự* trên VNExpress*

__**Chú ý:**__

Có thể dùng thư viện *beautifulsoup4* cho việc bóc tách dữ liệu HTML

https://pypi.python.org/pypi/beautifulsoup4

### 2.1 Tìm hiểu *HTTP protocol* qua trình duyệt Firefox/Chrome

https://tools.ietf.org/html/rfc2616

Specification của HTTP protocol khoảng 200 trang!!!

NHƯNG:
**Cách tìm hiểu các kiến thức cơ bản về HTTP nhanh nhất cho người chưa biết gì là thông qua trình duyệt**

![](https://raw.githubusercontent.com/mto/python-course/master/Session4/material/vnexpress_firebug.png)

__**Bài tập 3:**__

*Xem các HTTP requests bằng công cụ Firebug/Inspect trên FireFox/Chrome khi truy cập vào trang *e.vnexpress.net**



__**Bài tập 4:**__

*Bật chức năng dịch của Google với trang *e.vnexpress.net* và xem các AJAX requests liên quan đến chức năng dịch*

__**Bài tập 5:**__

*Lấy ra danh sách video links trên trang *video.vnexpress.net**

__**Bài tập 6:**__

*Tải 5 videos đầu tiên trong danh sách videos ở bài tập 5 về máy, tên file được cắt ra từ link video*

## 3 Virtual Environment

![](https://raw.githubusercontent.com/mto/python-course/master/Session4/material/virtual_environment.jpg)

__Vấn đề với Pip:__

*Pip cài đặt third-party dependencies trực tiếp vào thư mục sites-package*

-> Dependencies versions conflict RISK

### 3.1 Cài đặt *virtualenv*

https://virtualenv.pypa.io/en/stable/

```shell
mkdir VIRTUAL_ENVs
cd VIRTUAL_ENVs

virtualenv ${YOUR_VIRTUAL_ENV_NAME}
source ${YOUR_VIRTUAL_ENV_NAME}/bin/activate
```

__**Bài tập 7:**__

*Cài đặt *virtualenv* với tên *python-course* và chạy lại các bài tập trước trên virtual environment này*

### 3.2 Cài đặt *VirtualEnv* trên *PyCharm*

![](https://raw.githubusercontent.com/mto/python-course/master/Session4/material/venv_pycharm.png)

Vào Preferences->Project -> Project-Interpreter -> Click Setting để cài đặt virtual environment cho PyCharm

## 4 **FB Console**

*Ứng dụng làm việc với Facebook API phát triển đến hết khoá học*

__**Công nghệ:**__

* Python Prompt Toolkit
* requests
* sqlalchemy

### 4.1 Tạo project & virtual environment

* Tạo thư mục *fbcli* có chứa file *requirements.txt*
* Tạo virtualenv *fbcli* trong thư mục VIRTUAL_ENVs

### 4.2 Tạo GitHub repo

Tạo repository *fbcli* trên GitHub với tài khoản đã đăng ký

```
cd fbcli
git init
git remote add origin git@github.com:{account_name}/fbcli.git
```