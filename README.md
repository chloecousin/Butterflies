# The Butterfly Effect

## Project Overview
The World Economic Forum states that Biodiversity is _'critically important'_ for 5 reasons, as it: ensures health and food security, helps fight disease, benefits business, provides livelihood, protects us.

The butterfly population has been widely studied and is thought to be one of the best indicators of a healthy environment: as they have short life cycles, they have quick responses to environmental changes. The purpose of this analysis is to predict the evolution of the butterfly population in the context of climate change and see - if and how - external factors affect them. To do so, I am conducting a Time series analysis with different approaches:
- __Preprocessing steps__ (varies with each model, but can include): scaling, stationarity, Grange causality test, Cointegration test...
- __Models__: univariates (SARIMA, Prophet) and multivariates (VAR, Prophet)

## Key Findings
The model can be tested on the [Streamlit App](https://butterflies.streamlit.app/)

1. __EDA__(most important finding):
   - Most sightings located in England
   - The sightings have a trend upward, more and more sightings have been recorded over the years, BUT this is not an indicator of how the butterfly population is faring. 
2. __Data Preprocessing__:
   - *Indicator for the butterfly population evolution*: To get such indicator I found a way to know how many surveys had been conducted each month (unique pairs of sighting date and sighting number Ordnance Survey grid reference, aka date and location) and created a new variable: number of butterfly seen per survey (average for each month)
   - *Location*: focus on one location, London
   - *Trend*: focus on trend only (not the seasonality / residuals), to make sure I am not capturing for example high temperatures during the summer as predictive of high number of butterflies
   - *Lags*: focus on external factors lagged value - for example, if the temperatures were really high one summer, are the butterflies the year after suffering from this?
3. __Model iterations__:
    - *Univariate models*: failed to pick up variations in the data 
    - *Multivariate models*: one of them showed excellent train MAPE score and very good test MAPE score, and was able to pick up the data variations: a Prophet multivariate model. It retained the following external variables: temperatures / rain / O3 / SO2 / air frost / sun as the most predictive. Except for the last two, all of them have a negative impact on the butterfly population.
4.  __Best model evaluation__: the model is quite good to pick up the general trend and variations but will likely fail to predict the exact next values
5.  __Forecasts__: after several simulations of external factors variations (aka if the temperatures increase by 10%...) we can see that the butterfly population will suffer from poor external conditions. More simulations can be done on the [Streamlit App](https://butterflies.streamlit.app/).

## Datasets
### 1- __United Kingdom Butterfly Monitoring Scheme (UKBMS)__

'_One of the longest running insect monitoring schemes in the world. The scheme began in 1976 and now records data on over 2,000 sites per year; incorporating butterfly transects, the Wider Countryside Butterfly Survey (WCBS), and timed-counts. The resulting UKBMS dataset is one of the most important resources for understanding changes in insect populations_'. For further information, see the [UKBMS website](https://ukbms.org/)

The dataset in this project includes data from 2001 to 2020 (around 6M sightings) 

Source: https://registry.nbnatlas.org/public/showDataResource/dr1206 

Licence: [Open Government Licence 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)

### 2- __LepTraits v1.0__

A trait dataset for Lepidoptera (=order of winged insects that includes butterflies and moths). Originally created by:
Shirey, V., Larsen, E., Doherty, A., Kim, C.A., Al-Sulaiman, F.T., Hinolan, J.D., Itliong, M.G.A., Naive, M.A.K., Ku, M., Belitz, M., Jeschke, G., Barve, V., Lamas, G., Kawahara, A.Y., Guralnick, R., Pierce, N.E., Lohman, D.J., and Ries, L. 2022. For further information, see this [Nature article](https://www.nature.com/articles/s41597-022-01473-5#Sec7)

Source: https://github.com/RiesLabGU/LepTraits/tree/main

Licence: [Creative Commons CC BY 4.0](http://creativecommons.org/licenses/by/4.0/)


### 3- __Red List of Butterflies in the UK__

List of butterflies from least vulnerable to regionally extinct species in the UK

Source: https://butterfly-conservation.org/red-list-of-butterflies-in-great-britain 


### 4- __London weather historic data__

Monthly weather information from Heathrow (London Airport)

Source: https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data 


### 5- __London air quality historic data__

Hourly air quality information from Marylebone road (center London) - station with the most data points in London over 2001-2020

Source: https://www.londonair.org.uk/LondonAir/Default.aspx

Licence: [For informational and educational purposes](https://www.londonair.org.uk/london/asp/copyright.asp)