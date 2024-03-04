from pyspark.sql import SparkSession


def get_spark_session(master: str) -> SparkSession:
    spark: SparkSession = SparkSession.builder.master(master).getOrCreate()
    return spark
