import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from test import lstm

# Function to simulate fetching data based on commodity name and number of days
def fetch_data(num_days):
    data = pd.read_csv('next30.csv')
    data = data.head(num_days)
    return pd.DataFrame(data)


def runmodel():
    output = lstm()
    return output

# Main function to create Streamlit app
def main():
    st.title('Commodity Price Analysis')
    
    # Form to input commodity name and number of days
    commodity_name = st.text_input('Enter commodity name:')
    num_days = st.number_input('Enter number of days:', min_value=1, max_value=365, value=30)

    # Submit button for the form
    submitted = st.button('Submit')
    
    # Button to plot line chart
    plot_chart = st.button('Forecast Weather')
    
    # If the form is submitted
    if submitted:
        # Fetch data based on commodity name and number of days
        st.write('Data fetched successfully!')

        input_data = num_days  # Placeholder: Use num_days as input to the model
        output = runmodel()
        st.write('Machine Learning Model Output:', output)
        
    # If the plot button is clicked
    if plot_chart:
        # Plotting line chart
        data = fetch_data(num_days)
        st.write('Data fetched successfully!')
        plt.figure(figsize=(10, 6))
        # data['datetime'] = pd.to_datetime(data['datetime']).strftime('')
        plt.plot(data['datetime'], data['temp'], marker='o')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title(f'Price of {commodity_name}')
        st.pyplot(plt)


