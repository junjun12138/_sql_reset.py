# import pandas as pd 
# import pymysql

# conn = pymysql.connect(
#     host='127.0.0.1',
#     user="root",
#     passwd="123123",
#     port=3306,
#     db="sakila",
#     # charset="utf-8"


# )

# df = pd.read_sql(""" 
#     select * 
#     from sakila.table_1""",con=conn)
# df.to_excel("marketing.xlsx",index=False)