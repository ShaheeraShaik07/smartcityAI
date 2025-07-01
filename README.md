🌆 CityP'AI'Rtner – Smart City Sustainability AI Assistant

CityP'AI'Rtner is an AI-powered smart city sustainability assistant that leverages IBM Granite LLM to help urban planners, policy makers,
and citizens monitor, forecast, and improve environmental KPIs. This application combines FastAPI for the backend, Streamlit for the user-friendly interface, 
and AI to deliver real-time insights for building greener cities
Features:
- 🧠 **AI Assistant (IBM Granite LLM)** – Natural language query support for sustainability guidance.
- 📊 **KPI Forecasting** – Visual analytics and predictions for environmental indicators.
- 🌱 **Eco Tips** – Daily smart sustainability recommendations for urban citizens.
- 📚 **Sustainability Reports** – Structured summaries with actionable metrics.
- 🔄 **Interactive Streamlit Frontend** – Easy-to-use UI to explore smart city solutions.
- ⚡ **FastAPI Backend** – Efficient and modular server design.


📁 Project Structure
├── backend/
│ ├── main.py # FastAPI app with IBM Granite integration
│ └── utils.py # Utility functions for AI queries and responses
├── frontend/
│ └── app.py # Streamlit app with multiple tabs
├── requirements.txt # Required Python libraries
├── README.md # Project documentation
└── .gitignore

->Install dependencies
pip install -r requirements.txt

->Run FastAPI backend
uvicorn backend.main:app --reload


Sample Use Cases

Ask: “How can I reduce air pollution in industrial zones?”
View: Real-time dashboards on water usage, CO2 emissions, waste management
Get: Personalized eco tips for smart living
Analyze: Sustainability forecasts for upcoming city projects

IBM Granite Model Access
To use IBM Granite LLM:
Create an account at IBM watsonx.ai.
Generate an API Key and set your region.
Use credentials as follows:

wml_credentials = {
    "apikey": "YOUR_IBM_API_KEY",
    "url": "https://us-south.ml.cloud.ibm.com"
}

Acknowledgements
-IBM Granite
-Streamlit/HTML-JS
-FastAPI
