# Biological-Data-Analysis
## Description
This script analyzes synthetic high-resolution telemetry data (velocity and acceleration) from an Atlantic Spotted Dolphin to identify and quantify specific behavioral patterns. It specifically isolates "bow-riding" events (surfing the pressure waves of commercial vessels) versus natural free-swimming behavior using conditional logic and numerical integration.

## Objective
To algorithmically classify animal behavior based on kinematic thresholds and estimate the relative biomechanical energy conserved during human-vessel interactions.

## Technical Stack
*   **Language:** Python 3.8
*   **Libraries:** `pandas` (boolean indexing & data manipulation), `scipy.integrate` (Simpson's rule for energy expenditure estimation), `seaborn` / `matplotlib` (categorical data visualization).

## Methodology
1.  **Conditional Labeling:** Utilizes vectorized conditional logic to classify behavior second-by-second. (Threshold: Velocity > 4.0 m/s & Absolute Acceleration < 0.5 m/s²).
2.  **Biomechanical Integration:** Calculates the absolute area under the acceleration curve ($\int |a| dt$) as a proxy for raw physical exertion, separating the dataset to compare the energy profiles of both behaviors.
3.  **Data Visualization:** Generates categorical scatter plots to visually distinguish low-effort surfing zones from high-exertion natural swimming.

## Results
The algorithm successfully isolated the behavioral periods, mathematically demonstrating a significant drop in integrated acceleration during high-speed bow-riding events, supporting the hypothesis of extreme energy conservation.
