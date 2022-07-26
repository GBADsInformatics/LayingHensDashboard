# GBADs Dashboard Template Layouts 
# This file includes all the layout components seen in the dashboard pages. This template 
# includes many of the components that you might require.

# IMPORTS
# These are the imports required for building a dashboard with visualizations and user 
# authentication.
from logging import PlaceHolder, disable
from pydoc import classname
import dash
from dash import dcc,html,dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate 
import pandas as pd
import numpy as np
import json
import plotly.express as px
# from dash_extensions.enrich import FileSystemStore

#  IMAGES
# Example images set for the dashboard template, used for logos of the company/entity that is
# showcasing the data visualization. Add more by adding local files to \assets or by image URL.
GBADSLOGOB = "https://i0.wp.com/animalhealthmetrics.org/wp-content/uploads/2019/10/GBADs-LOGO-Black-sm.png"
GBADSLOGOW = "https://i0.wp.com/animalhealthmetrics.org/wp-content/uploads/2019/10/GBADs-LOGO-White-sm.png"

# TAB STYLING
# This is the styling that is applied to the selected tab.
selectedTabStyle = {
    'border': '3px solid white',
    'backgroundColor': 'white',
    'color': 'black'
}

# PAGE LAYOUT
# All the components for a page will be put here in this HTML div and will be used as the layout 
# for this dashboard template.
page_1 = html.Div([
    html.Div([
        html.Img(src=GBADSLOGOW, className="header-logo"),
        html.Div([html.H1('Laying Hens', className="header-title")], className="header-title-div"),
        # dbc.Button("Login", id="login-button", href=env.get("AUTH0_LOGIN"), style={'margin-top': '10px', 'margin-right':'10px', 'float': 'right'}),
        # dbc.Button("Logout", id="logout-button", href=env.get("AUTH0_LOGOUT"), style={'margin-top': '10px', 'margin-right':'10px', 'float': 'right', 'display':'none'}),
    ],className='header-section'),
    
    html.Div([
        html.Div([
            # This is the tabs component. It holds all the pages for the tabs. Add more tabs and change the 
            # tab contents here.
            dcc.Tabs(
                id='tabs',
                children=[
                dcc.Tab(
                    label='Graphs', 
                    className='cattabs',
                    selected_style=selectedTabStyle,
                    children=[
                        html.Div(
                            className='tab-section',
                            children=[
                                "Summary section"
                            ]
                        ),
                        html.Div(
                            className='tab-section-flex-container',
                            children=[
                                html.Div(
                                    className='tab-section data-options',
                                    children=[
                                        html.Div(
                                            id='options-container',
                                            children=[
                                                html.H4("Options",style={"text-align":"center"}),
                                                html.Hr(),
                                                html.H5("Graph Type",style={"margin":"0.4rem 0 0.2rem 0"}),
                                                dcc.Dropdown(
                                                    id='options-graph-type',
                                                    clearable=False,
                                                ),
                                                html.H5("Country",style={"margin":"0.4rem 0 0.2rem 0"}),
                                                dcc.Dropdown(
                                                    id='options-dropdown-1-a',
                                                    clearable=False,
                                                    multi=True,
                                                ),
                                                html.Div(
                                                    id='prodsys-container',
                                                    children=[
                                                        html.H5("Production System",style={"margin":"0.4rem 0 0.2rem 0"}),
                                                        dcc.Dropdown(
                                                            id='options-dropdown-2-a',
                                                            clearable=False,
                                                            multi=True,
                                                        ),
                                                    ],
                                                ),
                                                html.Div(
                                                    id='year-container',
                                                    children=[],
                                                ),
                                            ]
                                        ),

                                    ]
                                ),
                                html.Div(
                                    id='graph-section',
                                    className='tab-section data-section',
                                    children=[

                                    ]
                                ),

                            ]
                        ),
                    ],  
                ),
                dcc.Tab(
                    label='Data table', 
                    className='cattabs', 
                    selected_style=selectedTabStyle,
                    children=[
                        html.Div(
                            className='tab-section',
                            children=[
                                "Summary section"
                            ]
                        ),
                        html.Div(
                            className='tab-section-flex-container',
                            children=[
                                html.Div(
                                    className='tab-section data-options',
                                    children=[
                                        html.Div(
                                            id='options-container',
                                            children=[
                                                html.H4("Options",style={"text-align":"center"}),
                                                html.Hr(),
                                                html.H5("Country",style={"margin":"0.4rem 0 0.2rem 0"}),
                                                dcc.Dropdown(
                                                    id='options-dropdown-1-b',
                                                    clearable=False,
                                                    multi=True,
                                                ),
                                                html.H5("Production System",style={"margin":"0.4rem 0 0.2rem 0"}),
                                                dcc.Dropdown(
                                                    id='options-dropdown-2-b',
                                                    clearable=False,
                                                    multi=True,
                                                ),
                                                html.Div(
                                                    id='year-container-b',
                                                    children=[
                                                        html.H5("Year",style={"margin":"0.4rem 0 0.2rem 0"}),
                                                        html.Div(
                                                            className='year-slider-container',
                                                            children=[
                                                                dcc.RangeSlider(
                                                                    step=1, 
                                                                    marks=None,
                                                                    id='options-dropdown-3-b',
                                                                    className='year-slider',
                                                                    tooltip={"placement": "top", "always_visible": True},
                                                                    dots=True,
                                                                )
                                                            ]
                                                        ),
                                                    ],
                                                ),
                                            ]
                                        ),

                                    ]
                                ),
                                html.Div(
                                    id='data-table-section',
                                    className='tab-section data-section',
                                    children=[
                                        html.Div(
                                            id='data-table-container',
                                            className='data-table-container',
                                            children=[
                                                
                                            ]
                                        ),
                                    ]
                                ),

                            ]
                        ),
                    ],  
                ),
            ]),
        ], className="tab-panel"),
        html.Div(id='dummy_div',style={'display':'none'}),
    ],className='mid'),

    # Storing data in the session. Data gets deleted once tab is closed
    dcc.Store(id='stored-options', storage_type='memory', data=None),

], className="main-div")
