import requests

import json
import threading

output_file = 'products.json'

products = []


def fetch_and_save_data(product_id):
    url = f"https://dummyjson.com/products/{product_id}"
    response = requests.get(url)

    product = {
        'id': data.get('id'),
        'title': data.get('title'),
        'description': data.get('description'),
        'price': data.get('price'),
        'discountPercentage': data.get('discountPercentage'),
        'rating': data.get('rating'),
        'stock': data.get('stock'),
        'brand': data.get('brand'),
        'category': data.get('category'),
        'thumbnail': data.get('thumbnail'),
        'weight': data.get('weight')
    }

    products.append(product)

threads = []
for i in range(1, 30):
    t = threading.Thread(target=fetch_and_save_data, args=(i,))
    threads.append(t)
    t.start()


for t in threads:
    t.join()

with open(output_file, 'w') as file:
    json.dump(products, file)

print("Ma'lumotlar muvaffaqiyatli saqlandi.")
