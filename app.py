from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <html>
        <head>
            <title>Hello, World!</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
                h1 { color: #4CAF50; }
            </style>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>Welcome to my Flask application!</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
