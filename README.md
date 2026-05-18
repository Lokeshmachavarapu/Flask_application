# DevOps Flask Application

This is a beginner-friendly DevOps project demonstrating:

- Docker containerization
- CI/CD concepts
- Kubernetes deployment
- Jenkins automation
- Monitoring with Prometheus & Grafana

## Tech Stack

- Python Flask
- Docker
- Jenkins
- Kubernetes
- Prometheus
- Grafana

## Project Structure

```bash
devops-project/
│
├── app/
├── Dockerfile
├── k8s/
├── Jenkinsfile
└── README.md
```

## Docker Commands

Build Image:

```bash
docker build -t flask-devops-app .
```

Run Container:

```bash
docker run -d -p 5000:5000 flask-devops-app
```
