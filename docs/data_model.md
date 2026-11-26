# P7: IT Help-Desk Data Model (Star Schema)

## Overview
To support analytical reporting in SQL and Power BI, the cleaned dataset is modeled into a **Star Schema** consisting of one central Fact table and four Dimension tables.

## Tables
1. **fact_tickets (Fact Table)**: Granularity = 1 row per unique ticket (id). Contains metrics (
esolution_time_hours, sla_target_hours, wf_total_time, processing_steps, issue_comments_count, is_reopened).
2. **dim_project**: Unique projects (issue_proj).
3. **dim_agent**: Unique support assignees (issue_assignee, is_assigned).
4. **dim_priority_sla**: Priority levels (issue_priority) mapped to SLA targets (sla_target_hours).
5. **dim_date**: Calendar attributes (created_year, created_month, created_day_of_week).
