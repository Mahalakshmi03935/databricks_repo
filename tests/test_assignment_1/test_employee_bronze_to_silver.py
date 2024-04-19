# Databricks notebook source
def test_read_bronze_data():
    spark = SparkSession.builder.appName("unit_test_employee_bronze_to_silver").getOrCreate()

    # Test reading data from bronze layer
    employee_bronze_df = spark.read.format("delta").load("/source_to_bronze/dim_employee")

    assert employee_bronze_df.count() > 0

    spark.stop()
