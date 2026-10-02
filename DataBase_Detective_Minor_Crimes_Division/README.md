# Database Detective: Minor Crimes Division — SQL 정리

> **Database Detective: Minor Crimes Division**을 플레이하면서 필요한 SQL 문법이 메뉴얼 느낌으로 써져 있습니다. 그걸 한 번 더 따로 적으며 정리했습니다.

---

## 목차

1. [SQL 기본 구조](#1-sql-기본-구조)
2. [WHERE — 조건으로 찾기](#2-where--조건으로-찾기)
3. [AND / OR — 여러 조건 사용하기](#3-and--or--여러-조건-사용하기)
4. [범위 조건](#4-범위-조건)
5. [ORDER BY — 결과 정렬](#5-order-by--결과-정렬)
6. [AS — 별명 붙이기](#6-as--별명-붙이기)
7. [계산하기](#7-계산하기)
8. [집계 함수](#8-집계-함수)
9. [GROUP BY — 그룹별 계산](#9-group-by--그룹별-계산)
10. [WHERE와 HAVING 차이](#10-where와-having-차이)
11. [SQL 실행 순서](#11-sql-실행-순서)
12. [JOIN — 테이블 연결](#12-join--테이블-연결)
13. [여러 테이블 JOIN](#13-여러-테이블-join)
14. [GROUP BY + JOIN](#14-group-by--join)
15. [Subquery — 쿼리 안의 쿼리](#15-subquery--쿼리-안의-쿼리)
16. [비율 계산](#16-비율-계산)
17. [Self Join — 자기 자신과 JOIN](#17-self-join--자기-자신과-join)
18. [EXCEPT — 차집합](#18-except--차집합)
19. [LIKE — 문자열 검색](#19-like--문자열-검색)
20. [IN — 여러 값 중 하나](#20-in--여러-값-중-하나)
21. [DISTINCT — 중복 제거](#21-distinct--중복-제거)
22. [LIMIT — 결과 개수 제한](#22-limit--결과-개수-제한)
23. [자주 쓰는 패턴 — 조건으로 후보 줄이기](#23-자주-쓰는-패턴--조건으로-후보-줄이기)
24. [자주 쓰는 패턴 — 사건 당시 현장에 있던 사람](#24-자주-쓰는-패턴--사건-당시-현장에-있던-사람)
25. [자주 쓰는 패턴 — 두 증거의 교집합](#25-자주-쓰는-패턴--두-증거의-교집합)
26. [자주 쓰는 패턴 — 사람별 횟수](#26-자주-쓰는-패턴--사람별-횟수)
27. [자주 쓰는 패턴 — 사람별 합계](#27-자주-쓰는-패턴--사람별-합계)
28. [자주 쓰는 패턴 — 최고값](#28-자주-쓰는-패턴--최고값)
29. [자주 쓰는 패턴 — 옆자리 찾기](#29-자주-쓰는-패턴--옆자리-찾기)
30. [자주 쓰는 패턴 — A에는 있고 B에는 없는 데이터](#30-자주-쓰는-패턴--a에는-있고-b에는-없는-데이터)
31. [사건 풀 때 생각하는 순서](#31-사건-풀-때-생각하는-순서)
32. [최종 치트시트](#32-최종-치트시트)

---

# 1. SQL 기본 구조

SQL에서 가장 기본적인 조회 형태는 다음과 같다.

```sql
SELECT column_name
FROM table_name;
```

- `SELECT` : 어떤 데이터를 볼 것인지
- `FROM` : 어느 테이블에서 가져올 것인지

예시:

```sql
SELECT name
FROM suspects;
```

`suspects` 테이블에서 모든 사람의 `name`을 가져온다.

여러 열을 보고 싶으면 쉼표로 구분한다.

```sql
SELECT name, age, occupation
FROM suspects;
```

모든 열을 보고 싶으면 `*`를 사용한다.

```sql
SELECT *
FROM suspects;
```

Database Detective에서 기본적으로 반복하게 되는 흐름은 다음과 같다.

```text
단서 확인
→ 필요한 테이블 선택
→ 필요한 열 선택
→ 조건 추가
→ 후보 줄이기
```

---

# 2. WHERE — 조건으로 찾기

특정 조건에 맞는 행만 가져오려면 `WHERE`를 사용한다.

```sql
SELECT *
FROM suspects
WHERE age = 25;
```

## 비교 연산자

```text
=    같다
!=   다르다
<>   다르다
>    초과
<    미만
>=   이상
<=   이하
```

예:

```sql
SELECT *
FROM suspects
WHERE height >= 180;
```

문자열은 `' '` 안에 넣는다.

```sql
SELECT *
FROM suspects
WHERE occupation = 'Teacher';
```

숫자는 따옴표 없이 작성한다.

```sql
SELECT *
FROM suspects
WHERE age = 32;
```

---

# 3. AND / OR — 여러 조건 사용하기

여러 조건을 **전부 만족**해야 한다면 `AND`를 사용한다.

```sql
SELECT *
FROM suspects
WHERE age = 25
AND occupation = 'Teacher';
```

의미:

```text
age = 25
그리고
occupation = Teacher
```

둘 중 하나만 만족하면 되는 경우 `OR`를 사용한다.

```sql
SELECT *
FROM suspects
WHERE occupation = 'Teacher'
OR occupation = 'Principal';
```

조건이 복잡하다면 괄호를 사용하는 것이 좋다.

```sql
SELECT *
FROM suspects
WHERE age >= 20
AND (
    occupation = 'Teacher'
    OR occupation = 'Principal'
);
```

게임에서는 단서 하나하나를 SQL 조건으로 바꾼다고 생각하면 쉽다.

```text
갈색 눈
30세 이상
교사

↓

WHERE eye_color = 'Brown'
AND age >= 30
AND occupation = 'Teacher'
```

---

# 4. 범위 조건

시간이나 숫자의 범위를 찾을 때 사용한다.

예를 들어 사건 발생 시간이 `15:00`이고 그 시간에 근무 중이던 사람을 찾는다면:

```sql
SELECT *
FROM timesheet
WHERE check_in <= '15:00'
AND check_out >= '15:00';
```

의미:

```text
15:00 이전에 출근했고
15:00 이후에 퇴근한 사람
```

숫자 범위도 같은 방식이다.

```sql
SELECT *
FROM suspects
WHERE age >= 20
AND age <= 30;
```

---

# 5. ORDER BY — 결과 정렬

결과를 정렬할 때 `ORDER BY`를 사용한다.

```sql
SELECT *
FROM suspects
ORDER BY age;
```

기본값은 오름차순이다.

```text
ASC  = 작은 값 → 큰 값
DESC = 큰 값 → 작은 값
```

오름차순:

```sql
SELECT *
FROM suspects
ORDER BY age ASC;
```

내림차순:

```sql
SELECT *
FROM suspects
ORDER BY age DESC;
```

예를 들어 가격이 낮은 순서:

```sql
SELECT *
FROM orders
ORDER BY price ASC;
```

가격이 높은 순서:

```sql
SELECT *
FROM orders
ORDER BY price DESC;
```

---

# 6. AS — 별명 붙이기

열이나 테이블 이름에 별명을 붙일 수 있다.

## 열 별명

```sql
SELECT price AS total_price
FROM orders;
```

## 테이블 별명

```sql
SELECT s.name
FROM suspects AS s;
```

보통은 `AS`를 생략하고 다음처럼 작성하기도 한다.

```sql
SELECT s.name
FROM suspects s;
```

JOIN이 많아지면 별명이 매우 유용하다.

```sql
SELECT s.name, o.order_number
FROM suspects s
JOIN orders o
ON s.id = o.customer_id;
```

여기서:

```text
s = suspects
o = orders
```

---

# 7. 계산하기

`SELECT` 안에서 산술 연산을 사용할 수 있다.

```sql
SELECT price * quantity
FROM orders;
```

별명을 붙이면:

```sql
SELECT price * quantity AS total_price
FROM orders;
```

## 기본 연산

```text
+  더하기
-  빼기
*  곱하기
/  나누기
%  나머지
```

예:

```sql
SELECT final_score % 8
FROM games_history;
```

`%`는 배수 여부를 확인할 때 사용할 수 있다.

```sql
SELECT *
FROM games_history
WHERE final_score % 8 = 0;
```

위 쿼리는 `final_score`가 8의 배수인 데이터를 찾는다.

---

# 8. 집계 함수

여러 행을 계산해서 하나의 값으로 만드는 함수다.

## COUNT

행의 개수를 구한다.

```sql
SELECT COUNT(*)
FROM students;
```

조건을 추가할 수도 있다.

```sql
SELECT COUNT(*)
FROM students
WHERE class = 'Science';
```

## SUM

합계를 구한다.

```sql
SELECT SUM(price)
FROM orders;
```

## AVG

평균을 구한다.

```sql
SELECT AVG(price)
FROM orders;
```

## MIN

가장 작은 값을 구한다.

```sql
SELECT MIN(price)
FROM orders;
```

## MAX

가장 큰 값을 구한다.

```sql
SELECT MAX(score)
FROM games;
```

---

# 9. GROUP BY — 그룹별 계산

같은 값을 가진 데이터를 묶어서 계산할 때 사용한다.

예를 들어 주문별 총 가격을 계산하려면:

```sql
SELECT order_number, SUM(price)
FROM orders
GROUP BY order_number;
```

데이터가 다음과 같다고 하자.

```text
order_number | price
-------------|------
100          | 10
100          | 15
100          | 5
101          | 20
101          | 10
```

결과:

```text
order_number | SUM(price)
-------------|-----------
100          | 30
101          | 30
```

즉:

```text
GROUP BY order_number
→ 같은 order_number끼리 묶는다.

SUM(price)
→ 각 그룹의 price를 합친다.
```

여러 열을 기준으로 그룹화할 수도 있다.

```sql
SELECT student_id, class_name, COUNT(*)
FROM attendance
GROUP BY student_id, class_name;
```

---

# 10. WHERE와 HAVING 차이

SQL에서 자주 헷갈리는 부분이다.

## WHERE

그룹화하기 전에 개별 행을 필터링한다.

```sql
SELECT *
FROM attendance
WHERE student_id = 10;
```

## HAVING

`GROUP BY` 이후 만들어진 그룹을 필터링한다.

```sql
SELECT student_id, COUNT(*)
FROM attendance
GROUP BY student_id
HAVING COUNT(*) < 10;
```

다음처럼 사용하는 것은 일반적으로 잘못된 형태다.

```sql
WHERE COUNT(*) < 10
```

`COUNT(*)`는 그룹화 이후에 계산되는 값이기 때문이다.

기억:

```text
WHERE  = 행 조건
HAVING = 그룹 조건
```

---

# 11. SQL 실행 순서

SQL을 작성하는 순서는 보통 다음과 같다.

```sql
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
```

하지만 개념적인 처리 순서는 다음과 같다.

```text
FROM
↓
WHERE
↓
GROUP BY
↓
HAVING
↓
SELECT
↓
ORDER BY
```

정리하면:

```text
WHERE
→ 원본 행 제거

GROUP BY
→ 남은 행을 그룹화

HAVING
→ 만들어진 그룹 제거

SELECT
→ 출력할 값 계산

ORDER BY
→ 마지막 결과 정렬
```

---

# 12. JOIN — 테이블 연결

서로 다른 테이블의 데이터를 연결할 때 사용한다.

예를 들어 다음 두 테이블이 있다고 하자.

## suspects

```text
id | name
---|------
1  | Alice
2  | Bob
```

## orders

```text
customer_id | item
------------|-------
1           | Pizza
2           | Burger
```

두 테이블을 연결한다.

```sql
SELECT s.name, o.item
FROM suspects s
JOIN orders o
ON s.id = o.customer_id;
```

결과:

```text
Alice | Pizza
Bob   | Burger
```

기본 구조:

```sql
SELECT *
FROM table1
JOIN table2
ON table1.key = table2.key;
```

Database Detective에서는 다음처럼 생각하면 된다.

```text
이 두 데이터가 같은 사람이라는 것을
어떻게 확인할 수 있을까?

↓

공통 key를 찾아 JOIN
```

예:

```text
person_id
customer_id
student_id
badge_number
order_number
```

같은 식별자가 테이블 연결의 기준이 된다.

---

# 13. 여러 테이블 JOIN

두 개가 아니라 세 개 이상의 테이블도 연결할 수 있다.

```sql
SELECT
    c.name,
    o.order_number,
    t.dollars_tipped
FROM customers c
JOIN orders o
ON c.order_number = o.order_number
JOIN tips t
ON o.order_number = t.order_number;
```

구조:

```text
customers
    |
order_number
    |
orders
    |
order_number
    |
tips
```

---

# 14. GROUP BY + JOIN

후반부 사건에서 자주 사용하게 되는 형태다.

예를 들어 하나의 주문이 여러 행으로 나뉘어 있고 주문 전체 가격을 구해야 한다면:

```sql
SELECT
    order_number,
    SUM(price) AS total_price
FROM orders
GROUP BY order_number;
```

그 결과를 다른 테이블과 연결한다.

```sql
SELECT
    o.order_number,
    o.total_price,
    t.dollars_tipped
FROM (
    SELECT
        order_number,
        SUM(price) AS total_price
    FROM orders
    GROUP BY order_number
) o
JOIN tips t
ON o.order_number = t.order_number;
```

핵심:

```text
1. 먼저 데이터를 요약한다.
2. 요약된 결과를 다른 테이블과 JOIN한다.
```

---

# 15. Subquery — 쿼리 안의 쿼리

SQL 쿼리 결과를 다시 하나의 테이블처럼 사용할 수 있다.

```sql
SELECT *
FROM (
    SELECT
        order_number,
        SUM(price) AS total_price
    FROM orders
    GROUP BY order_number
) x;
```

안쪽 쿼리:

```sql
SELECT
    order_number,
    SUM(price) AS total_price
FROM orders
GROUP BY order_number;
```

이 부분이 먼저 실행된다.

그 결과를 `x`라는 임시 테이블처럼 사용한다.

기본 형태:

```sql
SELECT ...
FROM (
    SELECT ...
    FROM ...
) alias;
```

여러 단계로 데이터를 가공해야 할 때 유용하다.

---

# 16. 비율 계산

가격, 팁, 점수 등 두 값을 비율로 비교할 수 있다.

```sql
SELECT
    dollars_tipped * 1.0 / total_price AS tip_ratio
FROM orders;
```

일부 SQL 환경에서는 정수끼리 나누면 정수 연산이 발생할 수 있다.

예:

```text
1 / 2
```

따라서 `1.0`을 곱해서 실수 계산을 유도한다.

```sql
SELECT
    order_number,
    dollars_tipped * 1.0 / total_price AS tip_ratio
FROM order_totals
ORDER BY tip_ratio ASC;
```

위 쿼리는 팁 비율이 낮은 주문부터 보여준다.

---

# 17. Self Join — 자기 자신과 JOIN

같은 테이블을 두 번 사용하는 JOIN이다.

예를 들어 좌석 테이블이 다음과 같다고 하자.

```text
student_id | row | seat
-----------|-----|-----
1          | 1   | 3
2          | 1   | 4
3          | 2   | 1
```

바로 옆자리 학생을 찾으려면 같은 테이블을 두 번 사용한다.

```sql
SELECT
    a.student_id,
    b.student_id
FROM seats a
JOIN seats b
ON a.row = b.row
AND a.seat = b.seat - 1;
```

여기서:

```text
a = seats의 첫 번째 복사본
b = seats의 두 번째 복사본
```

조건:

```sql
a.row = b.row
```

같은 줄이어야 한다.

```sql
a.seat = b.seat - 1
```

바로 옆 좌석이어야 한다.

좌우 둘 다 찾으려면:

```sql
SELECT
    a.student_id,
    b.student_id
FROM seats a
JOIN seats b
ON a.row = b.row
AND (
    a.seat = b.seat - 1
    OR
    a.seat = b.seat + 1
);
```

---

# 18. EXCEPT — 차집합

첫 번째 결과에는 있지만 두 번째 결과에는 없는 값을 찾는다.

```sql
SELECT column
FROM table_a

EXCEPT

SELECT column
FROM table_b;
```

개념적으로:

```text
첫 번째 결과
-
두 번째 결과
=
첫 번째 결과에만 존재하는 데이터
```

예:

```sql
SELECT directly_influenced
FROM philosophy
WHERE philosopher = 'Zoran'

EXCEPT

SELECT directly_influenced
FROM philosophy
WHERE philosopher <> 'Zoran';
```

의미:

```text
Zoran의 영향을 받은 사람

중에서

다른 철학자의 영향도 받은 사람을 제거
```

결과적으로:

```text
Zoran에게만 영향을 받은 대상
```

을 찾을 수 있다.

---

# 19. LIKE — 문자열 검색

문자열의 일부를 검색할 때 사용한다.

```sql
SELECT *
FROM customers
WHERE name LIKE 'A%';
```

`%`는 문자 0개 이상 아무거나를 의미한다.

```text
'A%'
→ A로 시작

'%A'
→ A로 끝남

'%A%'
→ 문자열 어딘가에 A가 포함됨
```

예:

```sql
SELECT *
FROM orders
WHERE item_name LIKE '%pineapple%';
```

이름에 `pineapple`이 들어간 데이터를 찾는다.

반대로 해당 문자열이 포함되지 않은 것을 찾고 싶으면:

```sql
SELECT *
FROM orders
WHERE item_name NOT LIKE '%pineapple%';
```

---

# 20. IN — 여러 값 중 하나

한 열이 여러 값 중 하나인지 검사할 때 사용한다.

다음과 같이 쓸 수도 있지만:

```sql
WHERE category = 'Food'
OR category = 'Service'
OR category = 'Craft'
```

`IN`을 사용하면 더 간단하다.

```sql
WHERE category IN ('Food', 'Service', 'Craft');
```

반대는 `NOT IN`.

```sql
WHERE category NOT IN ('Food', 'Service', 'Craft');
```

---

# 21. DISTINCT — 중복 제거

중복된 값을 제거한다.

```sql
SELECT DISTINCT occupation
FROM suspects;
```

원래 데이터가:

```text
Teacher
Teacher
Teacher
Doctor
Doctor
```

라면 결과는:

```text
Teacher
Doctor
```

후보 데이터의 종류를 먼저 확인할 때 유용하다.

---

# 22. LIMIT — 결과 개수 제한

결과를 원하는 개수만큼만 출력한다.

```sql
SELECT *
FROM suspects
LIMIT 10;
```

`ORDER BY`와 함께 사용하면 특히 유용하다.

```sql
SELECT *
FROM orders
ORDER BY price DESC
LIMIT 1;
```

위 쿼리는 가장 비싼 데이터 하나를 반환한다.

상위 5개:

```sql
SELECT *
FROM orders
ORDER BY price DESC
LIMIT 5;
```

---

# 23. 자주 쓰는 패턴 — 조건으로 후보 줄이기

```sql
SELECT *
FROM suspects
WHERE condition1
AND condition2
AND condition3;
```

예:

```sql
SELECT *
FROM suspects
WHERE age >= 20
AND age <= 30
AND occupation = 'Teacher';
```

게임에서는 단서를 하나씩 `WHERE` 조건으로 변환하면 된다.

---

# 24. 자주 쓰는 패턴 — 사건 당시 현장에 있던 사람

```sql
SELECT *
FROM timesheet
WHERE check_in <= '사건시간'
AND check_out >= '사건시간';
```

예:

```sql
SELECT *
FROM timesheet
WHERE check_in <= '15:30'
AND check_out >= '15:30';
```

이 쿼리는 `15:30` 시점에 근무 중이던 사람을 찾는다.

---

# 25. 자주 쓰는 패턴 — 두 증거의 교집합

서로 다른 증거 테이블에서 동시에 등장하는 사람을 찾는다.

```sql
SELECT *
FROM evidence_a a
JOIN evidence_b b
ON a.person_id = b.person_id
WHERE a.condition = '조건1'
AND b.condition = '조건2';
```

개념:

```text
증거 A 후보
∩
증거 B 후보
=
범인 후보
```

---

# 26. 자주 쓰는 패턴 — 사람별 횟수

사람마다 데이터가 몇 번 등장했는지 계산한다.

```sql
SELECT
    person_id,
    COUNT(*) AS count
FROM records
GROUP BY person_id;
```

특정 횟수 이상:

```sql
SELECT
    person_id,
    COUNT(*) AS count
FROM records
GROUP BY person_id
HAVING COUNT(*) >= 5;
```

특정 횟수 미만:

```sql
SELECT
    person_id,
    COUNT(*) AS count
FROM records
GROUP BY person_id
HAVING COUNT(*) < 5;
```

---

# 27. 자주 쓰는 패턴 — 사람별 합계

```sql
SELECT
    person_id,
    SUM(amount) AS total
FROM transactions
GROUP BY person_id;
```

합계가 큰 순서:

```sql
SELECT
    person_id,
    SUM(amount) AS total
FROM transactions
GROUP BY person_id
ORDER BY total DESC;
```

합계가 작은 순서:

```sql
SELECT
    person_id,
    SUM(amount) AS total
FROM transactions
GROUP BY person_id
ORDER BY total ASC;
```

---

# 28. 자주 쓰는 패턴 — 최고값

전체 데이터의 최고값:

```sql
SELECT MAX(score)
FROM scores;
```

사람별 최고값:

```sql
SELECT
    person_id,
    MAX(score)
FROM scores
GROUP BY person_id;
```

조건까지 적용:

```sql
SELECT
    person_id,
    MAX(score) AS max_score
FROM scores
GROUP BY person_id
HAVING MAX(score) >= 90;
```

---

# 29. 자주 쓰는 패턴 — 옆자리 찾기

Self Join을 사용한다.

```sql
SELECT
    a.student_id AS student,
    b.student_id AS neighbor
FROM seats a
JOIN seats b
ON a.row = b.row
AND ABS(a.seat - b.seat) = 1;
```

`ABS()`를 사용하지 않는다면:

```sql
SELECT
    a.student_id AS student,
    b.student_id AS neighbor
FROM seats a
JOIN seats b
ON a.row = b.row
AND (
    a.seat = b.seat + 1
    OR
    a.seat = b.seat - 1
);
```

---

# 30. 자주 쓰는 패턴 — A에는 있고 B에는 없는 데이터

`EXCEPT`를 사용한다.

```sql
SELECT id
FROM table_a

EXCEPT

SELECT id
FROM table_b;
```

개념:

```text
A
-
B
=
A에만 존재하는 데이터
```

---

# 31. 사건 풀 때 생각하는 순서

SQL부터 바로 작성하기보다 아래 순서로 접근하면 편하다.

```text
1. 단서에서 사실을 전부 뽑는다.

2. 각각을 SQL 조건으로 바꾼다.

3. 어떤 테이블에서 확인할 수 있는지 찾는다.

4. 테이블마다 후보 목록을 따로 만든다.

5. 후보를 연결할 공통 key를 찾는다.

6. 필요한 테이블을 JOIN한다.

7. GROUP BY가 필요하면 그룹화한다.

8. 집계 결과에 조건을 걸어야 한다면 HAVING을 사용한다.

9. 가장 크거나 작은 값을 찾는다면 ORDER BY를 사용한다.

10. 필요하면 LIMIT으로 결과를 줄인다.

11. 최종 후보가 모든 증거를 만족하는지 다시 확인한다.
```

핵심 흐름을 압축하면:

```text
단서
↓
WHERE
↓
후보 생성
↓
JOIN
↓
GROUP BY
↓
HAVING
↓
ORDER BY
↓
최종 후보
```

---

# 32. 최종 치트시트

## 기본 조회

```sql
SELECT column
FROM table;
```

## 전체 조회

```sql
SELECT *
FROM table;
```

## 조건

```sql
SELECT *
FROM table
WHERE condition;
```

## 여러 조건

```sql
SELECT *
FROM table
WHERE condition1
AND condition2;
```

```sql
SELECT *
FROM table
WHERE condition1
OR condition2;
```

## 범위

```sql
SELECT *
FROM table
WHERE value >= minimum
AND value <= maximum;
```

## 정렬

```sql
SELECT *
FROM table
ORDER BY column ASC;
```

```sql
SELECT *
FROM table
ORDER BY column DESC;
```

## 중복 제거

```sql
SELECT DISTINCT column
FROM table;
```

## 개수

```sql
SELECT COUNT(*)
FROM table;
```

## 합계

```sql
SELECT SUM(column)
FROM table;
```

## 평균

```sql
SELECT AVG(column)
FROM table;
```

## 최소 / 최대

```sql
SELECT
    MIN(column),
    MAX(column)
FROM table;
```

## 그룹화

```sql
SELECT
    category,
    COUNT(*)
FROM table
GROUP BY category;
```

## 그룹 조건

```sql
SELECT
    category,
    COUNT(*)
FROM table
GROUP BY category
HAVING COUNT(*) > 5;
```

## JOIN

```sql
SELECT *
FROM table1 a
JOIN table2 b
ON a.id = b.id;
```

## 여러 JOIN

```sql
SELECT *
FROM table1 a
JOIN table2 b
ON a.id = b.id
JOIN table3 c
ON b.id = c.id;
```

## Self Join

```sql
SELECT *
FROM table a
JOIN table b
ON a.group_id = b.group_id
AND a.id <> b.id;
```

## 문자열 검색

```sql
SELECT *
FROM table
WHERE column LIKE '%text%';
```

## 문자열 제외

```sql
SELECT *
FROM table
WHERE column NOT LIKE '%text%';
```

## 여러 값 중 하나

```sql
SELECT *
FROM table
WHERE column IN ('A', 'B', 'C');
```

## 여러 값 제외

```sql
SELECT *
FROM table
WHERE column NOT IN ('A', 'B', 'C');
```

## 차집합

```sql
SELECT id
FROM table1

EXCEPT

SELECT id
FROM table2;
```

## Subquery

```sql
SELECT *
FROM (
    SELECT ...
    FROM ...
) x;
```

## 상위 몇 개

```sql
SELECT *
FROM table
ORDER BY column DESC
LIMIT 5;
```

## 사람별 횟수

```sql
SELECT
    person_id,
    COUNT(*) AS count
FROM records
GROUP BY person_id;
```

## 사람별 합계

```sql
SELECT
    person_id,
    SUM(amount) AS total
FROM records
GROUP BY person_id;
```

## 사람별 최고값

```sql
SELECT
    person_id,
    MAX(score) AS max_score
FROM scores
GROUP BY person_id;
```

## 계산 결과 정렬

```sql
SELECT
    id,
    value1 * 1.0 / value2 AS ratio
FROM table
ORDER BY ratio ASC;
```

---

# 핵심 개념 요약

```text
SELECT
→ 무엇을 볼 것인가

FROM
→ 어디에서 가져올 것인가

WHERE
→ 어떤 행을 남길 것인가

JOIN
→ 다른 테이블과 어떻게 연결할 것인가

GROUP BY
→ 무엇을 기준으로 묶을 것인가

HAVING
→ 어떤 그룹을 남길 것인가

ORDER BY
→ 어떤 순서로 보여줄 것인가

LIMIT
→ 몇 개만 보여줄 것인가

Subquery
→ 쿼리 결과를 다시 데이터처럼 사용

Self Join
→ 같은 테이블 안에서 데이터끼리 비교

EXCEPT
→ A에는 있지만 B에는 없는 데이터
```

---

# 게임 진행 기준으로 기억할 순서

```text
SELECT
↓
WHERE
↓
AND / OR
↓
ORDER BY
↓
집계 함수
↓
GROUP BY
↓
HAVING
↓
JOIN
↓
Subquery
↓
Self Join
↓
EXCEPT
```

특히 후반부에서는 다음 흐름을 확실하게 이해해 두면 좋다.

```text
JOIN
→ GROUP BY
→ HAVING
→ Subquery
→ Self Join
→ EXCEPT
```

---


```text
단서를 조건으로 변환한다.
↓
조건으로 후보를 줄인다.
↓
공통 ID로 데이터를 연결한다.
↓
집계가 필요하면 GROUP BY를 사용한다.
↓
그룹 조건은 HAVING으로 처리한다.
↓
최종적으로 모든 증거를 만족하는 대상을 찾는다.
```
