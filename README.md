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
$ python functional_tests.py

# 執行單元測試
$ python manage.py test
```

## TDD 流程
- 功能測試 (使用者觀點)
- 單元測試 (程式員觀點)
- 單元測試/編程週期
- 重構
![The TDD process with functional and unit tests](https://www.obeythetestinggoat.com/book/images/twp2_0404.png)

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