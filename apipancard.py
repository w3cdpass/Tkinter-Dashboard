import requests
import json 

def chec_my(enter_pan):
    url = "https://pan-card-verification1.p.rapidapi.com/v3/tasks/sync/verify_with_source/ind_pan"

    payload = {
        "task_id": "74f4c926-250c-43ca-9c53-453e87ceacd1",
        "group_id": "8e16424a-58fc-4ba4-ab20-5bc8e7c3c41e",
        "data": { "id_number": enter_pan }
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "d2ec0d3958msh9a4c35e841eb4d2p1fb84cjsnffd7656bc39d",
        "X-RapidAPI-Host": "pan-card-verification1.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()


detial = chec_my("NNEPS7326P")

person = detial['result']['source_output']

print(person['first_name'], person['last_name'])

print(f"Linked with aadhar: {person['aadhaar_seeding_status']}")


# print(response.json())\
# preety = json.dumps(response, indent=4)
# print(preety)

# 