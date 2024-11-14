--drop table member;
--drop table date_tab;
--drop table no_tab;
--drop table students;

-- create: 테이블 생성, alter: 테이블 수정, drop: 테이블 삭제
create table member(
 no number(4),
 id varchar2(20),
 pw varchar2(20),
 name VARCHAR2(20),
 phone varchar2(20),
 mdate date
);

-- insert: 데이터 입력, select 데이터 검색, update 데이터 수정, delete 데이터 삭제
INSERT INTO member VALUES (
1,'aaa','1111','홍길동','010-1111-1111','2024-10-29'
);

insert into member values (
2,'bbb','2222','유관순','010-2222-2222','2024-09-20'
);

-- select 데이터 검색
SELECT * FROM member;

commit;
rollback;

-- delete 삭제
--delete member where no='2';
--DELETE member;

--updete 수정
UPDATE member set name='홍길자' where no=1;
update member set name='김구';

select * from member;

-- create 테이블 생성
create table students(
stuno number(4),
name varchar2(20),
kor number(3),
eng number(3),
total number(3),
sdate date
);
-- sysdate: 현재 날까 저장
insert into students values(
1, '홍길동', 100, 100, 100+100, sysdate
);

commit;

-- * 모든 컬럼 검색
select * from students;

--틀정 컬럼을 입력하면 컬럼만검색
select name,sdate from students;

-- 특정 컬럼만 입력하면 컬럼 입력
INSERT INTO students (stuno,name) VALUES(
2,'유관순'
);
select * from students;

-- 
select * from employees;
SELECT count(*) FROM employees;

-- 테이블을 생성하면서 테이블 내용을 모두 복사 복사
create table emp2 as select * from employees;
select * from emp2
select count(*) from emp2; -- 데이터 개수

-- 테이블을 생성하면서 테이블 구조만 복사
create table emp3 as SELECT * FROM employees where 1=2;
select * from emp3;

-- 테이블이 존재할 경우 데이터만 복사
create table member2 as select * from member where 1=2;
INSERT INTO member2 select * from member;

-- 컬럼 데이터타입, 길이 변경
-- alter변경 member테이블 no컬럼 타입길이 변결
alter table member modify no number(10);
--alter 변경, 컬럼의 이름을 변경
alter table member rename column no to memberNo;

desc member;

--명령어는 대, 소문자 상관없이 작동함
select * from member;
SELECT * FROM MEMBER;
select memberno from member;
SELECT MEMBERNO FROM MEMBER;
SELECT memberno from member;

sele

update member set no='';
select * from member;
commit;
alter table member modify no varchar2(10);

select * from member;

desc member;

--drop table emp3;

-- 테이블 구조
desc employees;

-- employees테이블에서 사원번호, 사원 이름, 입사일 출력
SELECT employee_id,emp_name,hire_date FROM employees;

select *from employees;

-- 연산자 : 산술연산자, +,-,*,/

--drop table member;
--drop table member2;
--drop table emp2;

create table member (
	id VARCHAR2(50),
	pw varchar2(4),
	name VARCHAR2(50),
	email VARCHAR2(50),
	phone VARCHAR2(50),
	gender VARCHAR2(50),
	hobby varchar2(50),
	mdate DATE
);
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('aaa', '1111', '홍길동', 'rsherville0@tinyurl.com', '324-226-8544', 'Male', 'golf', '2024-03-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('bbb', '1111', '유관순', 'mrubinlicht1@fotki.com', '475-964-8193', 'Female', 'book', '2024-08-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('ccc', '1111', '이순신', 'bchstney2@walmart.com', '541-891-0085', 'Female', 'run', '2024-08-16');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('ddd', '1111', '강감찬', 'cstubbes3@chron.com', '900-194-4605', 'Female', 'game', '2024-02-10');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('eee', '1111', '김구', 'tnacey4@list-manage.com', '727-883-1542', 'Female', 'golf', '2024-09-10');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Trineman', '6216', 'Riobard', 'rtrineman5@prweb.com', '140-720-7698', 'Male', 'book', '2024-09-03');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Towell', '5201', 'Bryan', 'btowell6@stumbleupon.com', '365-214-7874', 'Male', 'run', '2024-03-16');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Neagle', '4903', 'Horacio', 'hneagle7@nifty.com', '114-384-4352', 'Male', 'run', '2024-02-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Gresham', '4089', 'Valentine', 'vgresham8@quantcast.com', '547-694-3516', 'Female', 'swim', '2024-10-11');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('O''Dare', '6041', 'Doroteya', 'dodare9@dyndns.org', '102-500-7735', 'Female', 'game', '2024-07-29');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Doumic', '1343', 'Stepha', 'sdoumica@com.com', '745-998-5005', 'Female', 'game', '2024-08-08');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Allmann', '9173', 'Husein', 'hallmannb@imageshack.us', '122-775-3647', 'Male', 'book', '2024-01-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Tommis', '6716', 'Roderic', 'rtommisc@sourceforge.net', '673-244-8303', 'Male', 'book', '2024-07-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Bleaden', '4168', 'Drud', 'dbleadend@123-reg.co.uk', '838-544-2408', 'Male', 'golf', '2024-06-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('D''Aguanno', '7476', 'Wini', 'wdaguannoe@cyberchimps.com', '237-714-1340', 'Female', 'run', '2024-06-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Gegay', '8185', 'Bernette', 'bgegayf@yahoo.com', '982-358-5670', 'Female', 'golf', '2024-07-05');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Flea', '6937', 'Fidelity', 'ffleag@reverbnation.com', '602-708-0462', 'Female', 'run', '2024-01-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Shory', '1240', 'Robb', 'rshoryh@intel.com', '621-231-3542', 'Male', 'run', '2024-09-13');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Harm', '1438', 'Flinn', 'fharmi@yelp.com', '328-792-9216', 'Male', 'golf', '2023-12-05');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Poschel', '9693', 'Sterling', 'sposchelj@usnews.com', '499-462-1400', 'Male', 'swim', '2024-05-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Medford', '5717', 'Jacquenette', 'jmedfordk@epa.gov', '634-270-7550', 'Female', 'book', '2024-02-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Gianelli', '5559', 'Katherina', 'kgianellil@wikipedia.org', '967-878-2128', 'Female', 'game', '2024-05-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Kolodziejski', '5522', 'Danella', 'dkolodziejskim@jugem.jp', '110-354-1019', 'Female', 'golf', '2024-03-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Mildmott', '9678', 'Jule', 'jmildmottn@wix.com', '286-208-5611', 'Male', 'run', '2024-07-23');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Pietrowski', '6843', 'Ediva', 'epietrowskio@photobucket.com', '571-362-5389', 'Female', 'golf', '2023-12-30');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Chasemoore', '9290', 'Dunc', 'dchasemoorep@geocities.jp', '390-444-9215', 'Male', 'golf', '2024-03-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Overnell', '6410', 'Barth', 'bovernellq@cdbaby.com', '825-465-2790', 'Male', 'run', '2024-06-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Benford', '8906', 'Margette', 'mbenfordr@twitter.com', '210-839-4892', 'Female', 'swim', '2024-06-20');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Portman', '6013', 'Orson', 'oportmans@reverbnation.com', '258-285-2186', 'Male', 'golf', '2024-06-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Elflain', '7065', 'Trish', 'telflaint@intel.com', '319-787-3297', 'Female', 'golf', '2024-04-30');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Ockland', '7153', 'Deirdre', 'docklandu@sfgate.com', '895-501-5958', 'Female', 'run', '2023-12-03');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Le Floch', '5518', 'Linea', 'lleflochv@hp.com', '734-888-6261', 'Female', 'swim', '2024-01-24');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('McGaugan', '5439', 'Conny', 'cmcgauganw@imageshack.us', '376-451-4038', 'Male', 'game', '2023-11-08');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Lilburn', '6148', 'Shepherd', 'slilburnx@sina.com.cn', '250-173-1654', 'Male', 'swim', '2024-07-03');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Frew', '7401', 'Meaghan', 'mfrewy@unc.edu', '276-431-6409', 'Female', 'swim', '2023-12-04');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Myner', '1917', 'Lorrie', 'lmynerz@wikimedia.org', '550-264-0011', 'Male', 'book', '2024-10-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Knightsbridge', '2295', 'Elias', 'eknightsbridge10@dedecms.com', '906-789-7346', 'Male', 'swim', '2023-12-30');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Merwood', '6745', 'Georgy', 'gmerwood11@comcast.net', '904-984-7938', 'Male', 'golf', '2024-01-14');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Dewsbury', '1477', 'Bond', 'bdewsbury12@amazon.co.jp', '106-232-5734', 'Male', 'swim', '2024-02-02');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Kliche', '5468', 'Nevins', 'nkliche13@admin.ch', '608-113-7174', 'Male', 'game', '2024-06-22');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Fick', '7675', 'Panchito', 'pfick14@senate.gov', '430-438-4575', 'Male', 'book', '2024-03-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Danielczyk', '5661', 'Reinaldos', 'rdanielczyk15@irs.gov', '359-176-0405', 'Male', 'book', '2024-05-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Blazey', '8853', 'Lou', 'lblazey16@about.com', '729-460-3951', 'Male', 'run', '2024-04-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Godly', '6603', 'Pail', 'pgodly17@plala.or.jp', '190-426-8746', 'Male', 'run', '2024-06-02');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Attwoull', '3472', 'Cliff', 'cattwoull18@slideshare.net', '570-758-4710', 'Male', 'golf', '2024-08-10');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Chason', '5763', 'Terrie', 'tchason19@symantec.com', '650-189-0579', 'Female', 'run', '2024-03-11');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Noni', '2224', 'Jannel', 'jnoni1a@bloglovin.com', '871-506-4522', 'Female', 'book', '2024-01-04');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Graham', '3477', 'Mendy', 'mgraham1b@trellian.com', '887-280-4803', 'Male', 'swim', '2024-09-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Griffey', '8521', 'Raff', 'rgriffey1c@51.la', '947-561-4983', 'Male', 'swim', '2024-04-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Wretham', '3484', 'Laure', 'lwretham1d@ted.com', '183-800-2897', 'Female', 'book', '2023-11-07');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Sewart', '5890', 'Lodovico', 'lsewart1e@shareasale.com', '962-952-9409', 'Male', 'swim', '2024-05-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Leber', '3162', 'Cory', 'cleber1f@foxnews.com', '773-506-6136', 'Female', 'run', '2024-05-03');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Germain', '2786', 'Teodoor', 'tgermain1g@usda.gov', '287-887-6296', 'Male', 'book', '2024-09-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('O''Dooghaine', '4249', 'Jeni', 'jodooghaine1h@washingtonpost.com', '656-654-8738', 'Female', 'book', '2024-02-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Ralestone', '2620', 'Lenard', 'lralestone1i@w3.org', '692-797-1702', 'Male', 'book', '2024-09-07');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Yong', '8340', 'Kasey', 'kyong1j@seattletimes.com', '820-634-7148', 'Female', 'run', '2023-12-04');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Yukhov', '6010', 'Gallard', 'gyukhov1k@weather.com', '602-990-8790', 'Male', 'run', '2023-12-22');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Digman', '1555', 'Britt', 'bdigman1l@google.com', '997-747-6638', 'Female', 'game', '2023-11-04');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Rocks', '1647', 'Dane', 'drocks1m@latimes.com', '455-553-6937', 'Male', 'book', '2023-12-07');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Lewisham', '8757', 'Danni', 'dlewisham1n@addtoany.com', '597-704-9376', 'Female', 'swim', '2024-02-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('O''Spillane', '4868', 'Hamlen', 'hospillane1o@indiegogo.com', '584-856-0076', 'Male', 'golf', '2024-02-19');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Keoghane', '8511', 'Garrott', 'gkeoghane1p@accuweather.com', '655-285-1122', 'Male', 'game', '2024-01-23');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Gransden', '3139', 'Maire', 'mgransden1q@bloglines.com', '517-233-8716', 'Female', 'book', '2024-02-24');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Kobiera', '5689', 'Jaime', 'jkobiera1r@flickr.com', '325-635-7089', 'Female', 'run', '2023-11-16');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Craske', '6088', 'Isa', 'icraske1s@delicious.com', '903-771-5929', 'Male', 'golf', '2024-06-26');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Island', '9324', 'Terrance', 'tisland1t@cmu.edu', '569-238-3939', 'Male', 'golf', '2024-03-16');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Hazeldine', '9138', 'Glenn', 'ghazeldine1u@foxnews.com', '118-455-4847', 'Male', 'game', '2024-08-10');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Gutch', '8827', 'Davin', 'dgutch1v@jiathis.com', '602-127-7922', 'Male', 'book', '2024-07-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Pavlenkov', '8269', 'Elane', 'epavlenkov1w@cyberchimps.com', '172-572-0209', 'Female', 'game', '2023-12-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Kasman', '3887', 'Davita', 'dkasman1x@de.vu', '140-813-6914', 'Female', 'book', '2024-09-15');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Andraud', '6948', 'Gunter', 'gandraud1y@rambler.ru', '999-479-2224', 'Male', 'swim', '2024-03-10');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Mandrey', '9531', 'My', 'mmandrey1z@whitehouse.gov', '809-354-8112', 'Male', 'golf', '2024-04-17');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Teers', '1997', 'Lynda', 'lteers20@bigcartel.com', '831-197-8592', 'Female', 'golf', '2024-07-28');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('MacBey', '8775', 'Farand', 'fmacbey21@seesaa.net', '319-735-6030', 'Female', 'swim', '2024-06-05');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Bontoft', '2628', 'Blanca', 'bbontoft22@webnode.com', '818-469-6633', 'Female', 'run', '2024-09-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Gercken', '3185', 'Heinrik', 'hgercken23@webmd.com', '604-301-2929', 'Male', 'game', '2024-03-28');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Huzzay', '5857', 'Alf', 'ahuzzay24@sogou.com', '570-223-4310', 'Male', 'book', '2024-08-16');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Tredger', '7675', 'Sherwood', 'stredger25@bbc.co.uk', '527-871-8185', 'Male', 'run', '2024-06-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Canadine', '8566', 'Nicolis', 'ncanadine26@devhub.com', '800-674-8410', 'Male', 'golf', '2024-08-03');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Paireman', '7080', 'Nichol', 'npaireman27@msn.com', '668-411-8679', 'Female', 'run', '2024-01-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Powis', '6242', 'Mehetabel', 'mpowis28@surveymonkey.com', '271-883-5391', 'Female', 'book', '2024-09-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Walsh', '7311', 'Luther', 'lwalsh29@gmpg.org', '523-360-3018', 'Male', 'golf', '2024-09-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Pont', '4975', 'Edd', 'epont2a@nbcnews.com', '551-629-4794', 'Male', 'golf', '2024-02-22');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Osborne', '7007', 'Gauthier', 'gosborne2b@naver.com', '711-842-1931', 'Male', 'run', '2024-05-31');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Tinker', '8402', 'Andree', 'atinker2c@wp.com', '731-985-8198', 'Female', 'swim', '2023-12-23');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Persence', '7577', 'Obediah', 'opersence2d@elegantthemes.com', '549-594-4369', 'Male', 'run', '2024-05-28');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Boatwright', '1204', 'Ernie', 'eboatwright2e@printfriendly.com', '833-853-7804', 'Male', 'swim', '2024-01-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Kirkhouse', '6330', 'Pernell', 'pkirkhouse2f@soup.io', '412-173-6891', 'Male', 'book', '2024-06-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Ghidetti', '9376', 'Den', 'dghidetti2g@seattletimes.com', '165-768-1973', 'Male', 'run', '2024-10-21');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Keppel', '1397', 'Yolanthe', 'ykeppel2h@harvard.edu', '928-660-5279', 'Female', 'run', '2024-09-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Matteini', '7664', 'Zola', 'zmatteini2i@jalbum.net', '672-317-8567', 'Female', 'swim', '2024-05-28');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Malmar', '9156', 'Andriana', 'amalmar2j@ed.gov', '588-732-4548', 'Female', 'run', '2024-01-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Waplington', '7863', 'Tobiah', 'twaplington2k@dell.com', '996-187-6594', 'Male', 'game', '2024-07-11');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Cosyns', '2387', 'Lauri', 'lcosyns2l@edublogs.org', '943-340-9913', 'Female', 'game', '2024-04-05');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Atto', '5832', 'Had', 'hatto2m@mozilla.com', '624-750-8503', 'Male', 'game', '2024-06-07');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Bushell', '8202', 'Franz', 'fbushell2n@indiegogo.com', '274-938-6045', 'Male', 'game', '2024-03-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Glassford', '3189', 'Virgil', 'vglassford2o@usatoday.com', '361-318-5270', 'Male', 'run', '2024-05-23');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Aron', '3277', 'Freeland', 'faron2p@timesonline.co.uk', '724-482-5099', 'Male', 'game', '2024-08-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Tavner', '8684', 'Brig', 'btavner2q@webeden.co.uk', '366-125-0586', 'Male', 'run', '2024-05-14');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Shiliton', '5557', 'Sandi', 'sshiliton2r@abc.net.au', '407-488-9852', 'Female', 'book', '2024-01-11');

rollback;
SELECT * FROM member;
commit;

--drop table students;

create table students (
	no number(4),
	name VARCHAR2(50),
	kor number(3),
	eng number(3),
	math number(3),
	total number(3),
	avg number,
	rank number(3),
	sdate DATE
);
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (1, '홍길동', 77, 70, 92, 239, 79.6666666667, 0, '2023-12-02');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (2, '유관순', 89, 69, 55, 213, 71, 0, '2024-01-19');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (3, '이순신', 75, 89, 53, 217, 72.3333333333, 0, '2024-04-16');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (4, '강감찬', 85, 91, 81, 257, 85.6666666667, 0, '2023-11-23');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (5, '김구', 62, 71, 54, 187, 62.3333333333, 0, '2024-09-09');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (6, 'Beek', 57, 68, 73, 198, 66, 0, '2024-01-17');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (7, 'Sleicht', 73, 55, 83, 211, 70.3333333333, 0, '2023-12-14');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (8, 'Hulburd', 96, 85, 81, 262, 87.3333333333, 0, '2023-12-25');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (9, 'Tunnick', 50, 66, 100, 216, 72, 0, '2024-08-20');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (10, 'Horsell', 89, 83, 91, 263, 87.6666666667, 0, '2024-01-27');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (11, 'Hunnicutt', 63, 71, 85, 219, 73, 0, '2024-01-09');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (12, 'Gillis', 53, 65, 89, 207, 69, 0, '2024-05-10');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (13, 'Shotbolt', 76, 54, 52, 182, 60.6666666667, 0, '2024-04-19');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (14, 'Neil', 87, 98, 92, 277, 92.3333333333, 0, '2024-09-28');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (15, 'Gever', 56, 99, 54, 209, 69.6666666667, 0, '2024-05-31');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (16, 'Dobrovsky', 74, 65, 55, 194, 64.6666666667, 0, '2024-07-08');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (17, 'Giles', 93, 66, 63, 222, 74, 0, '2024-06-21');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (18, 'Mengue', 70, 59, 65, 194, 64.6666666667, 0, '2024-01-02');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (19, 'Thacker', 60, 95, 66, 221, 73.6666666667, 0, '2024-05-31');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (20, 'Alenshev', 77, 63, 55, 195, 65, 0, '2024-03-21');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (21, 'Baddow', 61, 69, 53, 183, 61, 0, '2024-09-11');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (22, 'Cordery', 72, 52, 86, 210, 70, 0, '2024-01-21');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (23, 'Buddell', 51, 90, 94, 235, 78.3333333333, 0, '2024-02-29');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (24, 'Colgrave', 58, 89, 74, 221, 73.6666666667, 0, '2024-06-06');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (25, 'MacCumiskey', 70, 50, 66, 186, 62, 0, '2024-04-10');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (26, 'Earie', 79, 93, 69, 241, 80.3333333333, 0, '2024-04-10');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (27, 'Lendrem', 93, 72, 80, 245, 81.6666666667, 0, '2024-04-30');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (28, 'Fardoe', 100, 76, 61, 237, 79, 0, '2024-03-22');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (29, 'Alkins', 66, 64, 87, 217, 72.3333333333, 0, '2023-12-16');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (30, 'Worswick', 91, 77, 100, 268, 89.3333333333, 0, '2024-03-31');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (31, 'Keymer', 70, 82, 63, 215, 71.6666666667, 0, '2024-01-22');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (32, 'Jacson', 59, 98, 73, 230, 76.6666666667, 0, '2024-05-11');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (33, 'Eadmeades', 79, 63, 60, 202, 67.3333333333, 0, '2024-09-07');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (34, 'Weeden', 72, 64, 89, 225, 75, 0, '2024-07-15');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (35, 'Starsmore', 92, 60, 50, 202, 67.3333333333, 0, '2024-06-19');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (36, 'Badsworth', 78, 95, 87, 260, 86.6666666667, 0, '2024-05-07');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (37, 'Marthen', 78, 61, 87, 226, 75.3333333333, 0, '2024-04-11');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (38, 'Hearsum', 93, 68, 77, 238, 79.3333333333, 0, '2024-02-09');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (39, 'Barrim', 69, 94, 93, 256, 85.3333333333, 0, '2024-07-30');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (40, 'Postlewhite', 60, 100, 83, 243, 81, 0, '2024-06-09');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (41, 'Ilem', 95, 71, 90, 256, 85.3333333333, 0, '2023-11-15');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (42, 'Birdsey', 85, 76, 65, 226, 75.3333333333, 0, '2024-05-19');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (43, 'Gabbatiss', 74, 99, 86, 259, 86.3333333333, 0, '2024-04-23');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (44, 'Volet', 100, 86, 85, 271, 90.3333333333, 0, '2024-08-02');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (45, 'Stockell', 73, 88, 68, 229, 76.3333333333, 0, '2023-12-09');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (46, 'Brew', 91, 54, 84, 229, 76.3333333333, 0, '2024-03-18');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (47, 'Eversfield', 90, 67, 83, 240, 80, 0, '2024-08-05');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (48, 'Rottgers', 70, 85, 64, 219, 73, 0, '2023-12-27');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (49, 'Twyning', 88, 92, 98, 278, 92.6666666667, 0, '2024-06-09');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (50, 'Primett', 52, 52, 54, 158, 52.6666666667, 0, '2024-06-28');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (51, 'Wisedale', 94, 71, 65, 230, 76.6666666667, 0, '2024-05-13');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (52, 'O'' Mahony', 68, 58, 83, 209, 69.6666666667, 0, '2024-08-28');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (53, 'Curnok', 96, 91, 54, 241, 80.3333333333, 0, '2024-05-02');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (54, 'Stigger', 86, 91, 59, 236, 78.6666666667, 0, '2024-05-20');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (55, 'Martinie', 82, 88, 84, 254, 84.6666666667, 0, '2024-02-04');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (56, 'Bettaney', 54, 57, 89, 200, 66.6666666667, 0, '2024-07-04');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (57, 'Munnis', 75, 99, 64, 238, 79.3333333333, 0, '2024-01-30');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (58, 'Allbut', 59, 68, 58, 185, 61.6666666667, 0, '2024-03-09');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (59, 'Hencke', 64, 64, 72, 200, 66.6666666667, 0, '2024-05-16');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (60, 'Oakenfield', 91, 72, 91, 254, 84.6666666667, 0, '2024-02-19');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (61, 'Matignon', 59, 86, 56, 201, 67, 0, '2024-02-28');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (62, 'Gulk', 69, 74, 62, 205, 68.3333333333, 0, '2024-10-26');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (63, 'Ivell', 88, 68, 63, 219, 73, 0, '2024-10-22');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (64, 'Vaud', 86, 100, 93, 279, 93, 0, '2024-01-28');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (65, 'Aveling', 81, 97, 75, 253, 84.3333333333, 0, '2023-12-03');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (66, 'Vahey', 77, 84, 57, 218, 72.6666666667, 0, '2024-08-19');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (67, 'Albrooke', 71, 84, 87, 242, 80.6666666667, 0, '2024-04-05');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (68, 'Pawlett', 94, 83, 61, 238, 79.3333333333, 0, '2024-08-02');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (69, 'Sparrowhawk', 73, 85, 94, 252, 84, 0, '2024-03-03');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (70, 'Bodle', 64, 74, 80, 218, 72.6666666667, 0, '2024-03-20');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (71, 'Josskovitz', 83, 82, 75, 240, 80, 0, '2024-07-02');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (72, 'Rappa', 99, 88, 87, 274, 91.3333333333, 0, '2024-05-20');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (73, 'Adolfsen', 63, 74, 95, 232, 77.3333333333, 0, '2024-07-24');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (74, 'Colley', 58, 54, 79, 191, 63.6666666667, 0, '2024-04-13');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (75, 'Spark', 85, 84, 98, 267, 89, 0, '2024-05-01');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (76, 'Perrington', 100, 90, 74, 264, 88, 0, '2024-09-07');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (77, 'Steynor', 67, 70, 73, 210, 70, 0, '2024-08-15');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (78, 'Glanester', 65, 99, 63, 227, 75.6666666667, 0, '2024-08-02');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (79, 'Dalglish', 100, 51, 51, 202, 67.3333333333, 0, '2024-03-29');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (80, 'Bowditch', 61, 94, 79, 234, 78, 0, '2023-11-27');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (81, 'Cosbey', 55, 73, 74, 202, 67.3333333333, 0, '2024-02-06');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (82, 'MacRinn', 76, 93, 50, 219, 73, 0, '2023-12-19');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (83, 'Strettell', 89, 94, 73, 256, 85.3333333333, 0, '2024-08-21');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (84, 'Stote', 53, 69, 51, 173, 57.6666666667, 0, '2024-02-04');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (85, 'Hovert', 92, 64, 89, 245, 81.6666666667, 0, '2024-08-21');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (86, 'Mannering', 73, 72, 80, 225, 75, 0, '2024-10-23');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (87, 'Rowlands', 77, 57, 79, 213, 71, 0, '2023-12-05');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (88, 'Barthelme', 80, 61, 58, 199, 66.3333333333, 0, '2024-05-04');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (89, 'Connue', 89, 96, 85, 270, 90, 0, '2024-08-09');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (90, 'Argyle', 70, 59, 98, 227, 75.6666666667, 0, '2024-06-02');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (91, 'Cainey', 72, 55, 99, 226, 75.3333333333, 0, '2024-05-29');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (92, 'Arling', 83, 84, 94, 261, 87, 0, '2024-10-24');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (93, 'Ilchuk', 69, 75, 60, 204, 68, 0, '2024-09-13');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (94, 'Joiris', 88, 74, 79, 241, 80.3333333333, 0, '2024-08-08');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (95, 'Josefsen', 78, 68, 68, 214, 71.3333333333, 0, '2024-05-22');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (96, 'Slorance', 97, 95, 87, 279, 93, 0, '2023-11-05');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (97, 'Timmons', 68, 65, 88, 221, 73.6666666667, 0, '2023-11-12');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (98, 'Arnaldi', 67, 75, 57, 199, 66.3333333333, 0, '2024-04-16');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (99, 'Rodrigo', 62, 68, 78, 208, 69.3333333333, 0, '2023-12-18');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (100, 'Howes', 59, 52, 86, 197, 65.6666666667, 0, '2024-07-19');
commit;
SELECT * FROM students;
commit;
--반올림, 버림, 올림도 적용 가능
select kor,eng,(kor+eng) from students;
select kor,eng,(kor+eng),abs(kor-eng) from students;

select * from employees;

-- 문자는 더하기가 안됨
select emp_name+email from employees; 

--concat 명령어
select concat(employee_id,emp_name) from employees;
SELECT * FROM employees;

-- 달러환산 1384
select salary from employees;
select 1384*salary from employees;
-- 문자로 변환, 천단위 표시
select to_char(salary*1384,'999,999,999') from employees;

select emp_name,salary,salary*1384 from employees;

create table stu(
no number(4),
name varchar2(20),
kor number(3)
);

-- null값 검색 is null
SELECT * FROM stu where name is null;

-- null값이 아닌 것 출력 : is not null
SELECT commission_pct from employees where commission_pct is not null;

SELECT salary FROM employees;
-- 연봉계산 *12
select salary, salary*12 from employees;
select salary, salary*12,salary*12*1384 from employees;

-- 커미션이 없는 사원은 null값이 들어가있는데, 이 null 값에 사칙연산을 하게 되면 null값이 되어 버린다.
SELECT salary, salary*12,salary*12+(salary*12)*commission_pct*0.01 FROM employees;

-- 컬럼명 별칭 사용 as ,쌍따옴표를 사용하면 특수문자, 사이공간까지 컬럼명으로 사용 가능
select salary, salary*12 as "년 봉",salary*12+(salary*12)*nvl(commission_pct,0)*0.01 as "r e a l_yearSalary" FROM employees;

-- nvl()함수 : kor칼럼에 null값이 있으면 0으로 표시
select * from stu;
select no,name,kor,kor+100 from stu;
SELECT no,name,kor,nvl(kor,0)+100 FROM stu;

-- kor 국어 영어수학 합계 평군 등수 
-- 입력일 컬럼명 별칭을 사용해서출력하시오
SELECT * FROM students;
SELECT no as "번호", name as "이름", kor as "국어", eng as "영어", math as "수학", total as "합계", avg as "평균", rank as "등수", sdate as "입력일" FROM students;
--select no as 번호, name as 이름, kor 국어, eng "영어, math 수학, total 합계, avg "평균", rank "등수", sdate "입력일" from students;
select * from students;

-- 사원번호, 이름, 이메일 합쳐서 출력
select employee_id||emp_name||email from employees;
SELECT concat(concat(employee_id,emp_name),email) FROM employees;
select emp_name||' is a '||job_id from employees;

-- 중복 제거
select department_id from employees;
select distinct department_id from employees;
-- 정렬 :oder by - asc 순차정렬: 생략 가능, desc - 역순정렬
select distinct department_id from employees order by department_id desc;

--job id 중복제거
select distinct job_id from employees;
select job_id from employees;

-- 문자열 자르기 substr(0,2) 0,1 / 2앞까지 출력
select * from employees;
select substr(job_id,0,2) from employees;

--4번째부터 컬럼 데이터를 가져와서 중복을 제거함
select distinct substr(job_id,4) from employees;

-- where절: 조건비교연산자: >,<,>=,<=,=,!= (<>, ^=)
select * from employees where manager_id != 124;
select * from employees where job_id = 'SH_CLERK';
select * from employees where employee_id > 100;

-- students에서 합계 250점 이상인 학생 출력
select * from students where total >= 250;

-- 합계가 250이상이면서 국어 점수가 90점 이상인 학생 출력
select * from students where kor >=90 and total >= 250;

-- 영어점수 70점 이상, 90점 이하 출력
select * from students where eng >= 70 and eng <= 90;

-- employees에서 월급이 5000이상이면서 8000이하 검색
select * from employees where salary >= 5000 and salary <= 7000 ;

-- 월급이 5000이 아닌 것을 모두 검색하시오
select * from employees where salary ^= 7000;

-- 부서가 50번인거 출력
select count(*) from employees where department_id = 50;

-- 부서가 50번이 아닌걸 출력
select count(*) from employees where department_id != 50;
--둘이 더해도 원래 길이가 안돼는데, 이는 null 값은 검색하지 않기 때문이다

select count(*) from employees where department_id is null; -- 1개
select count(employee_id) from employees;
select count(department_id) from employees;

-- 급여 4000이하 사원번호 사원명 급여만 출력
select employee_id as 사원번호,emp_name 사원명,salary 급여 from employees where salary <= 4000;

-- 숫자 비교연산자 가능, 날짜 비교연산자 가능
select emp_name,hire_date from employees;
select emp_name,hire_date from employees where hire_date >= '2002/01/01';

--1992/12/31 이전에 입사한 사람 출력
select emp_name,hire_date from employees where hire_date <= '1992/12/31';

-- 2001/0101 - 2004/12/31 출력
select emp_name,hire_date from employees where hire_date >= '2001/12/31' and hire_date <= '2004/12/31';

-- 논리연산자 or와 and의 차이
-- 국어점수가 90점 이상 또는 영어점수가 90점 이상을 출력하시오.
select count(*) from students where kor >= 90 or eng >= 90;
select count(*) from students where kor >= 90 and eng >= 90;

-- 부서번호(department_id)가 80번이면서 job - manager인 경우
select * from employees; 
select * from employees where department_id = 80 and substr(job_id,4) = 'MAN';
select * from employees where department_id = 80 and job_id = 'SA_MAN';

-- 0.2, 0.3, 0.5
select commission_pct from employees where commission_pct is not null;
select commission_pct from employees where commission_pct where commission_pct = 0.2 or commission_pct = 0.3 or commission_pct = 0.5;

-- in 연산자.
select commission_pct from employees where commission_pct in (0.2,0.3,0.5);

--사원번호 110,120,130 출력
select * from employees where employee_id = 110 or employee_id = 120 or employee_id = 130;   --or 연산자
select * from employees where employee_id in (110,120,130);  -- in연산자

--150-170 번호 출력
select * from employees where employee_id >= 150 and employee_id <= 170;

between 포함이 돼있는거에만 해당
select * from employees where employed_id betwen 150 and 60;

select hire_date from employees;
select hire_date from employees where hire_date in ('2004/02/17','2002/06/07');

select hire_date from employees where hire_date between '2002/06/17' and '2004/12/31';

-- job MAn 출력하시오.
select * from employees where substr(job_id,4) = 'MAN';
-- like 연산자 이용
-- MAN으로 끝나는 단어를 검색
SELECT * FROM employees where job_id like '%MAN';
-- ST로 시작하는 단어를 검색
SELECT * FROM EMPLOYEES WHERE JOB_ID LIKE 'ST%';
-- EMP NAME a가 들어가있는 이름 출력 (like 앞에 not을 붙여 반하는 결과 출력 가능)
select * from employees where emp_name like '%a%';

--2번째 자리에 t가 들어간 이름 찾기
select * from employees where emp_name like '_t%';
-- 4번째 자리에 v가 들어간 이름 찾기.
select * from employees where emp_name like '___v%';

--뒤에서 2번쨰 자리에 l 있ㅇ는 이름
select * from employees where emp_name like '%l_';

--첫번째 D가 들어간 이름
select * from employees where emp_name like'D%';

select * from employees where emp_name like '%A%';
select * from employees where emp_name like ':1';

SELECT * FROM employees;


