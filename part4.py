# Yuxuan Chen
# yuxuanc


# Imports -- you may add others but do not need to
import plotly.plotly as py
import plotly.graph_objs as go

# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets
word = []
freq = []

with open("noun_data.csv") as f:
    firstLine = True
    for line in f:
        if firstLine:
            firstLine = False
        else:
            data = line.split(",")
            word.append(data[0])
            freq.append(int(data[1].strip('\n')))

py.iplot([go.Bar(x=word, y=freq)], filename="part4_viz_image")

