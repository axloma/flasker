from flask import Flask, render_template, url_for, flash, request,redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length,EqualTo, Email, DataRequired,ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YASSER123456'
#app.app_context().push()

class Nform(FlaskForm):
    username = StringField("username")
    submit = SubmitField(label="login")


@app.route('/', methods=["GET", "POST"])
def index():
    #name = " <strong> yasser </strong> not bold"
    formx = Nform()
    #name = formx.username.data
    if formx.validate_on_submit():
        namex ="hi"
        #return redirect(url_for("myhome"))
        name = request.form["name"]
        name2 = formx.username.data
        return render_template("home.html",form=formx,name=name,name2=name2)
        return redirect(url_for("myhome",))
       #return render_template('home.html',form=formx,name=name)
    if request.method == "POST":
       #name = formx.username.data
       name= request.form["name"]
       name2= formx.username.data
       return render_template("home.html",form=formx,name=name,name2=name2)
    else:
        return render_template("myhome.html",name="name",form=formx)
@app.route("/home.html", methods=["GET", "POST"])
def myhome():
    form = Nform()
    myname = form.username.data
    return render_template('home.html',form=form , name=myname)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html'),500
