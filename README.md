# 🚀 URL Threat Detector  
Detect Scam Emails and Malicious URLs with Flask + Gemini AI  

![Project Screenshot](https://via.placeholder.com/1200x600)  

---

## 📌 Overview  
The **URL Threat Detector** is a Flask-based application that detects and classifies URLs and emails as **benign**, **phishing**, **malware**, or **defacement** using **Gemini AI**. This project enhances online security by identifying and blocking malicious links and scam emails.  

---

## 🎯 Features  
✅ Real-time URL threat detection  
✅ Classifies URLs into four categories: Benign, Phishing, Malware, Defacement  
✅ API-based detection using Flask  
✅ AI-driven analysis with Gemini AI  
✅ Lightweight and easy to use  

---

## 🛠️ Tech Stack  
| Technology | Purpose |  
|-----------|---------|  
| **Flask** | Backend Framework |  
| **Gemini AI** | AI Model for Threat Detection |  
| **HTML, CSS, JavaScript** | Frontend |  

---

## 📂 Project Structure  
url-threat-detector/
├── app.py
├── templates/
│ ├── index.html
├── .env
└── README.md


---

## 🚀 Setup Instructions  

### 1. **Clone the repository**  
```bash
git clone https://github.com/your-username/url-threat-detector.git
cd url-threat-detector
```
# 2. Setup Environment
Create a virtual environment:
``` bash
python -m venv venv  
source venv/bin/activate
```
# Install dependencies:
```
pip install -r requirements.txt
```  
# Create .env file and add your Gemini API Key:
```
GENAI_API_KEY="your-gemini-api-key"
```
# 3. Run Flask Server
```
python app.py
```
# 4. Access in Browser
```Open http://127.0.0.1:5000 in your browser```
# ⚙️ API Endpoints
Method	Endpoint	Description
POST	/analyze-url/	Analyze the URL and return classification
POST	/analyze-email/	Analyze the email content for threats
💡 Example Request

Request:
```bash
Edit
{
  "url": "http://example-phishing.com"
}
```
Response:
```bash
{
  "classification": "Phishing",
}
```
