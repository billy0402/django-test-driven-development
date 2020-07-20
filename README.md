# django-test-driven-development

## environment
- [macOS 10.15.6](https://www.apple.com/tw/macos/catalina/)
- [PyCharm 2020.2.1](https://www.jetbrains.com/pycharm/)
- [Python 3.8.5](https://www.python.org/)
- [Django 3.1.3](https://www.djangoproject.com/)
- [Selenium 3.141.0](https://github.com/SeleniumHQ/selenium)

## [Book](https://www.obeythetestinggoat.com/pages/book.html)

## test command
```shell script
# 執行 Django 開發伺服器
$ python manage.py runserver

# 執行功能測試
$ python functional_tests.py

# 執行單元測試
$ python manage.py test
```

## 單元測試/編程週期
1. 在終端機，執行單元測試，並查看它們失敗的原因
2. 在編輯器，修改最少量的程式，來處理目前的測試失敗
3. 重複做！