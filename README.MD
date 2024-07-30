# Online Store Revenue Analysis

## Description
This application reads customer orders data from a CSV file and performs various revenue analysis tasks.

## Tasks
1. Compute total revenue by month.
2. Compute total revenue by product.
3. Compute total revenue by customer.
4. Identify top 10 customers by revenue.

## Architecture

### Services

1. **app**: The main application service that runs the revenue analysis tasks.
2. **test**: The test service that runs the unit tests for the application.

### Dockerfiles

- **Dockerfile**: Used for building the main application container.
- **Dockerfile.test**: Used for building the test container.

### Docker Compose

The `docker-compose.yml` file defines two services:
- **app**: Builds the main application container using `Dockerfile` and runs `main.py`.
- **test**: Builds the test container using `Dockerfile.test` and runs tests using `pytest`.

## How to Run

### Prerequisites
- Docker
- Docker Compose

### Steps
1. Clone the repository and use Tanx.fi Folder:

   ```bash
   git clone https://github.com/ARMNX10/ProductAR_Infra
   cd ProductAR_Infra
2. Ensure Docker is running with superuser (SU) permissions if necessary.
3. Build and run Docker container using : 
   ```bash
   docker-compose up --build


### Additonal cmds
1. If you need to stop the containers, use the following command:
   ```bash
   docker-compose down
1. To remove all containers, networks, and images created by docker-compose up, use:
   ```bash
   docker-compose down --rmi all

