
import requests
import subprocess

#debug
import pprint


base_url = "https://canvas.instructure.com/api/v1/courses"

#curl -H "Authorization: Bearer <ACCESS-TOKEN>" "https://canvas.instructure.com/api/v1/courses"

def get_grade_info():
 #   url = f"{base_url}/users?/{name}"

    headers = {"Authorization": "Bearer 10706~wJETeETFe6nwyHhTkDkGnth8yBYrWmKyzP438Qnww3h2hWknDHCMextVf8X4KTrU"}
    response = requests.get("https://canvas.instructure.com/api/v1/courses/107060000000355464/assignments", headers=headers)

    if response.status_code == 200:
        test_data = response.json()
        pprint.pprint(test_data) 
    else:
        print(f"Failed to retrieve data {response.status_code}")

get_grade_info()
