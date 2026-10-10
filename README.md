# 🚚 Shipment Route Optimizer

A Python-based shipment route optimization system that recommends suitable routes by balancing shipping cost, transit time, delay probability, and operational risk using weighted scoring.

## 📌 Overview

Choosing a shipment route involves balancing multiple factors. The cheapest route may take longer, while the fastest route may involve higher costs or operational risks.

The **Shipment Route Optimizer** evaluates multiple candidate routes for each shipment, calculates a weighted score, and recommends the route with the highest score. It also includes performance evaluation, sensitivity analysis, and result verification.

## ✨ Features

- Generates synthetic data for 30 shipments with 4 candidate routes each.
- Evaluates 120 candidate-route records.
- Scores routes using cost, transit time, delay probability, and risk.
- Recommends the highest-scoring route for each shipment.
- Generates explanations for route recommendations.
- Compares recommendations against cheapest and fastest route baselines.
- Performs sensitivity analysis under different weighting strategies.
- Verifies calculated scores and saved recommendations.

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas |
| Data Storage | CSV |
| Optimization Technique | Weighted Scoring |
| Normalization | Min-Max Normalization |
| Development Environment | Visual Studio Code |

## 📁 Project Structure

```text
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
└── test_scorer.py
```

| File | Purpose |
|---|---|
| `data_generator.py` | Generates synthetic shipment and route data |
| `route_scorer.py` | Normalizes route metrics and calculates weighted scores |
| `optimizer.py` | Selects the best-scoring route for each shipment |
| `main.py` | Runs the optimization workflow |
| `evaluation.py` | Evaluates recommendations against baseline routes |
| `sensitivity_analysis.py` | Examines the impact of different scoring weights |
| `verify_results.py` | Recalculates scores and validates saved recommendations |
| `test_scorer.py` | Contains tests for the scoring logic |
| `data/routes.csv` | Stores generated candidate routes |
| `data/recommendations.csv` | Stores recommended routes and their results |

## 📊 Dataset

The project uses a reproducible synthetic dataset containing 30 shipments and 4 candidate routes per shipment.

| Dataset Property | Value |
|---|---:|
| Total Shipments | 30 |
| Candidate Routes per Shipment | 4 |
| Total Candidate-Route Records | 120 |
| Data Source | Synthetic |
| Random Seed | Fixed for reproducibility |

Each candidate route contains the following attributes:

| Attribute | Description |
|---|---|
| `shipment_id` | Unique shipment identifier |
| `route_id` | Candidate route identifier |
| `origin` | Shipment origin |
| `destination` | Shipment destination |
| `route` | Route description, including intermediate hubs |
| `cost` | Estimated shipping cost |
| `transit_days` | Estimated transit time in days |
| `delay_probability` | Estimated probability of delay, between 0 and 1 |
| `risk_score` | Illustrative operational risk score from 1 to 10 |

All dataset values are illustrative and do not represent live shipping data.

## ⚙️ Optimization Methodology

### 1. Scoring Criteria

The baseline scoring model assigns weights to four route-selection criteria.

| Criterion | Weight | Preference |
|---|---:|---|
| Shipping Cost | 40% | Lower is better |
| Transit Time | 30% | Lower is better |
| Delay Probability | 20% | Lower is better |
| Operational Risk | 10% | Lower is better |
| **Total** | **100%** | |

### 2. Min-Max Normalization

Because the criteria use different units and scales, each metric is normalized across the candidate routes for an individual shipment.

For metrics where lower values are better:

\[
\text{Normalized Score} =
\frac{\text{Maximum Value} - \text{Route Value}}
{\text{Maximum Value} - \text{Minimum Value}}
\]

The normalized score ranges from 0 to 1, where higher values indicate better relative performance.

If all candidate routes have the same value for a criterion, each route receives a score of 1 for that criterion.

### 3. Weighted Score Calculation

The final route score is calculated using the normalized values and their corresponding weights.

\[
\begin{aligned}
\text{Final Score} = 100 \times (&0.40C + 0.30T\\
&+ 0.20D + 0.10R)
\end{aligned}
\]

Where:

| Symbol | Meaning |
|---|---|
| \(C\) | Normalized cost score |
| \(T\) | Normalized transit-time score |
| \(D\) | Normalized delay-probability score |
| \(R\) | Normalized operational-risk score |

The route with the highest final score is recommended for each shipment.

**Note:** The final score measures relative performance among available alternatives. It is not the probability that a recommendation is correct.

## 📈 Evaluation Results

The current synthetic dataset produced the following results.

### Recommendation Performance

| Evaluation Metric | Result |
|---|---:|
| Shipments Evaluated | 30 |
| Recommended Route Was Cheapest | 20 of 30 (67%) |
| Recommended Route Was Fastest | 14 of 30 (47%) |

### Average Recommended-Route Metrics

| Metric | Average Result |
|---|---:|
| Shipping Cost | 46,905.93 |
| Transit Time | 13.70 days |
| Delay Probability | 22.4% |
| Operational Risk | 4.77 / 10 |

The optimizer considers all four criteria together. Therefore, the recommended route may not always be the cheapest or fastest option.

These results apply only to the current synthetic dataset and should not be interpreted as real-world shipping performance.

## 🔍 Sensitivity Analysis

Sensitivity analysis evaluates how route recommendations change when decision priorities are adjusted.

### Weighting Strategies

| Criterion | Balanced | Cost-Focused | Risk-Focused |
|---|---:|---:|---:|
| Shipping Cost | 40% | 60% | 20% |
| Transit Time | 30% | 20% | 20% |
| Delay Probability | 20% | 15% | 25% |
| Operational Risk | 10% | 5% | 35% |
| **Total** | **100%** | **100%** | **100%** |

### Recommendation Changes

| Scenario | Recommendations Changed | Interpretation |
|---|---:|---|
| Balanced | Baseline | Reference strategy |
| Cost-Focused | 3 of 30 | Prioritizes shipping cost |
| Risk-Focused | 9 of 30 | Prioritizes operational risk and delay probability |

The results demonstrate that different business priorities can lead to different route selections. The risk-focused scenario changes both delay-probability and operational-risk weights, so the observed changes reflect their combined influence.

## 🚀 Getting Started

### Prerequisites

| Requirement | Details |
|---|---|
| Python | 3.10 or later |
| Package Manager | pip |
| Editor | Visual Studio Code or another Python-compatible editor |

### 1. Clone the Repository

```bash
git clone https://github.com/manognakundam/shipment-route-optimizer.git
cd shipment-route-optimizer
```

### 2. Create a Virtual Environment

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
python -m pip install pandas
```

### 4. Generate the Dataset

```bash
python data_generator.py
```

This generates `data/routes.csv`.

### 5. Run the Optimizer

```bash
python main.py
```

The recommended routes are saved to `data/recommendations.csv`.

### 6. Evaluate Recommendations

```bash
python evaluation.py
```

### 7. Run Sensitivity Analysis

```bash
python sensitivity_analysis.py
```

### 8. Verify Results

```bash
python verify_results.py
```

This independently recalculates route scores and checks the saved recommendations against the highest-scoring candidate routes.

## ✅ Validation

The project includes a verification script to check whether the calculated scores and saved recommendations agree with the scoring methodology.

| Validation Check | Purpose |
|---|---|
| Score Recalculation | Independently recalculates route scores |
| Recommendation Check | Confirms that selected routes have the highest scores |
| Saved Results Check | Validates generated recommendation records |

Run the verification script after generating the dataset and running the optimizer.

## ⚠️ Limitations

- The dataset is synthetic and does not represent live shipping conditions.
- Scoring weights are predefined and may not suit every business requirement.
- Scores are relative to the candidate routes available for each shipment.
- Live disruptions, carrier capacity, emissions, and hard delivery or budget constraints are not currently incorporated.
- Evaluation results are specific to the generated dataset.

## 🔮 Future Improvements

| Enhancement | Potential Benefit |
|---|---|
| Real Shipment and Carrier Data | Improve practical relevance |
| Customizable Scoring Weights | Adapt recommendations to business priorities |
| Delivery and Budget Constraints | Support operational requirements |
| Emissions and Additional Risk Metrics | Include sustainability and broader risk factors |
| Interactive Dashboard | Compare routes and visualize trade-offs |
| Expanded Automated Testing | Improve reliability and edge-case handling |

## 🎯 Conclusion

The Shipment Route Optimizer demonstrates an explainable approach to multi-criteria decision-making. By combining shipping cost, transit time, delay probability, and operational risk into a weighted scoring model, it recommends routes based on their overall relative performance.

The project provides a foundation for further development using real operational data, configurable business constraints, and interactive route comparisons.

---

**Developed by:** [manognakundam](https://github.com/manognakundam)

**Project:** [Shipment Route Optimizer](https://github.com/manognakundam/shipment-route-optimizer)
