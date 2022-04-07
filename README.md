# Section3project
국민건강증진을 위한 운동추천 서비스 앱 구현

- 프로젝트 기간 : 211006-211012
- 데이터 출처 : NITHILAA가 kaggle에 업로드한 ‘[Fitness Analysis](https://www.kaggle.com/datasets/nithilaa/fitness-analysis)’
- 사용된 Skills : PostgreSQL, FLASK, HTML, Bootstrap, HEROKU, METABASE, Docker, machine learning
- 주제 : 개인에게 적합한 운동을 추천해 줄 수 있는 웹서비스 Fitness App을 구현합니다.
  - 데이터베이스와 API 서비스, 대시보드 개발 및 배포까지의 데이터 파이프라인을 구축합니다.
  - 머신러닝으로 구현된 추천 알고리즘이 서비스화되도록 합니다.


### 파일설명
- heroku : 헤로쿠 배포에 필요한 파일모음
  - flask_app : flask app을 실행하는 데 필요한 코드
  - Procfile : 헤로쿠 배포를 위해 사용할 웹서버
  - requirements : 앱을 실행하기 위해 설치되어야 할 모듈
- fitness.csv : 전처리가 끝난 원본 데이터셋
- fitness_export.csv : PostgreSQL 데이터베이스 서버에서 추출한 데이터셋
- postgre.py : 데이터베이스 서버에 테이블을 생성하고 데이터를 저장하는 코드
- postgre_export.py : 서버에 저장된 데이터를 적절하게 추출해서 로컬에 저장하는 코드
- predict.py : 데이터베이스에서 추출된 데이터셋으로 모델링 후 모델을 pickle파일로 추출하는 코드 
