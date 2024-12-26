```markdown
# Secure Database Operations Demo

This project demonstrates secure database operations using SQLite with encrypted sensitive data using the Fernet encryption from the `cryptography` library.

## Features

- In-memory SQLite database implementation
- Encryption of sensitive data using Fernet symmetric encryption
- Basic user and transaction data management
- Demonstration of SQL joins with encrypted data handling

## Prerequisites

- Python 3.9+
- Docker 

## Installation

1. Clone the repository
2. Install dependencies:
```sh
pip install -r requirements.txt
```

## Running the Application

### Direct Python Execution

```sh
python app.py
```

### Using Docker

1. Build the Docker image:
```sh
docker build -t secure-db-demo .
```

2. Run the container:
```sh
docker run secure-db-demo


## Project Structure

app.py
 - Main application code with database operations and encryption logic

requirements.txt

 - Python dependencies

Dockerfile

 - Container configuration for Docker deployment

## Security Features

- Uses Fernet symmetric encryption for sensitive data
- In-memory database to prevent data persistence
- Data encryption/decryption functions for secure data handling

## Note
This is a demonstration project and should be adapted with additional security measures for production use.
```
