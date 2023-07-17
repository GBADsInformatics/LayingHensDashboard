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
    'borderTop': '1px white',
    'borderBottom': '1px white',
    'borderLeft': '1px white',
    'borderRight': '1px white',
    'background-color': '#f6f6f6d1',
    'box-shadow': '1px 1px 0px white',
    'color': 'orange',
    'fontWeight': 'bold'
}

# PAGE LAYOUT
# All the components for a page will be put here in this HTML div and will be used as the layout 
# for this dashboard template.
page_1 = html.Div([
    html.Div([
        html.Img(src=GBADSLOGOB, className="header-logo"),
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
                                html.P('This section highlights the percentage of laying hens kept for egg production by production system.',style={'margin-bottom':'0'})
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
                                                html.Div(
                                                    id='alert-container',
                                                    children=[],
                                                    style={'margin-top':'1rem'}
                                                ),
                                            ]
                                        ),

                                    ]
                                ),
                                html.Div(
                                    id='graph-section',
                                    className='tab-section data-section',
                                    children=[
                                        dcc.Loading(
                                            id='graph-container',
                                            type='cube',
                                            parent_className='graph-container',
                                            children=[html.P('Please select appropriate dropdown options.')]
                                        ),
                                    ]
                                ),

                            ]
                        ),
                    ],  
                ),
                dcc.Tab(
                    label='Data Table', 
                    className='cattabs', 
                    selected_style=selectedTabStyle,
                    children=[
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
                dcc.Tab(
                    label='Metadata', 
                    className='cattabs', 
                    selected_style=selectedTabStyle,
                    children=[
                        html.Div([
                            html.P(
                                'GBADs Informatics metadata provides information about data presented in the \'Graphs\' and \'Data Table\' tabs. Metadata is provided for data that is used as inputs to the model used to produce data outputs. Metadata is provided for output data including provenance information and methodology for the model.',
                                style={'color':'#000','margin':'0'}
                            )
                        ],className='tab-section'),
                        html.Div(
                            className='meta-section-wrapper',
                            children=[
                                html.Div(
                                    className='tab-section-flex-container meta-section',
                                    children=[
                                        html.Div(
                                            className='meta-section-left tab-section',
                                            id='meta-left',
                                            children=[
                                                html.H5(children="Data Source",style={"text-align":"center"}), 
                                                html.Div(
                                                    className='meta-gbads-source',
                                                    id='gbads-source',
                                                    children=[
                                                        dcc.Dropdown(
                                                            className="meta-source-button meta-source-dropdown",
                                                            id="meta-source-dropdown",
                                                            value='LAYING HENS',
                                                            options=['LAYING HENS'],
                                                            clearable=False,
                                                            style={"color": "black"},
                                                        ),
                                                        html.P(
                                                            'GBADs Metadata',
                                                            className='meta-source-button meta-gbads-button',
                                                            id='meta-gbads-button'
                                                        ),
                                                        html.P(
                                                            'Provenance',
                                                            className='meta-source-button provenance-button',
                                                            id='provenance-button',
                                                        ),
                                                    ]
                                                ),
                                                html.Div(
                                                    className='meta-source-button',
                                                    id='glossary-button',
                                                    children=[
                                                        'Metadata Glossary'
                                                    ]
                                                ),
                                            ]
                                        ),
                                        html.Div([
                                            html.Div(
                                                children=[
                                                    html.H5(children='Metadata',style={"text-align":"center",'height':'2rem'}), 
                                                    html.Div(
                                                        children=[],
                                                        id='download-container',
                                                        className='download-container',
                                                    ),
                                                ],
                                                style={'position':'relative'}
                                            ),
                                            html.Div(
                                                dcc.Loading(
                                                    # parent_className='loading-wrapper',
                                                    id='metadata-container',
                                                    type='cube',
                                                    children=[
                                                        'Metadata shows here'
                                                    ],
                                                ),
                                                className='meta-data-container',
                                            ),
                                        ],className='meta-section-right tab-section'),
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
    dcc.Store(id='meta-type', storage_type='memory', data='meta'),

], className="main-div")
