from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

file_path = "/Volumes/test_cata/new_schema/vol/sales_data_sample.csv"

df = (
    spark.read
         .option("header", True)
         .option("inferSchema", True)
         .csv(file_path)
)

df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("test_cata.new_schema.sales_bronze")
