# %%
import numpy as np, pandas as pd, seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import category_encoders as ce
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score,classification_report
import matplotlib.pyplot as plt
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

# %%
df = pd.read_csv("new data.csv")

# %%
df.head(10)

# %%
df.shape

# %%
df["Interest"]

# %%
df["Latitude"]

# %%
df["Longitude"]

# %%
df["Place Name"]

# %%
df.isnull().sum()

# %%
df["Interest"].unique()

# %%
df["Interest"].nunique()

# %%
# le = LabelEncoder()
# le.fit(df["Interest"])

# %%
# df["Interest_label"] = le.transform(df["Interest"])

# %%
df

# %%
df["Place Name"].str.lower()

# %%
df["Interest"] = df["Interest"].str.lower()

# %%
# x_train,x_test,y_train,y_test = train_test_split(df["Place Name"],df["Interest"],test_size=0.3,random_state=42)

# %%
# vec = CountVectorizer()
# vec_tfidf = TfidfVectorizer()
# # x_train_vec = vec.fit_transform(x_train)
# # x_test_vec = vec.fit_transform(x_test)
# # x_vec = vec.fit_transform(df["Interest"])
# x_train_tfidf = vec.fit_transform(x_train)
# x_test_tfidf = vec.transform(x_test)

# %%
# model = make_pipeline(CountVectorizer(), MultinomialNB())
# model1 = make_pipeline(CountVectorizer(), LogisticRegression())

# %%
# model.fit(x_train,y_train)

# %%
# prediction = model.predict(x_test)

# %%
# accuracy_score(y_test,prediction)

# %%
# model1.fit(x_train,y_train)

# %%
# pred = model1.predict(x_test)

# %%
# accuracy_score(y_test,pred)

# %%
data = df
def find_place(interest):
    interest = interest.lower().strip()
    data['Interest'] = data['Interest'].str.lower().str.strip()

        # Filter the dataset based on the given interest
    filtered_data = data[data['Interest'] == interest]

        # Extract the list of places
    places = filtered_data['Place Name'].tolist()
#     print(places)
    return places

# %%
for i in df["Interest"].unique():
    print(i)
inp = input("\nenter a interest from the given list: ")
result = find_place(inp)
print("\nThe places which are related to your interest are: \n")
for i in result:
    print(i)
print("\ntotal number of places found: ",len(result))

# %%



