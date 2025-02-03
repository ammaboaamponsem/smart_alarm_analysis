# EXPLORATORY DATA ANALYSIS 

# 3.1 Cross-validation of Labels and Severity
cross_val_table <- table(`Asset Type` = combined_df$AssetType, combined_df$Severity)
print(cross_val_table)


# 3.2 Identify the Unknown alarms
unknown_alarms <- combined_df %>%
  filter(grepl("[^a-zA-Z0-9]", AlarmLabel))  # Filter out alarms with special characters
print(head(unknown_alarms))

# Could be essential to the analysis so we will investigate further

# 3.4 Severity Levels by Time Periods
# Create a sorted version of the data frame for visualization
sorted_combined_df <- combined_df[order(combined_df$week), ]

# Create a line plot to visualize severity alarms by weeks
ggplot(sorted_combined_df, aes(x = week, color = Severity, group = Severity)) +
  geom_line(stat = "count") +
  labs(title = "Severity Alarms by Week (Exploring Severity Levels by Time Periods)",
       x = "Week",
       y = "Count",
       color = "Severity") +
  theme_minimal() +
  scale_x_continuous(breaks = seq(1, max(sorted_combined_df$week), by = 1))
# Exploring Severity Levels by Time Periods: 
# This analysis focuses on understanding the distribution 
# of severity levels across different time periods (weeks 
# or months). It aims to identify whether certain severity 
# levels are more common during specific time periods or 
# under certain conditions. By visualizing the frequency 
# or proportion of each severity level within each time period,
# you can gain insights into temporal patterns in alarm severity.
# We could further explore the organizationid experiencing the 
# most number of critical alarms.
