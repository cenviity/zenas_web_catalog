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
# print(color_list)

# Add a pick list for picking the color
option = streamlit.selectbox(
    'Pick a sweatsuit color or style:',
    list(color_list)
    )

# Add image caption
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'

# Use the option selected to retrieve all the info from the database
my_cur.execute(
    "select direct_url, price, size_list, upsell_product_desc \
        from catalog_for_website \
        where color_or_style = '" + option + "';"
    )
df2 = my_cur.fetchone()

streamlit.image(
    df2[0],
    width = 400,
    caption = product_caption
)

streamlit.write('Price: ', df2[1])
streamlit.write('Sizes Available: ', df2[2])
streamlit.write(df2[3])
