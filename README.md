
# SALES FUNNEL VISUALIZATION

## Project Overview

This project generates a **Sales Funnel Visualization** using Plotly. The funnel chart displays various stages of a sales funnel along with the corresponding quantities for each stage. The data used in this project is simulated to demonstrate how sales typically move through various stages, from initial leads to final conversion.

## Features

- **Funnel Chart**: Visualizes the quantity at each stage of the sales funnel.
- **Interactive Visualization**: The chart dynamically displays values and percentages using Plotly's interactive features.

## Project Setup

### Prerequisites

Ensure the following Python libraries are installed:
- **plotly**: Used to create the interactive funnel chart.
- **pandas**: For data handling (optional, for future extensions).

### Installation

Install the required libraries using pip:
```bash
pip install plotly pandas
```

### Steps to Run

1. Clone or download the project files to your local machine.
2. Open the Python script `sales_funnel.py` in your preferred IDE (e.g., VS Code, PyCharm, or Jupyter Notebook).
3. Run the script to generate the funnel chart.

---

## Code Walkthrough

### Sales Funnel Data

The sales funnel consists of the following stages:
- **Lead**
- **Contacted**
- **Qualified**
- **Proposal**
- **Final Conversion**

Each stage has an associated quantity representing the number of prospects at that stage:
```python
funnel_stages = ['Lead', 'Contacted', 'Qualified', 'Proposal', 'Final Conversion']
quantities = [500, 400, 300, 200, 100]
```

### Funnel Chart

The funnel chart is created using Plotly's `go.Funnel` function:
```python
import plotly.graph_objects as go

# Create a funnel chart
funnel_fig = go.Figure(go.Funnel(
    y=funnel_stages,
    x=quantities,
    textinfo="value+percent initial+percent previous"
))

# Update layout for better visualization
funnel_fig.update_layout(
    title="Sales Funnel",
    title_x=0.5
)

# Display the chart
funnel_fig.show()
```

---

## Output

Running the script will generate an **interactive funnel chart** with:
- The **quantity of prospects** at each stage.
- The **percentage of total initial leads** and the **percentage change from the previous stage**.

### Screenshots

#### Example Funnel Chart
![Funnel Chart](https://github.com/RkAgrawal5099/pythonvisual/blob/main/Screenshot%202024-12-03%20233547.png)

#### Full Interface - Chart 1
![Chart 1](https://github.com/RkAgrawal5099/pythonvisual/blob/main/Screenshot%202024-12-03%20233611.png)

#### Full Interface - Chart 2
![Chart 2](https://github.com/RkAgrawal5099/pythonvisual/blob/main/Screenshot%202024-12-03%20234854.png)

---

## Customization

You can adapt the chart to your specific needs by modifying:
- `funnel_stages`: Update this list with your sales funnel stages.
- `quantities`: Replace with quantities that represent your data.

For example:
```python
funnel_stages = ['Step 1', 'Step 2', 'Step 3']
quantities = [1000, 600, 300]
```

---

## Additional Information

### Extending the Project

- Replace the simulated data (`funnel_stages` and `quantities`) with real values from your sales dataset.
- Customize the chart's layout, colors, or labels using Plotly's extensive customization options.
- Integrate the visualization into a web-based dashboard for real-time analytics.

---

