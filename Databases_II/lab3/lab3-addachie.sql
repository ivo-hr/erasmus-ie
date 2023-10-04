create or replace function AddAcheivement (stu_nam varchar(50), sub_nam varchar(50))
returns void as $$
begin insert into acheivement(sb_id, st_id) select sub.sb_id, stu.st_id
from student stu join subject sub 
on stu.st_name = stu_nam and sub.sb_name = sub_nam;
end;

$$ language plpgsql;