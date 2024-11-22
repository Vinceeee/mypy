def test_spark_one():
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col

    # 创建 Spark 会话
    spark = SparkSession.builder.appName("Simple PySpark Example").master("local[*]").getOrCreate()
    # 定义数据字典
    data = [
        {"name": "Alice", "age": 34, "city": "New York"},
        {"name": "Bob", "age": 45, "city": "Los Angeles"},
        {"name": "Charlie", "age": 23, "city": "Chicago"},
    ]

    # 从字典创建 DataFrame
    df = spark.createDataFrame(data)

    # 过滤年龄大于 30 的记录
    filtered_df = df.filter(col("age") > 30)
    # 显示过滤后的数据
    filtered_df.show()
    # 停止 Spark 会话
    spark.stop()
