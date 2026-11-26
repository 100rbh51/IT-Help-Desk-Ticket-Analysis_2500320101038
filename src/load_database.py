import sqlite3
import pandas as pd

def load_to_sqlite():
    df = pd.read_csv('data/clean/cleaned_issues.csv')
    cols = ['id','issue_num','issue_proj','issue_reporter','issue_assignee','is_assigned',
            'issue_contr_count','issue_type','issue_priority','issue_created','issue_resolution_date',
            'issue_resolution','issue_status','issue_comments_count','wf_total_time','processing_steps',
            'resolution_time_hours','sla_target_hours','sla_status','is_reopened',
            'created_year','created_month','created_day_of_week']
    conn = sqlite3.connect('data/clean/helpdesk.db')
    with open('sql/schema.sql', 'r') as f:
        conn.executescript(f.read())
    df[cols].to_sql('tickets', conn, if_exists='append', index=False)
    print('DONE P8: Loaded', len(df), 'rows into data/clean/helpdesk.db')
    res = pd.read_sql_query('SELECT sla_status, COUNT(*) as cnt FROM tickets GROUP BY sla_status', conn)
    print(res.to_string(index=False))
    conn.close()

if __name__ == '__main__':
    load_to_sqlite()
