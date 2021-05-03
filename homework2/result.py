import csv
from csv import DictReader
import json


class New_file:
    with open("users.json", "r") as f:
        users = json.loads(f.read())
    users_list = users
    index = len(users_list)

    with open("books.csv", newline='') as fm:
        data_books = []
        books = DictReader(fm)
        for row in books:
            data_books.append({
                "title": row['Title'],
                "author": row['Author'],
                "height": row['Height']
            })
    print(data_books[3])

    with open("result.json", "w") as fb:
        i = 0

        while i < index:
            for user in users:
                bbokk = data_books[i]
                print(bbokk)
                data = {
                    "name": user["name"],
                    "gender": user["gender"],
                    "address": user["address"],
                    "books": [
                            bbokk
                    ]
                }
                i += 1
                s = json.dumps(data, indent=4)
                fb.write(s)
