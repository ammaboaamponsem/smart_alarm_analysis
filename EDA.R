# EXPLORATORY DATA ANALYSIS 

# 3.1 Cross-validation of Labels and Severity
cross_val_table <- table(`Asset Type` = combined_df$AssetType, combined_df$Severity)
print(cross_val_table)


# 3.2 Identify the Unknown alarms
unknown_alarms <- combined_df %>%
  filter(grepl("[^a-zA-Z0-9]", AlarmLabel))  # Filter out alarms with special characters
print(head(unknown_alarms))

# Could be essential to the analysis so we will investigate further
