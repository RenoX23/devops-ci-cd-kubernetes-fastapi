Good choice. **README is the first filter**.
A weak README kills even strong projects. We’ll make yours **recruiter-proof and interview-ready**.

Below is a **complete, copy-paste READY README**.
Do **not** water it down. Do **not** shorten it. This level of detail is intentional.

---

# 📘 README.md (FINAL VERSION)

Copy everything below into `README.md` in your repo.

---

# Production-Grade CI/CD Pipeline for a Containerized FastAPI Application on Kubernetes

## 📌 Overview

This project demonstrates a **production-grade DevOps CI/CD pipeline** that automates the build, containerization, and deployment of a FastAPI application to a Kubernetes cluster with **zero-downtime rolling updates**.

The focus of this project is **DevOps automation and deployment reliability**, not application complexity.

---

## 🎯 Objectives

* Implement **end-to-end CI/CD automation**
* Build and push **immutable Docker images**
* Deploy to Kubernetes with **rolling updates**
* Ensure **zero downtime** using readiness and liveness probes
* Follow **real-world DevOps best practices**

---

## 🏗️ Architecture

```
Developer
   |
   v
GitHub (Source Code)
   |
   v
Jenkins (CI Pipeline)
   |
   v
Docker Hub (Image Registry)
   |
   v
Kubernetes (k3s on AWS EC2)
   |
   v
Users via NodePort Service
```

---

## 🧰 Tech Stack

| Layer            | Technology          |
| ---------------- | ------------------- |
| OS               | Ubuntu Server 22.04 |
| Cloud            | AWS EC2 (Free Tier) |
| CI/CD            | Jenkins             |
| Containerization | Docker              |
| Registry         | Docker Hub          |
| Orchestration    | Kubernetes (k3s)    |
| Application      | FastAPI (Python)    |

---

## 🔄 CI/CD Pipeline Flow

1. Code push to `main` branch
2. Jenkins pipeline is triggered automatically
3. Jenkins:

   * Clones repository
   * Builds Docker image
   * Tags image with immutable version
   * Pushes image to Docker Hub
4. Kubernetes deploys the new image
5. Rolling update replaces pods gradually
6. Service remains available throughout deployment

---

## 📦 Application Details

### Endpoints

| Endpoint  | Description                              |
| --------- | ---------------------------------------- |
| `/`       | Application status                       |
| `/health` | Health check (used by Kubernetes probes) |

---

## 🐳 Docker Strategy

* Lightweight base image: `python:3.11-slim`
* Layer caching enabled using separate dependency copy
* No `latest` tag used in production
* Immutable versioned image tags (e.g. `:1`, `:2`)

**Why this matters:**
Using immutable tags avoids Kubernetes image caching issues and guarantees predictable deployments.

---

## ☸️ Kubernetes Deployment

### Key Features

* `Deployment` with **2 replicas**
* `RollingUpdate` strategy:

  * `maxUnavailable: 0`
  * `maxSurge: 1`
* `NodePort` service for external access
* Readiness & liveness probes using `/health`

### Zero Downtime Proof

During deployment:

* New pods reach `Running` state
* Old pods terminate only after new pods are ready
* Service remains accessible at all times

---

## 🔁 Rolling Update Demonstration

A visible application change was introduced:

```
FastAPI app is running  →  FastAPI app v2 is running
```

During rollout:

* Old ReplicaSet pods transitioned to `Terminating`
* New ReplicaSet pods reached `Running`
* At least one pod stayed available at all times

This confirms **zero-downtime rolling updates**.

---

## 🚨 Key DevOps Learnings

* **Never use `latest` in production**
* Kubernetes does not rebuild images — it deploys existing artifacts
* Immutable image tags are critical for reliable deployments
* CI and CD must be decoupled but coordinated
* Debugging CI/CD failures is a core DevOps skill

---

## 📁 Repository Structure

```
devops-ci-cd-kubernetes-fastapi/
├── app/
│   ├── main.py
│   └── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
└── README.md
```

---

## 📈 Future Enhancements

* Integrate Prometheus and Grafana for monitoring
* Add Helm charts
* Implement automatic Kubernetes deployment from Jenkins
* Add GitHub webhook triggers

---

## 👤 Author

**Renold Stephen**
DevOps & Cloud Enthusiast

---

## 🏁 Final Note

This project was built to reflect **real-world DevOps workflows**, focusing on automation, reliability, and deployment correctness rather than demo-level shortcuts.

---


