from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date,to_timestamp

spark = SparkSession.builder.getOrCreate()

df = spark.table("test_cata.new_schema.sales_bronze")

df_clean =df.withColumn("SALES", col("SALES").cast("double"))\
      .withColumn("QUANTITYORDERED", col("QUANTITYORDERED").cast("int"))\
      .withColumn("PRICEEACH", col("PRICEEACH").cast("double"))\
      .withColumn("ORDERDATE", to_date(to_timestamp(col("ORDERDATE"), "M/d/yyyy H:mm"))
)

df_clean.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("test_cata.new_schema.sales_silver")
