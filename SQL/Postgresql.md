# 180428

원하는 데이터 불러오기

> SELECT 스키마 FROM 테이블 WHERE 조건

```
SELECT "textstyle", "text", "pitcher", "batter"
FROM livetext
WHERE "textstyle" = 2;
```

> 사이에 있는 값 불러오기

```
SELECT "idx", "textstyle", "text"
FROM livetext
WHERE "idx" BETWEEN 2840 AND 2850;
```

> 유니크한 값 불러오기

```
SELECT DISTINCT ON ("textstyle") "textstyle", "text" FROM livetext;
```

Aggregate Functions Docs:

https://www.postgresql.org/docs/9.5/static/functions-aggregate.html
