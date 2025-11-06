#import library 
import streamlit as st
import pandas as pd #untuk mengelola data dalam bentuk 
import numpy as np #untuk membuat data numerik acak 
import altair as alt 
#DataFrame :Struktur data berbentuk tabel (baris dan kolom  ) yang di sediakan oleh library pandas
st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for in range (10))
)

#Menampilkan dataaframe
st.dataframe(df)

#Highlight Nilai minimum 
st.subheader("Highlight Minimum Value di DataFrame")

#Highlight nilai terkecil di setiap kolom dataframe 
#Axis=0 bekerja  per kolom 
st.dataframe(df.style.hightlight_min(axis=0))

#tabel Statis
st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for in range (10))
)

#Menampilkan Tabel statis 
St.table(df)

#Matrics : Komponeen tampilan angka penting 
st.subheader ("Metrics")

#menampilkan metrics tunggal 
st.matrics(label="Temperature",value="31 C",delta="1.2 C")
#kenaikan 1.2 C

#Metrics sesuai delta 