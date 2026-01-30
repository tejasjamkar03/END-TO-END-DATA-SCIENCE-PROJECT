# END-TO-END-DATA-SCIENCE-PROJECT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: TEJAS VISHNU JAMKAR

*INTERN ID*: CTIS1750

*DOMAIN*: DATA SCIENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH


#OUTPUT:

<img width="1918" height="1012" alt="Image" src="https://github.com/user-attachments/assets/6bfb908a-19a3-43ec-9a74-4e12eff04b8d" />

#DESCRIPTION:

In this task, I completed an end-to-end data science project that involved everything from data collection and preprocessing to deploying a machine learning model using Flask. The main goal of this project was to learn how to build a machine learning model and deploy it as a web application, enabling users to interact with it in real time.

I used Visual Studio Code (VS Code) as my development environment, which helped me efficiently manage all project files, including the dataset, Python scripts, HTML templates, and the trained model file. The integrated terminal in VS Code was used to install necessary libraries and run the application.

The project was implemented in Python, a language widely used in data science and machine learning. I leveraged several Python libraries:

Pandas for data collection and handling CSV files

NumPy for numerical operations

Scikit-learn for training the machine learning model

Joblib for saving and loading the trained model

Flask for deploying the model as a web application

The dataset used in this project was a house price dataset containing features such as area (in square feet), number of bedrooms, number of bathrooms, and the corresponding house price. This dataset represents a typical regression problem where the target variable depends on multiple input features.

The project began with data collection and preprocessing. Using Pandas, the dataset was loaded, and input features were separated from the target variable. Basic preprocessing was performed to clean the data and prepare it for training. Features were carefully selected to ensure the model could learn meaningful relationships between house characteristics and price.

Next, a machine learning model was created using Linear Regression from Scikit-learn. This algorithm was chosen for its simplicity, efficiency, and suitability for predicting continuous values such as house prices. The model was trained on the dataset, and once training was completed, it was saved as a .pkl file using Joblib. Saving the model allows it to be reused later without retraining.

The final step was model deployment. I developed a Flask web application that loads the trained model and provides a user-friendly interface for predictions. Flask routes were created to handle user input and generate predictions dynamically. Users can enter values such as area, bedrooms, and bathrooms in a web form, which are then sent to the model to display the predicted house price on the same page.

A simple HTML interface was designed with inline CSS to ensure a clean and intuitive user experience. It includes input fields for the features and a button to generate predictions. After submitting the form, the predicted house price is displayed instantly.

This project demonstrates a full data science workflow, covering data handling, preprocessing, model training, model saving, and deployment through a web framework. Such end-to-end projects are highly relevant in real-world applications like real estate price prediction, sales forecasting, demand estimation, and financial analysis.

Through this project, I gained practical experience in integrating machine learning models with real applications. I learned how trained models can be deployed and used by end-users outside the development environment. This task enhanced my understanding of data science pipelines and provided hands-on experience in building deployable machine learning systems.
