import json
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def get_info():
    try:
        slack_name = request.args.get('slack_name')
        track = request.args.get('track')

        if not slack_name:
            raise ValueError("Slack name is required.")
        if not track:
            raise ValueError("Track is required.")

        current_day = datetime.datetime.now().strftime('%A')
        utc_time = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        github_file_url = request.url
        github_repo_url = "https://github.com/ZoeSamm/hng_Api"

        response = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": utc_time,
            "track": track,
            "github_file_url": github_file_url,
            "github_repo_url": github_repo_url,
            "status_code": 200
        }

        return jsonify(response)

    except Exception as e:
        error_message = {"error": str(e)}
        return jsonify(error_message), 400


if __name__ == '__main__':
    app.run()