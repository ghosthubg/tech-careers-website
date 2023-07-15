#import flask
from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Midrand',
    'salary': 'R8000',
  },
  {
    'id': 2,
    'title': 'Software Engineer',
    'location': 'Midrand',
    'salary': 'R14000',
  },
  {
    'id': 3,
    'title': 'Frontend Developer',
    'location': 'Sandton',
    'salary': 'R13000',
  },
  {
    'id': 4,
    'title': 'Backend Developer',
    'location': 'Remote',
    'salary': 'R15000',
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


#check if running as python script
#start app locally
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
