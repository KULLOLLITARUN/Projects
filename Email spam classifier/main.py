from flask import Flask,render_template,request
import pickle
# Creates a Flask web application.
app = Flask(__name__)


pipe = pickle.load(open("Naive_model.pkl","rb"))

@app.route('/', methods=["GET","POST"])
# Handles the main functionality of the web application.
def main_function():
    if request.method == "POST":
        text = request.form
        # print(text)
        emails = text['email']
        print(emails)
        
        list_email = [emails]
        # print(list_email)
        output = pipe.predict(list_email)[0]
        print(output)


        return render_template("show.html", prediction = output)
    
    else:
        # Runs the Flask web application in debug mode
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)