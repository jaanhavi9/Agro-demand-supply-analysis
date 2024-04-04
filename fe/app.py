import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# from test import lstm

# Function to simulate fetching data based on commodity name and number of days
def fetch_data(num_days):
    data = pd.read_csv('next30.csv')
    data = data.head(num_days)
    return pd.DataFrame(data)


# def runmodel():
#     output = lstm()
#     return output

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

        # input_data = num_days  # Placeholder: Use num_days as input to the model
        # output = runmodel()
        # st.write('Machine Learning Model Output:', output)
        
    # If the plot button is clicked
    if plot_chart:
    # Plotting line chart
        data = fetch_data(num_days)
        st.write('Data fetched successfully!')
        # Set Seaborn style
        sns.set_style("whitegrid")
        
        # Define custom colors
        colors = sns.color_palette("husl", 2)
        
        plt.figure(figsize=(10, 6))
        plt.plot(data['datetime'], data['temp'], marker='o', color=colors[0], linewidth=2)
        plt.xlabel('Date', fontsize=12, fontweight='bold')
        plt.ylabel('Price', fontsize=12, fontweight='bold')
        plt.title(f'Price of {commodity_name}', fontsize=14, fontweight='bold')
        plt.xticks(rotation=45)  # Rotate x-axis labels by 45 degrees
        
        # Customize grid lines
        plt.grid(True, linestyle='--', alpha=0.7)
        
        # Adding background color
        plt.gca().set_facecolor('#f5f5f5')
        
        st.pyplot(plt)


if __name__ == '__main__':
    main()
