create or replace function AddSubject (sub_nam varchar(50), sub_syl varchar(255))
returns integer as $$
declare sub_id integer;
begin insert into subject(sb_name, sb_syllabus) values (sub_nam, sub_syl)
returning sb_id into sub_id;
return sub_id;
end;

$$ language plpgsql;