
import dash
from dash import html, dcc, Input, Output


app = dash.Dash(__name__)

#
# Create app with several pages
# But, filters should be applied on all charts from all pages
#
# There should be switch buttons for choosing between layouts
# Filters should be present on each page i.e. always present on page
#
# Problem:  Some of inputs should be present in callbacks, but not on page at the time.
#           How to approach this?
#

app.layout = html.Div([

    # Purpose of this element is to be placeholder for URL bar
    # It isn't rendered on the page
    dcc.Location(id='url', refresh=False),

    dcc.Link('Homepage', href='/'),

    html.Br(),

    dcc.Link('Page 1', href='/page_1'),

    html.Br(),

    dcc.Link('Page 2', href='/page_2'),

    html.Br(),
    html.Br(),

    html.Div(id='page-content')


])


@app.callback(Output(component_id='page-content', component_property='children'),
              Input(component_id='url', component_property='pathname'))
def display_page(input_pathname):

    if input_pathname == '/':
        print('Home page')
        return 'Home page'
    elif input_pathname == '/page_1':
        print('Page 1')
        return 'Page 1'
    elif input_pathname == '/page_2':
        print('Page 2')
        return 'Page 2'


if __name__ == '__main__':
    app.run_server()



