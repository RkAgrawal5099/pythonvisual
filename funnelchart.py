import plotly.graph_objects as go

# Simulated sales funnel data
funnel_stages = ['Lead', 'Contacted', 'Qualified', 'Proposal', 'Final Conversion']
quantities = [500, 400, 300, 200, 100]

# Create a funnel chart using Plotly
funnel_fig = go.Figure(go.Funnel(
    y=funnel_stages,
    x=quantities,
    textinfo="value+percent initial+percent previous"
))

# Update layout for the funnel chart
funnel_fig.update_layout(
    title="Sales Funnel",
    title_x=0.5
)

# Display the funnel chart
funnel_fig.show()
