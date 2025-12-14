# DStv Zimbabwe — Customer Query Insight & Action Recommender

A prescriptive analytics web application that analyzes customer support queries for DStv Zimbabwe and recommends operational actions to reduce escalations and improve customer experience.

# The Problem
DStv Zimbabwe handles thousands of customer support queries each month across regions, channels, and issue types.
While operational teams can see what issues are occurring, they often struggle to understand which issues matter most, which are likely to escalate, and what actions should be taken immediately.

Escalations increase operational costs, customer dissatisfaction, and resolution times. Without a data-driven decision support system, supervisors must rely on intuition rather than evidence when prioritizing interventions.

This problem is common across subscription-based service providers, where small operational failures (e.g., payment issues or signal errors) can quickly lead to customer churn if not proactively managed.

# The Solution

This application is a **prescriptive analytics system** that transforms raw customer query data into **actionable recommendations.**

It combines:
- **Descriptive analytics** to summarize query volumes and escalation rates
- **Predictive models** to classify queries and estimate escalation risk
- **Prescriptive logic** to recommend concrete operational actions

Instead of stopping at insights, the system explicitly answers:
**“So what should the business do next?”**

🚀 Live Demo

Try it here → https://customer-query-insight-and-action-recommender-sbpsjavkqtssmvz8.streamlit.app

# How It Works

**1. User views the dashboard**
Key KPIs (total queries, escalation rate, top issue) summarize current operations.
**2. System analyzes patterns**
Machine learning models classify query text and estimate escalation probability.
**3. Prescriptive insight is generated**
The system highlights dominant drivers of escalation and recommends operational actions.

# The Analytics Behind It
- **Data**: Synthetic but realistic DStv Zimbabwe customer query dataset (2,000 rows, all regions)
- **Text Modeling**: TF-IDF vectorization
- **Classification**: Logistic Regression (query category)
- **Risk Prediction**: Random Forest (escalation probability)
- **Prescriptive Layer**: Rule-based logic driven by recent query patterns

# Example Output

Dashboard with Prescriptive “So What?” Insight
Identifies Payment Failure as the leading escalation driver
Recommends proactive payment system monitoring and automated SMS alerts
Supports decisions with real-time data trends

(Screenshots included in /assets folder)

# Technology Stack
- Frontend: Streamlit
- Analytics & ML: Python, pandas, scikit-learn
- Text Processing: TF-IDF Vectorization
- Models: Logistic Regression, Random Forest
- Visualization: Streamlit charts
- Deployment: Streamlit Cloud
- Data: Synthetic DStv Zimbabwe customer query dataset (2,000 records)

# About This Project
Built as the  **Final Project for ISOM 839 — Prescriptive Analytics** 
Suffolk University

Author: Hlatywayo Gamuchirai
LinkedIn: www.linkedin.com/in/hlatywayo-gamuchirai-t-76a08734
Email: gthlatywayo@gmail.com

# Future Possibilities
With more time, this system could be extended to:
- Optimize agent staffing levels using escalation forecasts
- Integrate real DStv operational data
- Trigger automated alerts or tickets in real time
- Add cost-based optimization for intervention prioritization

This project demonstrates how analytics + intelligence + recommendations can directly support real operational decisions in media and telecommunications.

🎬 Demo Video

Watch the walkthrough → https://www.loom.com/share/eae38104790a47639861164c14d94d98

