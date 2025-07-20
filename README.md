# Credit Card Fraud Detection

Link to the sample section: [Link Text](https://youtu.be/XlWoN0s6U6M?si=C-f2mK-e0AmYPEF9).

This project focuses on building a machine learning system to detect fraudulent credit card transactions. Credit card fraud is a serious issue in the financial industry, and detecting fraud in real-time is critical to minimizing financial losses. Our goal was to create a data-driven solution that can identify suspicious transactions with high accuracy, despite the dataset being highly imbalanced.

# Problem Statement
In real-world financial datasets, fraudulent transactions are extremely rare compared to legitimate ones. This imbalance poses a challenge for traditional machine learning models. The task was to explore the dataset, handle the imbalance, train robust models, and build an interactive web app for prediction.

# Project Overview
We used the Kaggle Credit Card Fraud Detection Dataset, which contains transactions made by European cardholders in September 2013. The dataset includes 284,807 transactions, of which only 492 are fraudulent (0.17%).

Our pipeline includes:
Data loading and exploration

Class balancing using Random Under Sampling and SMOTE

Feature selection
Model training and evaluation

A user-friendly web interface built with Streamlit

Technologies and Tools
Python, Pandas, NumPy, Matplotlib, Seaborn (for visualization)

Scikit-learn, Imbalanced-learn, LightGBM

Streamlit (for deployment)

Google Colab (for development)

Models Used
We trained several classification models to compare their performance:

Logistic Regression
Random Forest
Decision Tree
Random Forest
Logistic Regression
LightGBM

We evaluated the models using metrics such as accuracy, precision, recall, and F1-score, with a strong focus on minimizing false negatives (i.e., missing a fraudulent transaction).

Web Application
We built an interactive Streamlit web app that allows users to:

Input feature values manually or auto-fill them with sample values
Submit inputs to receive a prediction: Fraudulent or Non-Fraud

This makes the tool easy to test and demonstrates how such a system might work in a real-time environment.
