import streamlit as st
import pandas as pd
import joblib
model=joblib.load("KNN_heart.pkl")
scaler=joblib.load('scaler.pkl')
excepted_columns=joblib.load('columns.pkl')

st.title("❤️ Heart Disease Prediction By Shoukat Ali ❤️")
st.markdown("Provide The Following Details")
age=st.slider("Age",18,100,40)
sex=st.selectbox("SEX",['M',"F"])
chest_pain=st.selectbox("Chest Pain Type",["ATA","NAP","TA","ASY"])
Resting_bp=st.number_input("Resting Blood Pressure (mm Hg)",80,200,120)
Cholesterol=st.number_input("Cholesterol (mg/dL)",100,600,200)
FastingBS=st.selectbox("Fasting Blood Sugar > 120 mg/dL",[0,1])
RestingECG=st.selectbox("Resting ECG",["Normal","ST","LVH"])
Max_HR=st.slider("Max Heart Rate",60,220,150)
excercise_angina=st.selectbox("Exercise_Induced Angina",['Y','N'])
Old_Peak=st.slider("Oldpeak (ST Depression)",0.0,6.0,1.0)
St_slope=st.selectbox("ST Slope",["Up","Flat","Down"])


if st.button("Predict"):
    raw_input = {
        'Age': age,
        'RestingBP': Resting_bp,
        'Cholesterol': Cholesterol,
        'FastingBS': FastingBS,
        'MaxHR': Max_HR,
        'Oldpeak': Old_Peak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + RestingECG: 1,
        'ExerciseAngina_' + excercise_angina: 1,
        'ST_Slope_' + St_slope: 1
    }
    input_df=pd.DataFrame([raw_input])
    for col in excepted_columns:
        if col not in input_df.columns:
            input_df[col]=0

    input_df=input_df[excepted_columns]

    scaled_input=scaler.transform(input_df)

    prediction=model.predict(scaled_input)[0]
    if prediction ==1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")