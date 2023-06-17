import json
def retrieve_access_token(self):
    with open("/home/deepika/Desktop/Deepika/Testpro/login_data.json", 'r') as file:
            data = json.load(file)
            access_token = data['credentials']['access_token']
            print("access token---->",access_token)
            return access_token