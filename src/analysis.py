import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_analysis():
    df = pd.read_csv('data/clean/cleaned_issues.csv')
    os.makedirs('reports/charts', exist_ok=True)
    sns.set_theme(style='whitegrid')

    kpis = {
        'total_tickets': int(len(df)),
        'resolved_tickets': int(df['resolution_time_hours'].notnull().sum()),
        'pending_tickets': int(df['resolution_time_hours'].isnull().sum()),
        'sla_met_count': int((df['sla_status'] == 'Met SLA').sum()),
        'sla_breached_count': int((df['sla_status'] == 'Breached SLA').sum()),
        'sla_compliance_pct': round((df['sla_status'] == 'Met SLA').mean() * 100, 2),
        'avg_resolution_hours': round(float(df['resolution_time_hours'].mean()), 2),
        'median_resolution_hours': round(float(df['resolution_time_hours'].median()), 2),
        'reopen_rate_pct': round(float(df['is_reopened'].mean() * 100), 2),
        'unassigned_pct': round(float((df['is_assigned'] == 0).mean() * 100), 2)
    }
    with open('reports/kpis.json', 'w') as f:
        json.dump(kpis, f, indent=4)

    plt.figure(figsize=(8, 5))
    ax = sns.countplot(data=df, x='sla_status', order=['Breached SLA', 'Met SLA', 'Pending'], hue='sla_status', palette=['#e74c3c', '#2ecc71', '#f39c12'], legend=False)
    plt.title('Ticket Distribution by SLA Compliance Status', fontsize=14, fontweight='bold')
    plt.xlabel('SLA Status')
    plt.ylabel('Number of Tickets')
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height()):,}', (p.get_x() + p.get_width()/2., p.get_height()), ha='center', va='bottom', fontsize=10)
    plt.tight_layout()
    plt.savefig('reports/charts/01_sla_status.png', dpi=150)
    plt.close()

    plt.figure(figsize=(10, 5))
    top_prio = df['issue_priority'].value_counts().nlargest(6).index
    sns.countplot(data=df[df['issue_priority'].isin(top_prio)], x='issue_priority', hue='sla_status', order=top_prio)
    plt.title('Ticket Volume by Priority & SLA Status', fontsize=14, fontweight='bold')
    plt.xlabel('Priority')
    plt.ylabel('Ticket Count')
    plt.tight_layout()
    plt.savefig('reports/charts/02_priority_sla.png', dpi=150)
    plt.close()

    monthly = df.groupby('created_month').size().reset_index(name='tickets')
    plt.figure(figsize=(12, 5))
    plt.plot(monthly['created_month'], monthly['tickets'], marker='o', linewidth=2, color='#2980b9')
    plt.xticks(rotation=45, ha='right')
    plt.title('Monthly IT Help-Desk Ticket Volume Trend', fontsize=14, fontweight='bold')
    plt.xlabel('Month')
    plt.ylabel('Tickets Created')
    plt.tight_layout()
    plt.savefig('reports/charts/03_monthly_trend.png', dpi=150)
    plt.close()

    top_proj = df['issue_proj'].value_counts().nlargest(10)
    plt.figure(figsize=(10, 5))
    sns.barplot(x=top_proj.values, y=top_proj.index, hue=top_proj.index, palette='viridis', legend=False)
    plt.title('Top 10 IT Projects by Ticket Volume', fontsize=14, fontweight='bold')
    plt.xlabel('Number of Tickets')
    plt.ylabel('Project ID')
    plt.tight_layout()
    plt.savefig('reports/charts/04_top_projects.png', dpi=150)
    plt.close()

    wf_cols = [c for c in df.columns if c.startswith('wf_') and c != 'wf_total_time']
    avg_hrs = (df[wf_cols].mean() / 3600.0).sort_values(ascending=False).head(8)
    avg_hrs.index = [i.replace('wf_', '').replace('_', ' ').title() for i in avg_hrs.index]
    plt.figure(figsize=(10, 5))
    sns.barplot(x=avg_hrs.values, y=avg_hrs.index, hue=avg_hrs.index, palette='magma', legend=False)
    plt.title('Top 8 Workflow Stages by Average Time Spent (Hours)', fontsize=14, fontweight='bold')
    plt.xlabel('Average Hours per Ticket')
    plt.ylabel('Workflow Stage')
    plt.tight_layout()
    plt.savefig('reports/charts/05_workflow_bottlenecks.png', dpi=150)
    plt.close()

    print('DONE P9: KPIs and 5 charts generated successfully!')
    print('KPIs:', kpis)

if __name__ == '__main__':
    run_analysis()
