from bokeh.io import output_file
from bokeh.plotting import figure,show

#prepare data

x = [1,2,3]
y = [1,1,2]


#output the viz into a static html file

output_file("firstglyph.html", title = "First Glyph")

#create a figure with no tool bar

fig = figure(title = "My Data" ,
             plot_width=300,
             plot_height=300,
             x_range=(0,3),
             y_range=(0,3),
             toolbar_location=None)


#Draw the co-ordinates as circle

fig.circle(x= x, y = y, color = "green" , size = 10, alpha=0.5)

#show plot
show(fig)