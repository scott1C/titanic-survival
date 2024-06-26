import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


file_path = os.path.join(os.path.dirname(__file__), 'sample-data/Titanic-Dataset.csv')
df = pd.read_csv(file_path)

# Deleting rows which we do not need
df.drop(columns=['Cabin', 'PassengerId', 'Ticket', 'Name', 'Embarked'], inplace=True)

# Data Cleaning and handling missing values
df.drop_duplicates(inplace=True)

columns = df.columns.tolist()
for col in columns:
    if df[col].dtype == 'object':
        df[col] = df[col].str.lower()
    if col != 'Sex':
        df[col] = df[col].fillna(df[col].median())

# Data splitting
y = df['Survived']
X = df.drop(columns=['Survived'])

# Convert categorical variables into numerical representations
X = pd.get_dummies(X, drop_first=True)  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize logistic regression model
model = LogisticRegression(max_iter=1000)

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
prediction = model.predict(X_test)
accuracy = accuracy_score(y_test, prediction)
print("Accuracy:", accuracy)

# Print classification report
print(classification_report(y_test, prediction))