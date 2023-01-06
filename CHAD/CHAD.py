
# In[1]:


import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import time 
import requests
from streamlit_lottie import st_lottie


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('h_trained_model.sav','rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('CHAD: A Comprehensive Health Analysis Desk',
                          
                          ['HOME',
                            'Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['house','activity','heart','person'],
                          default_index=0) 
    
    
# Diabetes Prediction Page
if (selected == 'HOME'):
    st.title('WELCOME TO CHAD !!')
    def load_lottieurl(url: str):
         r = requests.get(url)
         if r.status_code != 200:
            return None
         return r.json()


    lottie_url_hello = "https://assets6.lottiefiles.com/packages/lf20_l13zwx3i.json"
    lottie_hello = load_lottieurl(lottie_url_hello)
    st_lottie(lottie_hello, key="hello",height=450)
    st.header('What is CHAD ? ')
    st.write('''CHAD or Comprehensive Health Analysis Desk is a professional diseaase detection system that tells or diagonises the user of a specific disease.
    It is beneficial WebApp made using various ML algorithms combined at one single place to produce a desired output. It is user friendly and has a beautiful interface that adheres with the need of the user. ''')
    lottie_url_hello1 = "https://assets1.lottiefiles.com/packages/lf20_5LVVIi.json"
    lottie_hello1 = load_lottieurl(lottie_url_hello1)
    st_lottie(lottie_hello1, key="hello1",height=450)
    st.header('WHY CHAD ? ')
    st.write('''Healthcare is probably the most engaging and emerging sector in the modern world. Therefore Healthcare Solution and Management is a must. These days due to a huge influx of people in Hospitals, the waiting time has increased also if an application can be developed which can give an analysis of health status then it would be very useful as people can check themselves without waiting for long queues in Hospitals or waiting for too long for the reports to come.
''')
    lottie_url_hello2 = "https://assets6.lottiefiles.com/packages/lf20_a3ntzciy.json"
    lottie_hello2 = load_lottieurl(lottie_url_hello2)
    st_lottie(lottie_hello2, key="hello2",height=450)
    st.markdown('You can toggle the Navbar using side button and check out different prediction models as per your choice. ')
    st.subheader("Enjoy this beautiful as much as I enjoyed making this application while spending endless nights for a good cause. Hats Off !! RISHAV MISHRA")
    

if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Early Stage Diabetes Prediction using ML')
    def load_lottieurl(url: str):
         r = requests.get(url)
         if r.status_code != 200:
            return None
         return r.json()


    lottie_url_hello = "https://assets9.lottiefiles.com/packages/lf20_tbjuenb2.json"
    lottie_hello = load_lottieurl(lottie_url_hello)
    st_lottie(lottie_hello, key="hello")
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        st.balloons()
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'YOU HAVE HIGH CHANCES OF DIABETES.'
        else:
          diab_diagnosis = 'YOU HAVE LOW DIABETES CHANCES.'
        
        
    st.success(diab_diagnosis)
    if diab_diagnosis == 'YOU HAVE LOW DIABETES CHANCES.':
        lottie_url_hello1 = "https://assets1.lottiefiles.com/private_files/lf30_kcsjht6h.json"
        lottie_hello1 = load_lottieurl(lottie_url_hello1)
        st_lottie(lottie_hello1, key="hello1",width=700,height=200)
        st.text('''                       You should take good and Healthy food to maintain this condition Go for Checkup in every 
        3-4 months and do excercises.
        You should do the following to maintain yourself:
        1. Drink Lots of Water.
        2. Exercise Regularly.
        3. Have Sprouts for Breakfast
        4. Do Yoga ''')
        st.write("Here are some really **good recommendations**:")
    elif diab_diagnosis == 'YOU HAVE HIGH CHANCES OF DIABETES.':
        lottie_url_hello2 = "https://assets3.lottiefiles.com/packages/lf20_j6fywzxe.json"
        lottie_hello2 = load_lottieurl(lottie_url_hello2)
        st_lottie(lottie_hello2, key="hello2",width=700,height=200)
        st.text('''                         You need to  see a doctor as your condition may go critical.
         Avoid Fast Food. Do regular ExercisE.
         **Here are some worthy advise**: 
         1. EAT HEALTHY.
         2. AVOID FAST FOOD.
         3. DO REGULAR CHECKUPS.
         4. WATCH YOUR ALCOHOL.
         5. MANAGE STRESS. 
         6. STOP SMOKING.
         7. Keep your blood pressure and cholesterol under control.
         8. Take Medications Seriously.''')
    else:
        st.text("Happy to serve !!! Thank You For Using this web app.")




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Early Stage Heart Disease Prediction using ML')
    def load_lottieurl(url: str):
         r = requests.get(url)
         if r.status_code != 200:
            return None
         return r.json()


    lottie_url_hello3 = "https://assets6.lottiefiles.com/packages/lf20_txlsmlkc.json"
    lottie_hello3 = load_lottieurl(lottie_url_hello3)
    st_lottie(lottie_hello3, key="hello3",height=400)
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        st.balloons()
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'YOU HAVE HIGH CHANCES OF HAVING HEART DISEASE.'
        else:
          heart_diagnosis = 'YOU HAVE LOW CHANCES OF HAVING ANY HEART DISEASE.'
        
    st.success(heart_diagnosis)
    if heart_diagnosis == 'YOU HAVE LOW CHANCES OF HAVING ANY HEART DISEASE.':
        lottie_url_hello1 = "https://assets1.lottiefiles.com/private_files/lf30_kcsjht6h.json"
        lottie_hello1 = load_lottieurl(lottie_url_hello1)
        st_lottie(lottie_hello1, key="hello1",width=700,height=200)
        st.text('''                       You should take good and Healthy food to maintain this condition Go for Checkup in every 
        3-4 months and do excercises.
        You should do the following to maintain yourself:
        1. Drink Lots of Water.
        2. Exercise Regularly.
        3. Have Sprouts for Breakfast
        4. Do Yoga 
        ''')
        st.write("These are some really **good recommendations**:")
    elif heart_diagnosis == 'YOU HAVE HIGH CHANCES OF HAVING HEART DISEASE.':
        lottie_url_hello2 = "https://assets3.lottiefiles.com/packages/lf20_j6fywzxe.json"
        lottie_hello2 = load_lottieurl(lottie_url_hello2)
        st_lottie(lottie_hello2, key="hello2",width=700,height=200)
        st.text('''                         You need to  see a doctor as your condition may go critical.
         Avoid Fast Food. Do regular ExercisE.
         **Here are some worthy advise**: 
        1. Eat healthy.
        2. Get active.
        3. Stay at a healthy weight.
        4. Quit smoking and stay away from secondhand smoke.
        5. Control your cholesterol and blood pressure.
        6. Drink alcohol only in moderation.
        7. Manage stress.
        8. Take Medications Seriously.''')
    else:
        st.text("Happy to serve !!! Thank You For Using this web app.")
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    def load_lottieurl(url: str):
         r = requests.get(url)
         if r.status_code != 200:
            return None
         return r.json()


    lottie_url_hello3 = "https://assets5.lottiefiles.com/packages/lf20_iarc855d.json"
    lottie_hello3 = load_lottieurl(lottie_url_hello3)
    st_lottie(lottie_hello3, key="hello3",height=400)
    
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        st.balloons()
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "YOU HAAVE HIGH PARKINSON CHANCES."
        else:
          parkinsons_diagnosis = "YOU HAVE LOW CHANCES OF HAVING PARKINSON'S DISEASE."
        
    st.success(parkinsons_diagnosis)
    if parkinsons_diagnosis  == "YOU HAVE LOW CHANCES OF HAVING PARKINSON'S DISEASE.":
        lottie_url_hello1 = "https://assets1.lottiefiles.com/private_files/lf30_kcsjht6h.json"
        lottie_hello1 = load_lottieurl(lottie_url_hello1)
        st_lottie(lottie_hello1, key="hello1",width=700,height=200)
        st.text('''                       You should take good and Healthy food to maintain this condition Go for Checkup in every 
        3-4 months and do excercises.
        You should do the following to maintain yourself:
        1. Drink Lots of Water.
        2. Exercise Regularly.
        3. Have Sprouts for Breakfast
        4. Do Yoga ''')
        st.write("Here are some really **good recommendations**:")
    elif parkinsons_diagnosis  == "YOU HAAVE HIGH PARKINSON CHANCES.":
        lottie_url_hello2 = "https://assets3.lottiefiles.com/packages/lf20_j6fywzxe.json"
        lottie_hello2 = load_lottieurl(lottie_url_hello2)
        st_lottie(lottie_hello2, key="hello2",width=700,height=200)
        st.text('''                         You need to  see a doctor as your condition may go critical.
         Avoid Fast Food. Do regular ExercisE.
         **Here are some worthy advise**: 
         1. More flexibility
         2. Do Better balance
         3. Take Less anxiety and depression
         4. Have Improved coordination
         5. Add muscle strength
Talk to your doctor before you start any kind of physical activity. They may
recommend that you team up with a physical therapist to help you find your 
best fitness fit. You may want to try:

1. Walking
2. Swimming or water aerobics
3. Gardening
4. Stretching
5. Dancing
6. Tai chi''')
    else:
        st.text("Happy to serve !!! Thank You For Using this web app.")


# In[ ]:




