# **내편** : 내 손 안에 모든 편의점 <br>- Project NP 전국 편의점 상품 공유 플랫폼


## 기획 의도

   > Covid-19 의 확산으로 편의점 이용객 수는 급증했지만 소비자가 원하는 상품이 근처 편의점에 없어, 일일이 주변 편의점을 찾아다녀야 하는 불편함이 있었습니다. 또한 현재 편의점 자사 웹, 모바일 서비스는 실시간 업데이트도 되지 않으며 소비자를 고려하지 않은 기능, 디자인으로 이용객의 수가 현저히 적었습니다.
   이를 개선하고자 저희 대학생 프로젝트 팀 '내편'은 전국 각각의 편의점 제품 목록과 해당 상품 재고가 있는 편의점 위치를 한눈에 확인하고, 더 나아가 편의점 음식 조합을 공유하거나 솔직한 후기를 나눌 수 있는 커뮤니티, 상품 예약 서비스 등을 누릴 수 있는 플랫폼을 기획 및 개발 중입니다.

<br/>


## Environment
> Language  : Python 3.8.5 <br/>
Framework   : Django 3.1.1  <br/>
Database    : PostgreSQL 12<br/>
PaaS        : AWS RDS
Server      : AWS EC2 - Ubuntu 18.04 <br/>
Storage     : AWS S3
IDE         : VS Code <br/>
OS          : Window 10

<br>


<br/>

## Project NP
+ **Project NP 기능**
   + 편의점 상품 검색 및 재고 확인
   + 내편찾기     : 내 주변 편의점 검색 및 내편으로 등록 기능
   + 할인행사     : 편의점 행사상품 검색
   + 커뮤니티     : 편의점 레시피 공유 및 솔직 후기 소통
   + Brand Story : 프로젝트 소개, 내편 팀 소개
<br>
<br>

+ **프로젝트 구조**
   ```
   ProjectNP
   ┗━accounts           # 유저 정보관리
   ┗━community          # 커뮤니티 게시판 (나만의 편의점 레시피, 꿀팁 등 공유)
   ┗━config             # root, admin 관련 Configuration
   ┗━media              # 상품사진, 댓글 사진, 프로필 사진등 media 파일 관리
   ┗━mycvs              # 지도에서 편의점 조회, 즐겨찾는 편의점(내편) 등록 및 삭제
   ┗━myside             # 편의점 상품 조회, 예약 등 메인 기능 관련
   ┗━static             # css, js, logo 디렉터리
   ┗━templates          # BASE Templates

   ┗━Procfile           # 배포 시 웹사이트 시작하기 위해 실행할 명령 순서
   ┗━manage.py          # runserver 등 웹 서버를 실행하고 관리하는 기능
   ┗━requirements.txt   # 패키지 설치 파일 목록
   ┗━runtime.txt        # python version
   ```
<br>

      
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
      아래는 config/settings/init.py 로 자동으로 실행되기 때문에 굳이 실행할 필요 없습니다.
      <br>
      가상환경안에 개발 모드로 실행하기 위한 환경변수를 등록합니다.
      ```
      $ DJANGO_SETTINGS_MODULES=config.settings.debug
      ```

      배포환경에서 실행하기 위해서는 환경변수를 아래와 같이 바꿔줍니다.
      ```
      $ DJANGO_SETTINGS_MODULES=config.settings.deploy
      ```
      <br>

   + **Requirements 로 패키지 관리** <br>
      가상환경이 실행되었다면 패키지 설치를 합니다.
      ```
      $ pip install -r requirements.txt
      ```
      이후 설치 파일이 있으면 아래와 같이 requirement.txt 에 추가합니다.
      ```
      $ pip freeze > requirements.txt
      ```
      <br>

   + **서버 실행하기**
      ```python
      $ python manage.py runserver
      ```
      <br>


   + **마이그레이션** <br>
      마이그레이션 파일 생성
      ```python
      $ python manage.py makemigrations [app 이름]
      ```  

      마이그레이션 파일 DB 에 적용
      ```python
      $ python manage.py migrate [app 이름] [migration 이름]
      ```

      마이그레이션 적용 상태 조회
      ```python
      $ python manage.py showmigrations [app 이름] [migration 이름]
      ```

      sql 쿼리 확인
      ```python
      $ python manage.py sqlmigrations [app 이름] [migration 이름]
      ```  

   + **React 서버 실행하기** <br>
      필수사항 : yarn 다운로드
      
      url : https://classic.yarnpkg.com/en/docs/install/#windows-stable

      터미널에서 + 버튼을 눌러서 새로운 터미널 생성

      frontend 폴더로 들어가기
      ```
      $ cd frontend
      ```
      
      라이브러리 다운
      ```
      $ yarn add axios
      $ yarn add react-router-dom
      ```

      서버 실행하기
      ```
      $ yarn start
      ```

      리액트 서버가 장고 서버와 따로 독립적으로 틀어집니다.