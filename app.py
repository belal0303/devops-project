from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps Application</title>
        </head>
        <body>
            <h1> Hello! Welcomemuhamed b belal tokavci DevOps CI/CD!</h1>
            <h2>   Application deployed using Docker and Jenkins.</h2>
            <p>Git + Docker + Jenkins</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
