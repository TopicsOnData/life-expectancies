import plotly.graph_objects as go
import pandas as pd
from pandas import Series, DataFrame

df = pd.read_csv('life-expectancy.csv')

# Data preparation: Smallest and largest life expectancies (rates)

# Top 5 in 2018
l18 = df.query('YEAR==2018')
l18_s = l18.nsmallest(5, 'RATE')
l18_l = l18.nlargest(5, 'RATE')

# Top 5 in 2019
l19 = df.query('YEAR==2019')
l19_s = l19.nsmallest(5, 'RATE')
l19_l = l19.nlargest(5, 'RATE')

# Top 5 in 2020
l20 = df.query('YEAR==2020')
l20_s = l20.nsmallest(5, 'RATE')
l20_l = l20.nlargest(5, 'RATE')

# Draw the figure
fig = go.Figure()

# Add the traces

# Worst Life Expectancies in 2018
fig.add_trace(go.Scatter(
    x=l18_s['RATE'], 
    y=l18_s['STATE'],
    mode='markers',
    name='Worst Life Expectancies in 2018',
    text=l18_s['STATE']
    )
)

# Best Life Expectancies in 2018
fig.add_trace(go.Scatter(
    x=l18_l['RATE'], 
    y=l18_l['STATE'],
    mode='markers',
    name='Best Life Expectancies in 2018',
    text=l18_l['STATE']
    )
)

# Worst Life Expectancies in 2019
fig.add_trace(go.Scatter(
    x=l19_s['RATE'], 
    y=l19_s['STATE'],
    mode='markers',
    name='Worst Life Expectancies in 2019',
    text=l19_s['STATE']
    )
)

# Best Life Expectancies in 2019
fig.add_trace(go.Scatter(
    x=l19_l['RATE'], 
    y=l19_l['STATE'],
    mode='markers',
    name='Best Life Expectancies in 2019',
    text=l19_l['STATE']
    )
)

# Worst Life Expectancies in 2020
fig.add_trace(go.Scatter(
    x=l20_s['RATE'], 
    y=l20_s['STATE'],
    mode='markers',
    name='Worst Life Expectancies in 2020',
    text=l20_s['STATE']
    )
)

# Best Life Expectancies in 2020
fig.add_trace(go.Scatter(
    x=l20_l['RATE'], 
    y=l20_l['STATE'],
    mode='markers',
    name='Best Life Expectancies in 2020',
    text=l20_l['STATE']
    )
)

# Customize axis view
fig.update_xaxes(showgrid=False)
fig.update_yaxes(
    showgrid=False,
    zeroline=True
    )

fig.show()
