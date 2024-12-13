# Sentiment Analysis System

## Description
The **Sentiment Analysis System** is a Natural Language Processing (NLP) application designed to analyze textual data and predict its sentiment. It categorizes sentiments into three categories: Positive, Negative, and Neutral. The system also provides insightful visualizations based on various factors such as age, gender, language, and location, aiding better understanding of the data.

## Features
- Sentiment analysis using VADER SentimentIntensityAnalyzer.
- Integration with Google Sheets for data import and export.
- Real-time visualization of sentiment results, including:
  - Pie charts
  - Histograms
  - Scatter plots
- Easy-to-use Streamlit interface with a menu-driven design:
  - **Home**: Overview of the application.
  - **Analysis**: Perform sentiment analysis on a selected column from a Google Sheet.
  - **Results**: View and visualize analyzed data.

## Technologies Used
- **Programming Language**: Python
- **Libraries**: 
  - pandas
  - vaderSentiment
  - google-auth-oauthlib
  - google-api-python-client
  - plotly
  - streamlit
- **Google Sheets API**: For seamless data integration.

## Data
The project utilizes user-provided Google Sheets as the primary dataset. Users specify:
- **Google Sheet ID**: Unique identifier of the sheet.
- **Range**: Range of columns to import.
- **Column to Analyze**: The column containing textual data for sentiment analysis.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AnoopCA/Sentiment-Analysis-System.git
   cd sentiment-analysis-system
