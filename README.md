# Dynamic Sentiment Dashboard for Corporate News Analysis

Title      : Dynamic Sentiment Dashboard for Corporate News Analysis
Subtitle   : Final Project for Dibimbing.id
Your Name  : Muthia Aisyah Putri
Date       : 28 Juni 2024

## Project Overview
### Objective:
To create an automated data pipeline using Apache Airflow for sentiment analysis of daily news articles about a specific company.
### Scope:
Collecting daily news articles.
Performing sentiment analysis on the collected articles.
Visualizing the sentiment analysis results in a dashboard.
### Technologies Used:
- Apache Airflow
- Python
- Natural Language Processing (NLP) libraries (such as NLTK, TextBlob, or SpaCy)
- Dashboarding tool (such as Tableau or Power BI)

## Workflow Diagram
![image](https://github.com/muthiaap/Dynamic-Sentiment-Dashboard-for-Corporate-News-Analysis/assets/108161059/341523bf-264c-45c3-b312-5a2eac56ee92)
Data Collection: Web scraping or API integration to collect daily news articles.
Data Storage: Store the collected articles in a database or cloud storage.
Data Processing: Use Airflow to schedule and manage the workflow for sentiment analysis.
Sentiment Analysis: Apply NLP techniques to analyze the sentiment of the news articles.
Data Visualization: Create a dashboard to display the sentiment analysis results.

## Expected Output
### Dashboard Features:
- Daily sentiment score for the company.
- Trend analysis of sentiment over time.
- Word clouds or key phrases extracted from the articles.
- Comparison of sentiment across different news sources.

## Dataset
### Data Source:
- News APIs (e.g., NewsAPI, Google News API)
- Web scraping from news websites
### Data Structure:
- Date of the article
- Source of the article
- Article content
- Sentiment score (calculated during processing)
