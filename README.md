# How to run

1. Install postgresql and obtain a URL for your database. URL looks like this:
```postgresql://user:password@localhost:5432/database-name```
Make sure, that user `user` either has acces to already existing database `database-name`, or have permissions to create database.

2. Create a file `.env` and put a DB URL from step 1 in it:
```
DB_URL='postgresql://user:password@localhost:5432/database-name'
```

3. Install dependencies:
```shell
pipenv install
```

4. Run backend server:
```shell
pipenv run python app.py
```

5. Open new terminal and make a query to the server:
```shell
curl -X POST \
-H "Content-Type: application/json" \
-d '{"query": "{ getAllLessons { id hall { id city street } coach { id name } } } "}' \
http://localhost:8080/graphql | jq
```

Output should look like this:
```json
{
  "data": {
    "getAllLessons": [
      {
        "id": "1",
        "hall": {
          "id": "1",
          "city": "Kyiv",
          "street": "Velyka Vasylkivska, 22"
        },
        "coach": {
          "id": "1",
          "name": "Alina"
        }
      },
    ]
  }
}
```

Array might contain duplicates, if you re-run backend server, because dummy data is added to database on each launch.