# Python + FastAPI + Microservices

## How to Run the Project

### Prerequisites

You need to have Docker installed on your machine. Follow this guide to install Docker for your operating system: [https://docs.docker.com/get-started/get-docker/](https://docs.docker.com/get-started/get-docker/).

### Running in Development Environment

To run the project in a development environment, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/hernique33comiitei/to-do-list-microservice-python.git
   ```
2. Navigate to the directory and rename `.env.example` to `.env`.

3. After doing that, simply run the command `docker compose up --build`. If you prefer not to keep your terminal busy, use `docker compose up --build -d` instead, and then check the created containers with `docker compose ps`.

4. To check if everything is working, open your browser and go to: [http://localhost:5000/docs](http://localhost:5000/docs).

5. If something doesn’t work as expected, check the port settings in the newly renamed `.env` file. There may be a conflict with another project or service running on your machine.
