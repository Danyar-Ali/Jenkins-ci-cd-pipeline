# Jenkins CI/CD Pipeline – Website Health Check

This project implements a Jenkins-based CI/CD pipeline that performs automated
health checks against a deployed web service before executing a deployment step.

The pipeline verifies that a target endpoint is reachable and responding
correctly before allowing further stages to run.

The goal is to illustrate how CI/CD pipelines can automate reliability checks
and prevent faulty deployments.

---

## Architecture

```
GitHub → Jenkins Pipeline → Python Health Check → Deployment Stage
```

The pipeline performs the following steps:

1. Checkout source code from GitHub
2. Install Python dependencies
3. Execute a website health check script
4. Retry the check if the service is temporarily unavailable
5. Run a simulated deployment step

If the website returns a non-200 HTTP status code, the pipeline fails.

---

## Project Structure

```
jenkins-website-health-check/
├─ monitor/
│ └─ check_site.py
│
├─ scripts/
│ └─ deploy.sh
│
├─ requirements.txt
├─ Jenkinsfile
└─ README.md
```

## Pipeline Stages

### Checkout
Retrieves the source code from GitHub.

### Install Dependencies
Creates a Python virtual environment and installs required packages.

### Run Health Check
Runs a Python monitoring script that verifies:

- HTTP response status
- Response latency
- Endpoint availability

If the health check fails, the pipeline stops.

### Deploy
Executes a simulated deployment script.

---

## Environment Variables

The target endpoint is configured via an environment variable.

Example:

```
TARGET_URL=https://example.com
```

This allows the pipeline to support different environments such as:

- development
- staging
- production

---

## Health Check Script

The monitoring script performs a simple HTTP request and verifies that:

- The service responds
- Status code is 200
- Response time is within acceptable limits

If the service fails these checks, the pipeline exits with a non-zero status,
causing Jenkins to fail the build.

---

## Example Use Cases

This type of pipeline is commonly used for:

- Synthetic monitoring
- Pre-deployment verification
- Service availability checks
- Basic reliability automation

---

## Technologies Used

• Jenkins
• Python
• Bash
• GitHub
• CI/CD Pipelines

---

# How to Deploy

Follow these steps to run the Jenkins CI/CD pipeline locally.

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/jenkins-website-health-check.git
cd jenkins-website-health-check
```
### 2. Start Jenkins using Docker
```
docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts
```

### 3. Retrieve the Jenkins admin password
```
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

### 4. Open Jenkins locally in your browser:
```
http://localhost:8080
```
Paste the password and install the suggested plugins.

### 5. Create a Jenkins Pipeline Job

In jenkins:
- Click New Item
- Select Pipeline
- Name the job ```website-health-check```

### 6. Connect the pipeline to the repository

Under the pipeline configuration:

```
Pipeline script from SCM
SCM: Git
Repository URL: https://github.com/YOUR_USERNAME/jenkins-website-health-check.git
Branch: main
Script Path: Jenkinsfile
```

### 7. Run the Pipeline

Click Build Now.

## Future Improvements

Possible extensions include:

- SSL certificate validation
- DNS resolution checks
- Response header validation
- Slack or email alerting
- Automatic rollback on failure


# Author

Danyar Ali Cloud & DevOps Engineer
