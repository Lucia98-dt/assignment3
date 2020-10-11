'''
select_sql='''select id, dm_product.re_id, dm_product.region, district, constr_product, gross_product, quarter, year
from dm_product
join dm_district
ON dm_product.re_id = dm_district.re_id'''
cur.execute(select_sql)
data3=cur.fetchall()
print(data3)
cur.close()
'''



‘’‘select_sql='''select SUM(cons_product) AS total_2 WHERE quarter=2 AND year=2020  from dm_product'''
cur.execute(select_sql)
data3=cur.fetchall()
print(data3)
cur.close()’‘’