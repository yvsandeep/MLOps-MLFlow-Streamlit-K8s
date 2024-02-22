import streamlit as st
import mlflow.pyfunc
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# MLflow server URI
MLFLOW_SERVER_URI = "http://mlflow-tracking-server.default.svc.cluster.local:5000"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./cs777.json"

# Function to load model from MLflow
def load_model_from_mlflow(model_name="demo_model", stage="Production"):
    mlflow.set_tracking_uri(MLFLOW_SERVER_URI)
    model_uri = f"models:/{model_name}/{stage}"
    return mlflow.pyfunc.load_model(model_uri)

# Load your initial model from MLflow
model = load_model_from_mlflow()

# Load Iris Data
def load_iris_data():
    iris = datasets.load_iris()
    data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    data['target'] = iris.target
    return data

# Streamlit app main function
def main():
    st.title("Term Paper MLFlow Demo with Iris Dataset")

    # Model reloading section
    st.subheader("Model Reloading")
    if st.button("Reload Model from MLflow"):
        global model
        model = load_model_from_mlflow()  # Reload the model from MLflow
        st.success("Model reloaded from MLflow!")

    # Data section
    data = load_iris_data()
    if st.checkbox("Show dataset"):
        st.write(data)

    # Model testing section
    test_size = st.slider("Test Size for Splitting Data", min_value=0.1, max_value=0.9, value=0.3, step=0.1)
    if st.button("Test Model"):
        if not data.empty:
            X = data.iloc[:, :-1]
            y = data['target']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
            predictions = model.predict(X_test)

            accuracy = accuracy_score(y_test, predictions)
            report = classification_report(y_test, predictions)

            st.write("Accuracy:", accuracy)
            st.text(report)

            # Plotting
            fig, ax = plt.subplots()
            sns.scatterplot(x=X_test.iloc[:, 0], y=X_test.iloc[:, 1], hue=y_test, style=predictions, ax=ax)
            plt.xlabel(data.columns[0])
            plt.ylabel(data.columns[1])
            st.pyplot(fig)
        else:
            st.error("Data is not loaded. Please load the data to test the model.")

if __name__ == "__main__":
    main()
