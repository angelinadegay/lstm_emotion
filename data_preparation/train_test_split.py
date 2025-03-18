from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("./data/result.csv")

X_train, X_test = train_test_split(df, test_size=0.25, random_state=42, stratify=df["source"])

X_train["type"] = "train"
X_test["type"] = "test"

combined = pd.concat([X_train, X_test], axis=0)
combined.sort_index(inplace=True)

[*cols, type] = combined.columns
combined = combined[[type, *cols]]

combined.to_csv("./data/result_split.csv", index=False)