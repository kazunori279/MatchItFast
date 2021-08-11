# Stub script

import os
import json

from flask import Flask, request, jsonify

import matching.query as matching_query

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    with open("build/index.html", "r") as f:
        html = f.read()
    return html

@app.route('/api/query', methods=["POST"])
def query():
    index_id = os.environ.get("MATCHING_ENGINE_DEPLOYED_INDEX_ID", "")
    ip = os.environ.get("MATCHING_ENGINE_ENDPOINT_IP", "")

    print(request);
    j = request.get_json();
    if "query" not in j:
        return jsonify({ "neighbors": [], "latency": 0.0 })
    with open("build/embeddings/{}.json".format(j["query"]), "r") as f:
        embedding = json.loads(f.read())

    cli = matching_query.MatchingQueryClient(ip, index_id)

    result, latency = cli.query_embedding(embedding, num_neighbors=25)

    return jsonify({ "neighbors": [ { "id": i.id, "distance": i.distance } for i in result.neighbor ], "latency": latency })

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
