# 学习笔记
## 安装
pip3 install django==2.2.13

## 创建项目
django-admin startproject douban
## 创建应用
python3 manage.py startapp index
## 启动应用程序
python3 manage.py runserver
默认是127.0.0.1：8000
python3 manage.py runserver 0.0.0.0:80  指定ip和端口
结束启动，用control+c
# 创建数据库表
$ python3 manage.py makemigrations 
$ python3 manage.py migrate

## 文档
https://docs.djangoproject.com/zh-hans/3.1/