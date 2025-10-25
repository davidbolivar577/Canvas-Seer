'''
import requests
import subprocess
import json


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
        print(list(test_data[1].keys()))
        courseList = []
        for course in test_data:
            name = course["name"]
            id = course["id"]
            
            courseList.append([name, id])
        pprint.pprint(courseList)
        #pprint.pprint(test_data) 
        #while():

        #assignments = test_data[0]['name']
        #grades = test_data[0]['points_possible']
        #pprint(assignments)
        #pprint(grades)
    else:
        print(f"Failed to retrieve data {response.status_code}")

get_grade_info()

'''