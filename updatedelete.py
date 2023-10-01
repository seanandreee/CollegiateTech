'''def update_page(page_id: str, data: dict):
    url = f"https://api.notion.com/v1/pages/{page_id}"

    payload = {"properties": data}

    res = requests.patch(url, json=payload, headers=headers)
    return res

page_id = "the page id"

new_date = datetime(2023, 1, 15).astimezone(timezone.utc).isoformat()
update_data = {"Published": {"date": {"start": new_date, "end": None}}}

update_page(page_id, update_data)



def delete_page(page_id: str):
    url = f"https://api.notion.com/v1/pages/{page_id}"

    payload = {"archived": True}

    res = requests.patch(url, json=payload, headers=headers)
    return res
'''