from flask import Flask, jsonify, render_template
import os, sys
from dotenv import load_dotenv
from app import run_pipeline

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():  
    return render_template("index.html")

@app.route("/api/ask", methods=["POST"])
def ask(): 
    result = run_pipeline()
    return jsonify(result)

if __name__ == "__main__":
    if not os.getenv("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY is not set in the environment variables.")
        sys.exit(1)
    print("running server...")
    app.run(debug=True)
