--drop table emp02;
--
--drop table mem2;

select * from mem;

create table emp02(
empno number(4) not null,
ename varchar2(30) not null,
job varchar2(9),
detno number(2)
);

insert into emp02 values(
1,'홍길동','clerk',2
);

insert into emp02 values(
2,'유관순',null,null
);

insert into emp02 values(
3,null,null,null
);

--drop table emp02;

create table emp02(
empno number(4) unique,
ename varchar2(30) not null,
job varchar2(9),
detno number(2)
);

insert into emp02 values(
1,'홍길동','clerk',2
);

insert into emp02 values(
2,'유관순',null,null
);

insert into emp02 values(
null,'이순신',null,null
);

insert into emp02 values(
null,'강감찬',null,null
);

insert into emp02 values(  --unipue조건에 걸림
2,'김구',null,null
);

select * from emp02;
desc emp02;
delete emp02 where empno is null;
commit;

-- alter로 중간에 제약 조건 변경을 잘 안함 (보통 생성할 때 정해둠)
alter table emp02 modify empno number(4) not null;

alter table emp02 modify empno number(4);

-- not null, pk_emp02_empno(별칭)
alter table emp02 add constraint pk_emp_empno primary key(empno);

alter table emp02 drop constraint pk_emp02_empno;

create table emp02(
empno number(4) primary key,
ename varchar2(30) not null,
job varchar2(9),
detno number(2)
);

--drop table mem;

create table mem(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(100) default '무명',
gender varchar2(6) check(gender in ('Male','Female')) --male,female MALE,FEMALE 등록불가(에러뜸)
);

insert into mem values(
'aaa','1111','홍길동','Male'
);

insert into mem values(
'bbb','1111','유관순','Female'
);

commit;

create table board2 (
bno number(4) primary key,
dtitle varchar2(1000) not null,
id varchar2(30),
constraint fk_board2_id foreign key(id) references mem(id)
);

select * from mem;
select * from board2;

delete mem where id = 'aaa';

-- 외래키로 등록 시 부모키에 해당 값이 없을시 에러
insert into board2 values(
4,'제목4','ccc'
);

--외래키 삭제
alter table board2 drop constraint fk_board2_id;

-- 부모키 삭제시, 외래키로 등록된 값들을 모두 삭제
alter table board2
add constraint fk_board2_id foreign key (id)
references mem(id) on delete cascade; -- on delete set null

-- default : on delete restricted : 부모키 삭제시, 외래키에 등록된 값이 있으면, 삭제가 되지 않음
-- on delete set null: 부모키 삭제 시 외래키로 등록된 값을 삭제하진 않고 해당되는 컬럼값만 null 처리

-- 부모테이블의 aaa삭제 시 자식 테이블의 aaa글이 모두 삭제
delete mem where id = 'aaa';

select * from mem;
select * from board2;

drop table mem;
drop table board2;

create table mem(
id varchar2(30) primary key,
pw varchar2(100) not null,
name varchar2(100),
deptno number(4)
);

insert into mem values(
'aaa','1111','홍길동',10
);


insert into mem values(
'ccc','1111','이순신',30
);

commit;

select * from mem;

-- 10'총무부', 20'인사부', 30'마케팅'

select id,pw,name,deptno,
decode(deptno,
10, '총무부',
20,'인사부',
30,'마케팅'
)
from mem;

select * from employees;
select job_id from employees;

-- clerk: 5%, rep: 10%, man15%

-- 1. clerk, rep, man인 사람을 선택 출력
select job_id from employees;
-- 뒷부분 글자만 가져오기
select substr(job_id,4) j_id from employees;
-- 1번을 선택해 출력하기
-- 소문자로 입력해도 출력 가능하게 하기 (lower 사용)
select substr(job_id,4) j_id from employees
where lower(substr(job_id,4)) in ('clerk','rep','man');

-------------------- decode문
select substr(job_id,4) j_id, salary,

decode (substr(job_id,4) ,
'CLERK',salary*1.05,
'REP',salary*1.1,
'MAN',salary*1.15
) as sal

from employees
where substr(job_id,4) in ('CLERK','REP','MAN');
-----------------


create table lavel_data (
	id VARCHAR2(50) primary key,
	lavel number(1) not null
);
insert into lavel_data (id, lavel) values ('Arlen', 4);
insert into lavel_data (id, lavel) values ('Catie', 4);
insert into lavel_data (id, lavel) values ('Adoree', 5);
insert into lavel_data (id, lavel) values ('Cher', 4);
insert into lavel_data (id, lavel) values ('Dorita', 5);
insert into lavel_data (id, lavel) values ('Zulema', 1);
insert into lavel_data (id, lavel) values ('Richy', 4);
insert into lavel_data (id, lavel) values ('James', 5);
insert into lavel_data (id, lavel) values ('Aeriel', 5);
insert into lavel_data (id, lavel) values ('Reinald', 3);
insert into lavel_data (id, lavel) values ('Bernardina', 1);
insert into lavel_data (id, lavel) values ('Tiertza', 2);
insert into lavel_data (id, lavel) values ('Carolyne', 5);
insert into lavel_data (id, lavel) values ('Jonis', 1);
insert into lavel_data (id, lavel) values ('Abigael', 5);
insert into lavel_data (id, lavel) values ('Pauli', 4);
insert into lavel_data (id, lavel) values ('Sheffie', 2);
insert into lavel_data (id, lavel) values ('Tully', 2);
insert into lavel_data (id, lavel) values ('Ricard', 5);
insert into lavel_data (id, lavel) values ('Jameson', 3);
insert into lavel_data (id, lavel) values ('Thorstein', 1);
insert into lavel_data (id, lavel) values ('Arlyne', 5);
insert into lavel_data (id, lavel) values ('Mela', 5);
insert into lavel_data (id, lavel) values ('Yetta', 3);
insert into lavel_data (id, lavel) values ('Corilla', 4);
insert into lavel_data (id, lavel) values ('Adoree', 1);
insert into lavel_data (id, lavel) values ('Sabine', 3);
insert into lavel_data (id, lavel) values ('Nelson', 3);
insert into lavel_data (id, lavel) values ('Isahella', 5);
insert into lavel_data (id, lavel) values ('Mandel', 5);
insert into lavel_data (id, lavel) values ('Sasha', 4);
insert into lavel_data (id, lavel) values ('Deanne', 1);
insert into lavel_data (id, lavel) values ('Thorny', 1);
insert into lavel_data (id, lavel) values ('Jacki', 3);
insert into lavel_data (id, lavel) values ('Sibby', 2);
insert into lavel_data (id, lavel) values ('Jack', 2);
insert into lavel_data (id, lavel) values ('Chandra', 2);
insert into lavel_data (id, lavel) values ('Cecilla', 5);
insert into lavel_data (id, lavel) values ('Saunder', 1);
insert into lavel_data (id, lavel) values ('Way', 4);
insert into lavel_data (id, lavel) values ('Velma', 3);
insert into lavel_data (id, lavel) values ('Keelia', 1);
insert into lavel_data (id, lavel) values ('Clay', 4);
insert into lavel_data (id, lavel) values ('Grace', 2);
insert into lavel_data (id, lavel) values ('Maura', 5);
insert into lavel_data (id, lavel) values ('Karolina', 4);
insert into lavel_data (id, lavel) values ('Mal', 5);
insert into lavel_data (id, lavel) values ('Annette', 4);
insert into lavel_data (id, lavel) values ('Issy', 2);
insert into lavel_data (id, lavel) values ('Reid', 2);
insert into lavel_data (id, lavel) values ('Dall', 4);
insert into lavel_data (id, lavel) values ('Sukey', 2);
insert into lavel_data (id, lavel) values ('Etty', 5);
insert into lavel_data (id, lavel) values ('Kendall', 5);
insert into lavel_data (id, lavel) values ('Gibby', 4);
insert into lavel_data (id, lavel) values ('Kylila', 2);
insert into lavel_data (id, lavel) values ('Orelia', 2);
insert into lavel_data (id, lavel) values ('Alexei', 4);
insert into lavel_data (id, lavel) values ('Iorgo', 1);
insert into lavel_data (id, lavel) values ('Clive', 1);
insert into lavel_data (id, lavel) values ('Roger', 1);
insert into lavel_data (id, lavel) values ('Halette', 3);
insert into lavel_data (id, lavel) values ('Clyve', 3);
insert into lavel_data (id, lavel) values ('Peadar', 1);
insert into lavel_data (id, lavel) values ('Mose', 4);
insert into lavel_data (id, lavel) values ('Raimundo', 3);
insert into lavel_data (id, lavel) values ('Glori', 1);
insert into lavel_data (id, lavel) values ('Merrel', 2);
insert into lavel_data (id, lavel) values ('Ulberto', 2);
insert into lavel_data (id, lavel) values ('Bren', 4);
insert into lavel_data (id, lavel) values ('Ker', 2);
insert into lavel_data (id, lavel) values ('Rosalinda', 1);
insert into lavel_data (id, lavel) values ('Delphinia', 5);
insert into lavel_data (id, lavel) values ('Johnette', 3);
insert into lavel_data (id, lavel) values ('Marilyn', 3);
insert into lavel_data (id, lavel) values ('Paddy', 2);
insert into lavel_data (id, lavel) values ('Antony', 3);
insert into lavel_data (id, lavel) values ('Kinna', 5);
insert into lavel_data (id, lavel) values ('Rogers', 5);
insert into lavel_data (id, lavel) values ('Zolly', 5);
insert into lavel_data (id, lavel) values ('Lance', 1);
insert into lavel_data (id, lavel) values ('Carroll', 2);
insert into lavel_data (id, lavel) values ('Geralda', 2);
insert into lavel_data (id, lavel) values ('Riobard', 2);
insert into lavel_data (id, lavel) values ('Sunshine', 4);
insert into lavel_data (id, lavel) values ('Betteanne', 2);
insert into lavel_data (id, lavel) values ('Andrea', 1);
insert into lavel_data (id, lavel) values ('Theresina', 3);
insert into lavel_data (id, lavel) values ('Koenraad', 4);
insert into lavel_data (id, lavel) values ('Eydie', 1);
insert into lavel_data (id, lavel) values ('Karolina', 2);
insert into lavel_data (id, lavel) values ('Sutton', 5);
insert into lavel_data (id, lavel) values ('Ikey', 5);
insert into lavel_data (id, lavel) values ('Ugo', 1);
insert into lavel_data (id, lavel) values ('Mallory', 4);
insert into lavel_data (id, lavel) values ('Mariska', 2);
insert into lavel_data (id, lavel) values ('Edmund', 3);
insert into lavel_data (id, lavel) values ('Twyla', 5);
insert into lavel_data (id, lavel) values ('Laney', 5);
insert into lavel_data (id, lavel) values ('Onida', 4);

commit;

select * from lavel_data;

-- 1: 100포인트, 2:1000포인트, 3:5000포인트, 4:10000포인트, 5:20000포인트
select id, lavel,
decode (lavel,
1,100,
2,1000,
3,5000,
4,10000,
5,20000
)||'point' as point from lavel_data; -- point 단어추가
as point from lavel_data;

-- decode는 일치하는 경우만 사용 가능
-- case, decode와 같은 기능이지만, 비교 연산자를 사용할 수 있음.
select id,pw,name,deptno,
case
when deptno = 10 then '총무부'
when deptno = 20 then '인사부'
when deptno = 30 then '마케팅'
end as deptName
from mem;

-- 1, 2, 3:5000포인트, 4, 5:20000포인트
select id, lavel,
decode (lavel,
1,5000,
2,5000,
3,5000,
4,20000,
5,20000
)||'point' as point from lavel_data; -- point 단어추가

select id,lavel,
case
when lavel >= 1 and lavel <= 3 then 5000
when lavel >= 4 then 20000
end point
from lavel_data;

select * from students;

-- avg 90점 이상 A, 80점 이상 B, 70:C, 60:d,f
--result 컬럼
select name,avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
when avg <= 60 then 'f'
end result
from students;

-- 테이블 전체 복사
create table stu as select * from students;

-- 컬럼추가
select * from stu;

alter table stu add result varchar2(2);

select
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
when avg <= 60 then 'f'
end re
from stu;

--
update stu set result = 
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
when avg <= 60 then 'f'
end
;

rollback;
select * from stu;
commit;

-- 파이썬에서 if문 구현을 해서 처리 대신 oracle에서 하는게 더 빠름

-- rank() over 순위를 구현하는 함수
select no, name, total, rank() over(order by total desc) from stu
order by no;

-- rank() over(): 중복순위 개수만큼 다음 순위 값을 증가시킴
-- desen_rank() over(): 중복순위가 존재해도 순차적으로 다음 순위 표시

--select no,name,total,
select rank() over(order by total desc) as ra from stu
;

select ranks from (
select rank() over(order by total desc) as ranks from stu b
);
-- 순위를 rank컬럼에 추가

update stu set rank = (

select ranks from (
select no, rank() over(order by total desc) as ranks from stu
) b
where b.no = a.no

);

select ranks from (select no,rank() over (order by total desc) as ranks from stu;

select * from stu;

select no, rank from stu;
select no,rank() over (order by total desc) as ranks from stu;

--rank 등수 입력처리
update stu a set rank = (
select ranks from (
select no,rank() over (order by total desc) as ranks from stu) b
where a.no = b.no
);

commit;

-- case
-- salary 5000 미만은 월급 15%인상, 5000~8000: 10%인상, 8000초과 5%인상
select * from employees;

select emp_name, salary,
case
when salary >= 8000 then salary * 1.05
when salary >= 5000 and salary <= 8000 then salary * 1.10
when salary < 5000 then salary * 1.15
end as upsal
from employees;

-- emp_name에 대문자 D가 포한된사람 10% M은 5%인상, 그 외는 0%인상 
select * from employees;

select emp_name, salary,
case
when emp_name like '%D%' then salary * 1.1
when emp_name like '%M%' then salary * 1.05
else salary
end as upsal
from employees;

select * from employees;

select department_id, commission_pct from employees
where commission_pct is not null;

-- 커미션이 있는 사원수를 출력하시오
select count(*) from employees
where commission_pct is not null;

-- 부서별 사원 수 를 출력하시오
select department_id,count(*) from employees
group by department_id
order by department_id;

--부서별 평균 월급
select department_id, avg(salary) from employees;

-- 그룹함수에서 조건을 사용하려면  비교연산 having절을 이용한다.
-- 부서별 평균월급이 70000보다 높은 사람의 인원수를 출력하시오
select department_id,avg(salary) from employees
group by department_id
having avg(salary) >= 7000
;

-- 전체 평균월급보다 적게 받는 사원 수를 출력하시오,
select department_id,count(*) from employees
where salary < (select avg(salary) from employees)
group by department_id
;

select avg(salary) from employees; -- 6461

select avg(salary) from employees
group by department_id;


select department_id,count(*) from employees
where salary < 6461
group by department_id;
--
select salary from employees
where department_id = 60;

-- 부서별 평균 월급이 6000 이하인 부서별 인원수를 구하시오
-- 그룹 함수는 having절이라는 조건문을 사용. whereㅈ절에는 사용 불가
select department_id,avg(salary) from employees
group by department_id
having avg(salary) <= 6000;

-- 부서 번호, 부서별 평균 월급
select department_id,avg(salary) from employees
group by department_id;

-- 부서 번호, 개인월급, 인원
select department_id, count(*) from employees
group by department_id,salary;

-- 부서별 평균 월급보다 적게 받는 사원을 출력
select department_id, emp_name from employees a
where salary <
(
select salarys from (
select department_id,avg(salary) salarys from employees
group by department_id
) b
where a.department_id = b.department_id
)
;

-- 부서별 평균 월급보다 적게 받는 사원 수
select department_id,count(*) from employees a
where salary <
(
select salarys from (
select department_id,avg(salary) salarys from employees
group by department_id
) b
where a.department_id = b.department_id
)
group by department_id
;

select department_id, emp_name, salary from employees
where department_id = 30;

select avg(salary) from employees
where department_id != 30;

-- 부서의 최대값과 최소값 출렷, 최대급여 5000이상ㅁ나추렫
select department_id,max(salary),min(salary) from employees
group by department_id
having max(salary)>= 5000
order by department_id desc;


-- 학번, 이름, 전화번호, 주소, 성별, 학년, 학기, 국어, 영어, 수학, 합계, 평균, 등수
-- 1001, 홍길동, 010, 서울, 남자, 1, 1, 100, 100, 100, 300, 1
-- 1001, 홍길동, 010, 서울, 남자, 1, 2, 90, 90, 90, 270, 8
-- 1001, 홍길동, 010, 서울, 남자, 1, 3, 95, 95, 95, 300, 285,15
-- 1001, 홍길동, 010, 서울, 남자, 1, 4, 100, 100, 99, 2991, 1

-- 부서명 department
select * from departments;

select * from employees;

donald OConnell의 부서명 알기

select emp_name, department_id from employees
where emp_name = 'Donald OConnell';

select department_id,department_name from departments
where department_id = 50;
-- 이 두 번의 반복을 한 문장으로 바꿀 수 없느냐

-- join을 사용해 두개의 쿼리를 한개의 쿼리로 구성하기.

-- join
-- 1. cross join
-- 1-1. inner join (equi join, non-equi-join)
-- 3. outer join
-- 4. self join

-- cross join: 특별한 키워드 없이 두개의 테이블을 검색하는 것 (경우의 수가 없음)
select * from employees; -- 107
select * from departments; -- 27

select count(*) from employees, departments; -- 107*27 = 2889
select * from employees,departments;

-- join
-- 두 테이블에 들어가있는 컬럼은 컬럼 앞에 테이블명을 꼭 적어줘야 한다.
select emp_name,a.department_id,department_name from employees a, departments b
where a.department_id = b.department_id;  -- (+): null값도 출력하라 : outer join

select * from member;
select bno,btitle,bcontent,id from board;

-- 101 * 4 = 404
-- 이큐조인 3개도 가능함
select bno,btitle,bcontent,a.id,email,phone,bgroup,bstep,bindent,bhit,bdate,bfile
from member a,board b
where a.id=b.id
;

select * from jobs;

-- inner join: 사원번호, 사원명,(JOb_id, job title 추력

select employee_id,emp_name,a.job_id,job_title 
from employees a, jobs b
where a.job_id = b.job_id and a.job_id= 'SH_CLERK'
;

-- 사원번호 사원명 / 부서번호 부서명 / job_id job_title을 추가하시오
select employee_id,emp_name,e.department_id,department_name,e.job_id, job_title
from employees e, departments d, jobs j
where e.department_id = d.department_id and e.job_id = j.job_id
;

-- member 닉네임
-- board 게시글

select * from board;
select * from member;

SELECT bno, btitle, bcontent,name,bgroup,bstep,bindent,bhit,bdate,bfile 
FROM board a,member b
where a.id = b.id
;

-- 사원번호 사원명 월급 부서번호 부서명 
-- 월급이 평균월급보다 적은 사원을 출력하시오

select employee_id, emp_name, salary, e.department_id, department_name 
FROM EMPLOYEES e, departments d
where e.department_id = d.department_id
and salary < (select avg(salary) from employees)
;

select avg(salary) from employees;

-- 사원번호 사원명 월급 부서번호 부서명 
-- 월급이 부서별 평균 월급보다 작은 사원을 출력하시오
SELECT employee_id, emp_name, salary, e.department_id, department_name
FROM employees e, departments d
WHERE e.department_id = d.department_id
and salary < select department_id, avg(salary) from employees;
 



-- 부서별 평균 월급보다 적게 받는 사원을 출력
select employee_id,emp_name,salary,a.department_id,department_name
from employees a, departments b
where a.department_id = b.department_id

and salary < (
select salarys from (select department_id, avg(salary) salarys from employees
group by department_id) c
where a.department_id = c.department_id
)
;


--
select * from employees;
select * from departments;
select * from jobs;
-- job_id가 CLERK인 사원의 사원명 사원번호 부서명 부서번호 직급번호 직급명 출력

select emp_name, employee_id, department_name, a.department_id, a.job_id, job_title
from employees a, departments b, jobs c
where a.department_id = b.department_id and a.job_id = c.job_id
and a.job_id like '%CLERK';

select salary from employees
order by salary;

--2000-4000 E , 4000-6000 D , 6000-8000 C , 8000-10000 B , 10000-100000 A
create table salgrade(
grade varchar2(10),
losal number(6),
hisal number(6)
);

insert into salgrade values(
'E등급',2000,4000
);
insert into salgrade values(
'D등급',4001,6000
);
insert into salgrade values(
'C등급',6001,8000
);
insert into salgrade values(
'B등급',8001,10000
);
insert into salgrade values(
'A등급',10001,100000
);

select * from salgrade;

-- salary, 등급을 넣으려고 함
-- 등급: salgrade
-- salgrade, employees 같은 컬럼이 없음
-- non-equi join을 이용해서 테이블을 조인
select salary from employees;
select * from salgrade;

-- non-equi join: 두 테이블간 같은 컬럼이 없으면서 
select emp_name, salary, grade
from employees,salgrade; --107 * 5 = 535
where salary between losal and hisal
; -- 107*5 = 535

-- non -equi join 구문 활용해서 students total ABCDE등급 출력하시오
-- 100-90a 89-80b 79-70c 69-60d 60점 미만 F
-- table명: stu_grade grade, lototal,hitotal

create table stu_grade(
grade varchar2(10),
loavg number(3),
hiavg number(3)
);
insert into stu_grade values(
'D등급',60,69
);
insert into stu_grade values(
'C등급',70,79
);
insert into stu_grade values(
'B등급',80,89
);
insert into stu_grade values(
'A등급',90,100
);
insert into stu_grade values(
'F등급',1,59
);

-- non -equi join 구문 활용해서 students total ABCDE등급 출력하시오
-- 100-90a 89-80b 79-70c 69-60d 60점 미만 F
-- table명: stu_grade grade, loavg,hiavg
--name total grade

select name, total,avg, grade
from students,stu_grade
where avg between loavg and hiavg(+);

select * from stu;
update stu set result = '';
commit;

--result 결과값 non equi join이용해 저장
desc stu;
alter table stu modify result varchar2(20);
commit;
--drop table stu_grade;
create table stu_grade(
grade varchar2(10), -- A,A등급
loavg number(5,2), -- 59.99
hiavg number(5,2)
);

--drop table stu_grade;

insert into stu_grade values(
'F등급',0,59.99);
insert into stu_grade values(
'D등급',60,69.99);
insert into stu_grade values(
'C등급',70,79.99);
insert into stu_grade values(
'B등급',80,89.99);
insert into stu_grade values(
'A등급',90,100.00);

select * from stu_grade;
commit;

select name,total,avg, grade
from stu,stu_grade
where avg between loavg and hiavg;



commit;

select name, roral,avg,resulr from stu



-- self join
select employee_id,emp_name,manager_id from employees;

select employee_id, emp_name from employees
where employee_id = 124;

-- 자신의 테이블 2개를 조인해서 결과값을 출력    
select a.employee_id,a.emp_name,a.manager_id,b.emp_name 
from employees a, employees b
where a.manager_id = b.employee_id and a.manager_id = 124;