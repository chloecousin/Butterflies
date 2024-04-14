# The Butterfly Effect

## Project Overview
The World Economic Forum states that Biodiversity is _'critically important'_ for 5 reasons, as it: ensures health and food security, helps fight disease, benefits business, provides livelihood, protects us

The butterfly population has been widely studied across the world over the last decades. The butterflies are indeed thought to be one of the best indicators of a healthy environment. As they have short life cycles, they have quick responses to environmental changes. The purpose of this analysis is to :
- understand how the butterflies population varies and
- predict its evolution over the next years in the context of climate change

To do so, we are conducting here a Time series analysis and trying different models:
- First with univariate models (SARIMA, Prophet)
- Then, with multivariate models (VAR, Prophet) and using external factors to optimize the model accuracy

## Key Findings
The model can be tested at: https://butterflies.streamlit.app/ 

In the last notebook, I try to predict the butterfly population evolution, with the following steps and findings:

1. __Data Preprocessing__:
   - *Indicator for the butterfly population evolution*: the dataset have sightings information and we can deduce the number of surveys when the butterflies were counted. I chose butterfly per survey as the indicator of the butterfly population
   - *Location*: focus on one location, London
   - *Trend*: focus on trend only (not the seasonality / residuals), to make sure I am not capturing for example high temperatures during the summer as predictive of high number of butterflies
   - *Lags*: focus on external factors lagged value - for example, if the temperatures were really high one summer, are the butterflies the year after suffering from this?
3. __Model iterations__:
    - *Univariate models*: failed to pick up variations in the data even if the Prophet univariate showed somewhat good MAPE results
    - *Multivariate models*: with several combinations of lags and variables selection. The best model retained the following external variables: temperatures / rain / O3 / SO2 / air frost / sun. Except for the last two, all of them have a negative impact on the butterfly population.
4.  __Best model evaluation__: the model is quite good to pick up the general trend and variations but will likely fail to predict the exact next values
5.  __Forecasts__: after several simulations of external factors variations (aka if the temperatures increase by 10%...) we can see that the butterfly population will suffer from poor external conditions. However, a good news from the analysis is that the general trend over the past years is upward for the butterflies. Even if temperatures and air quality impact their numbers, their trend remains upward, much likely due to conservation efforts or other context which we do not have the data for here. More simulations can be done on the Streamlit app: https://butterflies.streamlit.app/ 

## Datasets
### 1- __United Kingdom Butterfly Monitoring Scheme (UKBMS)__

'_One of the longest running insect monitoring schemes in the world. The scheme began in 1976 and now records data on over 2,000 sites per year; incorporating butterfly transects, the Wider Countryside Butterfly Survey (WCBS), and timed-counts. The resulting UKBMS dataset is one of the most important resources for understanding changes in insect populations_'. For further information, see: https://ukbms.org/

The dataset in this project includes data from 2001 to 2020 (around 6M sightings) 

Source: https://registry.nbnatlas.org/public/showDataResource/dr1206 

Licence: Open Government Licence 3.0, https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/ 

Dictionnary:
- `Occurrence ID`: An identifier for the Occurrence
- `Scientific name`: The full scientific name, with authorship and date information if known
- `Common name`: A common or vernacular name
- `Start date`: The date-time during which a Event occurred. For occurrences, this is the date-time when the Event was recorded
- `Start date day`: The day the event occurred in
- `Start date month`: The ordinal month the event occurred in
- `Start date year`: The year the event occurred in
- `OSGR`: Ordnance Survey grid reference as supplied with the raw record
- `Latitude (WGS84)`: Processed decimal latitude in WGS84 datum. Calculated from grid reference if not supplied
- `Longitude (WGS84)`: Processed decimal longitude in WGS84 datum. Calculated from grid reference if not supplied
- `Family`: The full scientific name of the family in which the Taxon is classified
- `Genus`: The full scientific name of the genus in which the Taxon is classified
- `OSGR 100km `: The processed 100km OS grid reference
- `OSGR 10km `: The processed 10km OS grid reference
- `OSGR 2km `: The processed 2km OS grid reference
- `OSGR 1km `: The processed 1km OS grid reference
- `State/Province`: UK country


### 2- __LepTraits v1.0__

A trait dataset for Lepidoptera (=order of winged insects that includes butterflies and moths). Originally created by:
Shirey, V., Larsen, E., Doherty, A., Kim, C.A., Al-Sulaiman, F.T., Hinolan, J.D., Itliong, M.G.A., Naive, M.A.K., Ku, M., Belitz, M., Jeschke, G., Barve, V., Lamas, G., Kawahara, A.Y., Guralnick, R., Pierce, N.E., Lohman, D.J., and Ries, L. 2022. For further information, see https://www.nature.com/articles/s41597-022-01473-5#Sec7

Source: https://github.com/RiesLabGU/LepTraits/tree/main

Licence: http://creativecommons.org/licenses/by/4.0/ 

Dictionnary (columns kept in the project): 
- `Species`: The scientific name of the species account
- `verbatimSpecies`: The given (from the original resource) name of the species account
- `WS_L_Fem`: The lowest measurement reported for female wingspan in centimeters
- `WS_U_Fem`: The highest (or sole) measurement reported for female wingspan in centimeters
- `WS_L_Mal`: The lowest measurement reported for male wingspan in centimeters
- `WS_U_Mal`: The highest (or sole) measurement reported for male wingspan in centimeters
- `Jan` to `Dec`: Whether or not adult flight can occur in a given month
- `FlightDuration`: Total potential duration of adult flight in number of months
- `Voltinism`: How many generations the species can have in a given year: (U)nivoltine, (B)ivoltine, (M)ultivoltine
- `CanopyAffinity`: The affinity of the species towards a specific type of canopy cover
- `EdgeAffinity`: The affinity of the species towards habitat edges
- `MoistureAffinity`: The affinity of the species towards a specific level of moisture
- `DisturbanceAffinity`: The affinity of the species towards a specific level of disturbance
- `NumberOfHostplantFamilies`: The number of reported hostplant families for the species


### 3- __Red List of Butterflies in the UK__

List of butterflies from least vulnerable to regionally extinct species in the UK

Source: https://butterfly-conservation.org/red-list-of-butterflies-in-great-britain 

Dictionnary:
- `Species`: species common name
- `Species_ScientificName`: species scientific name
- `Red List Category`: red list category as of 2024
- `Quelifying criteria`: further notes on category
- `Previous (2010) Red List category`: red list category in 2010

### 4- __London weather historic data__

Monthly weather information from Heathrow (London Airport)

Source: https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data 

Dictionnary:
- `yyyy`: year
- `mm`: month
- `tmax`: Mean daily maximum temperature (tmax) in Celsius
- `tmin`: Mean daily minimum temperature (tmax) in Celsius
- `af`: Days of air frost
- `rain`: Total rainfall in mm
- `sun`: Total sunshine duration in hours


### 5- __London air quality historic data__

Hourly air quality information from Marylebone road (center London) - station with the most data points

Source: https://www.londonair.org.uk/LondonAir/Default.aspx

Dictionnary:
- `code`: Station code
- `date`: Date
- `O3`: Ground Level Ozone
- `NO2`: Nitrogen Dioxide
- `NOXasNO2`: Nitrogen Dioxide
- `SO2`: Sulphur dioxide
- `CO`: Carbon Monoxide
- `PM10`: Particles
- `site`: Site name