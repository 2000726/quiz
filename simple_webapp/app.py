from flask import Flask, redirect, url_for, render_template, request, escape
from wtforms.validators import DataRequired
from wtforms import validators

app = Flask(__name__)

#class SimpleForm(FlaskForm):
#    text = StringField(label='text value', validators=[DataRequired(),validators.Regexp(regex="[a-zA-Z0-9]+", message="Bad")])
#    submit = SubmitField(label="Submit")

@app.route("/", methods=["POST","GET"])
def home():
    # 4a
    return render_template("index.html")

@app.route("/search", methods=["POST","GET"])
def search():
    if request.method == "POST":#
        # 4b
        search = format(escape(request.form["srch"]))
        return redirect(url_for("value", val=search))
    else:
        return render_template("index.html")

@app.route("/<val>")
def value(val):
    return f"<h1>htmlspecialchars({val}, 'UTF-8')</h1>"

if __name__ == "__main__":
    app.run(debug=True)