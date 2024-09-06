# Python + FastAPI + Microservices

## How to Run the Project

### Prerequisites

You need to have Docker installed on your machine. Follow this guide to install Docker for your operating system: [https://docs.docker.com/get-started/get-docker/](https://docs.docker.com/get-started/get-docker/).

It is also necessary to have an account on Docker Hub. If you don't have an account, you can create one at [https://hub.docker.com/signup](https://hub.docker.com/signup).

It is also necessary to have a Google Cloud account. If you don’t have one, you can create it here: [https://cloud.google.com/](https://cloud.google.com/)

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

### Running on Kubernetes

1. Let's build the image. Within the directory you cloned, use the following command:

   ```bash
   docker build -t your_user/to-do-list-microservice-python:v0.0.1 .
   ```

2. Verify if your image was built successfully using the command `docker images`.

3. Now enter `docker login` and log in to your Docker Hub account.

4. Now push your image to Docker Hub using:
   ```bash
   docker push your_user/to-do-list-microservice-python:v0.0.1
   ```
5. Once logged into your Google account, go to the home page and create a project with a name of your choice at [https://console.cloud.google.com/projectcreate](https://console.cloud.google.com/projectcreate).

6. After creating the project, enter it by clicking on the notification that will appear on your screen.

7. Now search for `Kubernetes Engine API` and enable it.

8. After enabling your API, search for `Kubernetes clusters` and click on the `Clusters` option. On this page, click on `Create`.

9. In the upper-right corner, next to the `Learn` button, click on `Switch to Standard cluster` and confirm.

10. Now you can click `Create` with all the default settings. The creation of the cluster takes approximately 5 minutes.
