# databricks_repo

**Question 1:**

1.Created three folders:

source_to_bronze, bronze_to_silver, silver_to_gold.

2.Developed four notebooks:

2 notebooks in source_to_bronze: utils (common functions), employee_source_to_bronze (driver).

1 notebook in bronze_to_silver: employee_bronze_to_silver.

1 notebook in silver_to_gold: employee_silver_to_gold.

3.In employee_source_to_bronze:

Read CSV files (Employee, Department, Country).

Applied common functions from utils notebook.

Stored processed data in DBFS (/source_to_bronze/file_name.csv).

4.In employee_bronze_to_silver:

Transformed data (Camel case to snake case).
Added load_date.
Stored as a delta table (/silver/Employee_info/dim_employee).

5.In employee_silver_to_gold:

Conducted various analytics on the data.
Stored analytics results in /gold/employee/fact_employee.

**Question 2:**

1.Fetched data from API (https://reqres.in/api/users?page=2) iteratively until no more data is available.

2.Dropped unnecessary columns and support block.

3.Read data with a custom schema and flattened the dataframe.

4.Derived a new column "site_address" from the email address (reqres.in).

5.Added load_date with the current date.

6.Stored the dataframe in DBFS (/site_info/person_info) as a delta table with overwrite mode.