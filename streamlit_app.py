import streamlit
import snowflake.connector

# Connect to Snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# Run a Snowflake query and store results in a variable
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

streamlit.text("Hello from Snowflake:")
streamlit.text(my_catalog)
