
import streamlit as st
import matplotlib.pyplot as plt

# Data
months = ['jan','feb','mar','apr','mei','jun','jul','agst','sep','okt','nov','dec']
product_A_sales = [10,20,15,25,30,45,40,50,60,55,65,70]
product_B_sales = [5,10,8,30,33,25,56,10,11,48,20,21]

# Title
st.title("Visualisasi Penjualan")
st.sidebar.header("Pengaturan Grafik")

# Selectbox – DIBENERIN
option = st.sidebar.selectbox(
    "Pilih Tipe Visualisasi",
    (
        "Single Line Plot",
        "Multiple & Customize",
        "Subplot C-D"
    )
)

# Identitas kelompok
st.caption("Praktikum 3 - Matplotlib Line Chart")
st.markdown("""
Kelompok 9 :
 - Santika Sintia Larasati -0110122045
 - Saepulloh  - 0110222183
 - Muhammad Ammar - 0110122308
""")

# 1. SINGLE LINE PLOT
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A')
    ax.set_title('Penjualan Produk A Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

# 2. MULTIPLE CUSTOMIZED LINE PLOT

def customize_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A', linestyle="--", marker='o')
    ax.plot(months, product_B_sales, label='Product B', linestyle="-", marker='x')
    
    ax.set_title('Perbandingan Penjualan Produk A & B')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# 3. SUBPLOT C - D

def subplot_CD():
    product_C_sales = [18,2,25,28,12,45,48,17,12,10,15,35]
    product_D_sales = [10,7,30,2,45,25,23,16,11,9,13,20]

    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    # Plot C
    axs[0].plot(months, product_C_sales, color='green', marker='o', label='Product C')
    axs[0].set_title('Penjualan Product C Per Bulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Penjualan')
    axs[0].legend()
    axs[0].grid(True)

    # Plot D
    axs[1].plot(months, product_D_sales, color='red', marker='x', label='Product D')
    axs[1].set_title('Penjualan Product D Per Bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Penjualan')
    axs[1].legend()
    axs[1].grid(True)

    st.pyplot(fig)

# LOGIKA PEMILIHAN GRAFIK
if option == "Single Line Plot":
    line_plot()
elif option == "Multiple & Customize":
    customize_line_plot()
elif option == "Subplot C-D":
    subplot_CD()