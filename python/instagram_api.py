from instagram_private_api import Client, ClientCompatPatch

user_name = 'fatma.janna.utp@gmail.com'
password = 'fatjan91'

api = Client(user_name, password)
results = api.feed_timeline()
print(results)
items = results.get('feed_items', [])
for item in items:
    # Manually patch the entity to match the public api as closely as possible, optional
    # To automatically patch entities, initialise the Client with auto_patch=True
    ClientCompatPatch.media(item)
    # print(media['code'])
    print(item)