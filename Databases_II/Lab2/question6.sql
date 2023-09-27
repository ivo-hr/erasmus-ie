select stf.staff_name from sample.sh_staff stf
where not exists(
	select * from sample.sh_stock stk
	where not exists (
		select * from sample.sh_sale sal where
		sal.staff_no  = stf.staff_no and 
		stk.stock_code = sal.stock_code 
	)
);