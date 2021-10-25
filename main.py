#main.py
import json

from flask import Flask, jsonify, request
from google.cloud import bigquery
from google.oauth2 import service_account

app = Flask(__name__)
# TODO(developer): Set key_path to the path to the service account key
#                  file.
key_path = "durable-melody-328621-3e36bc056967.json"

credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

# Construct a BigQuery client object.
client = bigquery.Client(credentials=credentials, project=credentials.project_id, )

# TODO(developer): Set table_id to the ID of the table
# table_id = "durable-melody-328621.bqml_tutorial.londom_tutorial_clusters"

query_job = client.query(
    """
    SELECT *
    FROM `durable-melody-328621.bqml_tutorial.london_tutorial_clusters`
    LIMIT 10"""
)

results = query_job.result()  # Waits for job to complete.

records = [dict(row) for row in results]
output = json.dumps(str(records))

#for row in results:
    # output = str(row[0])
 #   output = {}
  #  output.update(row)


#for row in results:
    # print("{} : {} views".format(row.station_name, row.num_trips))

songs = [
    {
        "title": "Rockstar",
        "artist": "Dababy",
        "genre": "rap",
    },
    {
        "title": "Say So",
        "artist": "Doja Cat",
        "genre": "Hiphop",
    },
    {
        "title": "Panini",
        "artist": "Lil Nas X",
        "genre": "Hiphop"
    }
]

@app.route('/')
def query():
    return output

@app.route('/songs')
def home():
    return jsonify(songs)

@app.route('/songs', methods=['POST'])
def add_songs():
    song = request.get_json()
    songs.append(song)
    return jsonify(songs)

if __name__ == '__main__':
    app.run(debug=True)
