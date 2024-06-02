import pickle
import streamlit as st

# Membaca Model
HepatitisC_model = pickle.load(open('viemganc_SVM.sav', 'rb'))

# Judul Web
st.title('Chuẩn đoán viêm gan C')

col1, col2, col3 = st.columns(3)
with col1:
    Age = st.number_input('Nhập tuổi của bạn.')
with col2:
    Gender = st.number_input('Nhập giới tính của bạn.')
with col3:
    st.caption('''
        Giới tính : \n
        Nam   = 0 \n
        Nữ = 1 \n
        ''')
with col1:
    ALB = st.number_input('Nhập giá trị ALB')
with col2:
    ALP = st.number_input('Nhập giá trị ALP')
with col1:
    ALT = st.number_input('Nhập giá trị ALT')
with col2:
    AST = st.number_input('Nhập giá trị AST')
with col1:
    BIL = st.number_input('Nhập giá trị BIL')
with col2:
    CHE = st.number_input('Nhập giá trị CHE')
with col1:
    CHOL = st.number_input('Nhập giá trị CHOL')
with col2:
    CREA = st.number_input('Nhập giá trị CREA')
with col1:
    GGT = st.number_input('Nhập giá trị GGT')
with col2:
    PROT = st.number_input('Nhập giá trị PROT')

# Code untuk pediksi
hepa_diagnosis = ''

# Membuat tombol untuk prediksi
if st.button('Dự đoán'):
    hepa_prediction = HepatitisC_model.predict(
        [[Age, Gender, ALB, ALP, ALT, AST, BIL, CHE, CHOL, CREA, GGT, PROT]])

    if (hepa_prediction[0] == 1):
        hepa_diagnosis = 'Bệnh nhân được chẩn đoán bị viêm gan C'
    else:
        hepa_diagnosis = 'Bệnh nhân được chẩn đoán không bị viêm gan C'

    st.success(hepa_diagnosis)
