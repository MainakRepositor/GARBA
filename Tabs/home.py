"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Ga-RBA: Gamma Ray Burst Anticipator")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Calculating the intensity and effects of a gamma ray Burst involves consideration of various critical parameters. These include the energy output of the gamma ray burst, measured in ergs or joules; the distance from the source to the point of impact, determining the energy flux received; spectral characteristics such as peak energy and duration of the burst; the angle of emission affecting the observed intensity; the environment's density, magnetic field strength, and composition impacting gamma ray attenuation; the isotropic equivalent energy to gauge its true power; the burst's duration, crucial in understanding its impact and the potential for afterglows; the redshift providing information about the distance and age of the source; the luminosity distance, aiding in understanding its true brightness; the beaming factor, considering the burst's directional emission; the gamma-ray fluence, providing the total energy received; the peak flux and its significance in determining the burst's intensity; the variability and temporal features offering insights into the burst's behavior; the polarization, if detected, revealing the emission's geometry; the host galaxy's characteristics and the burst's location within it; the absorption and scattering of gamma rays en route to Earth; the high-energy follow-up observations across different wavelengths; the afterglow properties in various wavelengths, aiding in understanding the burst's environment; and the associated multi-messenger counterparts, if any, like neutrinos or gravitational waves, providing complementary information about the event. These parameters collectively contribute to our comprehensive understanding of gamma ray bursts and their implications in astrophysics.
        </p>
    """, unsafe_allow_html=True)