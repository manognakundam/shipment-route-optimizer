
import pandas as pd
from pathlib import Path
from route_scorer import score_routes

DATA_FILE = Path(__file__).parent / "data" / "routes.csv"


def recommend_routes(df, weights):
    results = []

    for shipment_id, group in df.groupby("shipment_id"):
        scored = score_routes_with_weights(group, weights)
        best = scored.sort_values(
            "final_score", ascending=False
        ).iloc[0]

        results.append({
            "shipment_id": shipment_id,
            "recommended_route": best["route_id"],
            "final_score": best["final_score"]
        })

    return pd.DataFrame(results)


def score_routes_with_weights(routes, weights):
    routes = routes.copy()

    for column in weights:
        minimum = routes[column].min()
        maximum = routes[column].max()

        if maximum == minimum:
            routes[f"{column}_score"] = 1.0
        else:
            routes[f"{column}_score"] = (
                (maximum - routes[column]) / (maximum - minimum)
            )

    routes["final_score"] = sum(
        routes[f"{column}_score"] * weight
        for column, weight in weights.items()
    ) * 100

    return routes


def main():
    df = pd.read_csv(DATA_FILE)

    scenarios = {
        "Balanced": {
            "cost": 0.40,
            "transit_days": 0.30,
            "delay_probability": 0.20,
            "risk_score": 0.10
        },
        "Cost-focused": {
            "cost": 0.60,
            "transit_days": 0.20,
            "delay_probability": 0.15,
            "risk_score": 0.05
        },
        "Risk-focused": {
            "cost": 0.20,
            "transit_days": 0.20,
            "delay_probability": 0.25,
            "risk_score": 0.35
        }
    }

    recommendations = {}

    for name, weights in scenarios.items():
        result = recommend_routes(df, weights)
        recommendations[name] = result.set_index(
            "shipment_id"
        )["recommended_route"]

    comparison = pd.DataFrame(recommendations)
    comparison["changed_under_cost_focus"] = (
        comparison["Balanced"] != comparison["Cost-focused"]
    )
    comparison["changed_under_risk_focus"] = (
        comparison["Balanced"] != comparison["Risk-focused"]
    )

    print("\nSENSITIVITY ANALYSIS")
    print("=" * 55)
    print(comparison.to_string())

    print("\nRecommendation changes:")
    print(
        "Cost-focused:",
        int(comparison["changed_under_cost_focus"].sum()),
        "of", len(comparison), "shipments"
    )
    print(
        "Risk-focused:",
        int(comparison["changed_under_risk_focus"].sum()),
        "of", len(comparison), "shipments"
    )


if __name__ == "__main__":
    main()
