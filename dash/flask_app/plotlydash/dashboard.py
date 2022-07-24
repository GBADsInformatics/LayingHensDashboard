import json
from logging import disable
from os.path import exists
import requests
import numpy as np
import pandas as pd
import math
import urllib.parse
import dash
from dash import dcc,html,dash_table,callback_context
import dash_bootstrap_components as dbc
import plotly.express as px
from datetime import date, datetime
from functools import wraps
from flask import session, redirect
import plotly.graph_objects as go
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from dash.exceptions import PreventUpdate
from layouts import *
from dash.dependencies import Input, Output, State
# from dash_extensions.enrich import Output, DashProxy, Input, MultiplexerTransform
import json
from textwrap import dedent

# Importing dataset
LH_df = pd.read_csv('datasets/laying_hens.csv')

# Getting dropdown options
LH_countries = sorted(LH_df['Country'].unique())
LH_years = sorted(LH_df['Year'].unique())
LH_prodsys = ['Not enriched cage','Enriched cage','Free range','Barn','Organic']


# Chloropleth map country data
# from urllib.request import urlopen
# plotly_countries = {}
# with open("datasets/world_map_110m.geojson") as file:
#     plotly_countries = json.load(file)

stylesheet = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css'
]

PROFILE_KEY = 'profile'
JWT_PAYLOAD = 'jwt_payload'

def init_dashboard(server):
            
    dash_app = dash.Dash(__name__,
        server=server,
        title='Laying Hens Dashboard',
        routes_pathname_prefix="/dash/",
        external_stylesheets=[
            # 'https://codepen.io/chriddyp/pen/bWLwgP.css',
            dbc.themes.BOOTSTRAP,
            dbc.icons.BOOTSTRAP
        ],
    )
    # Setting active page
    dash_app.layout = html.Div([
        dcc.Location(id='url', refresh=False)
    ],id='page-content')
    init_callbacks(dash_app)
    return dash_app.server

isLoggedIn = False
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        global isLoggedIn
        if PROFILE_KEY not in session:
            isLoggedIn = False
            return redirect('/login')
        isLoggedIn = True
        return f(*args, **kwargs)
    return decorated

def checkRole():
    isRole = False
    y = json.dumps(session[JWT_PAYLOAD])
    person_dict = json.loads(y)
    p = (person_dict["http://gbad.org/roles"]) # This link sends you to the Ground Based Air Defense website lmao
    stringver = json.dumps(p)
    print(stringver)
    if 'Verified User' in stringver:
        isRole = True
    else:
        isRole = False
    return isRole

def getJWT(personDict,userCat):
    p = (personDict[userCat])
    stringVer = json.dumps(p)
    s1 = stringVer.replace("[]","")
    strippedString = s1.strip('"')
    return strippedString

@requires_auth
def getUserContent():
    y = json.dumps(session[JWT_PAYLOAD])
    personDict = json.loads(y)
    userEmail = getJWT(personDict,"email")
    print(userEmail)
    return userEmail

##CALLBACKS -------------------------------------------------------------------------------------------------------------------------------------------------------------
def init_callbacks(dash_app):
    
    # Callbacks to handle login components
    @dash_app.callback(
        Output(component_id='login-button', component_property='style'),
        Input('url', 'pathname')
    )
    @requires_auth
    def login_button(pathname):
        checkRole()
        return {'margin-left': '5px', 'display': 'none'}
    
    @dash_app.callback(
        Output(component_id='logout-button', component_property='style'),
        Input('url', 'pathname')
    )
    @requires_auth
    def logout_button(pathname):
        return {'margin-top': '10px', 'margin-right':'10px', 'float': 'right'}

    # Callback to handle feedback.
    @dash_app.callback(
        Output('feedback-text', 'value'),
        Output('feedback-button', 'disabled'),
        Output('feedback-text', 'disabled'),
        Input("feedback-button", "n_clicks"),
        State('feedback-text', 'value')
    )
    def feedback_box(n, text):
        if (n > 0 and text != None and text != ""):
            outF = open("feedback.txt", "a")
            outF.writelines('["'+text+'"]\n')
            outF.close()
            return\
                "Thank you for your feedback",\
                True,\
                True
        else:
            print("no")
    
    # Callback to handle changing the page based on the pathname provided.
    @dash_app.callback(
        Output('page-content', 'children'),
        Input('url', 'pathname')
    )
    def display_page(pathname):
        if pathname == '/dash/':
            layout = page_1
        else:
            layout = "404"
        return layout


    ##################################
    # Laying Hens Specific Callbacks #
    ##################################

    # Update stored options
    @dash_app.callback(
        Output('stored-options', 'data'),
        [State('tabs', 'value')],
        Input('options-dropdown-1-a', 'value'),
        Input('options-dropdown-1-b', 'value'),
        Input('options-dropdown-2-a', 'value'),
        Input('options-dropdown-2-b', 'value'),
        Input('options-dropdown-3-a', 'value'),
        Input('options-dropdown-3-b', 'value'),
    )
    def update_stored_options_a(tab, drop1a, drop1b, drop2a, drop2b, drop3a, drop3b):
        if tab == 'tab-2':
            return {'options-dropdown-1':drop1b,'options-dropdown-2':drop2b,'options-dropdown-3':drop3b}
        else:
            return {'options-dropdown-1':drop1a,'options-dropdown-2':drop2a,'options-dropdown-3':drop3a}


    # Update options values on changing tab
    @dash_app.callback(
        Output('options-dropdown-1-a', 'value'),
        Output('options-dropdown-1-b', 'value'),
        Output('options-dropdown-2-a', 'value'),
        Output('options-dropdown-2-b', 'value'),
        Output('options-dropdown-3-a', 'value'),
        Output('options-dropdown-3-b', 'value'),
        [Input('tabs', 'value')],
        State('stored-options', 'data'),
    )
    def options_on_tab_change(selected_tab,stored_options):
        if stored_options is None:
            return None, None, None, None, None, None
        return stored_options['options-dropdown-1'],stored_options['options-dropdown-1'],\
            stored_options['options-dropdown-2'],stored_options['options-dropdown-2'],\
            stored_options['options-dropdown-3'],stored_options['options-dropdown-3']
    # Update available options in dropdowns
    @dash_app.callback(
        Output('options-dropdown-1-a', 'options'),
        Output('options-dropdown-1-b', 'options'),
        Output('options-dropdown-2-a', 'options'),
        Output('options-dropdown-2-b', 'options'),
        Output('options-dropdown-3-a', 'options'),
        Output('options-dropdown-3-b', 'options'),
        Input('dummy_div', 'children'),
    )
    def dropdown_options(_a):
        return LH_countries,LH_countries,\
            LH_prodsys,LH_prodsys,\
            LH_years,LH_years