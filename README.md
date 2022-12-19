# Django 실행 방법
## 1. 파이썬 가상환경 설치하기
```
pip install virtualenv
python3 -m venv env
```
python3, python 으로 가상환경이 설치가 안될 경우에는 python이 설치되었는지 확인해보기

- python3
- python

입력 후 파이썬 버전이 나오면 설치가 되어있는 것임
안되어있으면 Python 공식홈페이지에서 파이썬 3.8.10 버전 설치하기.

## 2. 가상환경 들어가기
```
(Window)
env/Scripts/activate.bat

(Mac)
source env/bin/activate
```

## 3. django 설치하기
```
pip install django==3.2.14
```

## 4. 실행하기
```
python manage.py runserver
```

## 5. 실행 종료하기
터미널에서 Ctrl + C를 누르면 종료됩니다.
