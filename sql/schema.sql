DROP TABLE IF EXISTS tickets;
CREATE TABLE tickets (
    id INTEGER PRIMARY KEY,
    issue_num INTEGER,
    issue_proj TEXT,
    issue_reporter TEXT,
    issue_assignee TEXT,
    is_assigned INTEGER,
    issue_contr_count INTEGER,
    issue_type TEXT,
    issue_priority TEXT,
    issue_created TEXT,
    issue_resolution_date TEXT,
    issue_resolution TEXT,
    issue_status TEXT,
    issue_comments_count INTEGER,
    wf_total_time REAL,
    processing_steps INTEGER,
    resolution_time_hours REAL,
    sla_target_hours REAL,
    sla_status TEXT,
    is_reopened INTEGER,
    created_year INTEGER,
    created_month TEXT,
    created_day_of_week TEXT
);
CREATE INDEX idx_proj ON tickets(issue_proj);
CREATE INDEX idx_priority ON tickets(issue_priority);
CREATE INDEX idx_sla ON tickets(sla_status);
