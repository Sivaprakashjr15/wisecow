import random
import cowsay
from flask import Flask, Response

app = Flask(__name__)

# Predefined "fortunes"
fortunes = [
    "Living your life is a task so difficult, it has never been attempted before."
]

@app.route("/")
def serve_wisdom():
    # Select a random fortune
    mod = random.choice(fortunes)
    cow_message = cowsay.get_output_string("default", mod)
    return Response(f"<pre>{cow_message}</pre>", mimetype="text/html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4499)
