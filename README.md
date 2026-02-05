# Deutsche Bahn Train Delay Dashboard

This project analyzes train arrival delays in Deutsche Bahn services using real-world data.
The goal is to explore delay patterns across time, stations, train lines, and peak hours
through visual analysis and an interactive dashboard.

## Dataset
The dataset contains 1000 train records with information on:
- Arrival delays
- Train lines
- Stations
- Time of arrival
- Station categories

## Project Structure
- app.py – Streamlit dashboard application
- DBtrainrides_1000.csv – Dataset used for analysis
- Q01–Q15 PNG files – Visualizations created during analysis
- Analysis.ipynb / Analysis_Notebook.pdf – Exploratory data analysis

## Dashboard Features
- Interactive navigation for Q01–Q15
- Static visualizations displayed per question
- Summary results for each analysis
- Overview table of the dataset

## Technologies Used
- Python
- Pandas
- Matplotlib
- Streamlit

## How to Run
1. Install dependencies:
   pip install -r requirements.txt
2. Run the app:
   streamlit run app.py


