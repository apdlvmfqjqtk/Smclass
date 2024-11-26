alter session set "_ORACLE_SCRIPT"=true;
create user ora_user identified by 1111;

drop ora_user;

grant connect, resource, dba to ora_user;

drop user ora_user cascade;