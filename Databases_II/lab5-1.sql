--a
create or replace procedure add_sale(
	p_stock_code varchar,
	p_staff_no int,
	p_quantity  int
) as $$
--b
	declare v_quantitystock int;
	declare v_num_staff int;

begin
--c
	select count(*) into v_num_staff
	from sh_staff
	where staff_no = p_staff_no;
--d
	if v_num_staff = 0 then 
	raise info 'Error: no such staff member'; end if;
--e
	select quantityinstock into v_quantitystock
	from sh_stock
	where stock_code = p_stock_code;
--f
	if v_quantitystock < p_quantity then
	raise info 'Error: not enough stock'; end if;
--g
	insert into sh_sale(stock_code, staff_no, quantity, saledate)
	values (p_stock_code, p_staff_no, p_quantity, now());
--h
	update sh_stock 
	set quantityinstock = quantityinstock - p_quantity
	where stock_code = p_stock_code;
--i
exception when others then
	raise info 'Error description: %', sqlerrm;
	raise info 'Error code: %', sqlstate;
end

$$ language plpgsql;

CALL add_sale('A11113', 5, 10)

	
	
