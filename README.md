### 소준호

### 회원 인증 및 사용자 프로필
- Django의 `AbstractUser`를 상속한 Custom User Model 구현
- 회원가입 및 회원정보 수정 Form 구현
- 회원가입·로그인·로그아웃 기능 구현
- 회원정보 수정 및 회원 탈퇴 기능 구현
- 비밀번호 변경 기능 구현
- 사용자 모델에 추가 정보 필드를 구성하여 사용자 정보 커스터마이징
- 로그인한 사용자의 개인 프로필 조회 기능 구현
- `login_required` 및 HTTP Method 제한을 활용한 인증 기능의 접근 권한 제어

## 학습 내용
- Django의 기본 User Model과 `AbstractUser`를 활용한 Custom User Model 구현 방법
- Django Form을 활용한 회원가입 및 회원정보 수정 데이터 검증
- 회원가입·로그인·로그아웃 등 Django 인증 시스템 사용 방법
- `authenticate()`, `login()`, `logout()`을 활용한 사용자 인증 및 세션 관리
- 회원정보 수정 및 비밀번호 변경 처리 방법
- 로그인 여부에 따른 페이지 접근 권한 제어 방법
- `login_required` 및 HTTP Method 제한 데코레이터를 활용한 접근 제어
- 사용자별 프로필 정보를 조회하고 관리하는 방법

## 느낀 점





### 김유민 

### 도서 관리
- Django ORM을 활용한 Book Model 구현
- ModelForm 기반 도서 데이터 검증
- 도서 생성·조회·수정·삭제 기능 구현
- 로그인 여부 및 HTTP Method에 따른 접근 권한 제한

### 생성형 AI 연동
- 도서 등록 시 Wikipedia API를 이용한 작가 정보 및 이미지 검색
- gpt-5-nano를 활용한 작가 설명과 대표 작품 생성
- AI 응답을 JSON으로 파싱하여 데이터베이스에 저장
- API 호출 및 JSON 파싱 실패에 대한 예외 처리

## 학습 내용
- Django Model과 ORM 사용 방법
- ModelForm을 통한 입력 데이터 검증
- GET과 POST 요청을 구분하는 방법
- login_required 및 require_POST를 활용한 접근 제어
- 외부 API 호출 및 JSON 응답 처리
- API Key를 환경변수로 관리하는 방법

## 느낀 점
도서 CRUD 기능을 개발하며 각 html과 파일 사이의 데이터 흐름을 이해할 수 있었다.
특히 외부 API는 항상 정상적인 데이터를 반환한다고 가정할 수 없기 때문에 Timeout, 
검색 결과 없음, JSON 파싱 실패 등을 고려한 예외 처리가 중요하다는 점을 배웠다.
