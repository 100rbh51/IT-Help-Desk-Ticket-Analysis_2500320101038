# IT Help-Desk Ticket Analysis (End-to-End Data Analytics Project)


**Live Interactive Dashboard:** [Launch Streamlit App](https://it-app-desk-ticket-analysis2500320101038-8mvdyqpmtdyma4tbtwaqf.streamlit.app/)

An end-to-end IT Service Management (ITSM) analytics pipeline analyzing 66,691 IT help-desk tickets across workflow stages, SLA compliance, agent workload, and project bottlenecks using Python, SQL (SQLite), Excel, Power BI, and Streamlit.

## Key Business Findings (KPIs)
- Total Tickets Analyzed: 66,691 (65,838 Resolved | 853 Pending)
- Overall SLA Compliance Rate: 14.94% (9,966 Met SLA vs. 55,872 Breached SLA)
- Median Resolution Time: 837.81 hours
- Ticket Reopen Rate: 3.18%
- Unassigned Ticket Rate: 46.55% (Major driver of initial queue delays)

## Repository Structure (P1-P20 Roadmap)
- README.md : P16 Project overview & setup guide
- data/raw/issues.csv : P4 Raw ITSM dataset (66,691 rows, 58 cols)
- data/clean/ : P6 & P8 Cleaned CSV & SQLite database (helpdesk.db)
- docs/problem_statement.md : P1 Business problem definition
- docs/synopsis.md : P2 Project scope & objectives
- docs/SRS.md : P3 Software Requirements Specification
- docs/data_dictionary.xlsx : P5 Column-level metadata dictionary
- docs/data_model.md : P7 Star Schema architecture
- docs/powerbi_guide.md : P12 & P13 Power BI Star Schema & DAX measures
- docs/final_report.md : P17 Executive analytical findings & recommendations
- docs/viva_qa.md : P18 HCL evaluation & viva preparation guide
- src/clean_data.py : P6 Data cleaning & SLA feature engineering
- src/load_database.py : P8 SQLite ETL loader
- src/analysis.py : P9 KPI computation & chart generation
- sql/schema.sql & sql/queries.sql : P8 Relational schema & business SQL queries
- notebook/analysis.ipynb : P10 Interactive Jupyter EDA notebook
- app/streamlit_app.py : P11 Live interactive Streamlit web dashboard
- reports/charts/ : P9 5 high-resolution analytical PNG visuals
- reports/kpis.json : P9 Machine-readable executive metrics
- reports/helpdesk_excel_report.xlsx : P14 Multi-sheet Excel summary workbook
- tests/test_pipeline.py : P15 Automated pytest validation suite

## How to Run Locally
1. Activate Virtual Environment: .\.venv\Scripts\Activate.ps1
2. Run Data Cleaning (P6): python src/clean_data.py
3. Load SQL Database (P8): python src/load_database.py
4. Generate KPIs & Charts (P9): python src/analysis.py
5. Launch Interactive Dashboard (P11): streamlit run app/streamlit_app.py
6. Run Automated Tests (P15): pytest -v
