from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, GroupFilter

# Import the data
from read_nba_data import west_top_2

# Output to static HTML file
output_file('west_top_2_standings_race.html',
            title='Western Conference Top 2 Teams Wins Race')

# Create a ColumnDataSource
west_cds = ColumnDataSource(west_top_2)

# Create view for each team
rockets_view = CDSView(source=west_cds,
                       filters=[GroupFilter(column_name='teamAbbr', group='HOU')])
print(rockets_view)
warriors_view = CDSView(source=west_cds,
                        filters=[GroupFilter(column_name='teamAbbr', group='GS')])

# Create and configure the figure
west_fig = figure(x_axis_type='datetime',
                  plot_height=300, plot_width=600,
                  title='Western Conference Top 2 Teams Wins Race, 2017-18',
                  x_axis_label='Date', y_axis_label='Wins',
                  toolbar_location=None)

# Render the race as step lines
west_fig.step('stDate', 'gameWon',
              source=west_cds, view=rockets_view,
              color='#CE1141', legend='Rockets')
west_fig.step('stDate', 'gameWon',
              source=west_cds, view=warriors_view,
              color='#006BB6', legend='Warriors')

# Move the legend to the upper left corner
west_fig.legend.location = 'top_left'

# Show the plot
show(west_fig)