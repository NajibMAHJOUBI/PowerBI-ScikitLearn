# Import necessary libraries
import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add the target variable to the DataFrame
df['target'] = iris.target
df['target_name'] = df['target'].replace(dict(enumerate(iris.target_names)))

# Drop the target column
df.drop(columns=['target'], inplace=True)