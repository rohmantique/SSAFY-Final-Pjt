## 영화 플젝 User Story

-----------------

1. 서버 접속 & 로그인 페이지 (accounts/login.html)

   - MoodInside 로고

   - username, password 받는 로그인 폼

   - 회원가입 버튼, 로그인 버튼


2. 회원가입 페이지 (accounts/signup.html)

   - 사용자로부터 받을 데이터: username, nickname, password, password2

   - 회원가입 완료 버튼 누르면 홈 화면 (accounts/login.html)으로 이동
   

4. 로그아웃시 accounts/login.html 로 이동

   - 별도 페이지 없음


5. 감정상태 선택 페이지 (movies/mood_select.html)

   - Dropdown으로 6개의 감정 옵션: happy, hungry, low, chill, bored, stressed, savage

   - 하나의 감정상태 선택 시 Movie 클래스 중 해당 감정상태를 필드값으로 갖고 있는 영화 리스트들을 보여주는 movies/index.html으로 이동


6. 영화 추천 페이지 (movies/index.html)
   
   - 상단 nav bar에 프로필 (accounts/profile.html)로 이동하는 버튼

   - 영화는 row 당 카드 3개 & 보여지는 정보는 poster, title, grade

   - 선택한 감정상태에 해당하는 영화들 중 보관함에 저장한 영화가 있다면 한꺼번에 맨 위 출력 (Movie 클래스 bookmark 필드)

   - 보관함에 저장되어 있지 않고 평가하지 않은 영화들 중, 선택한 감정상태와 연결되어 있는 영화들 평점 순으로 내림차순 출력

   - 영화 card를 클릭하면 영화 상세 페이지(movies/detail.html)로 이동

   
6. 영화 상세 페이지 (movies/detail.html)

   - 상단 nav bar에 프로필 (accounts/profile.html)로 이동하는 버튼

   - poster | title | release_date[:4] (year만 사용) | genres (복수일 시 `\`로 구분)

   - grade | ('총 리뷰 개수')

   - 평가하기 (star icon) (reviews/create_review.html로 이동) | 저장하기 (plus-circle-dotted) --> 평가함 (star-fill) | 저장함 (check-circle-fill)

   - 줄거리 overview

   - 한줄평 created_at 내림차순 출력: (line 1) score | user.username; (line 2) content;
   

7. 리뷰 작성 페이지 (reviews/create_review.html)

   - content, grade, created_at, updated_at -> grade, content만 사용자가 직접 작성

   - 리뷰 수정 가능합니다. (reviews/review_update.html)

   - 리뷰 삭제 가능합니다.
   

8. 사용자 프로필 페이지 (accounts/profile.html)

   - 닉네임

   - 프로필 수정 (닉네임 수정)

   - 사용자가 저장한 영화 정보 출력 (3개 + 더보기 a 태그)

   - 사용자가 작성한 리뷰 출력
   

9. 사용자 계정 정보 페이지 (accounts/update.html)

   - 회원 탈퇴