from pyspark.sql import SparkSession
from pyspark.sql.functions import sum
 
spark = SparkSession.builder.getOrCreate()
 
df = spark.table("test_cata.new_schema.sales_silver")
 
df_gold = (
    df.groupBy("PRODUCTLINE")
      .agg(sum("SALES").alias("TOTAL_SALES"))
)
 
df_gold.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("test_cata.new_schema.sales_gold")