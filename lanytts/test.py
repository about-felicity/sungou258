from google import genai
import os

os.environ['http_proxy']='http://127.0.0.1:7890'
os.environ['https_proxy']='http://127.0.0.1:7890'
os.environ['all_proxy']='socks5://127.0.0.1:7890'


client = genai.Client(api_key="AIzaSyAVWVhjxANpmyZasFil2L3rWm9rVRaZ8ds")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="你是谁"
)
print(response.text)


