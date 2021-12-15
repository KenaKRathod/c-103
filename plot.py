import pandas as pd

import plotly.express as px

df = pd.read_csv("103-main/line_chart.csv")

fig = px.scatter(df, x="Year", y="Per capita income", color="Country", title='Per Capita Income')

fig.show()

