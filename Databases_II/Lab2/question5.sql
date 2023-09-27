select distinct stf.staff_name from sample.sh_staff stf 
join sample.sh_sale sal on stf.staff_no = sal.staff_no 
join sample.sh_stock stk on sal.stock_code = stk.stock_code 
where stk.stock_code = 'A11111'
except(
	select distinct stf.staff_name from sample.sh_staff stf 
	join sample.sh_sale sal on stf.staff_no = sal.staff_no 
	join sample.sh_stock stk on sal.stock_code = stk.stock_code 
	where stk.stock_code != 'A11111'
) ;
