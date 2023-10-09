# Import the necessary libraries
# Read the following dataset into a pandas dataframe: 'tourist_arrivals_countries.csv' and parse the Date field as a date
# Remove missing rows from the data
# Extract the year from the Date field and create a new column called Year
# Group the data by Year and calculate the average number of tourist arrivals for each year
# Select only the rows where the year is 1994 or 2018
# Select only the following columns: Year, PT and DE
# Create a new dataframe df_pi with three columns Year, Country, and Percentage Increase
# Add a new row to df_pi with the following values: 1994, PT, 0.0
# Add a new row to df_pi with the following values: 1994, DE, 0.0
# For columns PT and DE in the original dataframe df, calculate the percentge increase of the second row respect to first row and store the result as two new columns in df_pi. For the column year, add 2018
# Use the Altair library to plot two lines in the same chart showing the PT and DE columns versus the Year column of df_pi. Use the color channel to discriminate for the Country column. Encode the x channel as ordinal. Set chart width to 400
# Create a new chart with the following text: 'Thanks to the introduction of low-cost flights, \nPortugal has experienced an increase in tourist arrivals \nof over 200% in 25 years, \neven surpassing the increase in Germany, \none of the favorite destinations for tourists ever.' Use the \n as a line break to format the text. Set the font size to 14. 
# Place the two graphs side by side. Set title to 'Yes, you can build a new swimming pool!'
# Save the chart as an HTML. Name the file output.html
import pandas as pd
import altair as alt

df = pd.read_csv('tourist_arrivals_countries.csv', parse_dates=['Date'])
df = df.dropna()
df['Year'] = df['Date'].dt.year
df = df.groupby('Year').mean()
df = df.loc[[1994, 2018], ['PT', 'DE']]
df_pi = pd.DataFrame(columns=['Year', 'Country', 'Percentage Increase'])
df_pi.loc[0] = [1994, 'PT', 0.0]
df_pi.loc[1] = [1994, 'DE', 0.0]
df_pi.loc[2] = [2018, 'PT', (df.loc[2018, 'PT'] - df.loc[1994, 'PT']) / df.loc[1994, 'PT']]
df_pi.loc[3] = [2018, 'DE', (df.loc[2018, 'DE'] - df.loc[1994, 'DE']) / df.loc[1994, 'DE']]
chart1=alt.Chart(df_pi).mark_line().encode(
    x=alt.X('Year:O'),
    y=alt.Y('Percentage Increase:Q'),
    color='Country:N'
).properties(
    width=400
)
chart2=alt.Chart(pd.DataFrame({'text': ['Thanks to the introduction of low-cost flights, \nPortugal has experienced an increase in tourist arrivals \nof over 200% in 25 years, \neven surpassing the increase in Germany, \none of the favorite destinations for tourists ever.']})).mark_text(
    ).encode(text='text'
).properties(
    width=400
) 
chart3 = alt.hconcat(chart1, chart2).properties(title='Yes, you can build a new swimming pool!')
chart3.save('output.html')
