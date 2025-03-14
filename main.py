from flask import Flask, render_template, request
import google.generativeai as genai
import os
import PyPDF2

# ✅ Initialize Flask app
app = Flask(__name__)

# ✅ Set up the Google API Key
API_KEY = "AIzaSyCfRw4jp65Dl-jiA95TOz6e0hauRLWJW4o"  # Replace with your actual API key
if not API_KEY:
    raise ValueError("Google API key is missing.")

os.environ["GOOGLE_API_KEY"] = API_KEY
genai.configure(api_key=API_KEY)

# ✅ Initialize the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# ✅ Function to predict fake or real email content
def predict_fake_or_real_email_content(text):
    prompt = f"""
    You are an expert in identifying scam messages in text or email. Analyze the given text and classify it as:

    - **Real/Legitimate** – Authentic, safe message
    - **Scam/Fake** – Phishing, fraud, or suspicious message

    **Text:**
    {text}

    **Output:**
    - State if it's real or a scam, and explain why.
    - Provide a concise, clear response.
    """

    try:
        response = model.generate_content(prompt)
        return response.text.strip() if response else "Classification failed."
    except Exception as e:
        return f"Error: {str(e)}"

# ✅ Function to detect URL type
def url_detection(url):
    prompt = f"""
    Classify the given URL into one of these categories:

    1. Benign – Safe website.
    2. Phishing – Fraudulent website designed to steal information.
    3. Malware – Distributes viruses or malicious software.
    4. Defacement – Hacked or altered website.

    **Input URL:** {url}

    **Output:**
    - Return only the classification (e.g., benign, phishing, malware, defacement).
    """

    try:
        response = model.generate_content(prompt)
        return response.text.strip() if response else "Detection failed."
    except Exception as e:
        return f"Error: {str(e)}"

# ✅ Route for home page
@app.route('/', methods=['GET']) 
def home():
    return render_template("index.html")

# ✅ Route for scam detection
@app.route('/scam/', methods=['POST'])
def detect_scam():
    if 'file' not in request.files:
        return render_template("index.html", message="No file uploaded.")

    file = request.files['file']
    extracted_text = ""

    if file and file.filename.endswith('.pdf'):
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            extracted_text = " ".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
        except Exception as e:
            return render_template("index.html", message=f"PDF processing error: {str(e)}")

    elif file and file.filename.endswith('.txt'):
        extracted_text = file.read().decode("utf-8")
    else:
        return render_template("index.html", message="Invalid file type. Please upload a PDF or TXT file.")

    if not extracted_text.strip():
        return render_template("index.html", message="File is empty or text could not be extracted.")

    # ✅ Predict scam or real content
    message = predict_fake_or_real_email_content(extracted_text)
    return render_template("index.html", message=message)

# ✅ Route for URL prediction
@app.route('/predict/', methods=['POST'])
def predict_url():
    url = request.form.get('url', '').strip()

    if not url.startswith(("http://", "https://")):
        return render_template("index.html", message="Invalid URL format.", input_url=url)

    classification = url_detection(url)
    return render_template("index.html", input_url=url, predicted_class=classification)

# ✅ Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5001)
