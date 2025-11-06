import streamlit as st
import datetime
import pandas as pd # Diperlukan untuk bagian CSV

# Hapus semua impor berulang di tengah kode.

# --- 1. Text Widgets ---
st.title("Text Box & Area")

# Text Input
name_basic = st.text_input("Enter your Name (Basic)")
st.write("Your Name is ", name_basic)

# Text Input dengan limit karakter dan key unik
name_limited = st.text_input("Enter your Name (Max 10 chars)", max_chars=10, key="name_limit")
st.write(f"Your Name (Limited) is: {name_limited}")

# Password Input
password = st.text_input("Enter your password", type='password', key="pwd_input")

# Text Area
input_text = st.text_area("Enter your Review")
st.write(f"Your entered: \n{input_text}")

# --- 2. Number & Time Widgets ---
st.title("Number & Time Inputs")

# Number Input (basic)
st.number_input("Enter your Number (Basic)", key="num_basic")

# Number Input (with steps and range)
num_settings = st.number_input(
    "Enter your Number (Range/Step)", 
    min_value=0, 
    max_value=10, 
    value=5, 
    step=2,
    key="num_settings"
)
st.write(f"Min. Value: 0, Max. Value: 10")
st.write(f"Default Value: 5, Step Size: 2")
st.write(f"Current Value: {num_settings}")

# Time Input
st.time_input("Select Your Time")

# --- 3. Date & Color Widgets ---
st.title("Date & Color Picker")

# Date Input (Fixed syntax from previous fix)
selected_date = st.date_input(
    "Select Your date"   , value=datetime.date(1989, 12, 25),
    min_value=datetime.date(1987, 1, 1),
    max_value=datetime.date(2005, 12, 1)
)
st.write("You selected:", selected_date)

# Color Picker
color_code = st.color_picker("Select your Color")
st.write("Your selected color code is:", color_code)

# --- 4. File Uploader (CRITICAL ERROR FIXED) ---
st.title("CSV Data Uploader")
data_file = st.file_uploader("Upload CSV", type=["csv"])
details = st.button("Check Details")

if details:
    # Kesalahan 1: Ganti 'date_file' menjadi 'data_file'
    if data_file is not None:
        # Kesalahan 2: Perbaiki sintaks Dictionary (gunakan {} dan :)
        file_details = {
            "file_name": data_file.name,
            "file_type": data_file.type,
            "file-size": data_file.size
        }
        st.write(file_details)

        # Kesalahan 3: Membaca CSV harus di dalam blok 'if data_file is not None'
        try:
            df = pd.read_csv(data_file)
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error reading CSV: {e}")
    else:
        st.write("No CSV File is Uploaded") # Ini akan dieksekusi jika 'details' True, tapi 'data_file' None.

# --- 5. Streamlit Form (SYNTAX ERROR FIXED) ---
st.title("Form Example")

# Hapus 'else' yang menggantung
with st.form(key='my_form'):
    a = st.text_input(label='Enter any text inside the form')
    # Defining submit button
    submit_button = st.form_submit_button(label='Submit Form')

if submit_button:
    st.write(f"Value submitted from form: {a}")
else:
    st.write(f"Current value (outside form submission): {a}")