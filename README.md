XIn Chao Thay, Hom nay em se trinh bay demo Login don gian bang Facebook


Project su dung:
Ubuntu18.6
Python3.6
Django==2.2.6


**** Cai dat chuong trinh

Git Repo : git clone https://github.com/peter-dinh/login-oauth-django.git

+ Tao moi truong cai dat thu vien
$ virtualenv -p python3.6 env 

+ Active moi truong
$ source env/bin/activate

+ Cai dat thu vien
$ pip install -r req.txt

+ Cai dat database
$ python manage.py migrate

+ Run project
$ python manage.py runserver

+ Create Admin User
$ python manage.py createsuperuser


**** Chay Demo tinh nang

+ Dang nhap bang Facebook

+ Bo sung thong tin

+ Login lai

+ Update thong tin

+ Activity Update


Bai trinh bay cua em ket thuc tai day. Cam on thay da theo doi.


Con Phan Admin.
http://localhost:8000/admin/

User social auths > Record > infomation

Change KEY API IN `app/setting`