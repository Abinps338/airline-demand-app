# ✈️ Airline Booking Demand Web App

This is a Flask-based web application that displays **real-time market demand trends** in the airline industry using data from the **AviationStack API**.

---

## 🚀 Features

- 🔄 Fetches **live flight data** via API
- 📊 Visualizes **popular routes** using charts
- 📋 Displays flight status in a clean table format
- 🔍 Ready for future filters (by city, airline, time)
- ✅ Built with open, free tools — lightweight & fast

---

## 🧠 Approach

1. Used **Flask** to create a simple web interface
2. Fetched real-time data using **AviationStack API**
3. Processed and displayed:
   - Route (departure → arrival)
   - Airline
   - Status (active, delayed, landed)
   - Estimated departure & arrival times
4. Visualized popular routes using **Chart.js**
5. Clean separation of logic, views, and styling

---

## 🛠️ Tech Stack

- **Python** (Flask, Requests, Dotenv)
- **HTML/CSS (Jinja2 Templates)**
- **Chart.js** for visualization
- **AviationStack API** for flight data

---

## 📦 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Abinps338/airline-demand-app.git
cd airline-demand-app
