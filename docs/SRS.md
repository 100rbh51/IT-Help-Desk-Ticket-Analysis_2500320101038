
# P3 – Software Requirements Specification (SRS)

## 1. Purpose

This document describes the requirements for the IT Help Desk Ticket Analysis project. The project will analyze an authorized help desk ticket dataset and present findings through code, queries, reports, and visualizations.

## 2. Scope

The system will support a reproducible analytics workflow: load data, inspect and clean it, calculate descriptive summaries, and present supported findings in charts and a dashboard. It is an academic analytics project, not a live ticket-management system.

## 3. Intended Users

- Project team: prepares data, runs the analysis, and maintains project files.
- Project reviewer: reviews the method, documentation, and outputs.
- Help desk or IT service stakeholders: may use the summaries to understand ticket patterns.

## 4. Functional Requirements

- **FR-01:** The project shall use a public, synthetic, or otherwise authorized dataset.
- **FR-02:** The project shall preserve the original dataset separately from cleaned data.
- **FR-03:** The Python workflow shall check for missing values, duplicate records, invalid values, and inconsistent formats where applicable.
- **FR-04:** The project shall document dataset fields and their meanings in a data dictionary.
- **FR-05:** The analysis shall calculate ticket summaries supported by the available fields, such as volume, category, priority, status, and resolution time.
- **FR-06:** SQL queries shall provide documented summaries of the prepared data.
- **FR-07:** Charts and dashboard views shall communicate selected findings.
- **FR-08:** The project shall document assumptions, limitations, and steps to reproduce the analysis.

## 5. Non-Functional Requirements

- **NFR-01 Reproducibility:** A reviewer shall be able to follow the documented steps to reproduce the analysis, subject to required software and data availability.
- **NFR-02 Data protection:** Confidential or personally identifiable data shall not be published in the repository.
- **NFR-03 Clarity:** Reports and charts shall use clear titles, labels, and units.
- **NFR-04 Maintainability:** Code, SQL, documentation, data, and reports shall be kept in their designated folders.
- **NFR-05 Reliability:** The workflow shall report errors clearly and avoid silently treating invalid records as valid.

## 6. Proposed Tools

Python, pandas, Jupyter Notebook, SQL, Excel, Power BI, GitHub, and optionally Streamlit. Final tools may change based on project requirements and feasibility.

## 7. Data Requirements

The dataset source, license or permission, time period, row count, fields, and known limitations shall be recorded after dataset selection. Resolution-time calculations require usable creation and resolution timestamps or an equivalent duration field.

## 8. Constraints and Assumptions

- Dataset selection is pending.
- Metrics depend on the fields available and their quality.
- The project performs descriptive analysis; observed patterns alone will not establish causation.
- Streamlit is optional until the final scope is confirmed.

## 9. Acceptance Criteria

- Dataset source and usage permission are documented.
- Data dictionary is completed.
- Cleaning and analysis steps are reproducible.
- SQL queries and visual outputs run on the prepared data.
- Final documentation explains findings and limitations.
- No confidential data or secrets are committed to GitHub.

## 10. Pending Decisions

- Dataset source and schema
- Exact metrics and dashboard KPIs
- Whether Streamlit is included in the final submission
