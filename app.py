import pickle
import streamlit as st
import numpy as np 
 

pickle_in = open('adaboost.pkl', 'rb') 
classifier = pickle.load(pickle_in)
#st.header("Insurance Premium Prediction Using Machine Learning")

def prediction(Age, Gender, BMI, Children, Smoker, Region):   
 
    # Pre-processing user input    
    if Gender == "Female":
        Gender = 0
    else:
        Gender = 1
 
    if Smoker == "Yes":
        Smoker = 1
    else:
        Smoker = 0
 
    if Region == "North-West":
        Region = 0
    elif Region == "South-East":
        Region = 1
    elif Region =="South-West":
        Region = 2
    else:
        Region = 3
 
    # Making predictions 
    prediction = classifier.predict([[Age, Gender, BMI, Children, Smoker, Region]])
     
    #if prediction == 0:
     #   pred = 'Rejected'
    #else:
     #   pred = 'Approved'
    return prediction

def main():
    st.markdown("<h1 style='text-align: center; color: White;background-color:#e84343'>Insurance Premium Prediction Using Machine Learning</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: Black;'>Created By - Pooja J and Mahima A</h3>", unsafe_allow_html=True)

    Age = st.slider("Enter Your Current Age", 0, 100)   
    Gender = st.selectbox('Select Your Gender',("Male","Female"))
    BMI = st.number_input("What Is Your Updated BMI Value?",step=0.5)  
    Children = st.number_input("Enter The Number of Children You Have",min_value=1, max_value=10) 
    
    Smoker = st.selectbox('Do You Smoke?',("Yes","No")) 

    Region = st.selectbox('Select Your Region',("North-West","North-East","South-West","South-East"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Age, Gender, BMI, Children, Smoker, Region) 
        results = np.round(result,2)
        st.success('The Predicted Insurance Amount Is ${}'.format(results))
       # print(LoanAmount)
     
if __name__=='__main__': 
    main()