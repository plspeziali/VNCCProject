# Body Performance Predictor Docker Application

This is a dockerized application that uses machine learning to predict body performance based on physical and lifestyle data.
It was made by [Tommaso Martinelli](https://github.com/tommasomartinelli) and [Paolo Speziali](https://github.com/plspeziali) for the
"Virtual Networks and Cloud Computing" exam at UniPG.

## Machine Learning Model

The machine learning model used in this application was trained in a Jupyter Notebook. The code for this notebook can be found in the [Body-Performance-Predictor](https://github.com/tommasomartinelli/Body-Performance-Predictor) repository.

## Getting Started

To run this application, you must have Docker and Docker Compose installed on your machine. If you do not have these, please follow the installation instructions for your operating system:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

Clone this repository to your local machine:

```bash
git clone https://github.com/tommasomartinelli/Body-Performance-Predictor.git
```

## Setup Instructions

To run the application, follow these steps:

1. Install Docker and Docker Compose
2. Clone the repository: `git clone https://github.com/tommasomartinelli/Body-Performance-Prediction-App.git`
3. Navigate to the cloned directory: `cd Body-Performance-Prediction-App`
4. Run Docker Compose: `docker-compose up`

Once the initialization is complete, you can access the web application by visiting http://localhost:8080 in your web browser.

## Usage

To predict body performance, fill out the form on the home page with your personal data and click "Predict". The application will use machine learning to calculate your body performance score. You may also add more data, the model will automatically train again.

You can also access the PgAdmin web interface by visiting http://localhost:8081 in your web browser. The default login credentials are:

Email: admin@admin.com
Password: admin

## Docker Compose Configuration

This application consists of the following Docker containers:

- webserver: the web application
- predictor: the machine learning prediction service
- training: the machine learning training service
- inserter: the service responsible for inserting data into the database
- initializer: the service responsible for initializing the database with sample data
- db: the PostgreSQL database
- pgadmin: the PgAdmin web interface

### Ports

The application uses the following ports:

- 8080: the web application
- 5000: the prediction service
- 3002: the training service
- 3001: the inserter service
- 5432: the database
- 8081: the PgAdmin web interface

### Volumes

The application uses the following volumes:

- postgres_data: the PostgreSQL database data directory
- model_data: the machine learning model data and scaler model data directory

### Networks

The application uses a bridge network named app_network.
