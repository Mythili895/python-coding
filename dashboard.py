import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import os
import numpy as np
plotly.tools.set_credentials_file(username = 'mythili895' , api_key="p9tEOCTZjDNdJjwqP5kb")


username = 'mythili895'
password = "swissrus"

##x = np.random.randn(500)
##data = [go.Histogram(x=x)]
##
##py.iplot(data, filename='basic histogram')

iris = pd.read_csv("C:\Users\Mythili Sivakumar\Desktop\iris\iris.csv")
df = pd.DataFrame(iris)
print df
data = [go.Histogram(x = df['petal_length'])]
layout = go.Layout(title ='Iris Dataset - Petal.Length' , xaxis = dict(title='Sepal.Length'),yaxis = dict(title = 'Count' ) )
fig = go.Figure(data = data , layout = layout)
py.iplot(fig)

#graphJSON = json.dumps(layout)
