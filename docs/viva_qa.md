# P18: HCL Project Viva & Defense Q&A

Q1: What was the size and structure of your raw dataset?
A: The dataset contained 66,691 IT help-desk tickets and 58 columns, including ticket metadata (issue_proj, issue_priority, issue_type), timestamps, and workflow state durations (wf_*) and entry counts (wfe_*).

Q2: What data cleaning steps did you perform in Python (P6)?
A: Deduplicated records on id, standardized mixed UTC timestamps, imputed missing issue_assignee values as Unassigned (46.55%), filled null workflow stage durations (wf_*) with 0.0, and engineered resolution_time_hours, sla_target_hours, sla_status, and is_reopened.

Q3: How did you define SLA targets?
A: Priority-based thresholds: Blocker/Critical/Highest = 4 hrs, High = 24 hrs, Medium = 48 hrs, Low = 72 hrs, Lowest = 96 hrs.

Q4: Why use both Median and Mean for resolution time?
A: Mean resolution time (18,482 hrs) is heavily skewed by long-tail legacy tickets, whereas Median resolution time (837.81 hrs) accurately reflects typical ticket turnaround.

Q5: How did you validate pipeline integrity (P15)?
A: Built an automated pytest suite (tests/test_pipeline.py) verifying row counts (66,691), unique primary keys, SQLite database ingestion, KPI JSON accuracy, and chart exports.
