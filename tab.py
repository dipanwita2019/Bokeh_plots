from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.models.widgets import Tabs, Panel

# Import the data
from read_nba_data import standings

# Output to static HTML file
output_file('east_west_top_2_tabbed_layout.html',
            title='Conference Top 2 Teams Wins Race')

# Create a ColumnDataSource
standings_cds = ColumnDataSource(standings)

# Create view for each team
celtics_view = CDSView(source=standings_cds,
                       filters=[GroupFilter(column_name='teamAbbr', group='BOS')])
raptors_view = CDSView(source=standings_cds,
                        filters=[GroupFilter(column_name='teamAbbr', group='TOR')])
rockets_view = CDSView(source=standings_cds,
                        filters=[GroupFilter(column_name='teamAbbr', group='HOU')])
warriors_view = CDSView(source=standings_cds,
                        filters=[GroupFilter(column_name='teamAbbr', group='GS')])

# Create and configure the figure
east_fig = figure(x_axis_type='datetime',
                  plot_height=300,
                  x_axis_label='Date',
                  y_axis_label='Wins',
                  toolbar_location=None)

west_fig = figure(x_axis_type='datetime',
                  plot_height=300,
                  x_axis_label='Date',
                  y_axis_label='Wins',
                  toolbar_location=None)

# Increase the plot widths
east_fig.plot_width = west_fig.plot_width = 800

# Render the race as step lines
east_fig.step('stDate', 'gameWon',
              source=standings_cds, view=celtics_view,
              color='#007A33', legend='Celtics')
east_fig.step('stDate', 'gameWon',
              source=standings_cds, view=raptors_view,
              color='#CE1141', legend='Raptors')
west_fig.step('stDate', 'gameWon',
              source=standings_cds, view=rockets_view,
              color='#CE1141', legend='Rockets')
west_fig.step('stDate', 'gameWon',
              source=standings_cds, view=warriors_view,
              color='#006BB6', legend='Warriors')

# Move the legend to the upper left corner
east_fig.legend.location = 'top_left'
west_fig.legend.location = 'top_left'

# Create two panels, one for each conference
east_panel = Panel(child=east_fig, title='Eastern Conference')
west_panel = Panel(child=west_fig, title='Western Conference')

# Assign the panels to Tabs
tabs = Tabs(tabs=[west_panel, east_panel])

# Show the tabbed layout
show(tabs)