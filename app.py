import streamlit as st
import joblib
clf=joblib.load('loan.joblib')
st.title('LOAN APP RCE')
g=st.number_input('Enter Gender 0:Male 1:Female')
m=st.number_input('Enter Martial Status 0:No 1:Yes')
ai=st.number_input('Enter Applicant Income in thousands')
la=st.numder_input('Enter Loan amount in thousands')
if st.button('PREDICT'):
    prediction=clf.predict([[g,m,ai,la]])
    if prediction=='y':
        st.text('Loan is Approved')
        else:
            st.text('Loan is Rejected')
