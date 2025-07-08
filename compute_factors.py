import pandas as pd

# Step 1: Load factor score coefficients
coefs_df = pd.read_csv("factor_coefs.csv")  # columns: Region, Factor1, Factor2, ...
coefs_df.set_index("Region", inplace=True)

# Step 2: Load external means and STDs
# Format: columns = Region, Mean, SD
means_df = pd.read_csv("means_stds.csv")
means_df.set_index("Region", inplace=True)

# Step 3: Load user data
user_df = pd.read_csv("github_test.csv")

# Step 4: Match regions
region_cols = coefs_df.index.tolist()

# Check for missing regions
missing = [r for r in region_cols if r not in user_df.columns]
if missing:
    raise ValueError(f"Missing region(s) in user data: {missing}")

# Subset and order user data to match coefficient matrix
X = user_df[region_cols].copy()

# Step 5: Z-score using external means and SDs
X_z = (X - means_df.loc[region_cols, "Mean"].values) / means_df.loc[region_cols, "SD"].values

# Step 6: Compute factor scores
B = coefs_df
factor_scores = X_z.dot(B)

# Step 7: Combine with SubjectID if it exists
if "SubjectID" in user_df.columns:
    output = pd.concat([user_df[["SubjectID"]], factor_scores], axis=1)
else:
    output = factor_scores.copy()

output.to_csv("factor_scores_output.csv", index=False)
print("Factor scores computed and saved to 'factor_scores_output.csv'")