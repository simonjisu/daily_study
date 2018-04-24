# Jupyter Hub

## 빠른 설치 가이드
### 최소요구사항
* linux/unix를 기본으로하는 시스템
* python3.4 이상의 버전, pip 혹은 conda 로 파일을 설치 할줄 알면 도움됨
* nodejs/npm 필요 
    * 설치방법: `sudo apt-get install npm nodejs-legacy`
* TLS certificate & key for HTTPS communication
* Domain name
* jupyter notebook 4버전 이상

### 설치
**pip, npm**
```
python3 -m pip install jupyterhub
npm install -g configureable-http-proxy
python3 -m pip install notebook  # needed if running the notebook servers locally
```

**conda**
```
conda install -c conda-forge jupyterhub  # installs jupyterhub and proxy
conda install notebook  # needed if running the notebook servers locally
```

install 잘됐는지 테스트: help 가 뜨면 잘된거
```
jupyterhub -h
configurable-http-proxy -h
```

### 시작
브라우저에 `https://localhost:8000` 로 시작가능

```
(sudo) jupyterhub
```

## 기본설정
### Configfile 생성
```
jupyterhub --generate-config
```

막힘:
SSL 생성 방법: [링크](https://zetawiki.com/wiki/%EB%A6%AC%EB%88%85%EC%8A%A4_%EA%B0%9C%EC%9D%B8%EC%84%9C%EB%AA%85_SSL_%EC%9D%B8%EC%A6%9D%EC%84%9C_%EC%83%9D%EC%84%B1)




