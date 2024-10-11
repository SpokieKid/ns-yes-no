import json

data = []
for i in range(1, 101):
    category = "category1" if i <= 50 else "category2"
    item = {
        "content_id": i,
        "content": f"content {i}",
        "metadata": f"metadata {i}",
        "category": category
    }
    data.append(item)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("data.json is generated")