import pandas as pd
import numpy as np
import plotly
import plotly.graph_objects as go
import plotly.express as px

df_ = pd.read_csv('../files/uscities.csv')

fig = px.scatter_mapbox(df_.head(400), lat="lat", lon="lng", hover_name="city", hover_data=["city", 'population'],
                        color_discrete_sequence=["darkmagenta"], zoom=5.5, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

plotly.offline.plot(fig, filename='us_cities_population_map.png')
