from flask import Flask, jsonify

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def home_page():
    <!DOCTYPE HTML>
    <html lng="en=us">
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>

    <body>
        <!-- Header -->
        <h1>Home Page</h1>

        <!-- Image-->
       
        <br>

        <hr>

    
        <br>

        <hr>
        <br>

        <hr>
        <br>

        <hr>
    </body>
</html>

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Precipitation Records"""

    session = Session(engine)

    # Query precipitation records
    twelve_months = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

    # Calculate the date 1 year ago from the last data point in the database
    one_year = dt.date(2017, 8, 9) - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date > one_year).order_by(Measurement.date).all()
    
    session.close()

    # Convert results into a dictionary
    dict = dict(precipitation)

    return jsonify(dict)