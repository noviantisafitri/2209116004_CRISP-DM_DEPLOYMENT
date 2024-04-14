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

    
    # Visualisasi 1: Usia dan Konsumsi Alkohol
    plt.figure(figsize=(8, 6))
    sns.lineplot(data=df, x='age', y='Walc', marker='o', color='blue')
    plt.title('Hubungan antara Usia dan Konsumsi Alkohol')
    plt.xlabel('Usia')
    plt.ylabel('Konsumsi Alkohol')
    plt.grid(True)
    plt.show()
    st.pyplot()

    st.markdown("""

            **Interpretasi:**
            Terdapat hubungan yang jelas antara usia dan tingkat konsumsi alkohol di kalangan siswa. Grafik garis menunjukkan bahwa semakin tua siswa, semakin tinggi kemungkinan mereka untuk mengonsumsi alkohol secara reguler atau dalam jumlah yang lebih besar.

            **Insight:**
            Siswa yang lebih tua cenderung memiliki tingkat konsumsi alkohol yang lebih tinggi daripada siswa yang lebih muda. Artinya perlu perhatian khusus terhadap siswa yang berusia lebih tua dalam upaya pencegahan konsumsi alkohol di kalangan pelajar.

            **Actionable Insight:**
            Program pendidikan harus dirancang dengan mempertimbangkan perbedaan dalam konsumsi alkohol berdasarkan usia. Fokuskan upaya pencegahan pada siswa yang lebih tua dan berikan informasi yang sesuai dengan tingkat usia mereka.
            """)

    # Visualisasi 2: Perbedaan Gender dalam Konsumsi Alkohol
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x='sex', y='Walc', palette='Set2')
    plt.title('Perbedaan Gender dalam Konsumsi Alkohol')
    plt.xlabel('Gender')
    plt.ylabel('Konsumsi Alkohol')
    plt.show()
    st.pyplot()

    st.markdown("""

            **Interpretasi:**
            Data menunjukkan adanya perbedaan dalam pola konsumsi alkohol antara siswa laki-laki dan perempuan. Grafik menunjukkan bahwa konsumsi alkohol cenderung lebih tinggi di kalangan siswa laki-laki.

            **Insight:**
            Konsumsi alkohol cenderung lebih tinggi di kalangan siswa laki-laki. Hal tersebut mungkin disebabkan oleh faktor sosial, budaya, atau tekanan teman sebaya yang berbeda antara siswa laki-laki dan perempuan.

            **Actionable Insight:**
            Perlu untuk mengembangkan strategi pencegahan yang spesifik untuk menangani konsumsi alkohol di kalangan siswa laki-laki. Hal ini dapat mencakup program-program yang memahami dan menanggapi faktor-faktor sosial dan budaya yang mempengaruhi keputusan siswa dalam mengonsumsi alkohol.
            """)


    # Visualisasi 3: Tingkat Stres dan Konsumsi Alkohol
    plt.figure(figsize=(8, 6))
    sns.barplot(data=df, x='failures', y='Walc', palette='Set2')
    plt.title('Hubungan antara Tingkat Kegagalan dan Konsumsi Alkohol')
    plt.xlabel('Tingkat Kegagalan')
    plt.ylabel('Konsumsi Alkohol')
    plt.show()
    st.pyplot()

    st.markdown("""

            **Interpretasi:**
            Kegagalan dapat menjadi faktor risiko yang signifikan dalam mempengaruhi perilaku konsumsi alkohol di kalangan siswa. Siswa yang mengalami kegagalan mungkin menggunakan alkohol sebagai cara untuk mengatasi atau melarikan diri dari tekanan.

            **Insight:**
            Data menunjukkan bahwa siswa yang mengalami tingkat kegagalan yang tinggi cenderung memiliki kecenderungan yang lebih tinggi untuk mengonsumsi alkohol.

            **Actionable Insight:**
            Memperkuat program dan layanan penanganan kegagalan di sekolah. Hal ini dapat mencakup peningkatan akses ke konseling, dukungan emosional, dan pengembangan keterampilan penanganan kegagalan yang tepat.
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
