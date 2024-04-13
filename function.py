import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

def load_data():
    URL = 'student_alcohol.csv'
    df = pd.read_csv(URL)
    return df

def data_distribution(data) :
    st.subheader('Distribusi Konsumsi Alkohol pada Hari Kerja')

    # Deskripsi distribusi data
    st.write("""
    Visualisasi ini menampilkan distribusi konsumsi alkohol pada hari kerja oleh siswa.
    Dari distribusi ini, kita dapat melihat pola konsumsi alkohol dan frekuensi kemunculannya.
    """)

    # Plot distribusi data menggunakan histogram
    fig, ax = plt.subplots()
    sns.histplot(data['Dalc'], bins=5, kde=True)
    plt.xlabel('Konsumsi Alkohol pada Hari Kerja')
    plt.ylabel('Frekuensi')
    plt.title('Distribusi Konsumsi Alkohol pada Hari Kerja')
    st.pyplot(fig)

def relation(data):
    st.subheader('Relation')

    # Plot matriks korelasi menggunakan heatmap
    fig, ax = plt.subplots()
    sns.heatmap(data.corr(numeric_only=True), annot=True, fmt=".2f", cbar=True, cmap="Blues")
    plt.xlabel('Fitur')
    plt.ylabel('Fitur')
    plt.title('Matriks Korelasi Antar Fitur Numerik')
    plt.gcf().set_size_inches(15, 10)
    st.pyplot(fig)

    # Deskripsi matriks korelasi
    st.write("""
    Visualisasi diatas menampilkan matriks korelasi antara fitur-fitur numerik dalam dataset.
    Matriks korelasi adalah alat yang berguna untuk memahami hubungan linier antara variabel-variabel numerik.
    Korelasi bernilai antara -1 hingga 1, dengan nilai 1 menunjukkan korelasi positif sempurna, 
    nilai -1 menunjukkan korelasi negatif sempurna, dan nilai 0 menunjukkan tidak adanya korelasi.
    Berdasarkan hasil visualisasi korelasi di atas, terlihat bahwa setiap variabel memiliki nilai yang menggambarkan hubungannya dengan variabel lainnya. Sebagai contoh, variabel kegiatan di luar sekolah (goout) menunjukkan korelasi yang signifikan dengan konsumsi alkohol pada akhir pekan (Walc).
    """)

def composition(df):
    # Pilih kolom numerik untuk dianalisis
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    
    # Hitung rata-rata fitur untuk setiap kelas
    class_composition = df.groupby('Walc')[numeric_columns].mean()
    
    # Plot komposisi kelas
    plt.figure(figsize=(10, 6))
    sns.heatmap(class_composition.T, annot=True, cmap='YlGnBu')
    plt.title('Komposisi berdasarkan Konsumsi Alkohol di Akhir Pekan (Walc)')
    plt.xlabel('Konsumsi Alkohol di Akhir Pekan (Walc)')
    plt.ylabel('Fitur')
    st.pyplot(plt)

def comparison(df):
    # Pilih kolom numerik untuk dianalisis
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    
    # Bandingkan dua fitur
    feature1 = 'Dalc'  # Kolom konsumsi alkohol di hari kerja
    feature2 = 'Walc'  # Kolom konsumsi alkohol di akhir pekan
    
    # Plot perbandingan
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=feature1, y=feature2, data=df)
    plt.title('Perbandingan Konsumsi Alkohol di Hari Kerja dan Akhir Pekan')
    plt.xlabel('Konsumsi Alkohol di Hari Kerja (Dalc)')
    plt.ylabel('Konsumsi Alkohol di Akhir Pekan (Walc)')
    st.pyplot(plt)


def data_storytelling(df):
    st.title("Konsumsi Alkohol di Kalangan Siswa")
    st.image("img/student.jpg")
    st.markdown("""
                Konsumsi alkohol pada remaja merupakan masalah serius yang memerlukan perhatian mendalam. Dampaknya tidak hanya terbatas pada kesehatan fisik, tetapi juga berdampak pada kesejahteraan mental dan perilaku sosial. Konsumsi alkohol pada usia muda dapat menyebabkan kecanduan dan memengaruhi perkembangan otak, yang berpotensi merusak kemampuan belajar dan pengambilan keputusan siswa. Selain itu, risiko terjadinya kecelakaan, kekerasan, dan perilaku berisiko lainnya juga meningkat dengan konsumsi alkohol pada remaja, termasuk perilaku seksual yang tidak aman dan penggunaan narkoba.
                Ketika membahas tentang konsumsi alkohol di kalangan siswa, seringkali kita disadarkan oleh realitas yang cukup kompleks. 
                Dalam era di mana tekanan sosial, ekspektasi, dan aksesibilitas alkohol berdampak pada keputusan siswa, 
                sehingga hal ini menjadi suatu hal yang penting bagi kita untuk memahami faktor-faktor yang terlibat dalam perilaku konsumsi alkohol di kalangan siswa.""")

    # Data dan Variabel
    st.markdown("Untuk mengetahui hubungan antara variabel-variabel yang mempengaruhi konsumsi alkohol siswa, dapat menggunakan kumpulan data dari survei yang melibatkan ratusan siswa dari berbagai latar belakang. Berikut adalah variabel-variabel yang berpengaruh :")
    st.markdown("- **Usia** : Usia siswa dapat memengaruhi kecenderungan mereka untuk mencoba mengonsumsi alkohol.")
    st.markdown("- **Jenis Kelamin** : Terdapat perbedaan dalam pola konsumsi alkohol antara siswa laki-laki dan perempuan.")
    st.markdown("- **Pendidikan Orang Tua** : Lingkungan keluarga dan pendidikan orang tua dapat memainkan peran penting dalam membentuk sikap terhadap alkohol.")
    st.markdown("- **Tingkat Stres** : Siswa yang mengalami tingkat stres yang tinggi mungkin cenderung mencari pelarian dalam alkohol.")

    # Interpretasi
    st.header("Interpretasi")
    st.markdown("1. **Usia dan Konsumsi** : Siswa yang lebih tua cenderung memiliki tingkat konsumsi alkohol yang lebih tinggi daripada siswa yang lebih muda.")
    st.markdown("2. **Perbedaan Gender** : Meskipun terdapat perbedaan antara laki-laki dan perempuan dalam pola konsumsi, trennya menunjukkan bahwa konsumsi alkohol di kalangan siswa laki-laki cenderung lebih tinggi.")
    st.markdown("3. **Pengaruh Keluarga** : Siswa yang berasal dari lingkungan keluarga di mana pendidikan tentang bahaya alkohol diberikan cenderung memiliki tingkat konsumsi yang lebih rendah.")
    st.markdown("4. **Tingkat Stres** : Siswa yang mengalami tingkat stres yang tinggi cenderung memiliki kecenderungan yang lebih tinggi untuk mengonsumsi alkohol.")

    # Actionable Insight
    st.header("Actionable Insight")
    st.markdown("1. Membuat program pendidikan yang mengedukasi tentang bahaya alkohol dan strategi penanganan stres yang sehat agar dapat membantu mengurangi konsumsi alkohol di kalangan siswa.")
    st.markdown("2. Melibatkan orang tua dalam mendidik anak-anak mereka tentang bahaya alkohol dan menyediakan lingkungan keluarga yang mendukung dapat membantu mengurangi risiko konsumsi alkohol di kalangan remaja.")
    st.markdown("3. Membuat sebuah kebijakan yang mengatur aksesibilitas alkohol di sekitar sekolah dan daerah pemukiman yang dapat membantu mengurangi kesempatan siswa untuk mengonsumsi alkohol.")

    st.markdown("Dengan menggunakan pendekatan ini, kita dapat bekerja sama untuk mengurangi tingkat konsumsi alkohol di kalangan siswa dan mendorong perilaku yang lebih sehat dan aman.")

    # Visualisasi distribusi konsumsi alkohol berdasarkan jenis kelamin
    gender_counts = df['sex'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=gender_counts.index, y=gender_counts.values)
    plt.title('Distribusi Konsumsi Alkohol Berdasarkan Jenis Kelamin')
    plt.xlabel('Jenis Kelamin')
    plt.ylabel('Jumlah Siswa')
    st.pyplot()

    # Penjelasan visualisasi distribusi konsumsi alkohol berdasarkan jenis kelamin
    st.markdown("""
    Grafik di atas mengilustrasikan distribusi konsumsi alkohol siswa sekolah menengah berdasarkan jenis kelamin. 
    Kita dapat melihat bahwa siswa laki-laki (M) cenderung memiliki tingkat konsumsi alkohol harian yang lebih tinggi 
    dibandingkan dengan siswa perempuan (F). Ini menunjukkan adanya perbedaan perilaku konsumsi alkohol antara jenis kelamin.
    """)

    # Visualisasi distribusi konsumsi alkohol berdasarkan status keluarga
    family_status_counts = df['Pstatus'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=family_status_counts.index, y=family_status_counts.values)
    plt.title('Distribusi Konsumsi Alkohol Berdasarkan Status Keluarga')
    plt.xlabel('Status Keluarga')
    plt.ylabel('Jumlah Siswa')
    st.pyplot()

    # Penjelasan visualisasi distribusi konsumsi alkohol berdasarkan status keluarga
    st.markdown("""
    Grafik di atas menampilkan distribusi konsumsi alkohol siswa sekolah menengah berdasarkan status keluarga. 
    Kita dapat melihat bahwa siswa dari keluarga dengan status cohabitation (Tinggal Bersama) cenderung memiliki tingkat 
    konsumsi alkohol harian yang lebih tinggi dibandingkan dengan siswa dari keluarga dengan status apart (Tinggal Terpisah).
    Ini menunjukkan bahwa lingkungan keluarga dapat memengaruhi perilaku konsumsi alkohol siswa.
    """)

    # Visualisasi hubungan antara konsumsi alkohol dan kinerja akademik
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='G3', y='Dalc', data=df)
    plt.title('Hubungan antara Konsumsi Alkohol dan Kinerja Akademik')
    plt.xlabel('Nilai Akhir')
    plt.ylabel('Konsumsi Alkohol (Harian)')
    st.pyplot()

    # Penjelasan visualisasi hubungan antara konsumsi alkohol dan kinerja akademik
    st.markdown("""
    Visualisasi di atas menunjukkan hubungan antara konsumsi alkohol harian dan nilai akhir siswa. 
    Kita dapat melihat adanya kecenderungan bahwa siswa dengan tingkat konsumsi alkohol yang lebih tinggi cenderung memiliki
    nilai akhir yang lebih rendah. Hal ini menunjukkan adanya hubungan negatif antara konsumsi alkohol dan kinerja akademik.
    """)

def describe_data():
    # Judul dan Deskripsi
    st.write("""
    """)

    # Tujuan Analisis
    st.write("""
    Tujuan analisis ini adalah untuk mengidentifikasi faktor-faktor apa saja yang memengaruhi perilaku konsumsi alkohol pada remaja. Dengan memahami faktor-faktor ini, dapat ditemukan kelompok remaja yang lebih rentan terhadap konsumsi alkohol. Analisis ini diharapkan dapat memberikan wawasan bagi pihak terkait dalam merancang strategi yang efektif untuk mengurangi maupun mencegah konsumsi alkohol pada remaja.
    """)

    # Kontribusi Positif
    st.write("""
    Diharapkan bahwa hasil analisis ini dapat memberikan kontribusi positif dalam upaya mengurangi dampak negatif konsumsi alkohol pada remaja. Informasi yang diperoleh dari analisis ini dapat digunakan untuk menginformasikan kebijakan dan program-program pencegahan konsumsi alkohol pada remaja secara lebih efektif.
    """)

    # Sumber Data
    st.header('Sumber Data: Survei tentang Konsumsi Alkohol pada Siswa')
    st.write("""
    Data yang digunakan dalam analisis ini berasal dari survei terhadap siswa yang mengikuti kursus matematika dan bahasa Portugis di sekolah menengah. Data tersebut mencakup informasi tentang karakteristik sosial, gender, dan studi dari para siswa. Sumber data ini merupakan salah satu sumber penting untuk memahami perilaku konsumsi alkohol pada remaja.
    """)

def visualize_alcohol_consumption(df):
    st.subheader("Data Visualization")

    # Visualisasi 1 : Tingkat konsumsi alkohol di hari kerja (Dalc) berdasarkan cluster
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    # Plot histogram untuk Dalc
    axes[0].hist(df['Dalc'])
    axes[0].set_xlabel('Survey Response Score', fontsize=15)
    axes[0].set_ylabel('Instances', fontsize=15)
    axes[0].set_title('Weekday Consumption (Dalc)', fontsize=18)
    # Plot histogram untuk Walc
    axes[1].hist(df['Walc'])
    axes[1].set_xlabel('Survey Response Score', fontsize=15)
    axes[1].set_title('Weekend Consumption (Walc)', fontsize=18)
    # Menampilkan plot
    st.pyplot(fig)

    st.write("Lorem")



    # Visualisasi 1 : Tingkat konsumsi alkohol di hari kerja (Dalc) berdasarkan cluster
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df['G1'], y=df['G2'], hue=df['sex'])
    plt.xlabel('G1', fontsize=12)
    plt.ylabel('G2', fontsize=12)
    plt.title('Scatter Plot of G1 vs G2 with Sex Hue', fontsize=14)
    # Menampilkan plot
    st.pyplot()

    st.write("Lorem")



    # Visualisasi 1 : Tingkat konsumsi alkohol di hari kerja (Dalc) berdasarkan cluster
    fig = plt.figure(figsize=(17,5))
    # Menambahkan subplot pertama
    ax1 = fig.add_subplot(121)
    sns.distplot(df[df['romantic'] == 'no']['absences'], color='coral', ax=ax1)
    ax1.set_title('Distribution of absences for classes by single people')

    # Menambahkan subplot kedua
    ax2 = fig.add_subplot(122)
    sns.distplot(df[df['romantic'] == 'yes']['absences'], color='purple', ax=ax2)
    ax2.set_title('Distribution of absences for classes by people in love')

    # Menampilkan plot
    st.pyplot(fig)

    st.write("Lorem")

    
    
    # Visualisasi 1 : Tingkat konsumsi alkohol di hari kerja (Dalc) berdasarkan cluster
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))
    # Plot pertama: hubungan pergi keluar dan konsumsi alkohol di hari kerja
    sns.pointplot(x="goout", y="Dalc",
                data=df,
                ax=axs[0])
    axs[0].set_title("Hubungan Pergi keluar dan Konsumsi Alkohol di hari kerja")

    # Plot kedua: hubungan pergi keluar dan konsumsi alkohol di akhir pekan
    sns.pointplot(x="goout", y="Walc",
                data=df,
                ax=axs[1])
    axs[1].set_title("Hubungan Pergi keluar dan Konsumsi Alkohol di Akhir Pekan")
    # Menampilkan plot
    st.pyplot(fig)

    st.write("Lorem")


def predict_cluster():
    num_columns = 3

    for i in range(11):
        col1, col2, col3 = st.columns(num_columns)
        
        with col1:
            if i == 0:
                school = st.selectbox('School', ['Gabriel Pereira', 'Mousinho da Silveira'])
            elif i == 1:
                sex = st.selectbox('Sex', ['Female', 'Male'])
            elif i == 2:
                age = st.number_input('Age', 15, 22)
            elif i == 3:
                address = st.selectbox('Address', ['Urban', 'Rural'])
            elif i == 4:
                famsize = st.selectbox('Family Size', ['Less or equal to 3', 'Greater than 3'])
            elif i == 5:
                Pstatus = st.selectbox('Parent Cohabitation Status', ['Living Together', 'Apart'])
            elif i == 6:
                Medu = st.selectbox("Mother's Education", ['None','Primary education', '5th to 9th grade', 'Secondary education', 'Higher education'])
            elif i == 7:
                Fedu = st.selectbox("Father's Education", ['None','Primary education', '5th to 9th grade', 'Secondary education', 'Higher education'])
            elif i == 8:
                Mjob = st.selectbox("Mother's Job", ['Teacher', 'Health', 'Services', 'At_home', 'Other'])
            elif i == 9:
                Fjob = st.selectbox("Father's Job", ['Teacher', 'Health', 'Services', 'At_home', 'Other'])
            elif i == 10:
                reason = st.selectbox('Reason to Choose School', ['Home', 'Reputation', 'Course', 'Other'])
        
        with col2:
            if i == 0:
                guardian = st.selectbox('Guardian', ['Mother', 'Father', 'Other'])
            elif i == 1:
                traveltime = st.selectbox('Travel Time to School', ['<15 min', '15 to 30 min', '30 min to 1 hour,', '>1 hour'])
            elif i == 2:
                studytime = st.selectbox('Weekly Study Time', ['<2 hours', '2 to 5 hours', '5 to 10 hours', '>10 hours'])
            elif i == 3:
                failures = st.selectbox('Past Failures', ['1', '2', '3', '4'])
            elif i == 4:
                schoolsup = st.selectbox('Extra Educational Support', ['yes', 'no'])
            elif i == 5:
                famsup = st.selectbox('Family Educational Support', ['yes', 'no'])
            elif i == 6:
                paid = st.selectbox('Extra Paid Classes', ['yes', 'no'])
            elif i == 7:
                activities = st.selectbox('Extra-curricular Activities', ['yes', 'no'])
            elif i == 8:
                nursery = st.selectbox('Attended Nursery School', ['yes', 'no'])
            elif i == 9:
                higher = st.selectbox('Wants to Take Higher Education', ['yes', 'no'])
            elif i == 10:
                internet = st.selectbox('Internet Access at Home', ['yes', 'no'])
        
        with col3:
            if i == 0:
                romantic = st.selectbox('With a Romantic Relationship',['yes', 'no'])
            elif i == 1:
                famrel = st.selectbox('Quality of Family Relationships', ['1', '2', '3', '4', '5'])
            elif i == 2:
                freetime = st.selectbox('Free Time After School', ['1', '2', '3', '4', '5'])
            elif i == 3:
                goout = st.selectbox('Going Out with Friends', ['1', '2', '3', '4', '5'])
            elif i == 4:
                Dalc = st.selectbox('Workday Alcohol Consumption', ['1', '2', '3', '4', '5'])
            elif i == 5:
                Walc = st.selectbox('Weekend Alcohol Consumption', ['1', '2', '3', '4', '5'])
            elif i == 6:
                health = st.selectbox('Current Health Status', ['1', '2', '3', '4', '5'])
            elif i == 7:
                absences = st.number_input('Absences', 0, 20)
            elif i == 8:
                G1 = st.number_input('G1', 0, 20)
            elif i == 9:
                G2 = st.number_input('G2', 0, 20)
            elif i == 10:
                G3 = st.number_input('G3', 0, 20)


    data = pd.DataFrame({
        'school': [0 if school == 'Gabriel Pereira' else 1],
        'sex': [0 if sex == 'Male' else 1],
        'age': [age],
        'address': [0 if address == 'Urban' else 1],
        'famsize': [0 if famsize == 'Less or equal to 3' else 1],
        'Pstatus': [0 if Pstatus == 'Living Together' else 1],
        'Medu': [Medu.index(Medu)],
        'Fedu': [Fedu.index(Fedu)],
        'Mjob': [Mjob.index(Mjob)],
        'Fjob': [Fjob.index(Fjob)],
        'reason': [reason.index(reason)],
        'guardian': [guardian.index(guardian)],
        'traveltime': [traveltime.index(traveltime)],
        'studytime': [studytime.index(studytime)],
        'failures': [failures.index(failures)],
        'schoolsup': [0 if schoolsup == 'yes' else 1],
        'famsup': [0 if famsup == 'yes' else 1],
        'paid': [0 if paid == 'yes' else 1],
        'activities': [0 if activities == 'yes' else 1],
        'nursery': [0 if nursery == 'yes' else 1],
        'higher': [0 if higher == 'yes' else 1],
        'internet': [0 if internet == 'yes' else 1],
        'romantic': [0 if romantic == 'yes' else 1],
        'famrel': [int(famrel)],
        'freetime': [int(freetime)],
        'goout': [int(goout)],
        'Dalc': [int(Dalc)],
        'Walc': [int(Walc)],
        'health': [int(health)],
        'absences': [absences],
        'G1': [G1],
        'G2': [G2],
        'G3': [G3],

    })



    st.write(data)
    button = st.button('Predict')
    if button:

        try:
            with open('gnb.sav', 'rb') as file:
                loaded_model = pickle.load(file)
            predicted = loaded_model.predict(data)

            if predicted[0] == 0:
                st.write("Predicted Cluster: 1")
            elif predicted[0] == 1:
                st.write("Predicted Cluster: 2")
            elif predicted[0] == 2:
                st.write("Predicted Cluster: 3")
            else:
                st.write("Predicted Cluster: 4")
                
        except Exception as e:
           print("Terjadi kesalahan:", e)

if __name__ == "__main__":
    df = load_data()
    visualize_alcohol_consumption(df)
    predict_cluster()
