
volume_path = "/Volumes/test_cata/new_schema/vol"

df = (
    spark.read
         .option("header", "true")
         .csv(f"{volume_path}/*.csv")
)

df.display()
