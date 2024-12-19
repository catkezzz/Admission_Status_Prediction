import streamlit as st
import pandas as pd
import seaborn as sns
from PIL import Image
import matplotlib.pyplot as plt

def run():

    # Membuat Title
    st.title('Aplikasi Prediksi Status Admission Wharton Class 2025')
        #Menambah Deskripsi
    st.write('Aplikasi ini dibuat oleh **Catherine Kezia Wijaya**')

    st.markdown('---')

    # Menambahkan Gambar
    image = Image.open('dataset-cover.png')
    st.image(image, caption='Logo MBA 2025')

    # Membuat garis lurus horizontal
    st.markdown('---')

    st.subheader('Exploratory Data Analysis dari dataset MBA Admission Class 2025')
    st.write('Berikut adalah data dari 6194 calon mahasiswa')
    df_ori = pd.read_csv('MBA.csv')
    df = df_ori.copy()
    st.dataframe(df)

    st.write('### Ratio Admit vs Deny or Waitlist')
    df['admission'] = df['admission'].fillna('Deny')
    admission= df['admission'].value_counts(dropna=False)
    fig = plt.figure(figsize=(5, 5))
    plt.pie(admission, labels=admission.index, autopct='%1.1f%%', startangle=90, colors=['#4CAF50', '#FF5733', '#FFEB3B'])
    st.pyplot(fig)
    st.write('Sekitar 85% persen dari seluruh mahasiswa telah ditolak, dan hanya 14.5% telah diterima')


    st.write('### Distribusi GPA dan GMAT')
    pilihan_user = st.radio('Pilih tipe skor: ', ['gpa', 'gmat'])
    fig = plt.figure(figsize=(13, 6))
    sns.histplot(df[pilihan_user], bins=30, kde=True)
    st.pyplot(fig)
    st.write('Skor GPA dan GMAT mahasiswa kurang lebih mendekati rata - rata. Untuk GPA di sekitar 3.2, dan untuk GMAT di sekitar 670')


    st.write('### Distribusi Identitas Calon Mahasiswa')
    pilihan_user = st.radio('Pilih tipe identitas: ', ['gender', 'international', 'race'])
    fig = plt.figure(figsize=(5, 5))
    df['race'] = df['race'].fillna('International Student')
    score= df[pilihan_user].value_counts(dropna=False)
    plt.pie(score, labels=score.index, autopct='%1.1f%%', startangle=90, colors=['#4CAF50', '#FF5733', '#FFEB3B', '#FF9800', '#009688', '#3F51B5', '#E91E63'])
    st.pyplot(fig)
    st.write('''
            Dari Pie chart bisa terlihat ratio dari identitas calon mahasiswa:
            
            - Jenis kelamin mayoritas adalah laki - laki
            - Kebanyakan mahasiswa berasal dari luar negri
            - Mayoritas ras juga mahasiswa dari luar negri
            ''')

    st.write('### Visualisasi Work Experience dan Major yang dipilih')
    pilihan_user = st.radio('Pilih data: ', ['major', 'work_industry'])
    fig = plt.figure(figsize=(13, 6))
    sns.histplot(df[pilihan_user], bins=30, kde=True)
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)
    st.write('''
            Dari Histogam bisa terlihat distribusi dari jurusan dan pengalaman kerja:
            
            - Jurusan yang paling banyak terpilih adalah Humanities, diikuti dengan STEM, dan paling sedikit Business
            - Kebanyakan memiliki pengalaman kerja sebagai konsultan, diikuti dengan PE/VC dan background teknologi
            ''')