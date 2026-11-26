import streamlit as st
import pandas as pd

st.set_page_config(page_title='IT Help-Desk Ticket Analysis', layout='wide')
st.title('IT Help-Desk Ticket & SLA Performance Dashboard')

@st.cache_data
def load_data():
    return pd.read_csv('data/clean/cleaned_issues.csv')

df = load_data()

st.sidebar.header('Filter Tickets')
priorities = ['All'] + sorted(df['issue_priority'].dropna().unique().tolist())
sel_prio = st.sidebar.selectbox('Select Priority', priorities)

sla_opts = ['All'] + sorted(df['sla_status'].dropna().unique().tolist())
sel_sla = st.sidebar.selectbox('Select SLA Status', sla_opts)

filtered = df.copy()
if sel_prio != 'All':
    filtered = filtered[filtered['issue_priority'] == sel_prio]
if sel_sla != 'All':
    filtered = filtered[filtered['sla_status'] == sel_sla]

c1, c2, c3, c4 = st.columns(4)
c1.metric('Total Tickets', f'{len(filtered):,}')
sla_pct = (filtered['sla_status'] == 'Met SLA').mean() * 100
c2.metric('SLA Compliance %', f'{sla_pct:.1f}%')
med_res = filtered['resolution_time_hours'].median()
c3.metric('Median Resolution (Hrs)', f'{med_res:.1f}')
reopen_pct = filtered['is_reopened'].mean() * 100
c4.metric('Reopen Rate %', f'{reopen_pct:.1f}%')

st.subheader('Tickets by Priority & SLA Status')
st.bar_chart(filtered.groupby(['issue_priority', 'sla_status']).size().unstack(fill_value=0))

st.subheader('Top 10 Projects by Volume')
st.bar_chart(filtered['issue_proj'].value_counts().head(10))

st.subheader('Sample Filtered Ticket Records')
st.dataframe(filtered[['id', 'issue_proj', 'issue_type', 'issue_priority', 'issue_assignee', 'resolution_time_hours', 'sla_status']].head(50))
