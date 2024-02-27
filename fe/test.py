import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
from dateutil import parser
from numpy import concatenate
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # Disable oneDNN optimizations
from matplotlib import pyplot
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

def lstm():
    merged_data = pd.read_csv('merged_data.csv')
    date = merged_data['Date']
    precipitation = merged_data[' prcp']
    price = merged_data['Average']
    
    merged_data['Date'] = pd.to_datetime(merged_data['Date'])

    features = merged_data[[' prcp', 'tempmin', 'tempmax', 'temp', 'Minimum', 'Maximum']]
    target = merged_data['Average']

    scaler = MinMaxScaler()
    features_scaled = scaler.fit_transform(features)

    X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.2, random_state=42)

    X_train = np.reshape(X_train, (X_train.shape[0], 1, X_train.shape[1]))
    X_test = np.reshape(X_test, (X_test.shape[0], 1, X_test.shape[1]))

    model = Sequential()
    model.add(LSTM(units=50, activation='relu', input_shape=(X_train.shape[1], X_train.shape[2])))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')

    model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

    train_loss = model.evaluate(X_train, y_train, verbose=0)
    test_loss = model.evaluate(X_test, y_test, verbose=0)

    predictions = model.predict(X_test)

    future_data = pd.DataFrame({
    ' prcp': [0.1, 0.013, 0.7],  # Example precipitation values for future dates
    'tempmin': [20.1, 20.1, 19.2],   # Example minimum temperature values for future dates
    'tempmax': [28.9, 27.8, 27.8],   # Example maximum temperature values for future dates
    'temp': [23.4, 23.6, 23.2],      # Example temperature values for future dates
    'humidity': [80.8, 80.5, 80.5],  # Example humidity values for future dates
    'Maximum': [33, 30, 30], # Example maximum price values for future dates
    'Minimum': [15, 28, 20]
    })

    future_data_scaled = scaler.transform(future_data)

    # Reshape future data to match the model's input shape
    future_data_reshaped = np.reshape(future_data_scaled, (future_data_scaled.shape[0], 1, future_data_scaled.shape[1]))

    # Make predictions for future dates using the trained model
    future_predictions = model.predict(future_data_reshaped)


    # Create a DataFrame with the future dates and corresponding predictions
    future_dates = pd.date_range(start='2023-11-30', end='2023-12-02')  # Example future dates
    future_predictions_df = pd.DataFrame({'Date': future_dates, 'Predicted_Price': future_predictions.flatten()})

    # Display the predictions for future dates
    print(future_predictions_df)