# Git Branch 활용하기

* branch 생성: git branch (test)
* branch 이동: git checkout (test)
* branch 로그 보기: git log --oneline --decorate --graph --all
* branch 에서 master 로 push: git push --set-upstream origin (test)
* master 에서 branch 로 pull: git pull origin master

---

git clone 할때 SSH 상황이라면 "Use SSH"를 찾아보자, 단 미리 SSH 키를 등록해둬야한다.

```
pbcopy < ~/.ssh/id_rsa.pub
# Copies the contents of the id_rsa.pub file to your clipboard
```

`Settings > SSH and GPG keys > New SSH key` 를 눌러서 등록하자.


