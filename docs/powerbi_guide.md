# P12 & P13: Power BI Data Model & Dashboard Guide

## Step 1: Load Data into Power BI Desktop
1. Open **Power BI Desktop** -> **Get Data** -> **Text/CSV**.
2. Select data/clean/cleaned_issues.csv and click **Load**.

## Step 2: Star Schema Setup (P12)
- Create reference tables in Power Query for Dim_Project (issue_proj), Dim_Priority (issue_priority, sla_target_hours), and Dim_Agent (issue_assignee).
- Link them to the main Fact_Tickets table using **One-to-Many (1:*)** relationships.

## Step 3: Key DAX Measures (P13)
- Total Tickets = COUNTROWS(cleaned_issues)
- Met SLA Tickets = CALCULATE(COUNTROWS(cleaned_issues), cleaned_issues[sla_status] = 'Met SLA')
- SLA Compliance % = DIVIDE([Met SLA Tickets], [Total Tickets], 0)
- Median Resolution Hrs = MEDIAN(cleaned_issues[resolution_time_hours])
- Reopen Rate % = DIVIDE(SUM(cleaned_issues[is_reopened]), [Total Tickets], 0)

## Step 4: Recommended Visuals & Save
- **Page 1 (Executive Overview):** 4 KPI Cards, Donut Chart (sla_status), Line Chart (created_month vs Total Tickets), Clustered Bar (issue_priority vs Total Tickets).
- **Page 2 (Bottlenecks & Agents):** Top 10 Projects Bar Chart, Top 10 Agents Table, Slicers for issue_priority and issue_type.
- Save final file as powerbi/helpdesk_dashboard.pbix.
