import pandas as pd
from scipy.stats import zscore

# Step 1: Load factor score coefficients
# Format of factor_coefs.csv:
# | Region        | Factor1 | Factor2 | ... |
# | ------------- | ------- | ------- | --- |
# | mPFC          | 0.23    | -0.04   | ... |
factor_coef_path = "factor_coefs.csv"
coefs_df = pd.read_csv(factor_coef_path)

# Step 2: Load user brain region data
# Assumes format:
# | SubjectID | mPFC | occipital | ... |
user_data_path = "your_data.csv"  # replace with your filename
user_df = pd.read_csv(user_data_path)

# Step 3: Match and align columns
region_cols = coefs_df["Region"].tolist()

# Check that all required regions are present
missing = [r for r in region_cols if r not in user_df.columns]
if missing:
    raise ValueError(f"Missing required region(s) in your data: {missing}")

# Subset and reorder user data to match coefficient matrix
X = user_df[region_cols].copy()

# Step 4: Compute factor scores
# Drop the 'Region' column to get the coefficient matrix
B = coefs_df.drop(columns=["Region"])

# Z-score inputs (column-wise)
X_z = X.apply(zscore, axis=0)

# Compute factor scores
factor_scores = X_z.dot(B)

# Combine with SubjectID
output = pd.concat([user_df[["SubjectID"]], factor_scores], axis=1)
output.to_csv("factor_scores_output.csv", index=False)

print("Factor scores computed and saved to 'factor_scores_output.csv'")
