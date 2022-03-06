# Django_Instagram

### 1. 피드 생성
- templates/instagram/main.html
- content/models.py
- content/views.py -> img 파일 저장 기능
- AJAX
- 모달
- 이미지 드래그 & 드롭
- Django_MEDIA 폴더 기능

 ### 2. 피드 목록 불러오기
- templates/instagram/main.html
- content/models.py
- content/views.py


### 3. 회원가입
### 4. 로그인
### 5. 좋아요
### 6. 댓글
### 7. 북마크
### 8. 프로필 페이지
### 9. 프로필 사진 변경
### 10. 피드 목록 필터 조회


## 기타
### Django REST framwork
 - DRF(Django Rest Framework)란Django 안에서 RESTful API 서버를 쉽게 만들게 도와주는 라이브러리다.

### 아이콘
- 구글 머티리얼 아이콘
https://fonts.google.com/icons
```
 <link
    href="https://fonts.googleapis.com/css?family=Material+Icons|Material+Icons+Outlined|Material+Icons+Two+Tone|Material+Icons+Round|Material+Icons+Sharp"
    rel="stylesheet">
```
- 아이콘을 여러개 불러올때 위의 코드처럼 여러개를 묶어 가져와야함

### Django ORM
- 객체(Object)와 관계형 데이터베이스(Relational)을 연결(Mapping)해 주는 것을 의미
- 데이터베이스의 테이블을 객체(Object)와 연결하여 테이블에 CRUD를 할 때, SQL 쿼리를 사용하지 않고도, 가능하게 하는 것

### 모달 vs 팝업
- 팝업 : 새로운 브라우저창이 생성되 정보를 전달
- 모달 : 현재 브라우저의 부모 자식관계의 창을 생성
- templates/instagram/main.html

### 이미지 드래그 & 드롭
- templates/instagram/main.html
- https://kutar37.tistory.com/entry/HTML5-Javasciprt-DragDrop-%EA%B5%AC%ED%98%84-%EC%98%88%EC%A0%9C

### AJAX -> 파일업로드
- 비동기 자바스크립트와 XML -> 동적 웹 페이지를 만들어 주기위함
- content/views.py
- templates/instagram/main.html

### Django_MEDIA 폴더 기능
- 파일서버가 없을시 img, 등의 파일들을 저장할수 있는 기능
- instagram/settings.py
- instagram/urls.py
- media 디렉토리 생성
