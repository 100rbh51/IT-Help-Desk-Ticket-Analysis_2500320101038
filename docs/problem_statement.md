
# P1 – Problem Statement

## Project title

**IT Help Desk Ticket Analysis**

## Background

Organizations receive IT help desk tickets when employees experience issues with hardware, software, accounts, networks, and other IT services. If ticket records are not reviewed regularly, recurring issues and delays in resolving requests can be difficult to identify. This can make it harder for support teams to understand workload patterns and decide where process improvements may help.

## Problem statement

This project will examine an IT help desk ticket dataset to describe ticket volume, ticket categories, priorities, status, and resolution time. The analysis will look for patterns such as frequently reported issue types, changes in ticket volume over time, and differences in resolution time across available categories or priority levels. The project will present its findings through Python-based analysis, SQL queries, Excel outputs, and a Power BI report, with a Streamlit application if supported by the project scope.

The dataset has not yet been selected or analyzed. Therefore, the exact fields, time period, data quality limitations, and metrics will be confirmed after dataset selection (P4) and data dictionary preparation (P5). No conclusions about actual ticket performance are being made at this stage.

## Aim

To use ticket data to create a clear, reproducible view of help desk workload and resolution patterns that can support evidence-based discussion of service improvement opportunities.

## Objectives

1. Select or generate a suitable ticket dataset and document its source and limitations.
2. Define the dataset fields and business meaning in a data dictionary.
3. Clean and validate the data using Python, documenting the steps taken.
4. Use SQL and Python to summarize ticket volume, categories, priority, status, and resolution time where those fields are available.
5. Create appropriate charts and dashboard views to communicate the observed patterns.
6. Document the workflow, assumptions, testing, and findings so the work can be reproduced and reviewed.

## Scope

### In scope

- Descriptive analysis of the available ticket records.
- Data quality checks and cleaning, with raw data kept separate from cleaned data.
- Analysis only of measures supported by the selected dataset.
- SQL queries, Python analysis, Excel work, and a Power BI report as planned project outputs.
- A Streamlit interface if it remains feasible and is included in the approved project scope.

### Out of scope

- Accessing or analyzing a real organization's confidential help desk records without authorization.
- Claiming that observed relationships prove the cause of delays or other outcomes.
- Predictive modeling, automated ticket assignment, or a production help desk system unless these are explicitly added to the scope later.
- Making performance claims before the dataset has been selected and analyzed.

## Intended users

The intended audience is project reviewers and people interested in understanding help desk ticket patterns, such as IT support leads or service desk analysts. The dashboard and report are for analytical and educational use; they are not an operational ticket-management system.

## Expected outcome

A documented and reproducible analytics project containing a prepared dataset, code and queries, analysis outputs, and visual summaries of the ticket patterns that the selected data can support. Any recommendations will be tied to findings and limitations documented in the final report.

## Assumptions and constraints

- The dataset will be public, synthetic, or otherwise authorized for this project.
- The available data may not contain every field needed for every planned metric.
- Resolution-time analysis requires usable ticket creation and resolution timestamps, or an equivalent duration field.
- Personal or confidential information will not be published in the repository.
- The final scope and deliverables may be refined after dataset review and applicable HCL project requirements are confirmed.
