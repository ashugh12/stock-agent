# Stock Market AI Analysis API

This is a **FastAPI** application that fetches real-time stock prices from the **Alpha Vantage API** and provides AI-generated buy/sell/hold recommendations using **Google Gemini AI**.

## 🚀 Features
- Fetch latest stock prices using **Alpha Vantage API**
- Analyze stock trends based on price fluctuations
- Generate AI-based investment recommendations
- Health check endpoint for monitoring API status

---

## 🛠 Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo.git
cd your-repo
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and add:
```ini
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
GEMINI_API_KEY=your_gemini_api_key
```

Alternatively, export them manually:
```bash
export ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
export GEMINI_API_KEY=your_gemini_api_key
```

### 5️⃣ Run the FastAPI Server
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 📡 API Endpoints

### 🔹 Get Stock Analysis
Fetch stock price, trend, and AI-generated recommendation.
```http
GET /stock/{symbol}
```
**Example Request:**
```http
GET /stock/AAPL
```
**Response:**
```json
{
  "stock": "AAPL",
  "latest_price": 172.50,
  "previous_price": 170.00,
  "trend": "rising",
  "recommendation": "The stock AAPL has a current price of 172.50 and was 170.00 yesterday. It is currently rising. An investor should HOLD as it shows potential for growth."
}
```

### 🔹 Health Check
Check if the API is running.
```http
GET /health
```
**Response:**
```json
{
  "status": "API is running"
}
```

---

## 🐳 Deploy with Docker

### 1️⃣ Build the Docker Image
```bash
docker build -t stock-ai-api .
```

### 2️⃣ Run the Container
```bash
docker run -p 8000:8000 stock-ai-api
```

---

## 📝 Notes
- Ensure that your **Alpha Vantage API Key** has sufficient quota to fetch stock data.
- This API relies on **Google Gemini AI** to generate recommendations, ensure API access is enabled.

---

## 🤝 Contributing
Feel free to open issues and submit pull requests!

---

## 📜 License
MIT License. See `LICENSE` for details.

