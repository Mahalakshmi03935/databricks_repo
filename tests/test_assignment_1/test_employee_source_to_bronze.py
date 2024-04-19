# Databricks notebook source
def test_read_csv_files():
    spark = SparkSession.builder \
        .appName("unit_test_employee_source_to_bronze") \
        .getOrCreate()

    # Test reading CSV files
    employee_df = spark.read.csv("/source_to_bronze/employee.csv", header=True)
    department_df = spark.read.csv("/source_to_bronze/department.csv", header=True)
    country_df = spark.read.csv("/source_to_bronze/country.csv", header=True)

    assert employee_df.count() > 0
    assert department_df.count() > 0
    assert country_df.count() > 0

    spark.stop()


