import pandas
from flask import Flask, render_template
from flask import Blueprint
from web.models.data_models import Data, Artical
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///app.db', echo=False)
# 创建session
DbSession = sessionmaker(bind=engine)
session = DbSession()


statistics_blue = Blueprint('statistic', __name__)

@statistics_blue.route('/Statistic/language')
def Language_statistic():
    query = text("select * from PMdata")
    df = pandas.read_sql_query(query, con=engine)
    jsondata, list = column_count("Language", df)
    return render_template("echartPie.html", json=jsondata, legend=list)

@statistics_blue.route('/Statistic/year')
def Year_statistic():
    query = text("select * from Artical")
    df = pandas.read_sql_query(query, con=engine)
    jsondata, list = column_count("publication_year", df)
    return render_template("echartPie.html", json=jsondata, legend=list)

@statistics_blue.route('/Statistic/model')
def Model_statistic():
    query = text("select * from PMdata")
    df = pandas.read_sql_query(query, con=engine)
    jsondata, list = column_count("Model", df)
    return render_template("echartPie.html", json=jsondata, legend=list)

def column_count(column_name, df):
    values = df[column_name].value_counts(dropna=True).keys().tolist()
    counts = df[column_name].value_counts(dropna=True).tolist()
    value_dict = {'data': [{'value': c, 'name': v} for c, v in zip(counts, values)]}
    return value_dict.get("data"), values