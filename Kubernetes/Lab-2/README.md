# 📌 Integrate MongoDB & Mongo Express on Kubernetes

This project deploys **MongoDB** and **Mongo Express** on a Kubernetes cluster using a **StatefulSet** and **Secrets** for authentication.

---

## 🚀 Features
- **MongoDB** 🗄️ - NoSQL Database deployed as a **StatefulSet**
- **Mongo Express** 💻 - Web-based MongoDB admin interface
- **Kubernetes Secrets** 🔑 - Securely store database credentials
- **Persistent Storage** 💾 - Data persists across pod restarts
- **Port Forwarding** 🌐 - Access Mongo Express locally

---

## 📂 Project Structure
```
📁 Lab-2
 ├── mongodb-namespace.yaml         # Namespace for MongoDB
 ├── mongodb-deployment.yaml        # MongoDB StatefulSet deployment
 ├── mongodb-service.yaml           # Service to expose MongoDB
 ├── mongo-express-deployment.yaml  # Mongo Express deployment
 └── mongo-express-service.yaml     # Service to expose Mongo Express
```

---

## 🛠️ Setup & Deployment

### 1️⃣ Create a Namespace (Optional)
```yaml
# mongodb-namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: mongodb
```

```sh
kubectl apply -f mongodb-namespace.yaml
```

### 2️⃣ Create Secrets for MongoDB Credentials
```sh
kubectl create secret generic mongodb-secrets \
  --namespace=mongodb \
  --from-literal=root-username=admin \
  --from-literal=root-password=SecurePass123! \
  --from-literal=database=mydb
```

### 3️⃣ Deploy MongoDB with Authentication
```yaml
# mongodb-deployment.yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mongodb
  namespace: mongodb
spec:
  serviceName: mongodb
  replicas: 1
  selector:
    matchLabels:
      app: mongodb
  template:
    metadata:
      labels:
        app: mongodb
    spec:
      containers:
      - name: mongodb
        image: mongo:6.0
        env:
        - name: MONGO_INITDB_ROOT_USERNAME
          valueFrom:
            secretKeyRef:
              name: mongodb-secrets
              key: root-username
        - name: MONGO_INITDB_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mongodb-secrets
              key: root-password
        ports:
        - containerPort: 27017
        volumeMounts:
        - name: mongodb-pvc
          mountPath: /data/db
  volumeClaimTemplates:
  - metadata:
      name: mongodb-pvc
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 2Gi
```

```yaml
# mongodb-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: mongodb
  namespace: mongodb
spec:
  selector:
    app: mongodb
  ports:
    - protocol: TCP
      port: 27017
      targetPort: 27017
```

```sh
kubectl apply -f mongodb-deployment.yaml
kubectl apply -f mongodb-service.yaml
```

### 4️⃣ Deploy MongoDB-Express
```yaml
# mongo-express-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mongo-express
  namespace: mongodb
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mongo-express
  template:
    metadata:
      labels:
        app: mongo-express
    spec:
      containers:
      - name: mongo-express
        image: mongo-express:1.0
        env:
        - name: ME_CONFIG_MONGODB_ADMINUSERNAME
          valueFrom:
            secretKeyRef:
              name: mongodb-secrets
              key: root-username
        - name: ME_CONFIG_MONGODB_ADMINPASSWORD
          valueFrom:
            secretKeyRef:
              name: mongodb-secrets
              key: root-password
        - name: ME_CONFIG_MONGODB_URL
          value: "mongodb://admin:SecurePass123!@mongodb.mongodb.svc.cluster.local:27017/"
```

```yaml
# mongo-express-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: mongo-express
  namespace: mongodb
spec:
  type: NodePort
  selector:
    app: mongo-express
  ports:
    - protocol: TCP
      port: 8081
      targetPort: 8081
```

```sh
kubectl apply -f mongo-express-deployment.yaml
kubectl apply -f mongo-express-service.yaml
```

---

## 📌 Accessing Mongo Express

### 🌍 Option 1: Using Port Forwarding
```sh
kubectl port-forward -n mongodb svc/mongo-express 8888:8081
```
![forward](./images/port-forward.jpg)

- Open your browser and visit: **http://localhost:8888**
- Login using credentials: **admin / SecurePass123!**

#### Login
![login](./images/login.jpg)
#### Dashboard
![localhost](./images/localhost.jpg)
#### Viewing Admin Database
![admin](./images/admin.jpg)
#### Viewing System Users
![systemUsers](./images/system-users.jpg)
#### Viewing Local Database
![local](./images/local.jpg)


### 🌐 Option 2: Test connectivity from the mongo-express pod
```sh
kubectl exec -n mongodb -it mongodb-0 -- mongosh -u admin -p SecurePass123!
```

![exec](./images/exec.jpg)

---

## 🔍 Debugging

### 📜 Check Pod Status
```sh
kubectl get pods -n mongodb
```

### 📄 View Mongo Express Logs
```sh
kubectl logs -n mongodb -l app=mongo-express
```

### 🏗️ Restart Mongo Express
```sh
kubectl delete pod -n mongodb -l app=mongo-express
```

---

## 🎯 Key Takeaways
✅ Uses **StatefulSet** for MongoDB persistence

✅ Stores sensitive data in **Kubernetes Secrets**

✅ Provides **Mongo Express** for easy database management

✅ Uses **Services** to enable internal and external communication

✅ Implements **authentication** for secure access

---

