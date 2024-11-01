-- 입사일의 마지막 날짜를 출력하시오.
-- 10/1 -> 10/31, 9/5 -> 9/30
--last_day
select last_day(hire_date) from employees;

-- 가입입
select sdate from students;

-- 가입일로부터 1년 후 날짜를 출력
select sdate, add_months(sdate,12) from students;

-- 현재일 기준으로 6개월 이내에 가입한 회원만 출력하시오. (6개월 이후라면 등호 방향만 바꾸면 됨
select sdate from students
where sdate > add_months(sysdate,-6)
order by sdate;

-- 년도 월별로 가입 인원을 출력하시오
select mdate,last_day(mdate) from member;

select last_day(mdate) md from member
order by md;

select substr(last_day(mdate),1,5) md, count(*) from member
group by last_day(mdate)
order by md;

-- employees 테이블에서 부서별(department_id) 인원을 출력하시오
select department_id,count(*) from employees
group by department_id;

-- 그룹함수: sum,avg,count,min,max,median
--drop table emp3;

-- 테이블 데이터까지 복사해서 생성
create table emp3 
as select * from employees;

select * from emp3;

-- 테이블 구조만 복사해서 생성
create table emp4
as select * from employees where 1=2;

select * from emp4;
--drop table emp4;
--테이블 구조가 있는 상태에서 모든 데이터를 입력하는 방법
insert into emp4 select * from employees;
rollback;

-- 선택한 데이터만 가져와서 테이블에 집어넣는 방법.
-- 집어넣기 전에 제약 조건 보기
insert into emp4(employee_id,emp_name,salary,hire_date)
select employee_id,emp_name,salary,hire_date from employees;

-- insert, update, delete
-- commit, rollback

------ 테이블
-- create: 생성, alter: 변경, drop: 삭제   이 3개는 한번 결정하면 끝이다.
-- 삭제 전에 복사본 만들고 삭제하고, 복사본은 몇개월, 1년 후 삭제하던지 해야 추후 생길 문제를 대비할 수 있음

select * from emp4;

-- alter add: 테이블에 컬럼 추가
alter table emp4
add(hire_date2 date);

desc emp4;

-- 컬럼 변경: 컬럼 안에 데이터가 있다면 제약조건, 65길이의 문자가 있다면 50으로 변경 안됨
alter table emp4
modify(email VARCHAR2(70));

alter table emp4
modify(email VARCHAR2(50));

-- 에러가되
alter table emp4 
modify(emp_name varchar2(5));

-- 칼럼의 길이 확인
select max(length(emp_name)) from employees;
select length(emp_name) em from employees
order by em desc;

-- 컬럼 타입 변경: 컬럼 안 데이터가 Null이면 가능
-- 다른 타입인 경우: 데이터를 null로 바꾼 후 타입 변경
select * from emp4;
alter table emp4 
modify(email number(6));

alter table emp4
modify(emp_name number(20));

desc emp4;

--employee_id값을 email칼럼에 복사
update emp4 set email = employee_id; 

-- employee_id값을 phonr_number 입력하시오
update emp4 set phone_number = employeed_id;

rollback;
commit;

select * from emp4;
update emp4 set phone_number = '198a' where employee_id = 198;

-- 문자형 타입을 숫자형 타입에 복사
-- 안에 있는 데이터가 모두 숫자형 이기에 가능
-- 문자가 포함돼있으면 타입 변경이 불가
update emp4 set manager_id = phone_number;

-- 컬럼 이름 변경
desc emp4;
alter table emp4 rename column phone_number to p_number;

-- 속성 변경 가능
alter table emp4 modify hire_date date null;
alter table emp4 modify hire_date date not null;

-- 컬럼 삭제
alter table emp4
drop column hire_date2;
desc emp4;

-- 테이블 삭제
drop table emp2;
drop table emp3;

-- 테이블 이름 변경
rename emp4 to emp44;


---- 
select * from departments;

---
--drop table board;

-- primary key : 중복 불가, null값 불가
-- unique : 중복 불가, null값 허용
-- not null : 중복 가능, null값 허용
-- default : 값이 입력되지 않았을 때 디폴트값 지정

create table bmember(
id varchar2(30) PRIMARY KEY,
pw varchar2(30) not null,
name varchar2(30) not null,
age number(3) default 0,
gender varchar2(6) check(gender in ('Male','Female')),
nicname varchar2(30),
email varchar2(20),
bdate date default sysdate  -- default: 아무것도 오지 않으면 sysdate를 넣어줘
);

desc bmember;
-- 입력
insert into bmember (id,pw,name,nicname,age,gender,email,bdate) values (
'aaa','1111','홍길동','길동스',20,'Male','aaa@naver.com',sysdate
);

insert into bmember (id,pw,name,nicname,gender,email) values (
'bbb','2222','유관순','관순스','Female','bbb@bbb.com'
);

-- check - Male, Female 2가지 형태 외에는 입력이 안됨
-- male, MALE, malE 데이터 입력 불가
insert into bmember (id,pw,name,nicname,age,gender,email,bdate) values (
'ccc','1111','이순신','순신스',20,'Male','ccc@ccc.com',sysdate
);

-- not null - null을 허용하지 않음. 빈 공백은 가능함
insert into bmember (id,pw,name,nicname,age,gender,email,bdate) values (
'ddd',' ','강감찬','감찬스',20,'Male','ddd@ddd.com','2024/01/01'
);

-- primary key : 중복 불가, null 불가
insert into bmember (id,pw,name,nicname,age,gender,email,bdate) values (
'eee',' ','김구','구스',20,'Male','eee@eee.com','2024/02/21'
);

commit;

select * from bmember;

create table emp3(
empno number(4) unique,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);

insert into emp3 values(
1,'홍','01','01'
);

insert into emp3 values(
2,'유','02','02'
);

-- unique : null값은 허용
insert into emp3 (ename,job,deptno) values(
'이','03','03'
);

-- unique : 중복은 불가
insert into emp3 values(
2,'강','04','04'
);

select * from emp3;

-- primary key 등록할 때 null값, 중복된 값이 존재하면 안됨
-- primary key 추가, 수정
-- constraint id_pk : 이름설정
alter table member add constraint id_pk primary key (id);

-- primary key 삭제
alter table member drop constraint id_pk;

alter table member drop constraint id_pk primary key(id);  -- 예토전생

select * from member;

-- primary key 등록 : 중복불가, null불가
insert into member values (
'fff','1111','홍길자','aaa@aaa.com','123-456-7890','Female','golf',sysdate
);

commit;

desc bmember;

create table board (
bno number(4) primary key,
btitle varchar2(100) not null,
bcontent clob,
id varchar(30),
bgroup number(4),
bstep number(4),
bindent number(4),
bhit number(4),
bdate date,
bfile varchar2(100)
);

insert into board values(
board_seq.nextval,'제목1','내용1','aaa',board_seq.currval,0,0,0,sysdate,''
);

insert into board values(
board_seq.nextval,'제목2','내용2','bbb',board_seq.currval,0,0,0,sysdate,''
);

insert into board values(
board_seq.nextval,'제목5','내용5','eee',board_seq.currval,0,0,0,sysdate,''
);

select * from board;
select * from bmember;


-- 5개만(보드 5* 멤버 5 = 25)
select bno,btitle,bcontent,nicname,email,bgroup,bstep,bindent,bhit,bfile
from board, bmember
where
board.id = bmember.id  -- member id: primary key:, board.id: foreign key
;

-- 조인
select employee_id,emp_name,email,salary,employees.department_id,department_name
from employees,departments
where employees.department_id = departments.department_id;

select department_id,department_name from departments
where department_id = 20;



-- foreign key 추가, 변경
desc board;

--테이블 create 할 때 foreign key 생성
create table board2(
bno number(4) primary key,
btitle varchar2(1000) not null,
bcontent clob,
id varchar2(30)
constraint fk_board2_id foreign key(id)
references bmember(id)
);


-- 닉네임 : id_fk, foreign key : id, ,bmember테이블의 primary key : id 등록
alter table board add constraint id_fk foreign key (id) references bmember(id);

-- foreign key 삭제
alter table board drop constraint id_fk;

select * from board;

select * from bmember;

-- abc 글을 등록하면, 등록이 안됨(무결성 )
insert into board values (
board_seq.nextval,'제목6','내용6','abc',board_seq.currval,0,0,0,sysdate,''
);

-- bmember 테이블 id, foreign key로 board,borad2에 등록
-- foreign key : 외래키
-- 원본의 primary키의 데이터를 지우려면, 원칙상으로 foreign key의 데이터를 모두 삭제해야 삭제가 됨
--  foreign key를 해제해야 삭제가 됨
-- primary key : 기본키
select * from bmember;
delete bmember where id = 'aaa';
delete board where id='aaa';

select * from bmember;
select * from board;

alter table board drop constraint id_fk;

-- foreign key로 등록이 되면, primary key를 삭제할 때 foreign key에 데이터가 있으면 삭제가 안됨
-- on delete cascade: frimary key가 삭제가 되면, foreign key로 등록된 모든 글을 삭제시킴
alter table board add constraint id_fk foreign key (id) references bmember(id) on delete cascade;


alter table board drop constraint id_fk; --foreign key 삭제

-- 1. on delete cascade
-- 기본값 : 입력하지 않을 시, 자식데이터가 있을 경우, 부모데이터가 삭제되지 않음
alter table board add constraint id_fk foreign key (id) references bmember(id);
--자식테이블에 aaa로 쓴 데이터를 삭제해야 id를 삭제할 수 있음
delete bmember where id = 'aaa';
delete board where bno = 1;

-- 2. on delete cascade
-- 부모데이터 삭제 시, 자식데이터 모두 삭제
alter table board add constraint id_fk foreign key (id) references bmember(id) on delete cascade;
-- 부모 데이터를 삭제하면 자식 데이터의 모든 글이 삭제됨
delete bmember where id = 'aaa';
select * from board;

-- 3. on delete set null
-- 부모데이터 삭제 후, 자식데이터에 해당되는 값이 null로 표시
alter table board add constraint id_fk foreign key (id) references bmember(id) on delete set null;
-- 부모 데이터를 삭제하면 자식 데이터의 해당 컬럼만 null 변경되고, 데이터는 그대로 존재
delete bmember where id = 'aaa';
select * from board;

rollback;



rollback;
-- check 구문
create table emp01(
empno number(4) primary key,
ename varchar2(30) not null,
salary number(7,2) check(salary between 2000 and 20000),
gender varchar2(10) check(gender in('Male','Female'))
);

--check가 지정돼있는 칼럼에 추가
insert into emp01 values(
1,'홍길동',2500,'Male'
);
insert into emp01 values(
2,'유관순',20000,'female'
);
insert into emp01 values(
3,'이순신',20000,'male'
);

--default: insert시 값이 입력이 되지 않을 시, 문자, 숫자, 날짜를 넣을 수 있음
create table emp02(
empno number(4) primary key,
ename varchar2(30) default '무명',
income number(4) default 0,
salary number(7,2) check(salary between 2000 and 20000),
gender varchar2(10) check(gender in('Male','Female')),
edate date default sysdate
);

--
insert into emp02 (empno,salary,gender) values(
1,5000,'Male'
);

select * from emp02;

commit;

--drop table board2;
--
--drop table emp01;
--drop table emp3;
--drop table emp44;
--drop table stu;
--drop table chartable;
--drop table chartable2;
--drop table datetable;