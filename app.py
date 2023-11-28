import database
from flask import Flask, render_template

app=Flask(__name__)



@app.route("/")
def hello_world():
  cnx,cur=database.loadDB()
  cur.execute("SELECT * FROM rgukt.jobs")
  JOBS=cur.fetchall()
  print(JOBS)
  return render_template('home.html',jobs=JOBS)

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)