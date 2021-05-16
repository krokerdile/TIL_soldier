# github 명령어 정리
싸지방에서 구름 IDE 쓰면서 github명령어를 많이 쓰게 되는데 한번도 정리를 한 적이 없어서 쓸 때마다 다시 찾아줘야 되는게 좀 문제인듯
간단하게라도 찾아보면서 정리해두기 

## Command
#### git clone  
    git clone "저장소 주소"  
#### git add  
    git add "파일명" 해당파일만 추가하기  
    git add . 전체 파일 다 추가하기  
#### git commit
    git commit -m "커밋 메시지" 추가된 파일들에 대한 변경사항 확정 및 설명
#### git branch
    git branch - 브랜치 전체 목록 띄우기
#### git branch <브랜치이름>
    git branch ~~~~ - 해당 브랜치로 이동하기
#### git checkout -b <브랜치이름>	 
    Main 브랜치로 다시 돌아오기
#### git push origin master
    변경사항을 원격서버에 올리기
#### git pull	
    원격서버 내용 로컬로 땡겨오기
#### git merge <다른 브랜치이름>
    현재 브랜치에 다른 브랜치의 수정사항 병합
#### git checkout -- <파일명>
    현재 브랜치 상태를 변경사항 적용전으로 돌려놓음
#### git diff <브랜치이름><다른 브랜치이름>
    변경사항 merge 전에 비교할 수 있게 해줌

