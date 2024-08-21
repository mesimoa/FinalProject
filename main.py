from flask import Flask,redirect,request,url_for,render_template
import flask
import pymongo


app=Flask(__name__)
client=pymongo.MongoClient('mongodb://localhost:27017/mydatabase')
db=client['mydatabase']
collection=db['response']


@app.route('/')
def home():
        return render_template('template.html')


@app.route('/submit', methods=['POST'])
def submit ():
    if request.method == 'POST':
        age=request.form['age']
        gender=request.form['gender']
        total_income=request.form['total_income']
        expenses={
              'utilities':request.form.get('utilities',0),
              'entertainment':request.get('entertainment',0),
              'school_fees':request.get('school_fees',0),
              'healthcare':request.form('healthcare',0)
                 }
        user_data={'age':age,
                   'gender':gender,
                   'total_income':total_income,
                   'expenses':expenses
                   }
        collection.insert_one(user_data)
        return redirect(url_for('submit'))
    
if __name__=='__main__':
     app.run(debug=True)