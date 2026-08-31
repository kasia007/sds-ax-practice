https://ucanlabs.kr/classroom/sds-ax/lesson/1114/

### 실습 코드 완성

git add .
git commit -m "day5 완료" # 커밋 메시지는 자유
git push # 커밋 push
git tag day05-submit # 태그 붙임
git push origin day05-submit # 태그 push

* 잠시 후 본인 리포의 해당 commit 페이지에 자동 코멘트로 제출 확인됨

py scripts/grade.py --day 5

### 재제출

같은 태그를 강제로 이동시켜 다시 push합니다. -f (force) 옵션 필수.

git commit --allow-empty -m "day2 재제출"
git push
git tag -f day02-submit # 태그를 새 커밋으로 강제 이동
git push origin day02-submit -f # 원격 태그 강제 갱신


https://ucanlabs.kr/classroom/sds-ax/lesson/1142/


### langgraph 실행 
langgraph dev


