#main.py
import json

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
#from flask_session import Session
from google.cloud import bigquery
from google.oauth2 import service_account
import google.auth


app = Flask(__name__)
#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] - "filesystem"
#Session(app)
api = Api(app)
""" app.config['CORS_HEADERS'] = "Content-Type"
app.config['CORS_RESOURCES'] = {r"/*": {"origins": "*"}} """

#cors = CORS(app)
CORS(app, resources={r"*": {"origins": "*"}})
# TODO(developer): Set key_path to the path to the service account key
#                  file. TESTING ONLY
key_path = "durable-melody-328621-3e36bc056967.json"

# for TESTING ONLY
credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

# for TESTING ONLY
client = bigquery.Client(credentials=credentials, project=credentials.project_id, )

# for DEPLOY
# client = bigquery.Client()

# for loading table
#table_id = "black-nucleus-329901.bqml_tutorial.london_tutorial_clusters"

query_job = client.query(
    """
    SELECT *
    FROM `black-nucleus-329901.bqml_tutorial.london_tutorial_clusters`
    LIMIT 100
    """
)

#results = query_job.result()  # Waits for job to complete.
df = query_job.to_dataframe()
json_obj = df.to_json(orient='records')

""" records = [dict(row) for row in results]
output = json.dumps(str(records)) """

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

""" @app.after_request
@cross_origin()
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response """

@app.route('/', methods=['GET'])
@cross_origin()
def query():
    response = json_obj # results # jsonify(output)
    return response

@app.route('/songs')
def home():
    return jsonify(songs)

@app.route('/songs', methods=['POST'])
def add_songs():
    song = request.get_json()
    songs.append(song)
    return jsonify(songs)

''' if __name__ == '__main__':
    app.run(debug=True) '''
