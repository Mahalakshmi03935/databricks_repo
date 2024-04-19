# Databricks notebook source
def test_read_silver_data():
    spark = SparkSession.builder.appName("unit_test_employee_silver_to_gold").getOrCreate()

    
    employee_silver_df = spark.read.format("delta").load("/silver/Employee_info/dim_employee")

    assert employee_silver_df.count() > 0

    spark.stop()

