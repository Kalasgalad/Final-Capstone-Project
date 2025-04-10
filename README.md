# Final Capstone Project

## Classification Model predicting EV Charging Stations in the US
-----------------------------------------------------------------

**Summary/Objective: <br>** 
This project consists of building a classification model to predict which EV Charging Stations belong to an individual network. The dataset contains information pertaining to geographical positioning, as well as pricing, availability, and equipment. Several machine learning models will be compared and evaluated to determine the best model for predicting EV Charging Networks. The goal of the project is to accurately determine the most precise model, and deploy it for future predictions. Once the final model is chosen, it will be deployed in a Streamlit app to make predictions.

**Project Overview:**
1. Data Fetching
2. Data Exploration (EDA)
3. Data Cleaning and Preparation
4. Visualization
5. Feature Engineering
6. Model Building, Evaluation and Comparison
7. Model Exportation

**Reference to the API: <br>** 
(https://developer.nrel.gov/)

**Finalized dataset.csv file name: <br>**
- clean_ev_data.csv

**Python Notebook file containing: Data Fetching, Data Cleaning, Feature Engineering, Model Training, Model Evaluation, Saving Final Model, and Exporting.):**
- Final Project.ipynb <br>

**App Python file used to run code for Streamlit app: <br>**
- app.py <br> 

**Required/Imported files used for Streamlit app: <br>**
<br>
*Requirements text file:* 
- requirements.txt <br>

*Pipeline containing preprocessor and model (Joblib File):* 
- final_rf_model.pkl <br>

**M4P03 Powerpoint Presentation Slides (.pptx File): <br>**
- 

**URLs for Streamlit app:** <br>
Local URL: (http://localhost:8501/) <br>

**Classification models:**
1. Random Forest Classification
2. Logistic Regression
3. Support Vector Classification (SVC)
    
**Methodology and Techniques:**
1. Feature Engineering and Data Preprocessing
2. Classification Models (Random Forest Classification, Logistic Regression, and Support Vector Classification (SVC))
3. Model Evaluation and Comparison (Confusion Matrix and Classification Reports)
4. Pipeline Creation & Exportation
   
**EV Charging Network Prediction Project:** <br>
1. **Exploratory Data Analysis (EDA) includes:** <br>
- Check for missing data, value counts, and verifying value types.
- Visualizations to better understand data distributions and feature relationships.

    Observations from EDA:
    - The dataset contains information pertaining to geographical positioning (latitude, longitude, city, state), and a number of variable pricing ranges & equipment.
    - Significant imbalances in EV Networks, State & Connector Types. 

2. **Model Processing Steps:**
- Random Forest Classification: Uses an ensemble of decision trees to predict EV Charging Networks.
- Logistic Regression: A simple and interpretable linear model.
- Support Vector Classification (SVC): In high-dimensional spaces, this model focuses on finding the best hyperplane.

3. **Feature Engineering and Preprocessing:**
- Categorical features are encoded to numerical values through OneHotEncoder.
- Data split to training and testing sets for model evaluation.
- Stratifying train and test sets to address imbalances in the dataset.  
- Pre-processing and Feature Engineering on 'EV Network' (Target Variable): 

4. **Model Evaluation:**
- Comparing mode performance completed by using Evaluation metrics (accuracy, precision, recall, F1-score) and the confusion matrix. <br>

 **Validation and Evaluation:**
- Confusion Matrix: To visualize model performance. <br>
- Classification Report: To evaluate precision, recall, F1-score, and accuracy for each injury severity class. <br>
- Comparison of Results: Final comparison of Logistic Regression, SVC, and Random Forest models. <br>

5. **Final Model:**
- Random Forest Classification was chosen as the final model due to its superior accuracy and performance metrics.
- The model was trained on the dataset and deployed for future predictions.

6. **Model Deployment:**
- Saved the trained Random Forest Classifier model using the joblib library for deployment.
- The final model is saved as final_rf_model.pkl and will be loaded and used for predictions.
- The final model will be used for deployment as a Streamlit app and will be used to make a prediction.

## Conclusion 
In conclusion, three models were tested: Logistic Regression, Support Vector Classification (SVC) and Random Forest Classification. <br>
**Of the three models, the Random Forest Classification model was chosen as it had the best performance and the highest accuracy.** <br>

- For chosen features applied to the final model, the highest predictors are the year and month confirmation dates.<br>
- The features underwent various preprocessing and feature engineering techniques to enhance their suitability for model prediction.<br>
- Cross-validation with GridSearchCV and RandomizedSearchCV) was used as a validation scheme. Cross-validation was used to evaluate the holdout data for the final model, and has about the same results as the training model <br>
- The final model, Random Forest Classification, had the encoding feature OneHotEncoder to convert the categorical feature values to numerical form. This encoder was also applied as part of feature engineering for the final model. <br>  
- The final model and preprocessor were made into a pipeline and saved as the file final_rf_model.pkl').
- The final model was used for deployment as a Streamlit app and was able to make predictions. <br>
