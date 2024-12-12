from snowutils import SnowflakeConnector

# Snowflake connection details
account = "VUQXEMB-UB05841"
user = "ANKUSHPATIL"  # Ensure no leading/trailing whitespace
password = "Ankush@1234"
database = "SNOWFLAKE_SAMPLE_DATA"
schema = "TPCH_SF1"
role = "ACCOUNTADMIN"
warehouse = "COMPUTE_WH"

# Initialize and connect
sf_connector = SnowflakeConnector(
    account=account,
    user=user,
    password=password,
    database=database,
    schema=schema,
    role=role,
    warehouse=warehouse
)

sf_connector.connect()

# Execute a query
query = "SELECT * FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.SUPPLIER LIMIT 10"
result = sf_connector.execute_query(query)

# Print the result
for row in result:
    print(row)

# Close the connection
sf_connector.close_connection()
