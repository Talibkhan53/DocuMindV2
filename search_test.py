from app.config import get_settings
from app.Clients.search_client import SearchClient

s = get_settings()
client = SearchClient(s.search_engine_url, s.search_engine_api_key, s.request_timeout)

print("healthy:", client.health())

print(client.index_document(
    "dm-test1", "python.txt",
    "Python is a popular programming language used for web development, data science and automation." \
    "Game Of Thrones"
))

for hit in client.search("Game Of Thrones", top_k=3):
    print(round(hit["score"], 3), hit["text"][:80])