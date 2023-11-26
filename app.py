from flask import Flask, render_template

app=Flask(__name__)

JOBS=[
  {
    'id':1,
    'title':'Chemistry-Lab Assistant',
    'location':'RKValley,AndhraPradesh',
    'salary':'Rs.30K'
  },
  {
    'id':2,
    'title':'Maths Professor',
    'location':'Nuzvid,AndhraPradesh',
    'salary':'Rs.50K'
  },
  {
    'id':3,
    'title':'Dance Teacher',
    'location':'Ongole,AndhraPradesh',
    'salary':'Rs.35K'
  },
  {
    'id':4,
    'title':'Security-Guard',
    'location':'Srikakulam,AndhraPradesh',
    'salary':'Rs.15K'
  },
]
@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)