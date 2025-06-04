Soil Data Analysis Web App (Streamlit)

Overview

This project is a web-based soil data analysis tool built using Streamlit. It allows users to upload an Excel file containing soil data, visualize key statistics, and apply machine learning techniques to analyze soil properties. The app helps in determining soil suitability for agriculture based on pH levels and nutrient composition.

Features

Upload soil data (Excel format)

Data cleaning & preprocessing

Descriptive statistics & correlation analysis

Clustering analysis using K-Means

Regression model to predict soil pH

Interactive data visualization

Installation & Setup

1. Clone the Repository

git clone https://github.com/mahkzmi/Soil-Data-Analysis-Web-App-Streamlit.git
cd Soil-Data-Analysis-Web-App-Streamlit

2. Install Dependencies

pip install -r requirements.txt

3. Run the Streamlit App

streamlit run app.py

File Structure

soil-data-streamlit/
│── app.py              # Main Streamlit application
│── data/               # Sample dataset (Excel files)
│── requirements.txt    # Required Python packages
│── README.md           # Project documentation

How to Use

1. Upload Soil Data

The app accepts Excel (.xlsx) files containing soil parameters.

Ensure that the dataset has relevant columns such as Latitude, Longitude, pH, N (%), P (%), K (%).

2. Data Processing & Visualization

The uploaded data is displayed in a tabular format.

Users can view summary statistics and a correlation matrix.

3. Clustering Analysis

The app applies K-Means clustering to group soil locations based on similarity.

A scatter plot visualizes different clusters.

4. pH Prediction Model

A Linear Regression model predicts soil pH based on nutrient composition.

The model is trained using historical data and tested on unseen samples.

Users can visualize the prediction results in an interactive plot.

5. Interactive Map (Folium)

A map visualization highlights suitable soil locations.

Each point displays soil pH and its classification (suitable/unsuitable for cultivation).

Technologies Used

Python (Pandas, NumPy, Scikit-Learn, Matplotlib, Folium)

Streamlit (Web App Framework)

Machine Learning (Clustering, Regression)

Future Improvements

Support for real-time data updates.

Integration with geospatial analysis tools.

More advanced machine learning models for soil health prediction.

Author

 mahkzmi
