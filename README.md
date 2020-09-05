# **내편** - 전국 편의점 상품 공유 플랫폼

## 기획 의도
   > Covid-19 의 확산으로 편의점 이용객 수는 급증했지만 웹, 모바일 서비스는 상당히 부실해 원하는 상품이 근처 편의점에 없어 일일이 주변 편의점을 찾아야 하는 불편함이 있었습니다. 이를 개선하고자 전국 각각의 편의점 제품 목록과 재고를 한눈에 확인하고, 더 나아가 편의점 음식으로 나만의 레시피를 공유할 수 있는 커뮤니티, 예약 등을 함께 누릴 수 있는 서비스를 기획하게 되었습니다.  

<br/>

## Project NP 기능 설명
   1. 편의점 상품 검색 및 비교
   2. 편의점 상품 예약
   3. 내 주변 편의점 검색
   3. 커뮤니티 (편의점 레시피)

<br/>

## Environment
> Language  : Python 3.8.5 <br/>
Framework   : Django  <br/>
IDE         : VS Code <br/>
Database    : PostgreSQL 12<br/>
Server      : Heroku 3.1.1 <br/>
OS          : Window 10


## 프로젝트 실행하기
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
