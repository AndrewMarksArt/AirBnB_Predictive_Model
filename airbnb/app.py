"""Code for AirBnB app"""

from flask import Flask, render_template
from .models import DB, Listing
import pandas as pd

def create_app():
    """ Create and configure an instance of the Flask application """
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airbnb_db.sqlite3'

    DB.init_app(app)

    @app.route('/', methods=['GET'])
    def root():
        # create database and load cleaned AriBnB data
        DB.create_all()
        engine = DB.get_engine()
        session = DB.Session(bind=engine)
        df = pd.read_csv('https://raw.githubusercontent.com/AndrewMarksArt/AirBnB_Predictive_Model/master/listings_for_db.csv')
        df.to_sql(
            'listings',
            con=engine,
            index=True,
            index_label='id',
            if_exists='replace'
        )

        markets = [r.market for r in session.query(Listing.market).distinct()]
        bedrooms = [r.bedrooms for r in session.query(Listing.bedrooms).distinct()]
        bathrooms = [r.bathrooms for r in session.query(Listing.bathrooms).distinct()]
        room_type = [r.room_type for r in session.query(Listing.room_type).distinct()]
        accommodates = [r.accommodates for r in session.query(Listing.accommodates).distinct()]
        return render_template(
            'base.html', 
            markets=markets, 
            bedrooms=bedrooms, 
            bathrooms=bathrooms,
            room_type=room_type,
            accommodates=accommodates
            )

    @app.route('/dublin')
    def dublin_map():
        return render_template('Dublin_AirBnB_Value_Map.html')

    @app.route('/cork')
    def cork_map():
        return render_template('Cork_value_map.html')

    @app.route('/donegal')
    def donegal_map():
        return render_template('Donegal_value_map.html')

    @app.route('/galway')
    def galway_map():
        return render_template('Galway_value_map.html')
        
    @app.route('/limerick')
    def limerick_map():
        return render_template('Limerick_value_map.html')

    return app
