import streamlit as st
import pickle
import pandas as pd
import imblearn

def run():

    with open('best_lr_model_smote.pkl', 'rb') as file_1:
        model = pickle.load(file_1)

    with st.form('form_input'):
        st.subheader('Personal Info', divider='orange')
        gender = st.selectbox('Gender', ('Male', 'Female'), index=0)
        international = st.radio('International Student?', ('True', 'False'))
        race = st.selectbox('Race', ('Asian', 'Black', 'Hispanic', 'White', 'Other', 'International Student'))
        st.markdown('---')

        st.subheader('History', divider='orange')
        gpa = st.slider('GPA', 0.0, 4.0, 3.0)
        gmat = st.slider('GMAT', 200, 800, 600)
        work_exp = st.number_input('Work Experience', min_value=0, value=0)
        work_industry = st.selectbox('Work Industry Experience', ('Financial Services', 'Investment Management', 'Technology', 'Consulting',
        'Nonprofit/Gov', 'PE/VC', 'Health Care', 'Investment Banking', 'Other'), index=0)
        st.markdown('---')

        major = st.selectbox('Major', ('Business', 'Humanities', 'STEM'), index=0)
        st.markdown('---')

        data_inf ={
            'gender': gender, 
            'international': international, 
            'gpa': gpa, 
            'major': major,
            'race': race,
            'gmat': gmat,
            'work_exp': work_exp,
            'work_industry	': work_industry
        }
        data_inf = pd.DataFrame([data_inf])
        st.dataframe(data_inf)

        submitted = st.form_submit_button('Predict !')

    st.subheader('Admission Status:', divider='orange')
    if submitted:
        # prediksi status penerimaan
        y_pred_inf = model.predict(data_inf)
        if y_pred_inf == 1:
            st.write('## Admission Denied or in Waitlist')
        else:
            st.write('## Admitted')
    
    