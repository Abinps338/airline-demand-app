from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("AVIATIONSTACK_API_KEY")

app = Flask(__name__)  # ✅ This was missing

def fetch_flight_data():
    url = f"http://api.aviationstack.com/v1/flights?access_key={API_KEY}&limit=20"

    try:
        response = requests.get(url)
        data = response.json()

        flights = []
        for flight in data.get('data', []):
            route = f"{flight['departure']['airport']} - {flight['arrival']['airport']}"
            airline = flight['airline']['name']
            flight_status = flight['flight_status']
            departure_time = flight['departure']['estimated']
            arrival_time = flight['arrival']['estimated']

            flights.append({
                "route": route,
                "airline": airline,
                "status": flight_status,
                "departure": departure_time,
                "arrival": arrival_time
            })

        return flights

    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

@app.route("/")
def home():
    flights = fetch_flight_data()
    return render_template("index.html", flights=flights)

if __name__ == "__main__":
    app.run(debug=True)
