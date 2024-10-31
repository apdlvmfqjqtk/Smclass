select * from member;

update member set id='abc', pw='1111', name='임정우', email='zmgkgzmgkg4@gmail.com'
where id = 'abc';

commit;

update member set pw='1111' where id = 'Towell';

select * from member;


select sysdate-1,sysdate,sysdate+1 from dual;

select hire_date,round(hire_date,'Month') from employees;

select hire_date,trunc(hire_date,'month') from employees;

select add_months(trunc(sysdate,'month'),1) from dual;

-- vip요금제로 변경을 하면 다음 달 1일부터 혜택을 주어지게 하기

select sysdate,add_months(trunc(sysdate,'month'),1) from dual;


-- 입사일 기준 다음달 1일부터 혜톅을 주기
select emp_name,hire_date,add_months(trunc(hire_date,'month'),1) 
from employees;

-- 입사일 기준 1년 후 날짜를 출력
select hire_date,add_months(hire_date,12) from employees;
select hire_datr,hire_date+365 from employees;

commit;
-- 입사일 기준 1년 후 마지막 그 달의 날짜를 출력하시오
select hire_date,last_day(hire_date) from employees;
select hire_date,last_day(hire_date+365) from employees;



-- 입력일 기준 1년 후 마지막 날짜가 8/31,9/30,10/31 일인 학생들을 모두 출력하시오
select sdate from students;
select sdate,last_day(sdate+365) sdate2,last_day(add_months(sdate,12)) sdate3
from students
where last_day(sdate+365) in ('24/08/31','24/09/30','24/10/31','25/08/31','25/09/30','25/10/31')
order by sdate2
;

--extract함수: 년, 월, 일, 시 , 분, 초 만 분리해서 가져오는 함수
select sdate from students;
select sdate, extract(month from sdate), extract(month from last_day(sdate+365))
from students
where extract(month from last_day(sdate+365)) in (8,11,12);


-- sysdate 년월일
select sysdate from dual;
select extract(year from sysdate)from dual;
select extract(month from sysdate) from dual;
select extract(day from sysdate) from dual;
--시간은 안됨

--systimestamp 년월일시분초 
select systimestamp from dual;
select extract(hour from systimestamp) from dual;
select extract(minute from systimestamp) from dual;
select extract(second from systimestamp) from dual;

select sdate,extract(month from sdate) from students
where extract(month from last_day(sdate+365)) in (8,11,12)
;

-- substr함수: 문자에서 시작위치, 가져올 개수
select sysdate,substr(sysdate,4,2) from dual;

select sdate,last_day(sdate+365) sdate2 from students
where substr(last_day(sdate+365),4,2) in (6,8,12)
order by sdate2;

-- 날짜 -> 문자 to_char    ## 날짜포맷
-- 문자 -> 날짜 to_date    ## 날짜 사칙연산
-- 숫자 -> 문자 to_char    ## 천단위, 숫자 앞에 0을 표시, 통화 표시
-- 문자 -> 숫자 to_number  ## 천단위 표시, 천단위 삭제해서 사칙연산

-- 날짜 형변환해서 날짜 포맷을 변경
-- date타입 -> char 타입으로 변경해서 포멧 (to_char)
select sysdate from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd') from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd hh24:mi:ss day') from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd am hh:mi:ss day') from dual;
select sysdate,to_char(sysdate,'yy-mm-dd hh24:mi:ss day') from dual;
select sysdate,to_char(sysdate,'yy-MON-dd hh24:mi:ss') from dual;

select hire_date,to_char(hire_date,'yyyy-mm-dd hh:mi:ss') from employees; 

-- students테이블 sdate 2024-01-01 형태로 출력하시오
select sdate from students;
select sdate, to_char(sdate,'yyyy-mm-dd') from students;

select kor from students
where kor = 70;

-- 숫자타입을 문자타입으로 변경해서 포맷 (천단위 표시)
select salary*1382.86*12 from employees;

-- 자릿수 채우기 9: 빈공백으로 채움, 0: 0으로 채움
-- L: 국가통화기호 표시, $: $표시가 됨
select to_char(salary*1382.86*12,'L000,999,999') from employees;

select to_char(12,'000') from dual;
select 12 from dual;

select to_char(123456,'000000000'), to_char(123456,'999,999,999') from dual;

create table chartable2(
no number(4),
kor number(10),
kor_char number(10),
kor_mark number(10)
);

-- number,number,str-number타입을 넣어도 입력
-- 문자형 타입에는 숫자형 타입 넣기 가능(들어가는 즉시 문자형 됨)
insert into chartable values(
1,10000,to_char(1000000,'000000000'),to_char(100000,'0,000,000')
);
--rollback;
select * from chartable2;

-- 숫자형 타입, 문자형(숫자)타입은 사칙연산 가능
-- 숫자형 타입과 문자 천단위 표시 숫자타입은 사칙연산 불가능
select kor+kor_char from chartable;
select kor+kor_mark from chartable;

desc chartable; -- number,varchar2
desc chartable2; -- 모든타입 number

--commit;

-- 숫자형타입은 숫자 앞에 0있어도 표시가 되지 않음(문자형 타입만 가능)
insert into chartable2 VALUES(
3,3000000,30000000,3000000
);

select '20241031' from dual;

-- 2일 이후의 날짜를 출력하시오
select '20241031',to_date('20241031')+2 from dual;
select sysdate,sysdate+2 from dual;

-- to_date를 붙여서 날짜 타입으로 바꿀 수 있다.
-- 아니면 날짜 타입의 형태로만 바꿔도 된다(yyyy-mm-dd / vvvv/mm/dd)
select to_date('20241031')+2 from dual;


select to_date(20231031) from dual;

--number형 타입 -> 날짜형 타입으로 변경
select sysdate - to_date(20231101) from dual;
--문자형 타입 -> 날짜형 타입으로 변경
select sysdate - to_date('20231101') from dual;

-- 문자형 타입 -> 숫자형 타입
-- 천단위 문자형타입 -> 천단위 제외 숫자형 타입
select to_number('20,000','999,999') from dual;

-- 숫자형타입 이기에 사칙연산 가능
select kor+to_number(kor_mark,'999,999,999') from chartable;

delete  chartable;

insert into chartable values(
3,30000,'0030000','3,000,000'
);

commit;
select * from employees;

select department_id from employees;

select department_id from employees
where department_id is null;

select department_id from employees
where department_id is not null;

-- 월급 *커미션
select salary+salary*nvl(commission_pct,0) from employees;

-- null경우 0 표시
select nvl(department_id,0) from employees;

-- null경우 ceo 표시, 숫자형 타입을 문자형 타입으로 변경
select nvl(to_char(department_id),'ceo') from employees;


-- 그룹 함수 
-- sum 합계, avg 평균, count 개수, min 최소값, max 최대값, median: 중간값

select salary from employees;

select sum(salary) from employees;
select to_char(sum(salary),'999,999') from employees;

select avg(salary) from employees;
-- 소수점 2자리 반올림
select round(avg(salary),4) from employees;
select trunc(avg(salary),4) from employees;
-- 최대값, 최소값
select max(salary) from employees;
select min(salary) from employees;

--- 평균값보다 월급이 높은 사원 출력
select avg(salary) from employees;
select count(salary) from employees where salary >= 6461.83;

-- 평균값을 select해서 입력함
select count (salary) from employees
where salary >= (select avg(salary) from employees);

-- emp_name: 단일함수, avg: 그룹함수 (같이 두면 에러남)
select emp_name, avg (salary) from employees;

-- 단일함수, 그룹함수 닽이 사용할 수 없음
select department_id, max(salary) from employees;


-- students 테이블 모든 학생의 kor점수 합계와 평균, 최대,최소값을 구하시오
select kor from students;
select sum(kor),round(avg(kor),2),max(kor),min(kor),median(kor),median(kor), variance(kor), stddev(kor) from students;


-- 부서 번호가 50인 사원들의 월급의 합, 평균, 최댓값, 최소값 구하라
select sum(salary), avg(salary), max(salary), min(salary) from employees
where department_id = 50;

-- 부서번호 30
select sum(salary), avg(salary), max(salary), min(salary) from employees
where department_id = 30;
select sum(salary), avg(salary), max(salary), min(salary) from employees
where department_id = 10;

-- 부서별로 최고 연봉자를 알기
-- group by : 단일 함수를 출력하고 싶을 때, 단일 함수를 입력하면 됨
select department_id,max(salary) from employees
group by department_id;

select emp_name,salary from employees;

-- 107명의 평균
select avg(salary) from employees;

-- 단일함수, 그룹함수 함께 사용하려면, group by 지정
select department_id,round(avg(salary)), max(salary), min(salary) from employees
group by department_id
order by department_id;

-- 평균 월급보다 높은 사원 수를 출력하시오
select count(salary), min(salary) , max(salary) from employees
where salary >= (select avg(salary) from employees);


-- abs: 절대값, ceil: 올림, floor: 버림, round: 반올림, trunc: 절단, mod: 나머지, power: 제곱, sqrt: 제곱근
--제곱 
select power(2,2),2*2*2 from dual;

-- 문자, 숫자형 타입 -> 날짜형 타입 변경 가능
-- 숫자, 날짜형 타입 -> 문자형 타입 변경 가능
-- 문자형 타입 -> 숫자형 타입 변경 가능
-- 날짜형 타입 -> 숫자형 타입 변경 불가 // 형태를 변경해서 문자형으로 변경한 후, 숫자형으로 변경 가능
select 20240101,to_date(20240101) from dual;
select '2',to_number('2') from dual;

select '20240101',to_number('20240101') from dual;
select to_number(to_date('20240101')) from dual;

select sysdate,to_number(sysdate) from dual;

-- 날짜형 -> 문자형 변환
select sysdate,to_number(to_char(sysdate,'yyyymmdd')) from dual;

-- 년 월 일 한글 입력하는 방법
-- 날짜형타입을 문자형 타입으로 변경 시
select sysdate,to_char(sysdate,'yyyy"년"mm"월"dd"일"') from dual;
select sysdate,to_char(sysdate, 'yyyy"년"mm-dd day')from dual; -- 글자는 특수문자기에 쌍따옴표 넣어서 바꿔야 함


--------------------------------------------------------------------
-- 문자형 함수
select emp_name,email from employees;

-- 문자형 타입을 +를 이용해 합치려고 하면 에러
select emp_name+email from employees;

-- ||, concat함수
select emp_name||email from employees;  -- 얘가 속도 더 빠름
select concat(emp_name,email) from employees;

select name from member;

-- 숫자형 타입: 사칙연산 계산해서 출력됨
select kor+eng from employees;


-- lower: 소문자 취환, upper: 대문자 취환, initcap: 첫글자 대문자 취환
select * from member
where lower(name) ='bryan';

select 'join',initcap('joHn'),lower('john'),upper('joHn') from dual;

-- lpad: 왼쪽 자리수 채우기
select 'john',lpad('john',10,'#') from dual;

-- rpad: 오른쪽 자리수 채우기
select 'john',rpad('john',10,'#') from dual;

--trim: 앞,뒤 공백 없에기, ltrim: 왼쪽 공백, rtrim: 오른쪽 공백
select length('   aaa   '),length(trim('   aaa   ')),ltrim('   aaa   '),rtrim('   aaa   ') from dual;

-- replace: 취환
select '  a b c  ',trim('  a b c  ') from dual;

select '  a b c  ',length(trim('  a b c  ')),length(replace('  a b c  ',' ','')) from dual;

-- substr: 특정위치 자르기 (시작위지,잘라 올 개수)
select 'abcdefg',substr('abcdefg',1,3),substr('abcdefg',3,1) from dual;

-- hire_date, employees
-- 입사일이 3월인 사람 출력
select hire_date from employees
where substr(hire_date,4,2) in(3,8,10);

--7월 이상
select hire_date from employees
where substr(hire_date,4,2) >= 7;

-- translate 취환 (한번에 여러개를 바꾸기 좋음)
-- 한글자 한글자에 해당하는 단어를 각각의 단어로 취환
-- 순서에 없는 변환글자는 삭제 처리
select 'axyz',translate('axyzxbbcyaccx','xyc','ab') from dual;
select 'axyz',replace('axyzxbbcyaccx','xy','ab') from dual;

--length() : 문자열 길이
-- students 테이블 name 글자 길이 5자 이상만 출력
select count(*) from students
where length(name) >= 9
;


-- 사원의 월급의 합과 평균을 구하시오
select emp_name,sum(salary),avg(salary) from employees
group by emp_name;

-- 영어점수의 합,평,최대,최소 구하기
select sum(eng), avg(eng), max(eng), min(eng) from students;

--students테이블에서 
--홍길동, 등록일: 2023년12월02일 
--이렇게 글자 나타나도록 출력
select name,(to_char(sdate,'"등록일: "yyyy"년 "mm"월 "dd"일"')) from students;

