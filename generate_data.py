import json

data = []
for i in range(1, 101):
    category = "category1" if i <= 50 else "category2"
    item = {
        "content_id": i,
        "content": f"内容项 {i}",
        "metadata": f"元数据 {i}",
        "category": category
    }
    data.append(item)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("data.json 文件已生成")