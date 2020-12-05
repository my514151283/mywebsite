#环境
ubuntu18
anaconda3
python3.7
django2.2.5
uwsgi2.0.18
nginx1.14
mysql5.7.29

#安装django
这里使用的anaconda安装的
```
conda install django
```
#安装nginx
```
apt-get update
apt-get upgrade
apt-get install nginx
```
#安装uwsgi
```
conda config --add channels conda-forge
conda install uwsgi
conda install -c conda-forge libiconv
```
如果不装libiconv，在uwsgi启动的时候可能会出错。
#配置uwsgi
服务器项目下创个文件夹方便管理
![目录](https://upload-images.jianshu.io/upload_images/8111720-397b8524d5b6cff2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
其中nginx_conf.conf是nginx的配置文件，uwsgi_conf.ini是uwsgi的配置文件，logs目录下前两个是nginx的日志文件，最后一个是uwsgi的日志文件，这个文件可以用来看看启动是否抛出异常。
首先看uwsgi的配置
```
[uwsgi]
# ip和端口号
socket = 0.0.0.0:host  # 只需要改开放的端口
# 项目根目录
chdir = /home/xxx/to/project  # 需要改
# 项目中wsgi.py的位置，相对根目录的路径
wsgi-file = appname/wsgi.py  # 需要改
# 进程数
processes = 1
# 线程数
threads = 2
# uwsgi服务器端角色
master = True
# 存放进程编码文件
pidfile = uwsgi.pid  # 看情况改
# 日志文件
daemonize = logs/uwsgi.log  # 需要改
# 指定虚拟环境所在目录，不能填写相对目录
# virtualenv = /
# 请求的最大size
# buffer-size = 65535
```
需要改的地方根据实际情况改一下就行了
#  启动uwsgi
首先cd到刚才配置文件的目录
```
uwsgi --ini uwsgi_conf.conf
```
如果要停掉uwsgi就
```
uwsgi --stop uwsgi.pid
```
uwsgi.pid在配置文件中设置了。
如果不小心多启动了几次uwsgi导致启动失败可以通过
```
fuser -k host/tcp
```
来关掉
启动完可以看看日志文件是否启动成功了，启动时如果出现数据库方面的错误可以把项目中setting.py文件中数据库先注释掉。
#启动nginx
首先看下nginx的配置文件
```
server {
    listen      80;
    server_name x.x.x.x;  # 公网ip
    charset     utf-8;
    client_max_body_size 75M;

    access_log  /home/xxx/to_access.log;  # 看情况改
    error_log   /home/xxx/to_error.log;  # 看情况改

    location /static {
        root    /home/xxx/toproject/appname;  # 静态文件根目录
    }
    location / {
        include /etc/nginx/uwsgi_params;
        uwsgi_pass 127.0.0.1:host;  # 根据情况改端口，前面ip不用改
        uwsgi_read_timeout 2;
    }
}
```
然后把配置文件cp到/etc/nginx/conf.d文件夹下面
通过下面指令测试配置的语法是否正确
```
nginx -t -c /etc/nginx/nginx.conf
```
注意检测的是/etc/nginx/nginx.conf这个文件而不是/etc/nginx/conf.d下的配置文件，因为这才是包含所有内容的配置文件，但是它把刚才的配置文件include了进去，单独检测上面的配置文件肯定是会出错的。
然后启动nginx
```
nginx
```
如果不小心多启动了几次nginx导致启动失败也可以通过
```
fuser -k 80/tcp
```
来关掉
另外其他一些nginx指令
```
# 重新载入
nginx -s reload
# 停止nginx
nginx -s stop
# 重启nginx
nginx -s reopen
```
# 修改项目的setting文件
```
DEBUG = False
ALLOWED_HOSTS = ['x.x.x.x']  # 公网ip
```
到这里网页就可以通过公网ip访问到了
# 连接数据库
安装mysql
```
sudo apt-get install mysql-server
sudo apt-get install mysql-client
sudo apt-get install libmysqlclient-dev
```
给root加密码，首先登陆
```
mysql -u root -p
```
输入任意密码就能进入
```
use mysql;
update user set authentication_string=PASSWORD("密码") where user='root';
update user set plugin="mysql_native_password";
flush privileges;
quit;
```
之后登陆就需要用这次设置的密码了。
启动mysql服务
```
service mysql restart
```
安装python和mysql的连接模块
```
conda install mysqlclient
```
最后配置一下setting.py文件
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xxxx',  # 数据库名
        'USER': 'root',
        'PASSWORD': 'xxxxxx',  # 密码
        'HOST': '127.0.0.1',  # 不用改
        'PORT': '3306'
    }
}
```
在app下
```
python manage.py makemigrations 
python manage.py migrate
```
重启下uwsgi和nginx就可以了。
# navicat远程连接数据库
新建连接下勾选使用ssh通道，配置公网ip用户名和密码，在常规里配置数据库的用户名和密码，localhost不用改。

