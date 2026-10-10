
import csv
import random
from pathlib import Path

random.seed(42)

OUTPUT_FILE = Path(__file__).parent / "data" / "routes.csv"

origins = ["Shanghai", "Singapore", "Mumbai", "Rotterdam"]
destinations = ["Los Angeles", "London", "New York", "Sydney"]

hubs = [
    "Singapore Hub",
    "Dubai Hub",
    "Colombo Hub",
    "Suez Canal",
    "Panama Canal",
    "Malacca Strait",
    "Mediterranean Hub",
    "Pacific Hub"
]

fieldnames = [
    "shipment_id",
    "route_id",
    "origin",
    "destination",
    "route",
    "cost",
    "transit_days",
    "delay_probability",
    "risk_score"
]

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for shipment_num in range(1, 31):
        origin = random.choice(origins)
        destination = random.choice(destinations)

        for route_num in range(1, 5):
            transit_days = random.randint(7, 25)
            cost = random.randint(30000, 100000)
            delay_probability = round(random.uniform(0.05, 0.40), 2)
            risk_score = random.randint(1, 10)

            route_hubs = random.sample(hubs, 2)
            route_description = (
                f"{origin} -> {route_hubs[0]} -> "
                f"{route_hubs[1]} -> {destination}"
            )

            writer.writerow({
                "shipment_id": f"S{shipment_num:03d}",
                "route_id": f"R{route_num}",
                "origin": origin,
                "destination": destination,
                "route": route_description,
                "cost": cost,
                "transit_days": transit_days,
                "delay_probability": delay_probability,
                "risk_score": risk_score
            })

print(f"Dataset generated successfully: {OUTPUT_FILE}")
print("Shipments: 30")
print("Routes per shipment: 4")
print("Total route options: 120")