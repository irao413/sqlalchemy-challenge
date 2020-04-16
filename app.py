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

    twelve_months = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

    one_year = dt.date(2017, 8, 9) - dt.timedelta(days=365)

    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date > one_year).order_by(Measurement.date).all()
    
    session.close()

    dict = dict(precipitation)

    return jsonify(dict)


 @app.route("/api/v1.0/stations")
    def stations():
    """Station Records"""

    session = Session(engine)
    
    stations = session.query(Measurement.station, func.count(Measurement.station)).\
        group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
    
    session.close()

    station_list = [list(U) for U in stations]

    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
    def tobs():
    "Temperatures"

    session = Session(engine)

    stations = session.query(Measurement.station, func.count(Measurement.station)).\
        group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()

    one_year = dt.date(2017, 8, 9) - dt.timedelta(days=365)

    tobs = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > one_year).all()
    
    session.close()

    tobs_list = [list(t) for t in tobs]

    return jsonify(tobs_list)

@app.route("/api/v1.0/<1/1/2010>")
    def start():
        """Start Date"""

        session = Session(engine)

        start_session = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).group_by(Measurement.date).all()

        session.close()

        start_list = [list(s) for s in start]

        return jsonify(start_list)

@app.route(/api/v1.0/1/1/2010/<8/9/2017>)
    def end():
        "End Date"

        session = Session(engine)

        end_session = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= end_date).group_by(Measurement.date).all()

        session.close()

        end_list = [list(e) for e in end]

        return jsonify(end_list)

if __name__ == "__main__":
    app.run(debug=True)
