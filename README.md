# AWS Serverless Lambda + API Gateway ( mini project )

[Video Tutorial]()

---


## 🔷 Project Overview

This project is a hands-on AWS Serverless Architecture Workshop designed to demonstrate how a <br> 
fully managed, scalable, and event-driven application can be deployed on AWS without managing servers.

The architecture follows a **serverless model**, separating the application into:

- API Layer (API Gateway)
- Compute Layer (AWS Lambda)
- Database Layer (DynamoDB)

The application allows users to send data via API requests (GET/POST), which are processed by  
AWS Lambda and stored in DynamoDB.

![Architecture Diagram](https://github.com/nikiimisal/Project__AWS-Serverless-Mini-Project/blob/main/img/serverless.png?raw=true)


---

## 🏗️ Architecture Design (Layers)

• A **REST API (Amazon API Gateway)** receives incoming client requests (GET/POST).  
• API Gateway triggers the **AWS Lambda function** using Lambda Proxy Integration.  
• The Lambda function processes the request using Python runtime.  
• Processed data is stored in **Amazon DynamoDB**.  
• DynamoDB acts as a fully managed NoSQL database backend.  

This architecture eliminates the need for server provisioning and manual infrastructure management.

---

## 🔐 Security & Networking

- IAM Role is attached to Lambda for secure AWS resource access  
- API Gateway uses Lambda proxy integration  
- No direct database exposure to public internet  
- AWS manages underlying infrastructure security  
- Role-based access control via IAM policies  

---

## 📈 Scalability & Availability

- API Gateway automatically scales based on incoming traffic  
- AWS Lambda scales automatically per request  
- DynamoDB provides built-in high availability  
- No server management or capacity planning required  

---

## 🎯 Purpose of the Workshop

This workshop is intended to:

- Provide hands-on experience with AWS Serverless services  
- Demonstrate event-driven architecture design  
- Understand Lambda execution and API integrations  
- Learn DynamoDB table creation and partition key usage  
- Build a foundational project for Cloud & DevOps roles  

---

---

## 1. Create a DynamoDB Table

- Go to DynamoDB in AWS Console.
- Click **Create table**.
  - **Table name:** `nikhil`
  - **Partition key:** `email`
- Click **Create table**.

---

## 2. Create an IAM Role for Lambda

- Go to **IAM > Roles**.
- Click **Create role**.
  - **Trusted entity type:** AWS Service
  - **Use case:** Lambda
- Attach the **AdministratorAccess** policy.
- **Role name:** `Lambda-Role`
- Click **Create role**.

---

## 3. Create a Lambda Function

- Go to **Lambda > Create function**.
  - **Function name:** `nikii`
  - **Runtime:** Python 3.13
  - **Permissions:** Use an existing role (`Lambda-Role`)
- After creation, go to **Configuration > General configuration > Edit**.
  - **Timeout:** 15 minutes 0 seconds
- Upload your code in the **Code** section.


---

## 4. Create an API Gateway

- Go to **API Gateway > Create API**.
  - Choose **REST API** (Build).
  - **API name:** `Lambda`
- Create a **GET** method:
  - **Integration type:** Lambda proxy integration (Enable)
  - **Lambda function:** Select your Lambda function
- Create a **POST** method:
  - **Integration type:** Lambda proxy integration (Enable)
  - **Lambda function:** Select your Lambda function
- Deploy the API:
  - **Stage name:** `dev`
- Copy the **Invoke URL** (e.g., `https://xxxxxx.execute-api.ap-south-1.amazonaws.com/dev`).

---
---
---


  ===<br>
  ===<br>
  ===<br>


##  Optional

 ## 5. Create an ACM Certificate

- Go to **AWS Certificate Manager (ACM)**.
- Request a public certificate for your custom domain (e.g., `api.nikiimisal.xyz`).
- Complete domain validation as instructed.

---

## 6. Access API Gateway via Custom Domain

- In **API Gateway**, go to **Custom domain names**.
- Click **Create** or **Add domain name**.
  - **Domain name:** `api.nikiimisal.xyz`
  - Attach the ACM certificate.
- Configure **API mappings**:
  - **API:** `Lambda`
  - **Stage:** `dev`
  - **Path (optional):** `dev`

---

## 7. Add a Record in Route 53

- Go to **Route 53 > Hosted zones**.
- Create a new **Record**:
  - **Record name:** `api`
  - **Record type:** Alias
  - **Alias to:** API Gateway domain
  - **Region:** Select your region
  - **Value:** Select the API Gateway URL
 

  ===<br>
  ===<br>
  ===<br>

---
---


## Clean-up

- Api Gateway
- lambada
- Dynamo DB


**Done! Your serverless Lambda API is now accessible via your custom domain.**

---
---
---
