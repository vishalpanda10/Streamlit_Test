import streamlit as st
import plotly.figure_factory as ff
import seaborn as sns
import plotly.express as px

iris = sns.load_dataset("iris")


st.write("""
# Iris Dataset 

- Attributes of different species of iris plants
""")


fig = px.scatter_3d(iris, x='sepal_length', y='sepal_width', z='petal_width',
              color='species')

fig.show()