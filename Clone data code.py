import pandas as pd

# Load the original CSV file into a pandas DataFrame
original_df = pd.read_csv('your_file.csv')

# Create a new column with the desired values
original_df['new_column'] = original_df['existing_column'] - 1

# Load the updated CSV file into a pandas DataFrame
updated_df = pd.read_csv('updated_data.csv')

# Append the updated data to the original data
new_df = original_df.append(updated_df, ignore_index=True)

# Save the new data to a CSV file
new_df.to_csv('new_file.csv', index=False)