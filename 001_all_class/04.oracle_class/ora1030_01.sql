select sysdate from dual;

select sysdate-30,sysdate,sysdate+30 from dual;

-- employees 테이블 hire_date컬럼
select hire_date-1,hire_date,hire_date+1 from employees;

-- 날짜 범위 검색가능, 정렬 order by, asc: 순차정렬, desc: 역순정렬
select emp_name,hire_date from employees
where hire_date >= '02/01/01' and hire_date <= '04/12/31'
order by hire_date desc;

select emp_name,hire_date from employees where hire_date between '02/01/01' and '04/12/31' order by hire_date;

--like
select emp_name from employees
where emp_name like '___a%';

select emp_name from employees
where emp_name like '%a_';


-- 정렬
select department_id from employees
order by department_id desc;


-- 월급(salary) 높은순 정렬
select emp_name,salary from employees
order by salary desc;


-- students 테이블 total 역순
select no,name,total from students
order by total desc;

-- 입사일 기준 순차정렬
select employee_id,emp_name,hire_date from employees
order by hire_date asc;

select name,kor,eng,math from students
order by kor desc, eng desc;

select name from students
order by name;

-- 입사일 빠른 순, 이름은 역순
select emp_name,hire_date from employees
order by hire_date asc,emp_name desc;


-- abs 절대값
select -10,abs(-10) as abs from dual;

select kor,kor-eng,abs(kor-eng) abs from students
order by abs desc;

-- floor 소수점 이하 버림
select 3.141592, floor(3.141592) from dual;

-- trunc: 버림, 소수점 자리수 지정 버림
select 34.5678,trunc(34.5678,2) from dual;
select 34.5678,trunc(34.5678,-1) from dual;

-- ceil 소수점 이하 올림
select 34.5678,ceil(34.5678) from dual;

-- round 반올림, 자리수 범위 지정
-- 소수점 첫째 자리에서 반올림
select 34.5678, round(34.5678) from dual;

-- 소수점 둘째 자리까지 출력(셋째자리에서 반올림) 
select 34.5678, round(34.5678,2) from dual;

-- 양수 첫째자리에서 반올림
select 34.5678, round(34.5677,-1) from dual;


-- mod : 나머지
select 27/2,mod(27,2) from dual;
select 30/3, mod(31,7) from dual;

-- 사원번호가 홀수인 사원을 출력하시오
select employee_id, emp_name from employees
where mod(employee_id,2) = 1
order by employee_id asc;

-- 최종연봉 : (월급*12) + (월급*12*커미션), 소수점 2번째 자리에서 반올림, (소수점 첫째 자리까지만 출력)
select employee_id,emp_name,salary "$" ,trunc((salary*12)+((salary*12)*nvl(commission_pct,0))*1381.86795,1) ysalary from employees ;

select * from students;



-- 시퀀스: 자동으로 번호를 부여
create sequence stu_seq
start with 1
increment by 1
minvalue 1
maxvalue 9999
nocycle
nocache;

-- 시퀀스에서 번호 생성
select stu_seq.nextval from dual;

select stu_seq.currval from dual;

-- 게시판 케이블 생성
create table board(
bno number(4),
btitle varchar2(100),
bcontent varchar2(4000),
id varchar2(30),
bhit number(10),
bdate date
);


insert into board values(
1, '제목입니다.','내용입니다.','aaa',1,sysdate
);

insert into board values(
2, '제목입니다.','내용입니다.','aaa',2,sysdate
);

insert into board values(
stu_seq, '제목입니다.','내용입니다.','aaa',1,sysdate
);

select * from board;
commit;

select * from board;

create SEQUENCE board_seq
start with 14   -- 시작 번호
INCREMENT by 1  -- 증감 숫자
MINVALUE 1      -- 최소값
MAXVALUE 9999   -- 최댓값
NOCYCLE         -- 1-9999 이상이 되면, 다시 1 
NOCACHE         -- 메모리에 시퀀스값 미리 할당
;
insert into board values(
board_seq.nextval,'제목14','내용14','aaa',1,sysdate
);

select * from board;
commit;

--drop table board;

create table board(
bno number(4),
btitle varchar2(100),
bcontent clob, --대용량 글자 타입
id varchar2(20),
bgroup number(4), -- 답변달기 그룹핑
bstep number(4),   -- 답변달기 경우 순서정의
bindent number(4), -- 답변달기 들여쓰기
bhit number(10), -- 조회수
bdate date  --등록일
);

select board_seq.currval from dual;

insert into board values(
board_seq.nextval,'제목1','내용1','aaa',board_seq.currval,0,0,1,sysdate
);

select * from board;

-- students_seq.nextval
--students 테이블 100 -> 101번
-- 101,홍길순,100,99,90,total,avg,rank,sysdate(날짜)

select * from students;
rollback;
create sequence students_seq
start with 101
increment by 1
minvalue 101
maxvalue 9999
nocycle
nocache
;

insert into students values(
students_seq.nextval,'홍길순',99,99,90,(99+99+90),(99+99+90)/3,0,sysdate
);
select * from students;
select *,round(avg,2) from students;  --요렇게 하면 에러가 뜸
select s.*,round(avg,2) from students s;

select dept_seq.nextval from dual;

--s_seq
-- 시작 1, 증분 1 최대값 99999
create sequence s_seq
start with 1
increment by 1
minvalue 1
maxvalue 99999
nocycle
nocache
;
-- 시퀀스 생성,nextval:다음 시퀀스번호 생성, currval: 현재 시퀀스번호 보여줌

select s_seq.nextval from dual;
select emp_seq.nextval from dual;
select emp_seq.currval from dual;


-- 타입
-- 문자형, 숫자형, 날짜형 총 3가지
-- char, varchar2, nchar, nvarchar2, long, clob (문자형)
-- char, varchar2: 한글문자 입력 시 3byte사용
-- varchar2(6): 한글 2문자 입력
-- nvarchar2(5): 한글 5자리까지 입력 가능 - 2byte

-- number                                       (숫자형)

-- date, timestamp                              (날짜형)
-- date: 초까지 입력, timestamp: 미리세컨드(ms) 초까지 입력


select '홍길동' from dual;

-- length: 문자길이
select length('홍길동') from dual;

-- 이름의 길이로 역순정렬
select name,length(name) n from students
order by n desc;

-- lengthb: byte 크기
SELECT lengthb('홍길동') from dual;



select * from students;

-- 합계가 200이면서 번호가 10이상 50이하이면서 이름의 2번째 자리에 e가 들어가있는 학생을 출력하시오
select * from students
where total >= 200 and no >=10 and no <= 50 and name like '_e%';

select * from students
where total >= 200;

-- select * from 테이블
-- 이중쿼리
select * from (
select * from students
where total >= 200
)where name like '_e%'and no >= 30;

ROLLBACK;

select no,name,total,rank from students;

-- 등수 함수 rank() over(기준점) 입력, no중복이 없음(유일키, 기본키, 프라이머리키(primary key))

select no,name,total,rank() over(order by total desc) ranks from students;
select rnaks from (select no, rank() over(order by total desc) ranks from students);

select * from students;

select no,name,total,rank from students
order by total desc;


-- 수정: update
update students a
set rank = (
select ranks from (select no,name,total,rank() over(order by total desc) ranks from students) b 
where a.no =b.no
);

select * from students;

update students a 
set rank = 1
where a.no = 101;

rollback;

select no, rank() over(order by total desc) as ranks from students;

update students
set rank = 1
where no = 101;

update students
set rank = 2
where no = 96;

update students
set rank = 3
where no = 64;

update students
set rank = 4
where no = 49;

update students
set rank = 5
where no = 14;


-- 사원번호가 낮은 순으로 등수를 생성
select employee_id,emp_name,rank() over(order by employee_id desc) as ranks from employees;


commit;
-- 사원번호가 높은순으로 등수를 생성하시오.
-- 사원번호, 사원명, 등수

select rank() over(order by employee_id desc) ranks from employees;
--drop table /EMP2;

-- emp2 테이블에 employees 복사시켜서 생성
create table emp2 as select * from employees;

-- rank() 실행
select rank() over(order by employee_id desc) from employees;
desc emp2;

-- 테이블 컬럼 추가
alter table emp2 add rank number(4);
desc emp2;

select * from emp2;

--rank()등수를 rank에 입력
update emp2 e set rank =(
select ranks from (select employee_id,rank() over(order by employee_id desc) as ranks from employees e2
where e.employee_id = e2.employee_id
);

select employee_id,rank from emp2
order by employee_id desc;

select * from emp2;

-- 컬럼의 순서를 변경
-- emp_name 뒤에 rank칼럼을 배치
alter table emp2 modify EMAIL invisible;
alter table emp2 modify phone_number invisible;
alter table emp2 modify hire_date invisible;
alter table emp2 modify salary invisible;
alter table emp2 modify MANAGER_ID invisible;
alter table emp2 modify COMMISSION_PCT invisible;
alter table emp2 modify RETIRE_DATE invisible;
alter table emp2 modify DEPARTMENT_ID invisible;
alter table emp2 modify JOB_ID invisible;
alter table emp2 modify CREATE_DATE invisible;
alter table emp2 modify UPDATE_DATE invisible;

--select * from emp2;
-- 컬럼을 나타나게함
alter table emp2 modify EMAIL visible;
alter table emp2 modify phone_number visible;
alter table emp2 modify hire_date visible;
alter table emp2 modify salary visible;
alter table emp2 modify MANAGER_ID visible;
alter table emp2 modify COMMISSION_PCT visible;
alter table emp2 modify RETIRE_DATE visible;
alter table emp2 modify DEPARTMENT_ID visible;
alter table emp2 modify JOB_ID visible;
alter table emp2 modify CREATE_DATE visible;
alter table emp2 modify UPDATE_DATE visible;

-- 컬럼 삭제
alter table emp2 drop column email;
alter table emp2 drop column phone_number;
alter table emp2 drop column hire_date;
alter table emp2 drop column salary;
alter table emp2 drop column MANAGER_ID;
alter table emp2 drop column COMMISSION_PCT;
alter table emp2 drop column RETIRE_DATE;
alter table emp2 drop column CREATE_DATE;
alter table emp2 drop column UPDATE_DATE;

select * from emp2;

select * from departments;
desc departments

alter table emp2 add DEPARTMENT_NAME varchar2(80);

-- emp2에는 부서명이 없음
select * from emp2;

select department_id, department_name from emp2;
select department_id, department_name from departments;

update emp2 
set department_name = '배송부'
where department_id = 50
;

update emp2 e
set e.department_name = 
(
select d form (select department_id,department_name d from departments) e2
where e.department_id = e2.department_id
)
;

-- table 복사 
--drop table stu;
create table stu as select * from students;

desc stu;

alter table stu drop column rank;

select * from stu;


--total 칼럼,avg컬럼, rank컬럼 추가
alter table stu add total number(4);
alter table stu add avg number(4);
alter table stu add rank number(4);
alter table emp2 modify EMAIL invisible;
alter table stu modify sdate visible;
update stu set total = kor+eng+math,avg = (kor+eng+math)/3;

--update stu 
select total ,rank() over(order by total desc) as ranks from stu;

update stu s set rank =
(select ranks from (select no, rank() over(order by total desc) as ranks from stu) s2 
where s.no = s2.no
);

select * from stu;
commit;


-- 날짜 함수
--현재 날짜: sysdate
select sysdate from dual;
select sysdate-1 from dual;
select sysdate+30 from dual;

create table datetable (
no number(4),
predate date,
today date,
nextdate date
);

-- 회원가입 1달치, 6개월, 1년
insert  into datetable values(
1, sysdate - 30, sysdate,sysdate+180
);


select no,predate,today 가입일, nextdate 만료일 from datetable;

select * from member;

select id,name,mdate,sysdate,round(sysdate-mdate) from member
where sysdate >= mdate + 180;

-- 입사일 기준으로 현재 날짜와 며칠이 지났는지 출력하시오
select * from employees;
select emp_name,hire_date,sysdate,round(sysdate-hire_date) from employees;

-- 15일 이상이면 한달을 올림(다음달 1일), 15일 이하면 일 초기화
select hire_date,round(hire_date,'month') from employees;

-- 일의 숫자르 1로 초기화 함
select hire_date,
trunc(hire_date,'month') from employees;

-- 입사일과 현재일 기준의 달 수 
select hire_date,sysdate,months_between(sysdate,hire_date) from employees;
--month_between 두 일자 사이에 지나간 달 수를 알려줌
select hire_date,sysdate,round(months_between(sysdate,hire_date))as 개월수 ,round(sysdate-hire_date) as 일수 from employees;

-- add_manths 3개월 추가
select hire_date,add_months(hire_date,3) from employees;

-- next_day: 다음주 수요일 날짜를 알려줌
select sysdate,next_day(sysdate,'수요일')from dual;

select sysdate,next_day(sysdate,'토요일')from dual;

-- last_date : 그달의 마지막 날짜를 알려줌
select hire_date, last_day(hire_date)from employees;
select sysdate last_;


-- 형변환 함수
select sysdate from dual;

select to_char(sysdate, 'yy/mm/dd') from dual;

select to_char(hire_date,'yyyy-mm-dd') from employees;

select to_char(to_date('24/01/01');

select * from member where id='aaa' and pw='1111';
select * from member;   

update member set id='abc',pw='1111',name='임정우',email='zmgkgzmgkg4@gmail.com',gender='male'
where id='Trineman';

commit;

select * from member where id='eee';

select * from member;

alter table member modify pw VARCHAR2(4);

alter table member modify pw VARCHAR2(8);
