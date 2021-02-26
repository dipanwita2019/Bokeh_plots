import numpy as np

##imports
from bokeh.io import output_file
from bokeh.plotting import figure,show

#My word count

days = np.linspace(1,10,10)
words = [200,300,400,400,200,500,100,800,200,100]
cum = np.cumsum(words)

#output file

output_file("legend_added.html",title = "With Legends")

#create figure

fig = figure(title = "progress", plot_height = 400, plot_width =400 ,
             x_axis_label = "Days" , y_axis_label = "Count", x_minor_ticks =2,
             y_range = (0,5000) , toolbar_location = None)

#add glyphs

fig.vbar(x = days, bottom = 0 , top = words , color = "blue" , width = 0.75 , legend = "Daily" )

fig.line(x = days , y = cum , color = "gray"  , line_width = 1 , legend = "Cumulative")

#add legend location

#fig.legend.location = "top_left"

#show

show(fig)