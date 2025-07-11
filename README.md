# 🔍 Deepfake Detection Web App (AWS Lambda + S3 + API Gateway + SightEngine)

This is a serverless web application that allows users to upload an image and detect if it has been AI-generated (deepfake) using the SightEngine API. The app is built with:

- ✅ **Frontend**: HTML/CSS/JS
- ✅ **Backend**: AWS Lambda
- ✅ **Storage**: Amazon S3 (for uploaded images)
- ✅ **API Gateway**: REST API configuration with CORS
- ✅ **Third-party AI Service**: [SightEngine API](https://sightengine.com/)


---

## 📊 Example Verdict Labels

### Score Range	Verdict
### **0.8 – 1.0**	🔴 High probability (Fake)
### **0.6 – 0.79**	🟠 Likely fake
### **0.4 – 0.59**	🟡 Uncertain
### **0.2 – 0.39**	🟢 Low probability
### **0.0 – 0.19**	✅ Very unlikely (Real)

---

## 📁 Project Structure

- aws-deepfake-detector/
- │
- │  .gitignore
- │  README.md
- │          
- ├─api-definition
- │      DeepfakeAPI-stg-oas30-apigateway.json
- │      
- ├─backend
- │  ├─analyze_image
- │  │      lambda_function.py
- │  │      
- │  └─generate_presigned_url
- │          lambda_function.py
- │          
- └─frontend
-  │    └─ Index.html



---


## 🌐 Live API Gateway URL
https://p29u8owr14.execute-api.us-west-1.amazonaws.com/stg


| Endpoint                  | Method | Description                          |
|--------------------------|--------|--------------------------------------|
| `/generate-presigned-url` | `GET`  | Returns a presigned S3 upload URL    |
| `/analyze`               | `GET`  | Analyzes uploaded image using AI     |

---

## 🖼️ Frontend Overview

The `index.html` provides:

- File input and upload button
- Preview of uploaded image
- AI-generated probability score
- Verdict: Real, Uncertain, or Fake

📍 You can test it locally by opening the HTML file in a browser or host it on GitHub Pages / AWS S3.

---

## 🧠 Backend Functions

### 1. `GeneratePresignedUrl`

- Creates a temporary URL to upload a file to your S3 bucket securely
- Returns the necessary fields for a client-side POST request

### 2. `AnalyzeImage`

- Calls the SightEngine API with a public S3 image URL
- Returns a probability score and AI-based verdict

**Environment Variables required for Lambda:**
- `API_USER`: Your SightEngine user ID
- `API_SECRET`: Your SightEngine API secret key

---

## 🔧 How to Deploy

### 🔸 Deploy Lambda Functions (Manual)

1. Go to AWS Lambda Console
2. Create two functions:
   - `GeneratePresignedUrl`
   - `AnalyzeImage`
3. Upload each `lambda_function.py` code
   - For `AnalyzeImage`, bundle with `requests` if not available in the Lambda runtime:

```bash
mkdir package && pip install requests -t package/
cp backend/analyze_image/lambda_function.py package/
cd package && zip -r ../analyze_image.zip .
```


---

# 📎 Additional Notes

### The API Gateway configuration is stored in:

-  api-definition/DeepfakeAPI-stg-oas30-apigateway.json

####  You can import this file in AWS API Gateway to recreate the API

###  Hosting suggestions:

####  GitHub Pages (for frontend) 

####  AWS S3 + CloudFront (for production hosting)