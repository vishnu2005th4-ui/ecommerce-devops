from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"name": "Laptop", "price": "₹50000"},
    {"name": "Phone", "price": "₹20000"},
    {"name": "Headphones", "price": "₹3000"}
]

@app.route('/')
def home():
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
