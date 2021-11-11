from sklearn.datasets import load_train_set_label
from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import numpy as np
st.title("Malicious program")
var = load_train_set_label()
x = var.data
y = var.target
model = KNeighborsClassifier(n_neighbors = 7)
model.fit(x,y)
xmin = np.min(x, axis = 0)
xmax = np.max(x, axis = 0)
SizeOfStackReserve = st.slider('SIZE OF STACK RESERVE',int(xmin[0]),int(xmax[0]))
SizeOfHeapReserve = st.slider('SIZE OF HEAP RESERVE',int(xmin[1]),int(xmax[1]))
class = st.slider('CLASS',int(xmin[2]),int(xmax[2]))
y_pred = model.predict([[SizeOfStackReserve,SizeOfHeapReserve,class]])
op = ['1048576','1048576','1']
st.title(op[y_pred[0]])
