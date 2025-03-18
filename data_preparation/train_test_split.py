from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("./data/result.csv")

X_train, X_test = train_test_split(
    df, test_size=0.25, random_state=42, stratify=df["source"]
)

X_train.sort_index(inplace=True)
X_test.sort_index(inplace=True)

X_train.to_csv("./data/result_train.csv", index=False)
X_test.to_csv("./data/result_test.csv", index=False)
