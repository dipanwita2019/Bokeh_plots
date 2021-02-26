#bokeh libraries

from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, GroupFilter

#import the data
from read_nba_data import west_top_2

#output file

output_file("vis example.html" , title = "Viz example")

#separate the data

rockets = west_top_2[west_top_2["teamAbbr"] == "HOU"]
warriors = west_top_2[west_top_2["teamAbbr"] == "GS"]

#ColumnDataSource

rockets = ColumnDataSource(rockets)
warriors = ColumnDataSource(warriors)

fig = figure(x_axis_type = "datetime" , plot_height = 300 , plot_width=900,
             title = "Viz example" , x_axis_label = "Date" , y_axis_label = "Wins")



# Render the race as step lines
fig.step('stDate', 'gameWon',
         color='#CE1141', legend='Rockets',
         source=rockets)
fig.step('stDate', 'gameWon',
         color='#006BB6', legend='Warriors',
         source=warriors)

# Move the legend to the upper left corner
fig.legend.location = 'top_left'

# Show the plot
show(fig)

















