from flask import Flask, render_template, request, jsonify
import json
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/<category>')
def category_page(category):
    return render_template('index.html', category=category)

@app.route('/get_items/<category>')
def get_items(category):
    data = load_data()
    items = [item for item in data if item['category'] == category][:3]  # 修改为获取3个项目
    return jsonify({'items': items})

@app.route('/submit_response', methods=['POST'])
def submit_response():
    action = request.form.get('action')
    content_id = int(request.form.get('content_id'))
    category = request.form.get('category')
    
    print(f'内容ID: {content_id}, 用户动作: {action}')

    data = load_data()
    data = [item for item in data if item['content_id'] != content_id]

    remaining_items = [item for item in data if item['category'] == category]

    new_items = remaining_items[:3] if remaining_items else []  # 返回最多3个新项目
    
    save_data(data)

    return jsonify({'new_items': new_items})

def load_data():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f"JSON 解码错误: {e}")
        raise
    except IOError as e:
        logging.error(f"文件 I/O 错误: {e}")
        raise

def save_data(data):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)