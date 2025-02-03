# 3. Time-Series Analysis
# Convert timestamps to datetime
smart_alarm_df['ActivatedTimestamp'] = pd.to_datetime(smart_alarm_df['ActivatedTimestamp'])
smart_alarm_df['ClearedTimestamp'] = pd.to_datetime(smart_alarm_df['ClearedTimestamp'])

# Calculate AlarmDuration
smart_alarm_df['AlarmDuration'] = smart_alarm_df['ClearedTimestamp'] - smart_alarm_df['ActivatedTimestamp']

# Set the ActivatedTimestamp as the index for time-series analysis
smart_alarm_df.set_index('ActivatedTimestamp', inplace=True)

# Sort the DataFrame by the index (ActivatedTimestamp)
smart_alarm_df.sort_index(inplace=True)

# Calculate rolling count of alarms for each AssetId
rolling_count = smart_alarm_df.groupby('AssetId')['AlarmLabel'].rolling('10min').count()

# Filter frequent alarms
frequent_alarms = rolling_count[rolling_count > 10]
