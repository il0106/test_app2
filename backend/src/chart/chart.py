import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

def candle_chart(df, title, html=False):

    df['begin'] = pd.to_datetime(df['begin'])

    fig = go.Figure(data=[go.Candlestick(
        x=df['begin'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close']
    )])

    fig.update_layout(
        title=title,
        xaxis_title='Время',
        yaxis_title='Цена',
        xaxis_rangeslider_visible=False
    )

    if html:
        return pio.to_html(fig, full_html=False)
    else:
        fig.show()