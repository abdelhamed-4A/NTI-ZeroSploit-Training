# 🚀 Hello World Kubernetes Deployment

## 🎯 Overview
This project demonstrates how to deploy a simple **Hello World** application using **Kubernetes**. It includes:
✅ **Deployment** → Runs the `crccheck/hello-world` Docker image 🐳  
✅ **Service** → Exposes the application internally 🔗  
✅ **Ingress** → Routes external traffic using a custom domain 🌍

---

## 🔧 Prerequisites
- A **Kubernetes cluster** with an **NGINX Ingress Controller** installed.
- `kubectl` configured to access your cluster.

---

## 🏗️ Deployment Steps

### 1️⃣ Create the Deployment 📦
The deployment runs the `crccheck/hello-world` image and exposes port **8000**.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-world-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hello-world
  template:
    metadata:
      labels:
        app: hello-world
    spec:
      containers:
      - name: hello-world-container
        image: crccheck/hello-world
        ports:
        - containerPort: 8000
```
🚀 **Apply the deployment:**
```bash
kubectl apply -f deployment.yaml
```

---

### 2️⃣ Create the Service 🔄
The service exposes the deployment internally on port **80** and routes traffic to the pods on port **8000**.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: hello-world-service
spec:
  selector:
    app: hello-world
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
```
🚀 **Apply the service:**
```bash
kubectl apply -f service.yaml
```

---

### 3️⃣ Create the Ingress 🌐
The ingress routes external traffic using the domain **sub-domain.abdelhamedabdelnasser.com**.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: hello-world-ingress
spec:
  ingressClassName: nginx
  rules:
  - host: sub-domain.abdelhamedabdelnasser.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: hello-world-service
            port:
              number: 80
```
🚀 **Apply the ingress:**
```bash
kubectl apply -f ingress.yaml
```

---

## 🧪 Testing the Application

### 1️⃣ Using `kubectl port-forward` 🛠️
```bash
kubectl port-forward svc/hello-world-service 8000:80
```
Then, open in a browser or use `curl`:
```bash
http://localhost:8000
```

---

### 2️⃣ Testing the Ingress 🌍
#### ✅ **Method 1: Use curl with a Custom Host Header**
```bash
curl -H "Host: sub-domain.abdelhamedabdelnasser.com" http://198.96.95.206
```
![curl](./images/curl.jpg)

#### ✅ **Method 2: Use a Browser Extension**
- Install **ModHeader** (Chrome/Edge) and add:
  - **Header Name:** `Host`
  - **Header Value:** `sub-domain.abdelhamedabdelnasser.com`
- Navigate to: `http://198.96.95.206`

![Hello_World](./images/Hello_World.jpg)

#### ✅ **Method 3: Use a Temporary DNS Service**
```bash
http://sub-domain.abdelhamedabdelnasser.com.198.96.95.206.sslip.io/
```
![sslip](./images/sslip-io.jpg)

---

## 🔍 Verify Resources ✅
Check the status of your Kubernetes resources:
```bash
kubectl get deployment hello-world-deployment
kubectl get service hello-world-service
kubectl get ingress hello-world-ingress
```

---

## 🗑️ Clean Up 🧹
To delete all resources:
```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
kubectl delete -f ingress.yaml
```

---

## 📌 Notes
- Replace `198.96.95.206` with the actual IP address of your ingress.
- Ensure your **DNS** or `/etc/hosts` is configured correctly if using a custom domain.

🎉 **Your Hello World Kubernetes deployment is now complete** 🚀