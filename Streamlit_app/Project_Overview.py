### import libraries
import streamlit as st

#######################################################################################################################################
### PAGE CONFIG
st.set_page_config(page_title='The Butterfly Effect', page_icon='🦋', layout="wide")
st.write('A multivariate Time Series model aimed to predict the Butterfly Population Evolution amid climate change')
st.title("The Butterfly Effect")
st.divider()

#######################################################################################################################################
### SIDE BAR
# Sources
st.sidebar.markdown('**Data Sources**')
st.sidebar.caption('Butterfly sightings data: [UKBMS](https://registry.nbnatlas.org/public/show/dr1206)')
st.sidebar.caption('Weather data: [Met Office](https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data)')
st.sidebar.caption('Air Quality data: [London Air](https://www.londonair.org.uk/LondonAir/Default.aspx)')
st.sidebar.write('---')
st.sidebar.caption('More info about the [Time Series Analysis](https://github.com/chloecousin/Butterflies)')
st.sidebar.caption('Developed by [Chloe Cousin](https://www.linkedin.com/in/chloe-m-cousin/)')


#######################################################################################################################################
### Main page

## Project Overview
st.header("Purpose of the analysis")
st.markdown("""
            The World Economic Forum states that Biodiversity is _'critically important'_ for 5 reasons, as it: ensures health and food security, helps 
            fight disease, benefits business, provides livelihood, protects us. The butterfly population has been widely studied and are thought 
            to be one of the best indicators of a healthy environment: as they have short life cycles, they have quick responses to environmental changes. 
            """)
st.info("""
        __The purpose of this analysis is to predict the evolution of the butterfly population in the context of climate change and see - if and how - 
        external factors affect them__.
        """)
st.markdown("""
            To do so, I am conducting a Time series analysis with different approaches:
            - __Preprocessing steps__ (varies with each model, but can include): scaling, stationarity, Grange causality test, Cointegration test...
            - __Models__: univariates (SARIMA, Prophet) and multivariates (VAR, Prophet)

            The data used in this project comes from the [UKBMS](https://ukbms.org/index.php/), one of the longest running insect monitoring schemes in 
            the world. I explore 6M butterfly sightings recorded in the UK over the past 20 years. Here is how I approached the dataset to find the 
            model presented in the 🦋 Model App page:
            """)

## Key Findings
st.header("Key Findings")
st.subheader("1. __EDA__ (most important findings)")
col1, col2 = st.columns(2, gap='large')
with col1:
    st.image('Streamlit_app/pages/1.Sightings_Map.png')
    st.markdown("Most sightings located in England")
with col2:
    st.image('Streamlit_app/pages/2.Sightings_Timeline.png')
    st.markdown("""
            The sightings have a trend upward, more and more sightings have been recorded over the years, 
            BUT this is not an indicator of how the butterfly population is faring: this could mean that there are more surveys conducted to count 
            the butterflies or that there are indeed more butterflies, or both!
            """)
st.markdown('')

st.subheader("2. __Data Preprocessing__ (most important steps)")

col3, col4 = st.columns(2, gap='large')
with col3:
    st.markdown("*Indicator for the butterfly population evolution*")
    st.image("Streamlit_app/pages/3.Indicator.png")
    st.markdown("""
            To get such indicator I found a way to know how many surveys had been 
            conducted each month (unique pairs of sighting date and sighting number Ordnance Survey grid reference, aka date and location) 
            and created a new variable: number of butterfly seen per survey (average for each month)
            """)
with col4:  
    st.markdown("*Location*")
    st.image("Streamlit_app/pages/4.Focus_London.png")
    st.markdown("""
            Focus on London, using Latitude and Longitude data. Here, I was not able to extract City information using 
            reverse geocoding (for most locations the city was not extracted). 
            So I went for a slightly different approach: I found the North/West/South/East 
            London borders coordinates and selected all Survey sites within that rectangle. Given that the external factors I am going to work with do not stop 
            at the city delimitation (temperatures, air quality...), this will have minimal impact on the analysis. The selected sites are found within the 
            red rectangle above.
                """)
st.markdown('')

col5, col6 = st.columns(2, gap='large')
with col5:
    st.markdown("*Trend*")
    st.image("Streamlit_app/pages/5.TimeSeriesDecomposition.png")
    st.markdown("""
                Focus on trend only (not the seasonality / residuals), to make sure I am not capturing for example high temperatures during the 
                summer as predictive of high number of butterflies
                """)
with col6:
    st.markdown("*Lags*")
    st.image("Streamlit_app/pages/6.Lags.png")
    st.markdown("""
                Focus on external factors lagged value - for example, if the temperatures were really high one summer, are the butterflies the year after suffering from this?
                """)
st.markdown('')


st.subheader("3. __Model iterations__")
col7, col8 = st.columns(2, gap='large')
with col7:
    st.markdown("*Univariate models - Best one below:*")
    st.image("Streamlit_app/pages/7.UnivariateBestModel.png")
    st.markdown("Failed to pick up variations in the data")

with col8:
    st.markdown("*Multivariate models - Best one below:*")
    st.image("Streamlit_app/pages/8.MultivariateBestModel.png")
    st.markdown("""
                The best one showed excellent train MAPE score and very good test MAPE score, and was able to pick up the data variations: 
                a Prophet multivariate model. It retained the following external variables: temperatures / rain / O3 / SO2 / air frost / sun as the most 
                predictive. Except for the last two, all of them have a negative impact on the butterfly population.
                """)
st.markdown('')

st.subheader("4.  __Best model evaluation__")
st.markdown("The model is quite good to pick up the general trend and variations but will likely fail to predict the exact next values.")
st.markdown('')

st.subheader("5.  __Forecasts__")
st.markdown("""
            After several simulations of external factors variations (aka if the temperatures increase by 10%...) we can see that the butterfly 
            population will suffer from poor external conditions. Simulations of external factors variations can be done on the 🦋 Model App.
            """)