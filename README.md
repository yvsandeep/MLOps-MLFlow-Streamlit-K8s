# Kubernetes MLOps Pipeline Demo

This repository contains a demo project done as part of coursework showcasing the deployment of a Machine Learning Operations (MLOps) pipeline on a Kubernetes Cluster. This project demonstrates the scalability and efficiency of Kubernetes in managing complex ML workflows.

## Demo Objective

The primary goal of this demo is to illustrate the deployment of a MLOps pipeline on Kubernetes, which can be scaled for use by multiple data scientists in a production-grade system. The steps include:
- **Step 1:** Deploy a Machine Learning model from a Jupyter notebook to an MLFlow Server, which tracks multiple experiments.
- **Step 2:** Select and deploy a specific experiment to production using MLFlow Server Models.
- **Step 3:** Access the deployed model via a Streamlit Frontend, deployed on the Kubernetes Cluster.
- **Step 4:** Monitor cluster metrics using Grafana and Prometheus, including memory usage, CPU usage, filesystem usage, number of pods, and I/O bytes transferred【13†source】.

## Demo Setup

- **System:** Apple MacBook Pro 13.3 inch with 24GB RAM and 512GB Disk space.
- **Kubernetes Deployment:** Local deployment through Minikube with Docker driver.
- **Containerization:** Docker images created for MLFlow and Streamlit.
- **Services Deployed on Kubernetes:**
  - MLFlow-tracking-server with a backend via GCP PostgreSQL.
  - Streamlit-App for frontend.
  - Grafana for monitoring and alerting via Helm.
  - Prometheus for metric measurement via Helm【14†source】.

## Demo Architecture

The architecture of the demo is detailed in the term paper, providing insights into the configuration and interaction of various components within the Kubernetes environment【15†source】.

## Environment Setup Commands

To set up the working environment for this demo, the following commands are used:
- Start Minikube: `minikube start --memory 8192 cpus`
- Check services: `kubectl get svc`
- Deploy MLFlow Server: Steps include deploying configmap secrets and MLFlow deployment【16†source】.

## Deployment Screenshots

The following screenshots are available to demonstrate the deployment process:
- MLFlow logging experiments.
- Deployed MLFlow model.
- Streamlit Frontend interface.
- Grafana + Prometheus dashboards.
- Minikube dashboard showcasing cluster details and deployments【17†source】.