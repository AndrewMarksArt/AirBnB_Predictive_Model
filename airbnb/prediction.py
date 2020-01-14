"""make predictions on listing data"""
import pandas as pd
import statistics as stats
import category_encoders as ce
import folium
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

from .models import DB, Listing

engine = DB.get_engine()
session = DB.Session(bind=engine)

# build model
def predict_price():
    df = pd.read_sql_query(Listings.query.all(), engine)

    # target
    target = 'price'

    #features
    features = df.columns.to_list()
    features.remove(target)

    # split into train and test
    X_train, X_test, y_train, y_test = train_test_split( df[features], df[target], test_size=0.2, random_state=42)

    # encode categorical features
    encoder = ce.OneHotEncoder(use_cat_names=True)
    X_train = encoder.fit_transform(X_train)
    X_test = encoder.transform(X_test)

    # set up random forest regessor model
    rf = RandomForestRegressor(
        n_estimators=1400, 
        min_samples_split=2,
        min_samples_leaf=1,
        max_features='auto',
        max_depth=100,
        bootstrap=True,
        random_state=42, 
        n_jobs=-1
    )

    # fit train data on model
    rf_best.fit(X_train, y_train)

    ## TODO once user submits from base.html query db to create df and predict prices
    ## add predictions, dif from actual price, value, and color to that df and build map
