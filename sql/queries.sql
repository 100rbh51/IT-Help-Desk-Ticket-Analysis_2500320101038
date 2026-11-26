-- Q1: Overall Ticket Volume & SLA Compliance Rate
SELECT sla_status, COUNT(*) AS ticket_count,
       ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM tickets), 2) AS pct_share
FROM tickets GROUP BY sla_status ORDER BY ticket_count DESC;

-- Q2: Ticket Volume & Avg Resolution Hours by Priority
SELECT issue_priority, COUNT(*) AS total_tickets,
       ROUND(AVG(resolution_time_hours), 2) AS avg_resolution_hrs,
       SUM(CASE WHEN sla_status = 'Breached SLA' THEN 1 ELSE 0 END) AS breached_count
FROM tickets GROUP BY issue_priority ORDER BY total_tickets DESC;

-- Q3: Top 10 Projects by Ticket Volume & Reopen Rate
SELECT issue_proj, COUNT(*) AS total_tickets,
       ROUND(AVG(resolution_time_hours), 2) AS avg_res_hrs,
       ROUND(SUM(is_reopened) * 100.0 / COUNT(*), 2) AS reopen_rate_pct
FROM tickets GROUP BY issue_proj ORDER BY total_tickets DESC LIMIT 10;

-- Q4: Top 10 Most Active Support Agents (Excluding Unassigned)
SELECT issue_assignee, COUNT(*) AS assigned_tickets,
       ROUND(AVG(resolution_time_hours), 2) AS avg_res_hrs,
       ROUND(SUM(CASE WHEN sla_status = 'Met SLA' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS sla_met_pct
FROM tickets WHERE is_assigned = 1 GROUP BY issue_assignee ORDER BY assigned_tickets DESC LIMIT 10;

-- Q5: Monthly Ticket Trend
SELECT created_month, COUNT(*) AS tickets_created,
       ROUND(AVG(resolution_time_hours), 2) AS avg_res_hrs
FROM tickets GROUP BY created_month ORDER BY created_month;
