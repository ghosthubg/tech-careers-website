#import flask
from flask import  Flask, render_template

app = Flask(__name__)



@app.route("/")
def hello_world():
  return render_template('home.html')



#check if running as python script
#start app locally
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)