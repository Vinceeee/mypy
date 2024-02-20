from loguru import logger
from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import rand, udf
from pyspark.sql.types import StringType

from utils import get_spark_session



def gennerate_parquet(filename: str, length: int = 100000):
    """
    生成一个样例parquet
    """
    from faker import Faker
    _faker = Faker()

    @udf(StringType())
    def _udf():
        return _faker.name()

    # spark: SparkSession = SparkSession.builder.master(
    #     "spark://localhost:17077"
    # ).getOrCreate()
    spark = get_spark_session("local[*]")
    # 生成顺序列
    df = spark.createDataFrame(
        Row(
            row_id=i,
        )
        for i in range(length)
    )
    # 添加列
    df = df.withColumn("b", rand() * 10)
    # 通过udf添加列
    df = df.withColumn("c", _udf())
    df.show(10)
    df.write.parquet(filename, mode="overwrite")
    spark.stop()
    logger.info(f"write to {filename}")


if __name__ == "__main__":
    gennerate_parquet("/tmp/sample.parquet", length=100)
