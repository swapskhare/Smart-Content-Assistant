from flask import Flask, render_template
from app.models.content_generator import generate_content

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate')
def generate():
    content = generate_content("AI ethics")
    return f"<p>{content}</p>"

if __name__ == '__main__':
    app.run(debug=True)
