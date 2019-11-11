from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime
import requests


def get_data():
    url = 'https://api.unibit.ai/api/realtimestock/AAPL?size=10&AccessKey=demo'
    res = requests.get(url)
    res = res.json()['Stock price']
    return res


def get_simple_candlestick():
    data = get_data()
    x, y, z, w, k = [], [], [], [], []

    for item in data:
        x.append(item['date']),
        y.append(item['open']),
        z.append(item['high']),
        w.append(item['low']),
        k.append(item['close'])

    trace1 = go.Candlestick(
        x=x,
        open=y,
        high=z,
        low=w,
        close=k
    )
    layout = go.Layout(
        # autosize=True,
        # width = 800,
        # height=900,
        xaxis=dict(
            autorange=True
        ),
        yaxis=dict(
            autorange=True
        )
    )
    plot_data = [trace1]
    figure = go.Figure(data=plot_data, layout=layout)
    plot_div = plot(figure, output_type='div', include_plotlyjs=False)
    return plot_div


def get_topographical_3D_surface_plot():
    raw_data = pd.read_csv(
        'https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

    data = [go.Surface(z=raw_data.as_matrix())]

    layout = go.Layout(

        autosize=False,
        width=800,
        height=700,
        margin=dict(
            l=65,
            r=50,
            b=65,
            t=90
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div', filename='elevations-3d-surface')

    return plot_div
