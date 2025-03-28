# Dream11 Prediction Analysis

## Overview
This repository contains the code and resources for a predictive analysis system for Dream11, a popular fantasy cricket platform. The project uses historical IPL match data (2008-2017) to forecast player performance and optimize team selection. Machine learning models such as Random Forest, XGBoost, and Neural Networks are employed to predict Dream11 points, helping users make data-driven decisions. This work was developed as part of the course *21CSE304P - Cloud Computing Industry Essentials* at SRM Institute of Science and Technology.

### Features
- **Data Processing**: Cleans and normalizes IPL data using Pandas and NumPy.
- **Feature Engineering**: Extracts key features like Form Index and Venue Performance.
- **Machine Learning Models**: Implements Random Forest, XGBoost, and Neural Networks for prediction.
- **Prediction Module**: Generates player rankings and projected Dream11 points.
- **Visualizations**: Includes tables and diagrams to illustrate data, system architecture, and model performance.

### Repository Structure
- `cloud.py`: Generates the system architecture diagram (Fig. 1.2).
- `new_table_1_1.py`: Creates a table of IPL player match data (Fig. 1.1).
- `new_table_1_5.py`: Creates a table of IPL team performance by role (Fig. 1.5).
- `fig_1_3_bar.py`: Generates a bar chart comparing ML model accuracy (Fig. 1.3).
- `fig_1_4_bar.py`: Generates a bar chart of predicted Dream11 points by player role (Fig. 1.4).
- `fig_1_6_table.py`: Creates a table of sample IPL match statistics (Fig. 1.6).
- `output/`: Directory containing generated images (e.g., `dream11_architecture.png`, `fig_1_1_new_table.png`).

### Prerequisites
- Python 3.8+
- Libraries: `pandas`, `matplotlib`, `graphviz`
- Graphviz software (for rendering diagrams): [Download here](https://graphviz.org/download/)

Install the required Python libraries:
```bash
pip install pandas matplotlib graphviz
