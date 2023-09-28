select stf.staff_name from sample.sh_staff stf 
left join sample.sh_sale sal on stf.staff_no = sal.staff_no 
where sal.staff_no is null;