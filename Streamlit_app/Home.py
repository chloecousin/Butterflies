### import libraries
import streamlit as st
import pandas as pd
import numpy as np
from prophet import Prophet
import plotly.graph_objects as go

#######################################################################################################################################
### PAGE CONFIG
st.set_page_config(page_title='The Butterfly Effect', page_icon='🦋', layout="wide")

st.write('A multivariate Time Series model aimed to predict the Butterfly Population Evolution amid climate change (a focus around London, UK) - using Facebook Prophet model')
st.title("The Butterfly Effect")
st.divider()

#######################################################################################################################################
### DATA LOADING

# Define function to load data
# @st.cache_data # <- add decorators after tried running the load multiple times
def load_data(path, num_rows):
    df = pd.read_csv(path, nrows=num_rows)
    df = df.drop(columns=['Unnamed: 0'])
    return df

# Load observed data
df_o = load_data("Streamlit_app/observed_df.csv", 500)

# Load forecast data
df_f = load_data("Streamlit_app/forecast_df.csv", 500)


#######################################################################################################################################
### SIDE BAR
st.sidebar.subheader("Model filters")
st.sidebar.write('')

# Temperature slider + update in forecasts dataframe
tmax_perc = st.sidebar.slider('**Temperature variation**', min_value = -30, max_value = 30, value = 1, step = 1,format="%f%%")
df_f.loc['2020-06-01':,'Lag_Trend_tmax_12'] = df_f.loc['2020-06-01':,'Lag_Trend_tmax_12'].mul((100 + tmax_perc)/100)
df_f.loc['2020-06-01':,'Lag_Trend_tmax_24'] = df_f.loc['2020-06-01':,'Lag_Trend_tmax_24'].mul((100 + tmax_perc)/100)
# st.sidebar.write(f'=> For 20°C, this would mean {round(20 * ((100 + tmax_perc)/100),1)}°C')
st.sidebar.write('\n')

# O3 slider + update in forecasts dataframe
O3_perc = st.sidebar.slider('**O3 variation**', min_value = -30, max_value = 30, value = 1, step = 1,format="%f%%")
df_f.loc['2020-06-01':,'Lag_Trend_O3_24'] = df_f.loc['2020-06-01':,'Lag_Trend_O3_24'].mul((100 + O3_perc)/100)
st.sidebar.write('\n')

# SO2 slider + update in forecasts dataframe
SO2_perc = st.sidebar.slider('**SO2 variation**', min_value = -30, max_value = 30, value = 1, step = 1,format="%f%%")
df_f.loc['2020-06-01':,'Lag_Trend_SO2_24'] = df_f.loc['2020-06-01':,'Lag_Trend_SO2_24'].mul((100 + SO2_perc)/100)
st.sidebar.write('\n')

# Sources
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.markdown('**Data Sources**')
st.sidebar.caption('Butterfly sightings data: [UKBMS](https://registry.nbnatlas.org/public/show/dr1206)')
st.sidebar.caption('Weather data: [Met Office](https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data)')
st.sidebar.caption('Air Quality data: [London Air](https://www.londonair.org.uk/LondonAir/Default.aspx)')
st.sidebar.write('______')
st.sidebar.caption('More info about the [Time Series Analysis](https://github.com/chloecousin)')
st.sidebar.caption('Developed by [Chloe Cousin](https://www.linkedin.com/in/chloe-m-cousin/)')

#######################################################################################################################################
### MODEL
# Instantiate the model
model = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False, 
                holidays=None, seasonality_prior_scale=10, changepoint_prior_scale=1)

# Add regressors (independant variables)
for col in df_o.drop(columns=['y', 'ds']).columns:
    model.add_regressor(col)

# Train/test Split - Defining % of data points in the test sets (30%)
nobs = int(len(df_o)*0.70)

# Creating train and test sets
train = df_o.iloc[:nobs,:]
test = df_o.iloc[nobs:,:]

# Fit the Model
prophet_fit_multi = model.fit(train)

############### Preds on observed data ###############
# Model predictions
future = model.make_future_dataframe(periods=len(test), freq='MS')
future = pd.merge(future, df_o.drop(columns=['y', 'ds']), left_index=True, right_index=True, how='left')
preds  = model.predict(future)

# # Make sure no predictions is below 0 (not possible)
preds['yhat'] = np.where(preds['yhat']<0, 0, preds['yhat'])

# # Merge dataset and forecast
preds2 = pd.merge(df_o, preds.drop(columns=['ds']), left_index=True, right_index=True, how='left')

# ############### Preds on future data ###############
# Model predictions
future2 = model.make_future_dataframe(periods=108, freq='MS')
future2 = pd.merge(future2, df_f.drop(columns=['y', 'ds']), left_index=True, right_index=True, how='left')
forecasts = model.predict(future2)

# Make sure no predictions is below 0 (not possible)
forecasts['yhat'] = np.where(forecasts['yhat']<0, 0, forecasts['yhat'])

# Merge dataset and forecast
forecasts2 = pd.merge(forecasts, df_o.drop(columns=['ds']), left_index=True, right_index=True, how='left')


#######################################################################################################################################
### PLOT
# Split index (train/test)
index_split1 = test.index[1]
index_split2 = test.index[-1]

# ### Plot
fig = go.Figure()

fig.add_trace(go.Scatter(x=preds2.loc[:nobs,'ds'], y=preds2.loc[:nobs,'y'], mode='lines', line=dict(color='#233333'), name='Train', opacity=0.3))
fig.add_trace(go.Scatter(x=preds2.loc[nobs:,'ds'], y=preds2.loc[nobs:,'y'], mode='lines', line=dict(color='#EBACA0'), name='Test', opacity=0.3))
fig.add_trace(go.Scatter(x=preds2.loc[:, 'ds'],y=preds2.loc[:, 'yhat'], mode='lines', line_dash='dot', line=dict(color='#419D78'), name='Predictions'))
fig.add_trace(go.Scatter(x=forecasts2.loc['2020-06-01':, 'ds'], y=forecasts2.loc['2020-06-01':, 'yhat'], mode='lines', 
                         line_dash='dash', line=dict(color='#C42348'), name='Forecasts'))


# fig.add_trace(go.Scatter(x=df['ds'], y=df['y'], mode='lines', line=dict(color='#233333'), name='Train', opacity=0.3))
fig.update_layout(yaxis_title='Butterflies per Survey', height=600,
                  title=f'Butterflies population evolution estimation trend in London, UK', plot_bgcolor='white', showlegend=True)
fig.update_yaxes(range=[0, 12])
st.plotly_chart(fig, use_container_width=True)

######################################################################################################################################
### EVALUATION FUNCTIONS
# MAPE function
def mean_absolute_percentage_error(true_values, predicted_values):
    absolute_percentage_error = []

    for x, y in zip(true_values, predicted_values):
        error = x - y
        
        # Some true values in our dataset are = to 0 (months where there are no sightings), this is to avoid errors due to dividing by 0
        if x == 0:
            absolute_percentage_error.append(0)
        else: absolute_percentage_error.append(np.abs(error/x))

    mape = np.mean(absolute_percentage_error) * 100

    return mape

# Diff MAPE function
def Diff_MAPE_calculation(train_mape, test_mape):
    return test_mape - train_mape

#######################################################################################################################################
### MODEL EVALUATION
train_mape = mean_absolute_percentage_error(preds2.loc[:index_split1,'y'], preds2.loc[:index_split1,'yhat'])
test_mape = mean_absolute_percentage_error(preds2.loc[index_split1:,'y'], preds2.loc[index_split1:,'yhat'])
Diff_MAPE = Diff_MAPE_calculation(train_mape, test_mape)

st.write(f'Train set MAPE: {round(train_mape, 2)}% | Test set MAPE: {round(test_mape, 2)}% | Difference in accuracy between train and test sets: {round(Diff_MAPE, 2)}%')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')


#######################################################################################################################################
### DataFrame
st.subheader('Dataframe')
st.dataframe(df_f)