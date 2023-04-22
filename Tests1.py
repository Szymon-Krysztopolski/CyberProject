import pymongo
import sys
import numpy as np
from PIL import Image
from datetime import datetime

import properties

image = Image.open("Image1.jpg")
image_array = np.array(image)
image_array = image_array.tolist()

try:
	client = pymongo.MongoClient(
		f"mongodb+srv://{properties.DB_USERNAME}:{properties.DB_PASSWORD}@{properties.DB_CLUSTER}/test?retryWrites=true&w=majority")

except pymongo.errors.ConfigurationError:
	print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
	sys.exit(1)

db = client.myDatabase

my_collection = db["Images"]

image_documents = [
	{"Name": "1", "Date": datetime.today().replace(microsecond=0), "Image": image_array}]

try:
	result = my_collection.insert_many(image_documents)

except pymongo.errors.OperationFailure:
	print(
		"An authentication error was received. Are you sure your database user is authorized to perform write operations?")
	sys.exit(1)
else:
	inserted_count = len(result.inserted_ids)
	print("I inserted %x documents." % (inserted_count))

	print("\n")

