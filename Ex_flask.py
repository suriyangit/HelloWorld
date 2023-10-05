from flask import *

ob=Flask(__name__);

@ob.route('/')
def index():
    return("hai welcome");

@ob.route('/about')
def about():
    return("<body bgcolor='red'>About Us<br>Hykin Tech....</body>");
@ob.route('/contact')
def cotact():
    return render_template("login.html");

@ob.route('/insert',methods=['GET','POST'])
def insert():
    ss=request.form['t3']
    return ss;


@ob.route('/Add/<x>,<y>')
def Add(x,y):
    return(str(int(x)+int(y)))

if(__name__=='__main__'):
   ob.run();
