import os
import pandas as pd
import numpy as np

def clean_helpdesk_data():
    df = pd.read_csv('data/raw/issues.csv').drop_duplicates(subset=['id']).copy()
    df['id'] = df['id'].astype('int64')
    df['issue_num'] = df['issue_num'].astype('int64')
    df['issue_contr_count'] = df['issue_contr_count'].fillna(0).astype('int64')
    for col in ['started', 'ended', 'issue_created', 'issue_resolution_date', 'last_change_date']:
        df[col] = pd.to_datetime(df[col], format='mixed', errors='coerce', utc=True)
    df['issue_assignee'] = df['issue_assignee'].fillna('Unassigned')
    df['is_assigned'] = np.where(df['issue_assignee'] == 'Unassigned', 0, 1)
    df['issue_resolution'] = df['issue_resolution'].fillna('Unresolved')
    df['issue_status'] = df['issue_status'].str.strip().str.lower()
    df['issue_priority'] = df['issue_priority'].str.strip().str.title()
    df['issue_type'] = df['issue_type'].str.strip().str.title()
    wf_cols = [c for c in df.columns if c.startswith('wf_') and c != 'wf_total_time']
    df[wf_cols] = df[wf_cols].fillna(0.0)
    df['resolution_time_hours'] = (df['issue_resolution_date'] - df['issue_created']).dt.total_seconds() / 3600.0
    df.loc[df['resolution_time_hours'] < 0, 'resolution_time_hours'] = np.nan
    sla_map = {'Blocker': 4.0, 'Critical': 4.0, 'Highest': 4.0, 'High': 24.0, 'Medium': 48.0, 'Low': 72.0, 'Lowest': 96.0}
    df['sla_target_hours'] = df['issue_priority'].map(sla_map).fillna(48.0)
    df['sla_status'] = np.select([df['resolution_time_hours'].isna(), df['resolution_time_hours'] <= df['sla_target_hours'], df['resolution_time_hours'] > df['sla_target_hours']], ['Pending', 'Met SLA', 'Breached SLA'], default='Pending')
    df['is_reopened'] = np.where(df['wfe_reopened'] > 0, 1, 0)
    dt_naive = df['issue_created'].dt.tz_localize(None)
    df['created_year'] = dt_naive.dt.year
    df['created_month'] = dt_naive.dt.to_period('M').astype(str)
    df['created_day_of_week'] = dt_naive.dt.day_name()
    os.makedirs('data/clean', exist_ok=True)
    df.to_csv('data/clean/cleaned_issues.csv', index=False)
    print('UPDATED P6:', df.shape, df['sla_status'].value_counts().to_dict())

if __name__ == '__main__':
    clean_helpdesk_data()
