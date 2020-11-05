# django-test-driven-development

## environment
- [macOS 10.15.6](https://www.apple.com/tw/macos/catalina/)
- [PyCharm 2020.2.1](https://www.jetbrains.com/pycharm/)
- [Python 3.8.5](https://www.python.org/)
- [Django 3.1.3](https://www.djangoproject.com/)
- [Selenium 3.141.0](https://github.com/SeleniumHQ/selenium)

## [Book](https://www.obeythetestinggoat.com/pages/book.html)
![Test ALL the things](https://www.obeythetestinggoat.com/book/images/twp2_0401.png)

## test command
```shell script
# 執行 Django 開發伺服器
$ python manage.py runserver

# 執行功能測試
$ python manage.py test functional_tests

# 執行單元測試
$ python manage.py test app.todos
```

## TDD 流程
- 功能測試 (使用者觀點)
- 單元測試 (程式員觀點)
- 單元測試/編程週期
- 重構
![The TDD process with functional and unit tests](https://www.obeythetestinggoat.com/book/images/twp2_0701.png)

## 單元測試/編程週期
1. (紅燈) 編寫失敗的單元測試
2. (綠燈) 編寫最簡單的代碼使其通過 (作弊)
3. (重構) 重構以獲取更有意義.更好的代碼
    1. 消除重複
    2. 三角關係 (編寫另一個測試)

## 單元測試典型結構
1. 設置 (Setup)
2. 執行 (Exercise)
3. 斷言 (Assert)
    
## Don’t Repeat Yourself (DRY)
`不要寫出重複的程式`
- 重複兩次 >> 可能重構，太早重構
- 重複三次 >> 必須重構，立即重構

## You ain’t gonna need it! (YAGNI)
`你不會需要它！`
```
永遠在真正需要它們時，才實現它們，
永遠不要在僅僅預想到需要它們時，就實現它們。
```

## 測試機部署

### 安裝環境
```shell
$ sudo vim /etc/hosts
127.0.0.1 localhost superlists-staging.edu.tw

$ sudo pacman -S git python python-pipenv
```

### 安裝專案
```shell
$ export SITENAME=superlists-staging.edu.tw

$ echo $SITENAME

$ git clone https://github.com/billy0402/django-test-driven-development.git ~/sites/$SITENAME

$ cd ~/sites/$SITENAME

$ pipenv install 

$ pipenv shell

$ python manage.py migrate --noinput

$ python manage.py runserver

$ STAGING_SERVER=$SITENAME python manage.py test functional_tests --failfast
```

### [安裝網頁伺服器](https://wiki.archlinux.org/index.php/Nginx)
```shell
$ sudo pacman -S nginx

$ systemctl enable --now nginx

$ su -

$ mkdir -p /etc/nginx/sites-available/

$ vim /etc/nginx/sites-available/$SITENAME.conf

$ mkdir -p /etc/nginx/sites-enabled/

$ ln -s /etc/nginx/sites-available/$SITENAME.conf /etc/nginx/sites-enabled/$SITENAME.conf

$ readlink -f $SITENAME.conf

$ vim /etc/nginx/nginx.conf
include /etc/nginx/sites-enabled/*;

$ systemctl reload nginx

$ nginx -t
```

### 準生產部署
```shell
$ python manage.py collectstatic --noinput

$ gunicorn core.wsgi:application

$ set -a; source .env; set +a

$ gunicorn core.wsgi:application --bind unix:/tmp/$SITENAME.socket
```

### 開機時啟動
```shell
$ sudo vim /etc/systemd/system/gunicorn-superlists-staging.edu.tw.service

$ sudo systemctl daemon-reload

$ sudo systemctl enable --now gunicorn-superlists-staging.edu.tw
```