# -*-coding:utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Boostrap CSS and font awesome . Option 1) Run from codepen directly Option 2) Copy css file to assets folder and run locally
external_stylesheets = ['https://codepen.io/unicorndy/pen/GRJXrvP.css',
                        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = '新北市政府衛生局食安智慧監控中心指標儀表板'

# for heroku to run correctly
server = app.server

# Overwrite your CSS setting by including style locally
colors = {
    'background': '#2D2D2D',
    'text': '#E1E2E5',
    'figure_text': '#ffffff',
    'confirmed_text': '#3CA4FF',
    'deaths_text': '#f44336',
    'recovered_text': '#5A9E6F',
    'highest_case_bg': '#393939',
}

# Creating custom style for local use
divBorderStyle = {
    'backgroundColor': '#393939',
    'borderRadius': '12px',
    'lineHeight': 0.9,
}

# Creating custom style for local use
boxBorderStyle = {
    'borderColor': '#393939',
    'borderStyle': 'solid',
    'borderRadius': '10px',
    'borderWidth': 2,
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="stack")
fig2 = px.line(df, x="Fruit", y="Amount", color="City")
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div([
    html.Div([
        html.H4('Department of Health, New Taipei City Government',
                style={'textAlign': 'center'}),
        html.H4('IFSMC - Dashboard of Intelligent Index',
                style={'textAlign': 'center'})
    ], className='row'),
    html.Div([  # modal div
        html.Div([  # content div

            dcc.Markdown('''
                            Data Sources:
                            * World Health Organization (WHO): https://www.who.int/
                            * DXY.cn. Pneumonia. 2020. http://3g.dxy.cn/newh5/view/pneumonia.
                            * BNO News: https://bnonews.com/index.php/2020/02/the-latest-coronavirus-cases/
                            '''),
            html.Hr(),
            html.Button('Close', id='modal-close-button',
                        style={
                            'color': 'red',
                        })
        ],
            style={
                'fontSize': 10,
                'lineHeight': 0.9,
            },
            className='modal-content',
        ),
    ],
        id='modal',
        className='modal',
        style={"display": "none"},
    ),
    html.Div([
        html.Div([
            html.H4('柱狀範例圖',
                    style={
                        'textAlign': 'center',
                        'color': colors['text']
                    },
                    className="row"
                    ),
            html.Div('Dash: A web application framework for Python.', style={
                'textAlign': 'center',
                'color': colors['text']
            }),
            dcc.Graph(
                id='example-graph1',
                figure=fig
            )],
            className="six columns"
        ),
        html.Div([
            html.H4('折線圖範例圖',
                    style={
                        'textAlign': 'center',
                        'color': colors['text']
                    }, className="row"),
            html.Div('Dash: A web application framework for Python.', style={
                'textAlign': 'center',
                'color': colors['text']
            }),
            dcc.Graph(
                id='example-graph',
                figure=fig2
            )], className="six columns")
    ],
        className='ten columns offset-by-one',
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
