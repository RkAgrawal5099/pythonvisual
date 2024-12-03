import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# File path to your Excel file
file_path = r"C:\Users\rushi\AppData\Local\Temp\1aefb953-e9a8-4d06-8c8e-d500158f2a17_Waste_Management_System_A_Comprehensive_Approach.zip.a17\pythondetaset\exel\sales-funnel.xlsx"

# Load the dataset
df = pd.read_excel(file_path)

# Inspect the data
print(df.head())
print(df.info())

# Group by Status and calculate the total quantity
status_summary = df.groupby('Status').agg(
    Total_Quantity=('Quantity', 'sum')
).reset_index()

# Simulated data for the funnel chart (these should be the stages of your sales funnel)
funnel_stages = ['Lead', 'Contacted', 'Qualified', 'Proposal', 'Final Conversion']
quantities = [500, 400, 300, 200, 100]

# **Plotly Funnel Chart**
funnel_fig = go.Figure(go.Funnel(
    y=funnel_stages,
    x=quantities,
    textinfo="value+percent initial+percent previous"
))

funnel_fig.update_layout(
    title="Sales Funnel",
    title_x=0.5
)

# Create a 2x2 grid for matplotlib charts
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# **Chart 1: Line Chart for Total Quantity by Status**
axes[0, 0].plot(status_summary['Status'], status_summary['Total_Quantity'], marker='o', linestyle='-', color='blue')
axes[0, 0].set_title('Total Quantity by Status')
axes[0, 0].set_xlabel('Status')
axes[0, 0].set_ylabel('Total Quantity')
axes[0, 0].grid(True)

# **Chart 2: Frequency Chart (Bar Chart for Status Count)**
status_count = df['Status'].value_counts()
sns.barplot(x=status_count.index, y=status_count.values, ax=axes[0, 1], palette='Blues_d')
axes[0, 1].set_title('Frequency of Each Status')
axes[0, 1].set_xlabel('Status')
axes[0, 1].set_ylabel('Frequency')

# **Empty plot (can be used for additional charts or left blank)**
axes[1, 0].axis('off')  # Hides this plot (empty space)

# **Empty plot (can be used for additional charts or left blank)**
axes[1, 1].axis('off')  # Hides this plot (empty space)

# Adjust layout for matplotlib charts
plt.tight_layout()

# Display the Plotly funnel chart first
funnel_fig.show()  # Display Plotly funnel chart

# Display the matplotlib charts
plt.show()  # Display matplotlib charts
