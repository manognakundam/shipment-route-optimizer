
import pandas as pd
from pathlib import Path
from route_scorer import score_routes

data_file = Path(__file__).parent / "data" / "routes.csv"

df = pd.read_csv(data_file)

# Test the scoring algorithm on the first shipment.
shipment_id = df["shipment_id"].iloc[0]
routes = df[df["shipment_id"] == shipment_id].copy()

scored_routes = score_routes(routes)

scored_routes = scored_routes.sort_values(
    "final_score", ascending=False
)

print(f"\nShipment: {shipment_id}")
print("\nRoute scores:\n")

print(
    scored_routes[
        ["route_id", "cost", "transit_days",
         "delay_probability", "risk_score", "final_score"]
    ].round(2).to_string(index=False)
)

best_route = scored_routes.iloc[0]

print(f"\nRecommended route: {best_route['route_id']}")
print(f"Final score: {best_route['final_score']:.2f}/100")
