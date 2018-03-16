from google.cloud import storage

client = storage.Client.from_service_account_json('~/.interline-planetutils/valhalla-tilepacks-key.json') # TODO: allow override in arg or env var?

bucket = client.get_bucket('valhalla-tiles') # TODO: allow override?
# Then do other things...
blob = bucket.get_blob('remote/path/to/file.txt')
print(blob.download_as_string())
