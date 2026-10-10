
import pandas as pd
from pathlib import Path
from route_scorer import score_routes

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "routes.csv"
OUTPUT_FILE = BASE_DIR / "data" / "recommendations.csv"


def explain_recommendation(best_route, all_routes):
    reasons = []

    if best_route["cost"] == all_routes["cost"].min():
        reasons.append("lowest cost")

    if best_route["transit_days"] == all_routes["transit_days"].min():
        reasons.append("shortest transit time")

    if best_route["delay_probability"] == all_routes["delay_probability"].min():
        reasons.append("lowest delay probability")

    if best_route["risk_score"] == all_routes["risk_score"].min():
        reasons.append("lowest risk")

    if reasons:
        return "Selected route offers " + ", ".join(reasons) + "."

    return (
        "Selected for the best combined score across cost, "
        "transit time, delay probability, and risk."
    )


def optimize_shipments():
    df = pd.read_csv(DATA_FILE)
    recommendations = []

    # Evaluate routes separately for each shipment.
    for shipment_id, shipment_routes in df.groupby("shipment_id"):
        scored = score_routes(shipment_routes)
        scored = scored.sort_values(
            "final_score", ascending=False
        )

        best = scored.iloc[0]

        recommendations.append({
            "shipment_id": shipment_id,
            "origin": best["origin"],
            "destination": best["destination"],
            "recommended_route": best["route_id"],
            "route_description": best["route"],
            "cost": best["cost"],
            "transit_days": best["transit_days"],
            "delay_probability": best["delay_probability"],
            "risk_score": best["risk_score"],
            "final_score": round(best["final_score"], 2),
            "explanation": explain_recommendation(
                best, shipment_routes
            )
        })

    results = pd.DataFrame(recommendations)
    results.to_csv(OUTPUT_FILE, index=False)

    print("\nSHIPMENT ROUTE RECOMMENDATIONS")
    print("=" * 65)

    for _, row in results.iterrows():
        print(f"\nShipment: {row['shipment_id']}")
        print(f"Route: {row['recommended_route']}")
        print(f"Cost: {row['cost']}")
        print(f"Transit time: {row['transit_days']} days")
        print(f"Delay probability: {row['delay_probability']:.0%}")
        print(f"Risk score: {row['risk_score']}/10")
        print(f"Score: {row['final_score']}/100")
        print(f"Reason: {row['explanation']}")

    print("\nTotal shipments evaluated:", len(results))
    print("Results saved to:", OUTPUT_FILE)


if __name__ == "__main__":
    optimize_shipments()
