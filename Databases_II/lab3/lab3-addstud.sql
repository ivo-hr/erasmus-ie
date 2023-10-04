create or replace function AddStudent(stu_nam varchar (50))
returns integer as $$
declare stu_id integer;
begin insert into student(st_name) values (stu_nam) 
returning st_id into stu_id;
return stu_id;
end;

$$ language plpgsql;

