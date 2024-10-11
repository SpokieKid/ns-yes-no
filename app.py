from flask import Flask, render_template, request, jsonify
import json
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
@app.route('/<category>')
def category_page(category='category1'):
    return render_template('index.html', category=category)

@app.route('/get_items/<category>')
def get_items(category):
    data = load_data()
    items = [item for item in data if item['category'] == category]
    return jsonify({'items': items[:10]})

@app.route('/submit_response', methods=['POST'])
def submit_response():
    action = request.form.get('action')
    content_id = int(request.form.get('content_id'))
    category = request.form.get('category')
    
    logging.debug(f'Content ID: {content_id}, User action: {action}')

    data = load_data()
    data = [item for item in data if item['content_id'] != content_id]

    remaining_items = [item for item in data if item['category'] == category]

    new_items = remaining_items[:10]
    
    save_data(data)

    return jsonify({'new_items': new_items})

def load_data():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        logging.debug(f"Loaded {len(data)} items from data.json")
        return data
    except json.JSONDecodeError as e:
        logging.error(f"JSON decoding error: {e}")
        raise
    except IOError as e:
        logging.error(f"File I/O error: {e}")
        raise

def save_data(data):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    logging.debug(f"Saved {len(data)} items to data.json")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)