import streamlit as st #import library yang di butuhkan 

#text elements

st.header("ini header")#header untuk membuat tulisan header
st.subheader("ini sub header")#untuk membuat subjudul jadi lebih kecil 
st.text("ini teks biasa tanpa format")#untuk membuat teks polos tanpa format
st.markdown("**ini teks bold** dan ini teks italic")#markdown untuk memformat teks tebal/miring 
st.markdown("""
-ini baris 1
1.ini baris 2 
2.ini menggunakankan markdown multibaris
            *ini baris 3
            *ini menggunakan markdown multibaris                       """)
st.caption("ini caption")#teks kecil di bawah elemen(untuk penjelasan )
st.title("ini judul")

#coba mandiri
#tuliskan:
#1.Judul Praktikum pakai title ()= Praktikum 1 Visualisasi Data
st.title("Praktikum 1 Visualisasi Data")
#2.bagian praktikum pakai subheader() = Bagian 1 :Teks Element
st.subheader("Teks Element")
#3.Nama lengkap anggota - nim pakai markdown multibaris"""
st.markdown(""" Saepulloh - 0110222183""")

#Bagian 2 :Menampilkan Rumus (Latex)
st.header("Displaying Latex")
st.latex(r''' \cos^\theta = 1-2\sin^2\theta''') #rumus  trigonometri
st.latex(''' (a+b)^2 =A^2+B^2+2ab''')#Rumus kuadratbionominal

#Bagian 3 :Menampilkan kode Program 
st.header("Displaying Code")
st.subheader("Python Code")
#simpan ke variable
code ='''
def hello():
    print("Hello ,Streamlit)'''

#st.code()untuk menampilkan tampilan kode dengan format rapi dan syintax higlighting 
st.code(code,language='python')

st.subheader("Java code")
st
st.code("""
public class GFG {
        publik static void main(Stringarf[])} {
        System.out.printIn("Hello World!)};
""", language='Java')

st.subheader("Javascript Code")
st.code("""
<script>
try{
    addalert("Welcome guest!)
}
catch(err) {
    document.getElementById("demo").innerHTML = err.message;
}
        
</script>
        
""", language='Javascript')
