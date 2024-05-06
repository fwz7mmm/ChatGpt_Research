from web import db



class Data(db.Model):
    __tablename__ = 'PMData'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PMID = db.Column(db.Integer)
    Country = db.Column(db.String(128))
    Language = db.Column(db.String(128))
    Exam_Year = db.Column(db.String(128))
    Exam_Name = db.Column(db.String(128))
    Exam_Description = db.Column(db.String(1024))
    Question_Type = db.Column(db.String(128))
    Pass_Criteria = db.Column(db.String(128))
    Question_Filter = db.Column(db.String(128))
    Question_Num_Before = db.Column(db.String(128))
    Question_Num_After = db.Column(db.String(128))
    Model = db.Column(db.String(128))
    Correct_Response = db.Column(db.String(128))
    Score = db.Column(db.String(128))
    Accuracy = db.Column(db.String(128))
    Pass = db.Column(db.String(128))
    Data_availability = db.Column(db.VARCHAR(512))


class Artical(db.Model):
    __tablename__ = 'Artical'
    pmid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    authors = db.Column(db.String(512))
    title = db.Column(db.String(512))
    abstract = db.Column(db.String(1024))
    publication_date = db.Column(db.String(512))
    publication_year = db.Column(db.Integer)
    journal = db.Column(db.String(512))