import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# Load your dummy dataset (replace this with your actual data loading logic)
# Generate dummy data
np.random.seed(42)
categories = ["Other", "Infrastructure", "Renovation", "Design", "Importation", "Supervision", "Construction"]
project_status = ["Future", "Ongoing"]

# Create a DataFrame with random project counts
data = {
    "Category": np.random.choice(categories, 100),
    "Status": np.random.choice(project_status, 100, p=[0.745, 0.255])
}
df = pd.DataFrame(data)

# Calculate the distribution of projects by category
category_distribution = df["Category"].value_counts().reset_index()
category_distribution.columns = ["Category", "Count"]

# first tab
# Generate dummy data
np.random.seed(42)
num_projects = 10
projects = [f"Project {i+1}" for i in range(num_projects)]
start_dates = pd.date_range(start="2023-01-01", periods=num_projects, freq="M")
end_dates = start_dates + pd.to_timedelta(np.random.randint(30, 180, num_projects), unit="d")
planned_progress = np.random.randint(0, 100, num_projects)
actual_progress = planned_progress + np.random.randint(-20, 20, num_projects)
status = np.random.choice(["On Track", "Delayed", "Completed"], num_projects)

# Create DataFrame
project_performance = pd.DataFrame({
    "Project Name": projects,
    "Start Date": start_dates,
    "End Date": end_dates,
    "Planned Progress (%)": planned_progress,
    "Actual Progress (%)": actual_progress,
    "Status": status
})
# project_performance = pd.read_csv(r"C:\Users\fnafisa\WORKSPACE\professional\EXPRO\streamlit app\data\project_performance.csv")


# second tab
forecast_data = pd.DataFrame({
    "Month": pd.date_range(start="2023-01-01", periods=12, freq="M"),
    "Forecasted Revenue (SAR)": np.random.randint(1000, 5000, 12) * 1_000_000,
    "Actual Revenue (SAR)": np.random.randint(800, 4500, 12) * 1_000_000
})
# forecast_data= pd.read_csv(r"C:\Users\fnafisa\WORKSPACE\professional\EXPRO\streamlit app\data\forecast_data.csv")
portfolio_data = pd.DataFrame({
    "Project": [f"Project {i+1}" for i in range(10)],
    "Total Investment (SAR)": np.random.randint(10, 100, 10) * 1_000_000,
    "Return on Investment (ROI)": np.random.uniform(5, 20, 10)
})
# portfolio_data= pd.read_csv(r"C:\Users\fnafisa\WORKSPACE\professional\EXPRO\streamlit app\data\portfolio_data.csv")
roi_data = pd.DataFrame({
    "Year": [2020, 2021, 2022, 2023],
    "Average ROI (%)": [8.5, 10.2, 12.3, 15.0]
})
# roi_data= pd.read_csv(r"C:\Users\fnafisa\WORKSPACE\professional\EXPRO\streamlit app\data\roi_data.csv")
budget_data = pd.DataFrame({
    "Project": [f"Project {i+1}" for i in range(10)],
    "Planned Budget (SAR)": np.random.randint(50, 200, 10) * 1_000_000,
    "Actual Cost (SAR)": np.random.randint(60, 220, 10) * 1_000_000
})
# budget_data= pd.read_csv(r"C:\Users\fnafisa\WORKSPACE\professional\EXPRO\streamlit app\data\budget_data.csv")

# third tab
risk_data = pd.DataFrame({
    "Risk ID": [f"Risk {i+1}" for i in range(10)],
    "Risk Category": np.random.choice(["Financial", "Operational", "Technical", "Legal"], 10),
    "Likelihood": np.random.uniform(0.1, 1.0, 10),
    "Impact": np.random.uniform(1, 10, 10)
})
# risk_data= pd.read_csv(r'C:\Users\fnafisa\WORKSPACE\professional\EXPRO\streamlit app\data\risk_data.csv')
issue_data = pd.DataFrame({
    "Issue ID": [f"Issue {i+1}" for i in range(10)],
    "Issue Type": np.random.choice(["Resource Shortage", "Technical Delay", "Budget Overrun", "Stakeholder Conflict"], 10),
    "Severity": np.random.choice(["Low", "Medium", "High"], 10),
    "Status": np.random.choice(["Open", "In Progress", "Resolved"], 10)
})
# issue_data= pd.read_csv(r'C:\Users\fnafisa\WORKSPACE\professional\EXPRO\streamlit app\data\issue_data.csv')
compliance_data = pd.DataFrame({
    "Contract ID": [f"Contract {i+1}" for i in range(10)],
    "Compliance Status": np.random.choice(["Compliant", "Non-Compliant", "Under Review"], 10),
    "Penalty (SAR)": np.random.randint(0, 100_000, 10)
})
# compliance_data= pd.read_csv(r'C:\Users\fnafisa\WORKSPACE\professional\EXPRO\streamlit app\data\compliance_data.csv')


# Set page configuration to wide layout
# st.set_page_config(layout="wide")
# Set page config with dark theme preference
st.set_page_config(
    layout="wide",
    page_title="Projects Insights",
    page_icon="⭐",
    initial_sidebar_state="expanded",
    # menu_items={
    #     'Get Help': 'https://www.example.com',
    #     'Report a bug': "https://www.example.com",
    #     'About': "# This is a dark theme app!"
    # }
)
# Inject custom CSS for header, footer, and dark theme
st.markdown("""
<style>
/* General page styling */
body {
    background-color: #0E1117; /* Dark background */
    color: #FFFFFF; /* White text */
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
}

/* Header styling */
.header {
    background-color: #001F3F; /* Dark Navy Blue */
    color: #FFFFFF; /* White text */
    padding: 10px 20px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 1000;
}

/* Footer styling */
.footer {
    background-color: #001F3F; /* Dark Navy Blue */
    color: #FFFFFF; /* White text */
    padding: 10px 20px;
    text-align: center;
    font-size: 16px;
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    z-index: 1000;
}

/* Main content styling */
.main-content {
    padding-top: 70px; /* Space for header */
    padding-bottom: 70px; /* Space for footer */
}

/* Button styling */
.stButton>button {
    background-color: #4169E1; /* Royal Blue */
    color: #FFFFFF; /* White text */
    border-radius: 5px;
    border: none;
    padding: 10px 20px;
}

.stButton>button:hover {
    background-color: #001F3F; /* Dark Navy Blue */
    color: #FFFFFF; /* White text */
}

/* Table styling */
.stDataFrame {
    background-color: #1E1E1E; /* Dark background for tables */
    color: #FFFFFF; /* White text */
}

/* Chart styling */
.plotly-graph-div {
    background-color: #1E1E1E; /* Dark background for charts */
    color: #FFFFFF; /* White text */
}
</style>
""", unsafe_allow_html=True)

# Add header
st.markdown("""
<div class="header">
    My Streamlit App Header
</div>
""", unsafe_allow_html=True)

# Add footer
st.markdown("""
<div class="footer">
    © 2025 SCA. All rights reserved.
</div>
""", unsafe_allow_html=True)


st.markdown('</div>', unsafe_allow_html=True)


col_image, col_title= st.columns([.7,.3])
with col_image:
    # logo
    st.image("https://sca.sa/images/logo.png")
with col_title:
    # Streamlit app
    st.title("Project Performance Insights")


st.divider()
# Create a bar chart
fig3 = px.bar(
    category_distribution,
    x="Category",
    y="Count",
    title="Distribution of Projects by Category",
    labels={"Category": "Project Category", "Count": "Number of Projects"},
    text="Count",  # Display the count on top of each bar
    color="Category",  # Add color to differentiate categories
)

# Update layout for better readability
fig3.update_traces(textposition="outside")
fig3.update_layout(xaxis_title="Project Category", yaxis_title="Number of Projects", showlegend=False)

#  Pie chart
status_counts = df["Status"].value_counts(normalize=True) * 100
# Create donut chart
fig1 = px.pie(
    values=status_counts,
    names=status_counts.index,
    hole=0.5,
    title="Future Projects vs Ongoing Projects",
    labels={"names": "Status", "values": "Percentage"}
)
fig1.update_traces(textinfo="percent+label")
# Calculate percentages
infra_percentage = (df[df["Category"] == "Infrastructure"].shape[0] / df.shape[0]) * 100
other_percentage = 100 - infra_percentage
# Create donut chart
fig2 = px.pie(
    values=[infra_percentage, other_percentage],
    names=["Infrastructure", "Other"],
    hole=0.5,
    title="Infrastructure Projects vs Other Projects",
    labels={"names": "Category", "values": "Percentage"}
)
fig2.update_traces(textinfo="percent+label")

col_pie1, col_pie2, col_table= st.columns([.25,.25,.3])
with col_pie1:
    # Display the first donut chart
    st.subheader("Future Projects vs Ongoing Projects")
    st.plotly_chart(fig1, use_container_width=True)
with col_pie2:
    # Display the second donut chart
    st.subheader("Infrastructure Projects vs Other Projects")
    st.plotly_chart(fig2, use_container_width=True)

with col_table:
    # Display the dataset
    st.subheader("Project Performance Data")
    st.write(project_performance)
    # Add the bar chart to the Streamlit app

col_bar, col_emp= st.columns(2)

with col_bar:
    st.subheader("Distribution of Projects by Category")
    st.plotly_chart(fig3, use_container_width=True)

# st.subheader("Distribution of Projects by Category")
# st.plotly_chart(fig3, use_container_width=True)

# Add the bar chart to the Streamlit app

# Add KPIs in a row above the table
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Projects", value="22,000")
with col2:
    st.metric(label="Total Contractors", value="2,000")
with col3:
    st.metric(label="Portfolio Value", value="2000 billion SAR")

# # Display the dataset
# st.subheader("Project Performance Data")
# st.write(project_performance)

# Add a third tab for "Risk and Compliance"
tab1, tab2, tab3 = st.tabs(["Projects Progress", "Financials", "Risk and Compliance"])

with tab1:
    # Create columns for vertical layout
    col1, col2, col3 = st.columns(3)

    # Bar Chart: Planned vs Actual Progress (Interactive with Plotly)
    with col1:
        st.subheader("Planned vs Actual Progress")
        fig_bar = px.bar(project_performance, x="Project Name", y=["Planned Progress (%)", "Actual Progress (%)"], 
                         barmode="group", title="Planned vs Actual Progress")
        st.plotly_chart(fig_bar, use_container_width=True)
        st.write("""
        **Explanation:**  
        This bar chart compares the planned progress (%) with the actual progress (%) for each project.  
        - **Planned Progress:** The expected progress based on project timelines.  
        - **Actual Progress:** The achieved progress as of the current date.  
        Use this chart to identify projects that are ahead or behind schedule.
        """)

    # Pie Chart: Project Status Distribution (Interactive with Plotly)
    with col2:
        st.subheader("Project Status Distribution")
        status_counts = project_performance["Status"].value_counts().reset_index()
        status_counts.columns = ["Status", "Count"]
        fig_pie = px.pie(status_counts, values="Count", names="Status", title="Project Status Distribution")
        st.plotly_chart(fig_pie, use_container_width=True)
        st.write("""
        **Explanation:**  
        This pie chart shows the distribution of project statuses across all projects.  
        - **On Track:** Projects progressing as per the plan.  
        - **Delayed:** Projects lagging behind the planned schedule.  
        - **Completed:** Projects that have been successfully delivered.  
        Use this chart to understand the overall health of your project portfolio.
        """)

    # Line Chart: Progress Over Time (Interactive with Plotly)
    with col3:
        st.subheader("Progress Over Time")
        selected_project = st.selectbox("Select a Project", project_performance["Project Name"])
        project_data = project_performance[project_performance["Project Name"] == selected_project]

        fig_line = go.Figure()
        fig_line.add_trace(go.Scatter(x=["Start", "End"], y=[0, 100], mode="lines", name="Ideal Progress", line=dict(dash="dash")))
        fig_line.add_trace(go.Scatter(x=["Start", "End"], 
                                    y=[project_data["Planned Progress (%)"].values[0], project_data["Actual Progress (%)"].values[0]], 
                                    mode="lines", name="Actual Progress"))
        fig_line.update_layout(title=f"Progress Over Time for {selected_project}", 
                              xaxis_title="Timeline", yaxis_title="Progress (%)", yaxis_range=[0, 100])
        st.plotly_chart(fig_line, use_container_width=True)
        st.write(f"""
        **Explanation:**  
        This line chart tracks the progress of **{selected_project}** over time.  
        - **Ideal Progress:** Represents the expected progress if the project were on schedule.  
        - **Actual Progress:** Shows the real progress achieved so far.  
        Use this chart to monitor the performance of individual projects and identify delays or accelerations.
        """)

# Tab 2: Financials
with tab2:
    col_bar1, col_bar2= st.columns(2)
    with col_bar1:
        st.subheader("Financial Insights")

        # Insight 10: Portfolio Performance Insights
        st.markdown("### Portfolio Performance Insights")
        fig_portfolio = px.bar(portfolio_data, x="Project", y="Total Investment (SAR)", 
                            title="Total Investment by Project")
        st.plotly_chart(fig_portfolio, use_container_width=True)
        st.write("""
        **Explanation:**  
        This bar chart shows the total investment (SAR) for each project in the portfolio.  
        - **Total Investment:** The amount of money invested in each project.  
        Use this chart to understand the distribution of investments across projects.
        """)
    with col_bar2:
        # Insight 3: Budget & Cost Insights
        st.markdown("### Budget & Cost Insights")
        fig_budget = px.bar(budget_data, x="Project", y=["Planned Budget (SAR)", "Actual Cost (SAR)"], 
                            barmode="group", title="Planned Budget vs Actual Cost by Project")
        st.plotly_chart(fig_budget, use_container_width=True)
        st.write("""
        **Explanation:**  
        This bar chart compares the planned budget with the actual cost for each project.  
        - **Planned Budget:** The budget allocated for each project.  
        - **Actual Cost:** The real cost incurred for each project.  
        Use this chart to identify projects that are over or under budget.
        """)

    st.divider()

    # Insight 9: Financial Return & ROI Insights
    st.markdown("### Financial Return & ROI Insights")
    fig_roi = px.line(roi_data, x="Year", y="Average ROI (%)", 
                      title="Average ROI Over Time")
    st.plotly_chart(fig_roi, use_container_width=True)
    st.write("""
    **Explanation:**  
    This line chart shows the average ROI (%) over the years.  
    - **ROI (Return on Investment):** A measure of the profitability of investments.  
    Use this chart to track the performance of your investments over time.
    """)

    st.divider()

    # Insight 11: Forecasting & Predictive Insights
    st.markdown("### Forecasting & Predictive Insights")
    fig_forecast = px.line(forecast_data, x="Month", y=["Forecasted Revenue (SAR)", "Actual Revenue (SAR)"], 
                           title="Forecasted vs Actual Revenue Over Time")
    st.plotly_chart(fig_forecast, use_container_width=True)
    st.write("""
    **Explanation:**  
    This line chart compares the forecasted revenue with the actual revenue over time.  
    - **Forecasted Revenue:** Predicted revenue based on historical data and trends.  
    - **Actual Revenue:** Real revenue achieved in each month.  
    Use this chart to evaluate the accuracy of revenue forecasts and identify trends.
    """)

    # Tab 3: Risk and Compliance
with tab3:
    st.subheader("Risk and Compliance Insights")

    # Insight 4: Risk Insights
    st.markdown("### Risk Insights")
    fig_risk = px.scatter(risk_data, x="Likelihood", y="Impact", color="Risk Category", 
                          title="Risk Likelihood vs Impact")
    st.plotly_chart(fig_risk, use_container_width=True)
    st.write("""
    **Explanation:**  
    This scatter plot visualizes the likelihood and impact of various risks.  
    - **Likelihood:** The probability of the risk occurring (0.1 = Low, 1.0 = High).  
    - **Impact:** The severity of the risk if it occurs (1 = Low, 10 = High).  
    - **Risk Category:** The type of risk (Financial, Operational, Technical, Legal).  
    Use this chart to prioritize risks based on their likelihood and impact.
    """)

    st.divider()

    # Insight 5: Issue & Bottleneck Insights
    st.markdown("### Issue & Bottleneck Insights")
    fig_issue = px.bar(issue_data, x="Issue Type", y="Severity", color="Status", 
                       title="Issue Severity by Type and Status")
    st.plotly_chart(fig_issue, use_container_width=True)
    st.write("""
    **Explanation:**  
    This bar chart shows the severity of issues and bottlenecks by type and status.  
    - **Issue Type:** The category of the issue (e.g., Resource Shortage, Technical Delay).  
    - **Severity:** The level of severity (Low, Medium, High).  
    - **Status:** The current status of the issue (Open, In Progress, Resolved).  
    Use this chart to identify critical issues and track their resolution progress.
    """)

    st.divider()

    # Insight 8: Contract & Compliance Insights
    st.markdown("### Contract & Compliance Insights")
    fig_compliance = px.bar(compliance_data, x="Contract ID", y="Penalty (SAR)", color="Compliance Status", 
                            title="Contract Compliance Status and Penalties")
    st.plotly_chart(fig_compliance, use_container_width=True)
    st.write("""
    **Explanation:**  
    This bar chart shows the compliance status of contracts and associated penalties.  
    - **Compliance Status:** Whether the contract is compliant, non-compliant, or under review.  
    - **Penalty (SAR):** The financial penalty associated with non-compliance.  
    Use this chart to monitor contract compliance and identify potential financial risks.
    """)
