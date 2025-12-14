import pandas as pd
import pickle
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from scipy.sparse import hstack

# -------------------------------
# PATHS
# -------------------------------
BASE = Path(__file__).parent
DATA_PATH = BASE / "data" / "dstv_queries_2000.csv"
MODEL_DIR = BASE / "models"
MODEL_DIR.mkdir(exist_ok=True)

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv(DATA_PATH)

print("Data loaded:", df.shape)

# -------------------------------
# CATEGORY CLASSIFIER
# -------------------------------
X_text = df["Query_Text"]
y_category = df["Category"]

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=2000
)

X_vec = vectorizer.fit_transform(X_text)

X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y_category, test_size=0.2, random_state=42
)

category_clf = LogisticRegression(max_

