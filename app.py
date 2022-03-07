#Import Modules
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify


# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
base = automap_base()
base.prepare(engine,reflect = True)
base.classes.keys()

# Save references to each table
Measurement = base.classes.measurement
Station = base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)
app = Flask(__name__)


@app.route("/")
def welcome():
    return(
        f"Pages to visit: <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/yyyy-mm-dd<br/>"
        f"/api/v1.0/yyyy-mm-dd/yyyy-mm-dd"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    one_year_prior = dt.date(2017,8,23) - dt.timedelta(days = 365)
    date_precip = session.query(Measurement.date,Measurement.prcp).\
    filter(Measurement.date >= one_year_prior,Measurement.prcp != None).\
    order_by(Measurement.date).all()
    return jsonify(dict(date_precip))

#Only way I could get this JSON serializable was to make it a for loop
@app.route("/api/v1.0/stations")
def stations():
    items = [Station.station , Station.name]
    query1 = session.query(*items).all()
    session.close()

    stations = []
    for station,name in query1:
        station_dict = {}
        station_dict["Station"] = station
        station_dict["Name"] = name
        stations.append(station_dict)

    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def tobs():
    lateststr = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    latestdate = dt.datetime.strptime(lateststr, '%Y-%m-%d')
    querydate = dt.date(latestdate.year -1, latestdate.month, latestdate.day)
    sel = [Measurement.date , Measurement.tobs]
    query2 = session.query(*sel).filter(Measurement.date >= querydate).all()
    session.close()

    tob_all = []
    for date, tobs in query2:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Tobs"] = tobs
        tob_all.append(tobs_dict)

    return jsonify(tob_all)


@app.route('/api/v1.0/<start>')
def tobs_with_start(start):
    query_calc1 = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    session.close()

    tobsall = []
    for min,avg,max in query_calc1:
        tobs_dict = {}
        tobs_dict["Min"] = min
        tobs_dict["Average"] = avg
        tobs_dict["Max"] = max
        tobsall.append(tobs_dict)

    return jsonify(tobsall)



@app.route('/api/v1.0/<start>/<end>')
def tobs_with_start_end(start,end):
    query_calc2 = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()

    tobsall = []
    for min,avg,max in query_calc2:
        tobs_dict = {}
        tobs_dict["Min"] = min
        tobs_dict["Average"] = avg
        tobs_dict["Max"] = max
        tobsall.append(tobs_dict)

    return jsonify(tobsall)

#@app.route
if __name__ == '__main__':
    app.run(debug = True)