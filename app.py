from flask import Flask, render_template, jsonify

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Gaming Laptop",
        "price": 85000,
        "image": "https://imgs.search.brave.com/ygdlM8jmMelAeA6cNXrbTj3HamSWzMOzU376Ia4Q3FU/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9waXNj/ZXMuYmJ5c3RhdGlj/LmNvbS9pbWFnZTIv/QmVzdEJ1eV9VUy9p/bWFnZXMvcHJvZHVj/dHMvM2QwMTdhYzMt/NzI0Mi00ODA0LThj/NzQtODJiZTRkNTFj/Y2UyLmpwZw"
    },
    {
        "id": 2,
        "name": "iPhone 15",
        "price": 70000,
        "image": "https://imgs.search.brave.com/O8-0x_NDVZmqiQ6Syg3eV7PEpg9pwcryyEjuoEeqBw8/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/OTEtaW1nLmNvbS9w/aWN0dXJlcy8xNDg3/NjYtdjgtYXBwbGUt/aXBob25lLTE1LXBy/by1tb2JpbGUtcGhv/bmUtaHJlcy0xMi5q/cGc_dHI"
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 4000,
        "image": "https://imgs.search.brave.com/QSlmLAycuqSh_2mp-HAGYKKiafb6QaFHn80sbFKfoXc/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tLm1l/ZGlhLWFtYXpvbi5j/b20vaW1hZ2VzL0kv/NzFxdDRhUXBlZUwu/anBn"
    },
    {
        "id": 4,
        "name": "Smart Watch",
        "price": 6000,
        "image": "https://imgs.search.brave.com/QfypBRJu5548fyPQNDCZ0tiPvj9_g4qBZKlGBAX-Ad4/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/ZnJlZS12ZWN0b3Iv/c21hcnR3YXRjaC1m/cm9udC1zaWRlXzIz/LTIxNDc0OTg4MDIu/anBnP3NlbXQ9YWlz/X2luY29taW5nJnc9/NzQwJnE9ODA"
    },
    {
        "id": 5,
        "name": "Gaming Mouse",
        "price": 2500,
        "image": "https://imgs.search.brave.com/mQb69uBttMrWdLvyujwFD1WWPeOfPwNa4GXhZ_aQl-0/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9rcmVv/LXRlY2guY29tL2Nk/bi9zaG9wL2ZpbGVz/L2JsYWNrX2QyY19w/ZHBfMy5wbmc_dj0x/NzcxMjQ5MDY0Jndp/ZHRoPTEyMDA"
    },
    {
        "id": 6,
        "name": "Mechanical Keyboard",
        "price": 5500,
        "image": "https://imgs.search.brave.com/RKNNn7mCJGFBRJ2CYZQG7mH1C2R3q3NSuKV2yijpp2M/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tLm1l/ZGlhLWFtYXpvbi5j/b20vaW1hZ2VzL0kv/NjE4QStCMjVNS0wu/anBn"
    }
]

cart = {}

@app.route('/')
def home():

    cart_items = []
    total = 0

    for product_id, quantity in cart.items():

        product = next((p for p in products if p['id'] == product_id), None)

        if product:

            subtotal = product['price'] * quantity
            total += subtotal

            cart_items.append({
                'id': product['id'],
                'name': product['name'],
                'price': product['price'],
                'quantity': quantity,
                'subtotal': subtotal
            })

    return render_template(
        'index.html',
        products=products,
        cart_items=cart_items,
        cart_count=sum(cart.values()),
        total=total
    )

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    return jsonify({
        'success': True
    })

@app.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):

    if product_id in cart:

        cart[product_id] -= 1

        if cart[product_id] <= 0:
            del cart[product_id]

    return jsonify({
        'success': True
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)