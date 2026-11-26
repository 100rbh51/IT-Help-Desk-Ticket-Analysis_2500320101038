import os
import json
import sqlite3
import pandas as pd

def test_cleaned_dataset_exists_and_valid():
    assert os.path.exists('data/clean/cleaned_issues.csv'), 'Cleaned CSV missing'
    df = pd.read_csv('data/clean/cleaned_issues.csv')
    assert len(df) == 66691, f'Expected 66691 rows, got {len(df)}'
    assert df['id'].is_unique, 'Duplicate ticket IDs found'
    assert df['sla_status'].isin(['Met SLA', 'Breached SLA', 'Pending']).all(), 'Invalid SLA status values'

def test_sqlite_database():
    assert os.path.exists('data/clean/helpdesk.db'), 'SQLite DB missing'
    conn = sqlite3.connect('data/clean/helpdesk.db')
    count = conn.execute('SELECT COUNT(*) FROM tickets').fetchone()
    conn.close()
    assert count == 66691, f'Expected 66691 rows in DB, got {count}'

def test_kpis_and_charts():
    assert os.path.exists('reports/kpis.json'), 'KPIs JSON missing'
    with open('reports/kpis.json') as f:
        kpis = json.load(f)
    assert kpis['total_tickets'] == 66691
    charts = ['01_sla_status.png', '02_priority_sla.png', '03_monthly_trend.png', '04_top_projects.png', '05_workflow_bottlenecks.png']
    for c in charts:
        assert os.path.exists(f'reports/charts/{c}'), f'Missing chart: {c}'
