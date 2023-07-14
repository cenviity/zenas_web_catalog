import streamlit
import snowflake.connector
import pandas

streamlit.title('Zena\'s Amazing Athleisure Catalog')

# Connect to Snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# Run a Snowflake query and store results in a variable
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

# Put the data into a dataframe
df = pandas.DataFrame(my_catalog)

# Temporarily write the dataframe to the page
# streamlit.write(df)

# Put the first column into a list
color_list = df[0].values.tolist()
print(color_list)
