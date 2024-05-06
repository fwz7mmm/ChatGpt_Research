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


home_blue = Blueprint('home', __name__)
@home_blue.route('/')
def index():
    return render_template("Home.html")

@home_blue.route('/LeaderBoard')
def LeaderBoard():
    return render_template("LeaderBoard.html", PMdata=Data.query.all())

@home_blue.route('/Paper')
def Paper():
    return render_template("Paper.html", Articaldata=Artical.query.all())

@home_blue.route('/PaperCard/<id>')
def PaperCard(id):
    #print(id)
    paper = session.query(Artical).filter(Artical.pmid==id).first()
    #print(paper.pmid)
    return render_template("PaperCard.html", data=paper)

@home_blue.route('/Submit')
def Submit():
    return render_template("Submit.html")


@home_blue.route('/Statistic')
def Statistic():
    return render_template("Statistic.html")


