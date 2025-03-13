<<<<<<< HEAD
# Projects_Ramadan_coding_nights_python
=======
📌 FastAPI - Side Hustles & Money Quotes API
Welcome to the Side Hustles & Money Quotes API, a simple yet powerful FastAPI project that serves random business ideas and financial wisdom to inspire and motivate users!

🌟 Features
✅ FastAPI-Powered - Blazing-fast performance with modern Python web framework.
✅ Two Fun Endpoints - Get random side hustles and money quotes.
✅ Secure API Key Authentication - Only valid requests are accepted.
✅ Minimal & Clean Code - Easy to understand and modify.
✅ Randomized Responses - Get a new idea or quote every time you call the API.

🚀 Endpoints
Method	Endpoint	Description
GET	/side_hustles	Returns a random side hustle idea
GET	/money_quotes	Returns a random money-related quote
🔒 Authentication
All requests require an API key. Pass it as a query parameter:


🛠 How to Run Locally
1️⃣ Install Dependencies
Ensure you have FastAPI and Uvicorn installed:

pip install fastapi uvicorn
2️⃣ Run the API

uvicorn main:app --reload
3️⃣ Test in Your Browser
Once running, test the endpoints in your browser or tools like Postman:

Side Hustle → http://127.0.0.1:8000/side_hustles?apiKey=12345678901
Money Quote → http://127.0.0.1:8000/money_quotes?apiKey=12345678901

📝 Example API Responses
✅ Side Hustle Response

{
  "side_hustle": "Freelancing - Start offering your skills online!"
}

✅ Money Quote Response

{
  "money_quote": "The more you learn, the more you earn. - Warren Buffett"
}

❌ Error Response (Invalid API Key)

{
  "Error": "Invalid API key"
}
📌 Technologies Used
Python 3 🐍
FastAPI ⚡
Uvicorn 🌐
>>>>>>> d27198a (change main file name to app)
