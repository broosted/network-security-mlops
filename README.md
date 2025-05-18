# Network Security Project

A machine learning project for network security analysis and phishing detection.

## Project Overview

This project implements machine learning models for network security analysis, specifically focusing on phishing detection. It includes data processing, model training, and deployment capabilities.

### Key Features

1. **Phishing Detection**
   - Real-time analysis of network traffic
   - Detection of malicious URLs and phishing attempts
   - Classification of suspicious network activities
   - Confidence scoring for detected threats

2. **Data Processing**
   - Automated data collection from network traffic
   - Feature extraction and preprocessing
   - Data validation and cleaning
   - Schema enforcement for consistent data structure

3. **Model Management**
   - Model training and evaluation pipeline
   - Model versioning and tracking using MLflow
   - Automated model retraining
   - Model performance monitoring
   - A/B testing capabilities

4. **Deployment & Integration**
   - REST API for real-time predictions
   - Docker containerization for easy deployment
   - AWS integration for scalable storage and deployment
   - Continuous monitoring and logging
   - Easy integration with existing security systems

5. **Security & Compliance**
   - Secure data handling
   - AWS IAM integration for access control
   - Audit logging for all operations
   - Data encryption in transit and at rest

## Prerequisites

- Python 3.11+
- Docker
- AWS CLI configured with appropriate permissions for S3 and ECR
- Required Python packages (see `requirements.txt`)

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd NetworkSecurity
```

2. Create and activate virtual environment:
```bash
python -m venv network-venv
source network-venv/bin/activate  # On Unix/macOS
# or
.\network-venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Docker Usage

Build the Docker image:
```bash
docker build -t network-security .
```

Run the container:
```bash
docker run -p 5000:5000 network-security
```

## AWS Configuration

The project requires AWS credentials with permissions for:
- S3 bucket access
- ECR repository access

Configure AWS CLI:
```bash
aws configure
```

Required permissions:
- S3: ListBucket, GetObject, PutObject, DeleteObject, CreateBucket
- ECR: GetAuthorizationToken, BatchCheckLayerAvailability, GetDownloadUrlForLayer, etc.

## Project Structure

```
NetworkSecurity/
├── app.py                 # Main application file with REST API endpoints
├── main.py               # Entry point for model training and evaluation
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration for containerization
├── data_schema/         # Data schema definitions and validation rules
├── Network_data/        # Network data storage and processing
├── final_models/        # Trained model artifacts and versions
├── mlruns/             # MLflow tracking for experiment management
├── notebooks/          # Jupyter notebooks for analysis and development
└── networksecurity/    # Core package with ML models and utilities
    ├── models/         # ML model implementations
    ├── preprocessing/  # Data preprocessing modules
    ├── utils/         # Utility functions
    └── api/           # API endpoints and handlers
```

## Usage

1. Training the model:
```bash
python main.py
```
This will:
- Load and preprocess the training data
- Train the model with specified parameters
- Evaluate model performance
- Save the model artifacts
- Log metrics and parameters to MLflow

2. Running the application:
```bash
python app.py
```
This starts the REST API server which provides:
- Real-time phishing detection endpoints
- Model prediction services
- Health check endpoints
- Monitoring metrics

3. Making predictions:
```bash
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"url": "example.com", "features": {...}}'
```

4. Monitoring and Logging:
- Access MLflow dashboard for model metrics
- Check application logs in the logs directory
- Monitor model performance through API endpoints
- View AWS CloudWatch metrics for deployed instances