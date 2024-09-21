import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static', template_folder='./')

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":  

        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")  

        data_check = pd.read_csv('data.csv')
        for i in data_check['email']:
            if i == email:
                email_error = True
                return render_template("index.html", email_error=email_error)
        for i in data_check['username']:
            if i == username:
                username_error = True
                return render_template("index.html", username_error=username_error)

        data = pd.DataFrame({
            'email': [email],
            'username': [username],
            'password': [password]
        })
        data.to_csv('data.csv', mode='a', header=False, index=False)
        
        return '<body style="font-family: Fira Code; background-color: #2E3440;"><center><strong><h1 style="color: #81a1c1;">Form submitted successfully!<h1><strong><center><body>'
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
