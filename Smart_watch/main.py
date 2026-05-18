import datetime
import requests
from google_auth_oauthlib.flow import InstalledAppFlow
SCOPES = [
    'openid',
    'https://www.googleapis.com/auth/fitness.activity.read',
    'https://www.googleapis.com/auth/fitness.body.read',   # ADD
    'https://www.googleapis.com/auth/fitness.location.read', # ADD (distance)
    'https://www.googleapis.com/auth/fitness.heart_rate.read', # ADD
    'https://www.googleapis.com/auth/userinfo.profile',
    'https://www.googleapis.com/auth/userinfo.email'
]
# Step 1: Login
flow = InstalledAppFlow.from_client_secrets_file(
    'credentials.json',
    SCOPES
)

creds = flow.run_local_server(port=8080)
access_token = creds.token

print("\n✅ Login Success")

# Step 2: Get User Info (VERY IMPORTANT)
user_info = requests.get(
    "https://www.googleapis.com/oauth2/v2/userinfo",
    headers={"Authorization": f"Bearer {access_token}"}
)

user = user_info.json()
print("\n👤 USER DETAILS:")
print("Email:", user.get("email"))
print("Name:", user.get("name"))

# Step 3: Get TODAY time range (LOCAL TIME)
now = datetime.datetime.now()
start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)

start_millis = int(start_of_day.timestamp() * 1000)
end_millis = int(now.timestamp() * 1000)

print("\n🕒 Time Range:")
print("Start:", start_of_day)
print("End:", now)

# Step 4: API Request
url = "https://www.googleapis.com/fitness/v1/users/me/dataset:aggregate"

# body = {
#     "aggregateBy": [
#         {"dataTypeName": "com.google.step_count.delta"}
#     ],
#     "bucketByTime": {"durationMillis": 86400000},
#     "startTimeMillis": start_millis,
#     "endTimeMillis": end_millis
# }
body = {
    "aggregateBy": [
        {"dataTypeName": "com.google.step_count.delta"},
        {"dataTypeName": "com.google.distance.delta"},
        {"dataTypeName": "com.google.calories.expended"},
        {"dataTypeName": "com.google.heart_rate.bpm"}
    ],
    "bucketByTime": {"durationMillis": 86400000},
    "startTimeMillis": start_millis,
    "endTimeMillis": end_millis
}

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, json=body)

print("\n📡 Status Code:", response.status_code)

data = response.json()

# Debug (optional)
# print("\nRAW RESPONSE:", data)

# Step 5: Extract Steps
result = {
    "steps": 0,
    "distance": 0,
    "calories": 0,
    "heart_rate": []
}

for bucket in data.get("bucket", []):
    for dataset in bucket.get("dataset", []):
        dtype = dataset.get("dataSourceId", "")

        for point in dataset.get("point", []):
            for value in point.get("value", []):

                if "step_count" in dtype:
                    result["steps"] += value.get("intVal", 0)

                elif "distance" in dtype:
                    result["distance"] += value.get("fpVal", 0)

                elif "calories" in dtype:
                    result["calories"] += value.get("fpVal", 0)

                elif "heart_rate" in dtype:
                    result["heart_rate"].append(value.get("fpVal", 0))

print("\n📊 FINAL DATA:")
print(result)