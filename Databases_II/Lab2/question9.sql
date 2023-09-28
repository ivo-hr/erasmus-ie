set lc_monetary to "en_IE.utf8";
select cast(price as money) "Cost" from sample.sh_stock;

select sample.sh_stock.stock_name, sample.sh_category.catdescription, sample.sh_stock.price,
lag(sample.sh_stock.price, 1) over (partition by sample.sh_stock.catcode order by price) "Next Price",
price - lead (sample.sh_stock.price, 1) over (partition by sample.sh_stock.catcode order by sample.sh_stock.price) 
"Price difference"

from sample.sh_stock join sample.sh_category on sample.sh_stock.catcode = sample.sh_category.catcode;