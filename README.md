# **내편** : 전국 편의점 상품 공유 플랫폼 <br>- Project NP

---

## 기획 의도

   > Covid-19 의 확산으로 편의점 이용객 수는 급증했지만 웹, 모바일 서비스는 상당히 부실해 원하는 상품이 근처 편의점에 없어 일일이 주변 편의점을 찾아야 하는 불편함이 있었습니다. 이를 개선하고자 전국 각각의 편의점 제품 목록과 재고를 한눈에 확인하고, 더 나아가 편의점 음식으로 나만의 레시피를 공유할 수 있는 커뮤니티, 예약 등을 함께 누릴 수 있는 서비스를 기획하게 되었습니다.  

<br/>


## Environment
> Language  : Python 3.8.5 <br/>
Framework   : Django 3.1.1  <br/>
Database    : PostgreSQL 12<br/>
Server      : Heroku 3.1.1 <br/>
IDE         : VS Code <br/>
OS          : Window 10

<br>


<br/>

## Project NP
+ **Project NP 기능**
   + 편의점 상품 검색 및 비교
   + 편의점 상품 예약
   + 내 주변 편의점 검색
   + 커뮤니티 (편의점 레시피)

+ **프로젝트 구조**
   ```
   ProjectNP
   ┗━config             # root, admin 관련 Configuration
   ┗━myside             # 편의점 상품 조회, 예약 등 메인 기능 관련
   ┗━post               # 커뮤니티 (나만의 편의점 레시피, 꿀팁 등 공유)
   ┗━venv
   ┗━db.sqlite3
   ┗━manage.py          # runserver 등 웹 서버를 실행하고 관리하는 기능
   ```

      
+ **프로젝트 실행하기**
   + **가상환경 세팅**<br>
      아래의 명령어를 실행하여 가상환경을 생성합니다.
      ```
      $ python -m venv [가상환경 이름]
      ```

      가상환경을 활성화합니다.
      ```
      $ source [가상환경 이름]/Scripts/activate    #윈도우 bash shell
      $ source [가상환경 이름]/bin/activate        #리눅스, 맥
      ```

      가상환경을 비활성화합니다.
      ```
      $ deactivate
      ```

   + **Requirements 로 패키지 관리** <br>
      가상환경이 실행되었다면 패키지 설치를 합니다.
      ```
      $ pip install -r requirements.txt
      ```
      이후 설치 파일이 있으면 아래와 같이 requirement.txt 에 추가합니다.
      ```
      $ pip freeze > requirements.txt
      ```

   + 서버 실행하기
      ```python
      $python manage.py runserver
      ```

   + 마이그레이션 파일 생성
      ```python
      $python manage.py makemigrations [app 이름]
      ```  

   + 마이그레이션 파일 DB에 적용
      ```python
      $python manage.py migrate [app 이름] [migration 이름]
      ```

   + 마이그레이션 적용 상태 조회
      ```python
      $python manage.py showmigrations [app 이름] [migration 이름]
      ```

   + sql 쿼리 확인
      ```python
      $python manage.py sqlmigrations [app 이름] [migration 이름]
      ```  
