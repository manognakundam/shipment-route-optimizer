# Shipment Route Optimizer

A Python-based shipment route optimization system that recommends suitable routes by balancing shipping cost, transit time, delay probability, and operational risk using weighted scoring.

## Overview

Choosing a shipment route involves balancing multiple factors. The cheapest route may take longer, while the fastest route may have a higher cost or operational risk.

This project evaluates multiple candidate routes for each shipment, calculates a weighted score, and recommends the route with the highest score. It also includes performance evaluation, sensitivity analysis, and result verification.

## Features

- Generates synthetic data for 30 shipments with 4 candidate routes each.
- Evaluates 120 candidate-route records.
- Scores routes using cost, transit time, delay probability, and risk.
- Recommends the highest-scoring route for each shipment.
- Generates explanations for route recommendations.
- Compares recommendations against cheapest and fastest route baselines.
- Performs sensitivity analysis under different weighting strategies.
- Verifies calculated scores and saved recommendations.

## Technology Stack

- **Language:** Python
- **Data Processing:** Pandas
- **Data Format:** CSV
- **Development Environment:** Visual Studio Code
- **Optimization Technique:** Weighted scoring and min-max normalization

## Project Structure

Shipment-Route-Optimizer/
│
├── data/
│   ├── routes.csv
│   └── recommendations.csv
│
├── data_generator.py
├── route_scorer.py
├── optimizer.py
├── main.py
├── evaluation.py
├── sensitivity_analysis.py
├── verify_results.py
├── test_scorer.py


## Dataset

The project uses a synthetic dataset containing 30 shipments and 4 candidate routes per shipment, resulting in 120 route options.

Each candidate route contains:

- `shipment_id`: Unique shipment identifier.
- `route_id`: Candidate route identifier.
- `origin`: Shipment origin.
- `destination`: Shipment destination.
- `route`: Route description, including intermediate hubs.
- `cost`: Estimated shipping cost.
- `transit_days`: Estimated transit time in days.
- `delay_probability`: Estimated delay probability between 0 and 1.
- `risk_score`: Illustrative operational risk score from 1 to 10.

The dataset is generated locally using a fixed random seed for reproducibility. All values are illustrative and do not represent live shipping data.

## Optimization Methodology

### 1. Scoring Criteria

The optimizer uses the following baseline weights:

- **Cost:** 40%
- **Transit Time:** 30%
- **Delay Probability:** 20%
- **Risk Score:** 10%

Lower values are preferred for all four criteria.

### 2. Min-Max Normalization

Since the metrics use different units and scales, each criterion is normalized within the candidate routes for an individual shipment.

For metrics where lower values are better:

Normalized Score =
(Maximum Value - Route Value) /
(Maximum Value - Minimum Value)

The normalized score ranges from 0 to 1, with higher scores representing better relative performance. If all candidate routes have the same value for a criterion, they receive a score of 1 for that criterion.

### 3. Weighted Score Calculation

The final score is calculated using the normalized scores and their corresponding weights.

Final Score = 100 × (
    0.40 × Cost Score +
    0.30 × Time Score +
    0.20 × Delay Score +
    0.10 × Risk Score
)

The route with the highest final score is selected as the recommendation for that shipment.

The score represents relative performance among the available alternatives, not the probability that a recommendation is correct.

## Evaluation Results

Evaluation on the current dataset produced the following results.

**Recommendation Performance**
- Shipments evaluated: 30
- Recommended route was the cheapest: 20 out of 30 (67%)
- Recommended route was the fastest: 14 out of 30 (47%)

**Average Recommended-Route Metrics**
- Average cost: 46,905.93
- Average transit time: 13.70 days
- Average delay probability: 22.4%
- Average risk score: 4.77 out of 10

The optimizer considers all four criteria together. Therefore, the recommended route may not always be the cheapest or fastest alternative.

These results apply to the current synthetic dataset and should not be interpreted as real-world shipping performance.

## Sensitivity Analysis

Sensitivity analysis examines how recommendations change when the scoring weights are adjusted.

**Balanced Scenario**
- Cost: 40%
- Transit time: 30%
- Delay probability: 20%
- Risk score: 10%

**Cost-Focused Scenario**
- Cost: 60%
- Transit time: 20%
- Delay probability: 15%
- Risk score: 5%

**Risk-Focused Scenario**
- Cost: 20%
- Transit time: 20%
- Delay probability: 25%
- Risk score: 35%

**Observed Changes Compared with the Balanced Scenario**
- Cost-focused: 3 out of 30 recommendations changed.
- Risk-focused: 9 out of 30 recommendations changed.

The results demonstrate that changing decision priorities can influence route selection. The risk-focused scenario changes both delay-probability and risk-score weights, so the observed changes reflect their combined influence.

## Getting Started

### Prerequisites

- Python 3.10 or later
- pip
- Visual Studio Code or another Python-compatible editor

### 1. Clone the Repository

```bash
git clone <https://github.com/manognakundam/shipment-route-optimizer>
cd Shipment-Route-Optimizer
```

Replace the placeholder with your GitHub repository URL.

### 2. Create a Virtual Environment

For Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Generate the Dataset

```bash
python data_generator.py
```

This generates `data/routes.csv`.

### 4. Run the Optimizer

```bash
python main.py
```

The recommended routes are saved to `data/recommendations.csv`.

### 5. Evaluate Recommendations

```bash
python evaluation.py
```

### 6. Run Sensitivity Analysis

```bash
python sensitivity_analysis.py
```

### 7. Verify Results

```bash
python verify_results.py
```

Run the commands from the project root directory. Generate the dataset before running the optimizer if you want to recreate the sample data.

## Validation

The project includes a verification script that independently recalculates route scores and checks the saved recommendations against the highest-scoring candidate routes.

Run `verify_results.py` after generating the dataset and running the optimizer to validate the current results.

## Limitations

- The dataset is synthetic and does not represent live shipping conditions.
- The scoring weights are predefined and may not suit every business requirement.
- Scores are relative to the candidate routes available for each shipment.
- The model does not currently account for live disruptions, carrier capacity, emissions, or hard delivery and budget constraints.
- Evaluation results are specific to the generated dataset.

## Future Improvements

- Integrate real shipment and carrier data.
- Allow users to customize scoring weights.
- Add delivery deadlines, budget constraints, and capacity restrictions.
- Include emissions and additional risk indicators.
- Develop an interactive dashboard for route comparisons.
- Expand automated testing for edge cases and invalid input data.

## Conclusion

The Shipment Route Optimizer demonstrates an explainable approach to multi-criteria decision-making. By combining cost, transit time, delay probability, and operational risk, it recommends routes based on their overall weighted performance.

The project provides a foundation for further development using real operational data, additional constraints, and interactive visualizations.
