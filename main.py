"""
Basic RESTful API for calling BigQuery ML predictions and serving to front-end.
"""

from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restful import Api
from google.cloud import bigquery
from google.oauth2 import service_account


app = Flask(__name__)
api = Api(app)

CORS(app, resources={r"*": {"origins": "*"}})

# for DEPLOY
client = bigquery.Client()

######################BEGIN TESTING ONLY################################
# Set key_path to the path to the service account key file.
KEY_PATH = "durable-melody-328621-3e36bc056967.json"

credentials = service_account.Credentials.from_service_account_file(
    KEY_PATH, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

client = bigquery.Client(credentials=credentials, project=credentials.project_id, )
######################END TESTING ONLY################################

# for loading table
#table_id = "black-nucleus-329901.bqml_tutorial.london_tutorial_clusters"

query_job = client.query(
    """
    SELECT *
    FROM `black-nucleus-329901.bqml_tutorial.london_tutorial_clusters`
    LIMIT 100
    """
)

df = query_job.to_dataframe()
json_obj = df.to_json(orient='records')

@app.route('/', methods=['GET'])
@cross_origin()
def query():
    """End point to serve BigQuery response."""
    response = json_obj
    return response
