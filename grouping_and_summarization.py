# 5. Alarm Grouping and Summarization
alarm_groups = smart_alarm_df.groupby(labels)
for group_id, group in alarm_groups:
    print(f'Group {group_id}:')
    print(group['AlarmLabel'].value_counts())
    print(group['Severity'].value_counts())
