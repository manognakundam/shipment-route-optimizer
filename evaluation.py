
import pandas as pd
from pathlib import Path
from route_scorer import score_routes

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "routes.csv"
RESULT_FILE = BASE_DIR / "data" / "recommendations.csv"


def evaluate_optimizer():
    routes = pd.read_csv(DATA_FILE)
    recommendations = pd.read_csv(RESULT_FILE)

    cheapest_count = 0
    fastest_count = 0

    for _, shipment_routes in routes.groupby("shipment_id"):
        shipment_id = shipment_routes["shipment_id"].iloc[0]

        recommended_id = recommendations.loc[
            recommendations["shipment_id"] == shipment_id,
            "recommended_route"
        ].iloc[0]

        cheapest_id = shipment_routes.loc[
            shipment_routes["cost"].idxmin(), "route_id"
        ]

        fastest_id = shipment_routes.loc[
            shipment_routes["transit_days"].idxmin(), "route_id"
        ]

        if recommended_id == cheapest_id:
            cheapest_count += 1

        if recommended_id == fastest_id:
            fastest_count += 1

    total = len(recommendations)

    print("\nOPTIMIZER EVALUATION")
    print("=" * 45)
    print(f"Shipments evaluated: {total}")
    print(
        f"Recommended route is cheapest: "
        f"{cheapest_count}/{total} ({cheapest_count / total:.0%})"
    )
    print(
        f"Recommended route is fastest: "
        f"{fastest_count}/{total} ({fastest_count / total:.0%})"
    )

    print("\nAverage recommended-route metrics:")
    print(f"Cost: {recommendations['cost'].mean():.2f}")
    print(
        f"Transit time: "
        f"{recommendations['transit_days'].mean():.2f} days"
    )
    print(
        f"Delay probability: "
        f"{recommendations['delay_probability'].mean():.1%}"
    )
    print(
        f"Risk score: {recommendations['risk_score'].mean():.2f}/10"
    )


if __name__ == "__main__":
    evaluate_optimizer()
