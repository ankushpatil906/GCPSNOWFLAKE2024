from snowutils import SnowflakeConnector

# Snowflake connection details
account = "xxxxxxxxxxx"
user = "xxxxx"  # Ensure no leading/trailing whitespace
password = "xxxxxxxx"
database = "xxxxxxxxxxx"
schema = "xxxxxxxxx"
role = "xxxxxxxxxxxxx"
warehouse = "xxxxxxxxxxx"

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
