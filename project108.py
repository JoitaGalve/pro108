import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("projectData.csv")

fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Average Rating"])
fig.show()