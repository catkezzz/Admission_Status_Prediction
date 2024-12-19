# Admission_Status_Prediction
## Data Overview
Dataset used for this project contains synthetic data created based on statistics from applicants to the Wharton Class of 2025. Taken from kaggle __[here](https://www.kaggle.com/datasets/taweilo/mba-admission-dataset)__

## Objective
The primary goal of this project is to develop a model capable of predicting admission status between Admit, Deny, or Waitlist—for prospective students based on various factors in the data. The model aims to provide valuable insights for multiple stakeholders:
- **Prospective Students**: Gain an understanding of how attributes such as GPA, GMAT scores, work experience, and other factors influence admission decisions. This can help them identify areas for improvement to enhance their chances of acceptance.
- **Admission Team**: Understand the relationship between applicant attributes and their impact on the likelihood of receiving an Admit or Waitlist status, aiding in refining recruitment strategies.
- **Data Scientist/Analyst**: This synthetic data project serves as a practical exercise for building machine learning models applicable to real-world tasks, such as those in education, HR, or related fields.

The algorithms considered for this project include Decision Tree, Logistic Regression, Random Forest, K-Nearest Neighbors, XGBoost Classifier, Gaussian Naive Bayes, and Support Vector Classification. Model performance will be evaluated using Recall and the AUC-ROC score.

---
The best model found is then deployed at HuggingFace, as seen in this __[link](https://huggingface.co/spaces/ckezzz/Milestone2_AdmissionStatus_Kezia)__
