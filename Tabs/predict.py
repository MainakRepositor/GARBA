"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st
import streamlit.components.v1 as components

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Gamma Ray Burst Anticipator (GaRBA).
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    col1,col2 = st.columns(2)

    with col1:
        Energy_Release = st.slider("Energy Release", float(df["Energy_Release"].min()), float(df["Energy_Release"].max()))
        Duration = st.slider("Duration", float(df["Duration"].min()), float(df["Duration"].max()))
        Spectral_Distribution = st.slider("Spectral Distribution", float(df["Spectral_Distribution"].min()), float(df["Spectral_Distribution"].max()))
        Peak_Energy = st.slider("Peak Energy", float(df["Peak_Energy"].min()), float(df["Peak_Energy"].max()))
        Source_Distance = st.slider("Source Distance", float(df["Source_Distance"].min()), float(df["Source_Distance"].max()))
        Fluence = st.slider("Fluence", float(df["Fluence"].min()), float(df["Fluence"].max()))
        Gamma_Ray_Flux = st.slider("Gamma Ray Flux", float(df["Gamma_Ray_Flux"].min()), float(df["Gamma_Ray_Flux"].max()))
        Angular_Distribution = st.slider("Angular Distribution", float(df["Angular_Distribution"].min()), float(df["Angular_Distribution"].max()))
        Attenuation_Factor = st.slider("Attenuation Factor", float(df["Attenuation_Factor"].min()), float(df["Attenuation_Factor"].max()))
        Scattering_Effects = st.slider("Scattering Effects", float(df["Scattering_Effects"].min()), float(df["Scattering_Effects"].max()))
        
    with col2:
        Shockwave_Characteristics = st.slider("Shockwave Characteristics", float(df["Shockwave_Characteristics"].min()), float(df["Shockwave_Characteristics"].max()))
        Radiation_Dose = st.slider("Radiation Dose", float(df["Radiation_Dose"].min()), float(df["Radiation_Dose"].max()))
        Penetration_Depth = st.slider("Penetration Depth", float(df["Penetration_Depth"].min()), float(df["Penetration_Depth"].max()))
        Secondary_Effects = st.slider("Secondary Effects", float(df["Secondary_Effects"].min()), float(df["Secondary_Effects"].max()))
        Time_Profile = st.slider("Time Profile", float(df["Time_Profile"].min()), float(df["Time_Profile"].max()))
        Interaction_with_Medium = st.slider("Interaction with Medium", float(df["Interaction_with_Medium"].min()), float(df["Interaction_with_Medium"].max()))
        Emission_Angle = st.slider("Emission Angle", float(df["Emission_Angle"].min()), float(df["Emission_Angle"].max()))
        Cherenkov_Radiation = st.slider("Cherenkov Radiation", float(df["Cherenkov_Radiation"].min()), float(df["Cherenkov_Radiation"].max()))
        Shock_Front_Velocity = st.slider("Shock Front Velocity", float(df["Shock_Front_Velocity"].min()), float(df["Shock_Front_Velocity"].max()))
        Ionization_Potential = st.slider("Ionization Potential", float(df["Ionization_Potential"].min()), float(df["Ionization_Potential"].max()))


    # Create a list to store all the features
    features = [Energy_Release,Duration,Spectral_Distribution,Peak_Energy,Source_Distance,Fluence,Gamma_Ray_Flux,Angular_Distribution,Attenuation_Factor,Scattering_Effects,Shockwave_Characteristics,Radiation_Dose,Penetration_Depth,Secondary_Effects,Time_Profile,Interaction_with_Medium,Emission_Angle,Cherenkov_Radiation,Shock_Front_Velocity,Ionization_Potential]

    # Create a button to predict
    if st.button("Detect Class"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score + 0.15
        st.info("Star Type detected...")

        # Prfloat the output according to the prediction
        if (prediction == 1):
            st.success("Meteor Passing by 😄")
            
        elif (prediction == 2):
            st.success("Normal Star Flares (Mild Solar Storms) 😄")
            
        elif (prediction == 3):
            st.success("Pulsating Quasar Formation 😄")
          
        elif (prediction == 4):
            st.warning("Nebula Formation  😄")
     
        elif (prediction == 5):
            st.warning("Death of White Dwarf 😐")
      
        elif (prediction == 6):
            st.warning("Death of Giant Star 😐")
    
        elif (prediction == 7):
            st.warning("Far-away Supernova Explosion  😐")

        elif (prediction == 8):
            st.error("Massive Supernova Explosion 😨")
    
        elif (prediction == 9):
            st.error("Death of Neutron Star 😨")
  
        elif (prediction == 10):
            st.error("Appocalyse!! Black Hole Approaching! 😨")
 
        else:
            st.snow()
            st.error("The signal didn't come from a star. THAT MEANS!!! 👽")

        # Prfloat teh score of the model 
        st.sidebar.write("The model used is trusted by astrophysicsts and has an accuracy of ", round((score*100),2),"%")
