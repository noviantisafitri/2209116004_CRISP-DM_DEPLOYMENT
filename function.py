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

def data_storytelling(df):
    st.title("Student Alcohol Consumption")
    st.image("img/student.jpg")
    st.markdown("""
                Konsumsi alkohol pada remaja merupakan masalah serius yang memerlukan perhatian lebih. Dampaknya tidak hanya terbatas pada kesehatan fisik, tetapi juga berdampak pada kesejahteraan mental dan perilaku sosial. 
                Konsumsi alkohol pada usia muda dapat menyebabkan kecanduan dan memengaruhi perkembangan otak, yang berpotensi merusak kemampuan belajar dan pengambilan keputusan siswa. 
                Selain itu, dapat berisiko terjadinya kecelakaan, kekerasan, dan perilaku berisiko lainnya juga meningkat dengan konsumsi alkohol pada remaja, termasuk perilaku seksual yang tidak aman dan penggunaan narkoba.
                Ketika membahas tentang konsumsi alkohol di kalangan siswa, seringkali kita disadarkan oleh realitas yang cukup kompleks. 
                Dalam era di mana tekanan sosial, ekspektasi, dan aksesibilitas alkohol berdampak pada keputusan siswa, 
                sehingga hal ini menjadi suatu hal yang penting bagi kita untuk memahami faktor-faktor yang terlibat dalam perilaku konsumsi alkohol di kalangan siswa.""")


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

    st.header("Visualisasi Data")

    # Visualisasi distribusi konsumsi alkohol berdasarkan status keluarga
    family_status_counts = df['Pstatus'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=family_status_counts.index, y=family_status_counts.values)
    plt.title('Distribusi Konsumsi Alkohol Berdasarkan Status Keluarga')
    plt.xlabel('Status Keluarga')
    plt.ylabel('Jumlah Siswa')
    st.pyplot()

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

    st.markdown("""
                Visualisasi di atas menunjukkan hubungan antara konsumsi alkohol harian dan nilai akhir siswa. 
                Kita dapat melihat adanya kecenderungan bahwa siswa dengan tingkat konsumsi alkohol yang lebih tinggi cenderung memiliki
                nilai akhir yang lebih rendah. Hal ini menunjukkan adanya hubungan negatif antara konsumsi alkohol dan kinerja akademik.
    """)

def data_distribution(df) :
    st.header('Data Distribution')

    st.write("""
    Visualisasi ini menampilkan distribusi dari fitur yang dipilih. Histogram menunjukkan bagaimana data terdistribusi 
             di sepanjang sumbu horizontal, sementara frekuensi kemunculan nilainya ditampilkan di sumbu vertikal. 
             Semakin tinggi puncak histogram, semakin sering nilai tersebut muncul dalam dataset. 
             Selain itu, adanya garis KDE (Kernel Density Estimate) membantu menunjukkan estimasi kepadatan probabilitas dari data. 
             Semakin tinggi atau curamnya puncak KDE, semakin besar kepadatan probabilitas pada rentang nilai tersebut.
    """)

    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns

    selected_feature = st.selectbox("Pilih fitur untuk plot distribusi:", numeric_columns)

    st.subheader(f"Distribusi Kolom {selected_feature}")
    plt.figure(figsize=(10, 6))
    sns.histplot(df[selected_feature], kde=True, color='skyblue')
    plt.xlabel(selected_feature)
    plt.ylabel('Frekuensi')
    plt.title(f"Distribusi {selected_feature}")
    st.pyplot(plt)

def relation(data):
    st.header('Relation')

    # Plot matriks korelasi menggunakan heatmap
    fig, ax = plt.subplots()
    sns.heatmap(data.corr(numeric_only=True), annot=True, fmt=".2f", cbar=True, cmap="Blues")
    plt.xlabel('Fitur')
    plt.ylabel('Fitur')
    plt.title('Matriks Korelasi Antar Fitur Numerik')
    plt.gcf().set_size_inches(15, 10)
    st.pyplot(fig)

    st.write("""
    Visualisasi diatas menampilkan matriks korelasi antara fitur-fitur numerik dalam dataset.
    Matriks korelasi digunakan untuk memahami hubungan linier antara variabel-variabel numerik.
    Korelasi bernilai antara -1 hingga 1, dengan nilai 1 menunjukkan korelasi positif sempurna, 
    nilai -1 menunjukkan korelasi negatif sempurna, dan nilai 0 menunjukkan tidak adanya korelasi.
    Berdasarkan hasil visualisasi korelasi di atas, terlihat bahwa setiap variabel memiliki nilai yang menggambarkan hubungannya dengan variabel lainnya. Sebagai contoh, variabel kegiatan di luar sekolah (goout) menunjukkan korelasi yang signifikan dengan konsumsi alkohol pada akhir pekan (Walc).
    """)

def composition(df):
    st.header('Composition')

    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    class_composition = df.groupby('Walc')[numeric_columns].mean()

    plt.figure(figsize=(10, 6))
    sns.heatmap(class_composition.T, annot=True, cmap='YlGnBu')
    plt.title('Komposisi berdasarkan Konsumsi Alkohol di Akhir Pekan (Walc)')
    plt.xlabel('Konsumsi Alkohol di Akhir Pekan (Walc)')
    plt.ylabel('Fitur')
    st.pyplot(plt)

    st.write ("""
              Visualisasi diatas menampilkan rata-rata nilai fitur numerik berdasarkan tingkat konsumsi alkohol di akhir pekan (Walc). 
              Setiap sel dalam heatmap menunjukkan rata-rata nilai fitur tersebut untuk setiap kategori tingkat konsumsi alkohol di akhir pekan. 
              Warna dalam heatmap menggambarkan intensitas nilai, di mana warna yang lebih gelap menunjukkan nilai yang lebih tinggi dan warna yang lebih terang menunjukkan nilai yang lebih rendah. 
              Visualisasi ini berguna untuk melihat pola hubungan antara tingkat konsumsi alkohol di akhir pekan dengan berbagai fitur numerik dalam dataset. 
              Misalnya, kita dapat melihat apakah terdapat perbedaan dalam nilai akhir berdasarkan tingkat konsumsi alkohol di akhir pekan.
              """)

def comparison(df):
    st.header('Comparison')

    # Hitung rata-rata tingkat konsumsi alkohol di hari kerja (Dalc) dan akhir pekan (Walc) berdasarkan kategori umur
    avg_dalc_by_age = df.groupby('age')['Dalc'].mean()
    avg_walc_by_age = df.groupby('age')['Walc'].mean()
    
    plt.figure(figsize=(10, 6))
    plt.plot(avg_dalc_by_age.index, avg_dalc_by_age.values, marker='o', linestyle='-', color='blue', label='Konsumsi Alkohol di Hari Kerja (Dalc)')
    plt.plot(avg_walc_by_age.index, avg_walc_by_age.values, marker='o', linestyle='-', color='red', label='Konsumsi Alkohol di Akhir Pekan (Walc)')
    plt.title('Perbandingan Konsumsi Alkohol di Hari Kerja dan Akhir Pekan Berdasarkan Usia')
    plt.xlabel('Usia')
    plt.ylabel('Rata-rata Konsumsi Alkohol')
    plt.xticks(avg_dalc_by_age.index)
    plt.legend()
    st.pyplot(plt)

    st.write("""
              Visualisasi diatas digunakan untuk melihat melihat perbandingan rata-rata tingkat konsumsi alkohol di hari kerja (Dalc) dan akhir pekan (Walc) berdasarkan kategori umur siswa. 
              Dari visualisasi ini dapat terlihat apakah terdapat tren peningkatan atau penurunan dalam konsumsi alkohol dari hari kerja ke akhir pekan di setiap kelompok usia.
              """)


def predict_cluster():
    st.header("Let's Predict!")
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
