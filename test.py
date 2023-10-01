import requests
from datetime import datetime, timezone


NOTION_TOKEN = 'secret_56MUkMVoC11Troe8hqCO4OUKXrXUpj2nHzUeyx5rGjU'
DATABASE_ID = 'b775c507446f489db39fa5f9f7a096b0'

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}
def get_pages(num_pages=None):

    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    payload = {"page_size": 100}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    # Comment this out to dump all data to a file
    import json
    with open('db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]
    return results
pages = get_pages()
def create_page(data: dict):
    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": DATABASE_ID}, "properties": data}

    res = requests.post(create_url, headers=headers, json=payload)
    # print(res.status_code)
    return res

client = "John Doe"
client_parent_1 = "Test"
client_parent_2 = "Test"
client_contact_info = "Test"
client_parent_1_info = "Test"
client_parent_2_info = "Test"
counselor = "Ishaan Bansal"
application_manager = 'Sean Andre Membrido'
project_manager = 'Raghu P'
editor = "Mayuri"
published_date = datetime.now().astimezone(timezone.utc).isoformat()
data = {
    "Client": {"title": [{"text": {"content": client}}]},
    "Counselor": {"rich_text": [{"text": {"content": counselor}}]},
    "Application Manager": {"rich_text": [{"text": {"content": application_manager}}]},
    "Project Manager": {"rich_text": [{"text": {"content": project_manager}}]},
    "Editor": {"rich_text": [{"text": {"content": editor}}]},

    "Published": {"date": {"start": published_date, "end": None}}
}

create_page(data)

'''
for page in pages:
    page_id = page["id"]
    props = page["properties"]
    url = props["URL"]["title"][0]["text"]["content"]
    title = props["Title"]["rich_text"][0]["text"]["content"]
    published = props["Published"]["date"]["start"]
    published = datetime.fromisoformat(published)
    print(url, title, published)
'''

