from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

def csv_reader(file_path):
    df = (
        spark.read
            .option("header", True)
            .option("inferSchema", True)
            .csv(file_path)
    )

    df.write.format("delta") \
        .mode("overwrite") \
        .saveAsTable("test_cata.new_schema.sales_bronze")

def parquet_reader(file_path):
    df = spark.read.parquet(file_path)

    df.write.format("delta") \
        .mode("append") \
        .saveAsTable("test_cata.new_schema.sales_parquet_bronze")

def json_reader(file_path):
    df = (
        spark.read
            .option("mode", "PERMISSIVE")
            .json(file_path)
    )

    df.write.format("delta") \
        .mode("append") \
        .saveAsTable("test_cata.new_schema.sales_json_bronze")
