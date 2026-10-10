
def score_routes(routes):
    """
    Calculate a weighted score for each route.
    Higher scores indicate better routes.
    """

    weights = {
        "cost": 0.40,
        "transit_days": 0.30,
        "delay_probability": 0.20,
        "risk_score": 0.10
    }

    routes = routes.copy()

    # All four factors are costs: lower values are better.
    # Normalize each factor to a 0-1 scale.
    for column in weights:
        minimum = routes[column].min()
        maximum = routes[column].max()

        if maximum == minimum:
            routes[f"{column}_score"] = 1.0
        else:
            routes[f"{column}_score"] = (
                (maximum - routes[column]) / (maximum - minimum)
            )

    # Combine normalized scores using the chosen weights.
    routes["final_score"] = sum(
        routes[f"{column}_score"] * weight
        for column, weight in weights.items()
    )

    # Convert to a percentage for easier interpretation.
    routes["final_score"] = routes["final_score"] * 100

    return routes
