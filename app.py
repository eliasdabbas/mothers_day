
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd

mothers = pd.read_csv('mothers.csv')

app = dash.Dash()
server = app.server 
app.title = 'Mothers Day Celebrations Around the World'

app.layout = html.Div([
    dcc.Graph(id='nothin_really',
              figure={
                  'data': [go.Scattergeo(lon=mothers[mothers['celebration_date']==c]['lon'],
                                         lat=mothers[mothers['celebration_date']==c]['lat'],
                                         hoverinfo='text',
                                         name=c,
                                         marker={'size': 20, 'line': {'color': '#000000', 'width': 0.2}},
                                         hovertext='<b>'+ mothers[mothers['celebration_date']==c]['country'] + '</b>' +'<br>'+ 
                                         mothers[mothers['celebration_date']==c]['celebration_date'])
                           for c in mothers['celebration_date'].unique()],
                  'layout': {'title': 'Mothers Day Celebrations Across the World',
                            'font': {'family': 'Palatino'},
                            'titlefont': {'size': 22},
                            'paper_bgcolor': '#eeeeee',
                            'plot_bgcolor': '#eeeeee',
                            'width': 1420,
                            'height': 650,
                            'annotations': [{'text': '<a href="https://www.twitter.com">@eliasdabbas</a>', 
                                             'x': .2, 'y': -.1, 'showarrow': False},
                                            {'text': '<a href="https://en.wikipedia.org/wiki/Mother\'s_Day">Wikipedia</a>',
                                             'x': .2, 'y': -.13, 'showarrow': False}],
                            'geo': {'showland': True, 'landcolor': '#eeeeee',
                                 'countrycolor': '#cccccc',
                                 'showsubunits': True,
                                 'subunitcolor': '#cccccc',
                                 'subunitwidth': 5,
                                 'showcountries': True,
                                 'oceancolor': '#eeeeee',
                                 'showocean': True,
                                 'showcoastlines': True, 
                                 'showframe': False,
                                 'coastlinecolor': '#cccccc',
                                              }}
              })
])


app.run_server()