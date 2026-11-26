# P17: Final Project Report - IT Help-Desk Ticket Analysis

## 1. Executive Summary
This project evaluates 66,691 IT support tickets across 58 workflow attributes to uncover drivers of SLA breaches, resolution delays, and ticket reopenings.

## 2. Key Analytical Insights
1. High SLA Breach Rate (83.78% of all tickets): Out of 65,838 resolved tickets, only 9,966 met priority-based SLA targets, largely due to extended queue times in In Progress and Waiting workflow states.
2. Unassigned Backlog Bottleneck: 46.55% of incoming tickets lacked an initial assignee, increasing triage latency.
3. Low Reopen Rate (3.18%): Once resolved, over 96.8% of tickets stayed closed, indicating strong technical fix quality despite slow turnaround times.

## 3. Strategic Recommendations
- Automated Ticket Routing: Implement rule-based auto-assignment to reduce the 46.55% unassigned ticket pool.
- SLA Escalation Alerts: Trigger automated alerts at 75% of SLA target elapsed time for Blocker/Critical/High tickets.
- Waiting-State Purging: Auto-close or follow up on tickets stuck in Waiting or Pending Customer Approval beyond 7 days.
