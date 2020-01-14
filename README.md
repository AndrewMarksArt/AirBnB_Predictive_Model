# AirBnB_Predictive_Model
Build week project, AirBnB price prediction model using historical data

Tool to help people looking to book an AirBnB find a listing that offers good value.

Uses AirBnB data form Ireland to build map visualizations that display whether or not a listing is a good, fair, or poor value based on how the predicted prices compare to the actual price per night.

Maps show points for each listing, points are sized by price and colored red, yellow, and green based on how good or poor the value is.

The data exploration notebook covers the basic exploration and cleaning.

The model notebook is where a baseline, simple regression, feature selection, random forest regression, hyperparameter tuning and maps are created.

The airbnb folder contains the simple flask app which for now loads a simple two column page, in one column is links to premade maps of selected cities, in the other column there are drop down boxes for the user to select a few variables which will be used to create a custom map of listings showing what value the listings are.
