# Butterflies

## Project Overview
The World Economic Forum states that Biodiversity is _'critically important'_ for 5 reasons, as it:

1. Ensures health and food security
2. Helps fight disease
3. Benefits business
4. Provides livelihood
5. Protects us

The butterfly population has been widely studied across the world over the last decades. The butterflies are indeed thought to be one of the best indicators of a healthy environment. As they have short life cycles, they have quick responses to environmental changes. 

The purpose of this analysis is to :
- understand how the butterflies population varies and
- predict its evolution over the next years as external factors in their environment will evolve as well


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


