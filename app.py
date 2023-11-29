import database
from flask import Flask, render_template

app=Flask(__name__)



@app.route("/")
def hello_world():
  cnx,cur=database.loadDB()
  cur.execute("SELECT * FROM rgukt.jobs")
  JOBS=cur.fetchall()
  return render_template('home.html',jobs=JOBS)

@app.route("/job/<id>")
def show_job(id):
  cnx,cur=database.loadDB()
  qurey = "SELECT * FROM rgukt.jobs WHERE id=" + id
  cur.execute(qurey)
  job1=cur.fetchone()
  if not job1:
    return "Not Found",404
  return render_template('jobpage.html',job=job1)

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)