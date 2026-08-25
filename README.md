https://ucanlabs.kr/classroom/sds-ax/lesson/1114/

실습 코드 완성
git add {변경한 파일들}
git commit -m "day1 완료" # 커밋 메시지는 자유
git push # 커밋 push
git tag day01-submit # 태그 붙임
git push origin day01-submit # 태그 push
잠시 후 본인 리포의 해당 commit 페이지에 자동 코멘트로 제출 확인됨


● 재제출

같은 태그를 강제로 이동시켜 다시 push합니다. -f (force) 옵션 필수.

git commit --allow-empty -m "day1 재제출"
git push
git tag -f day01-submit # 태그를 새 커밋으로 강제 이동
git push origin day01-submit -f # 원격 태그 강제 갱신


https://ucanlabs.kr/classroom/sds-ax/lesson/1142/
