import json

with open('link.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

unique_urls = set()

def remove_duplicates(data):
    for category in data:
        unique_list = []
        for item in category['typeList']:
            if item['url'] not in unique_urls:
                unique_urls.add(item['url'])
                unique_list.append(item)
        category['typeList'] = unique_list

# 去重操作
remove_duplicates(data)

with open('link.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print("去重完成，结果已保存到 link.json 文件中。")