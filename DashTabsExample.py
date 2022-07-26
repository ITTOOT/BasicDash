# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 13:32:30 2022

@author: player_1

Title: Dash Tabs Example

Open terminal to run by typing in the command> python nameOfFile.py

Running on Dash default URL: http://127.0.0.1:8050/
"""

# Load Packages
import pandas as pd
import plotly.express as px

# Dash
# With html, Dash Core Components and Input & Output for callback functions
from dash import Dash, html, dcc, Input, Output

# Graph objects as "go"
import plotly.graph_objs as go

# Dash object
app = Dash(__name__)

# CSS file
tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}


# Prepare data
# Dataset - Save in same directory as the script to avoid using PATH
df = pd.read_csv('datasets/avocado-updated-2020.csv')

# Check data
df.info()
# print(df['type'].value_counts(dropna=False))
# print(df['geography'].value_counts(dropna=False))

# Plot
# Filter data frame
# msk = df['geography'] == 'Los Angeles'
# Chart
# px.line(df[msk], x='date', y='average_price', color='type')

# Dashboard components
# options: the options the geograpgy has, value: staring option
geo_dropdown = dcc.Dropdown(options=df['geography'].unique(),
                            value='New York')

# Dashboard
app.layout = html.Div(children=[
    # Dash Components as 'children'
    html.H1(children='Avocado Prices Dashboard'),
    # Tab Panel
    dcc.Tabs(id="tabsMenuBar", value='tab-1', children=[
        dcc.Tab(label='Tab 1', value='tab-1', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Tab 2', value='tab-2', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Tab 3', value='tab-3', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Tab 4', value='tab-4', style=tab_style, selected_style=tab_selected_style),
    ], style=tabs_styles),
    html.Div(id='tabsMenuBarContent'),
    # Content
    ])

# Interactivity
# Callback functions - @ binder
#
# Update graph
@app.callback(# Output/Input properties of the Dash components    
    Output(component_id='price-graph', component_property='figure'),
    Input(component_id=geo_dropdown, component_property='value')
    )
# Callback definitions
def update_graph(selected_geography):
    # Filter inputs
    filtered_df = df[df['geography'] == selected_geography]
    # Plot
    line_fig = px.line(filtered_df,
                       x='date',
                       y='average_price',
                       color='type',
                       title=f'Avocado Prices in {selected_geography}')
    # Return
    return line_fig
# 
# Render tab bar
@app.callback(# Output/Input properties of the Dash components
    Output(component_id='tabsMenuBarContent', component_property='children'),
    Input(component_id='tabsMenuBar', component_property='value'))
# Callback definitions
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1'),
            # Dropdown
            geo_dropdown,
            # Chart
            html.Div([
                dcc.Graph(id='price-graph')
            ])
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2'),
            # Dropdown
            geo_dropdown,
            # Chart
            html.Div([
                dcc.Graph(id='price-graph')
            ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
            # Chart
            html.Div([
                dcc.Graph(id='price-graph'),
                dcc.Graph(id='price-graph'),
            ], style={'display': 'inline-block', 'width': '49%'}),
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Tab content 3')
        ])
    elif tab == 'tab-4':
        return html.Div([
            html.H3('Tab content 4')
        ])
    
    
    
    

# Run app on local server @ http://127.0.0.1:8050/
if __name__ == "__main__":
    app.run_server(debug=False)
