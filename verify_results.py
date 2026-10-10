
import pandas as pd
from pathlib import Path

BASE = Path(__file__).parent
routes = pd.read_csv(BASE / "data" / "routes.csv")
saved = pd.read_csv(BASE / "data" / "recommendations.csv")

weights = {
    "cost": 0.40,
    "transit_days": 0.30,
    "delay_probability": 0.20,
    "risk_score": 0.10
}

errors = []

for shipment_id, group in routes.groupby("shipment_id"):
    group = group.copy()

    for column in weights:
        low = group[column].min()
        high = group[column].max()

        if high == low:
            group[column + "_score"] = 1.0
        else:
            group[column + "_score"] = (
                (high - group[column]) / (high - low)
            )

    group["verified_score"] = sum(
        group[column + "_score"] * weight
        for column, weight in weights.items()
    ) * 100

    best = group.sort_values(
        ["verified_score", "route_id"],
        ascending=[False, True]
    ).iloc[0]

    selected = saved[
        saved["shipment_id"] == shipment_id
    ]

    if len(selected) != 1:
        errors.append(
            f"{shipment_id}: expected one saved recommendation"
        )
        continue

    selected = selected.iloc[0]

    actual_route = group[
        group["route_id"] == selected["recommended_route"]
    ]

    if actual_route.empty:
        errors.append(
            f"{shipment_id}: saved route not found in dataset"
        )
        continue

    actual_score = actual_route.iloc[0]["verified_score"]

    if abs(actual_score - selected["final_score"]) > 0.02:
        errors.append(
            f"{shipment_id}: saved score does not match recalculation"
        )

    if actual_score < group["verified_score"].max() - 0.000001:
        errors.append(
            f"{shipment_id}: saved route is not the highest-scoring route"
        )

print("Shipments checked:", routes["shipment_id"].nunique())

if errors:
    print("\nVerification issues:")
    for error in errors:
        print("-", error)
else:
    print("PASS: All saved scores and route selections verified.")
