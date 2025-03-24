# **NewsApp - Django Multi-App Project**

## **Overview**
NewsApp is a lightweight, Django-based tech news aggregator designed to display static technology-related updates. The project follows a multi-app structure, with containerization using Docker and automated deployment via Jenkins CI/CD.

## **Project Structure**
- **Project Name:** StudentProject  
- **Apps:**
  - **NewsApp:** Displays "Latest News" and "Tech Trends" sections.
  - **TrendsApp:** Provides static pages such as "AI Trends" and "Blockchain Updates."

## **Features**
✔️ Simple and lightweight Django project with static content  
✔️ No database required – purely template-based rendering  
✔️ Dockerized for easy deployment  
✔️ Jenkins-powered CI/CD pipeline for automated builds and deployment  
✔️ Fully containerized with a pre-built Docker image available on Docker Hub  

---

## **Installation & Setup**

### **Run Locally**
#### **Prerequisites:**
- Python 3.x installed
- Django installed

Run the following commands:
```sh
# Clone the repository
git clone https://github.com/SRCEM-AIML/C_50-Assignment-2.git
cd studentproject

# Install dependencies
pip install django

# Start the development server
python manage.py runserver
```
Access the application at: `http://127.0.0.1:8000/`

### **Run with Docker**
#### **Prerequisites:**
- Docker installed

Run the following commands:
```sh
# Build Docker Image
docker build -t newsapp .

# Run Docker Container
docker run -p 8000:8000 newsapp
```
Access the application at: `http://localhost:8000/`

---

## **CI/CD with Jenkins**
This project includes a `Jenkinsfile` to automate deployment, ensuring a seamless CI/CD process. The pipeline:
1. Clones the GitHub repository.
2. Builds the Docker image.
3. Pushes the Docker image to Docker Hub.

---

## **Deployment to Docker Hub**
The latest Docker image is available on Docker Hub:
🔗 **Docker Hub Repository:** (https://hub.docker.com/repositories/vedanshgupta25)

## **Repository Links**
🔗 **GitHub Repository:** (GitHub Link](https://github.com/SRCEM-AIML/C_50-Assignment-2)

---

### 🚀 *Happy Coding!*

