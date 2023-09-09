from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week
    current_day = datetime.datetime.utcnow().strftime('%A')

    # Get current UTC time with +/-2 minute validation
    current_time = datetime.datetime.utcnow()
    current_time_str = current_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    # GitHub URLs
    github_file_url = 'https://zoesamm.github.io/hng_Api/'
    github_repo_url = 'https://github.com/ZoeSamm/hng_Api.git'

    # JSON response
    response = {
        "slack_name": "Akinyele oluwakemi",
        "current_day": "saturday",
        "utc_time": "2023-09-09 00:29:11",
        "track": "Backend",
        "github_file_url": "https://zoesamm.github.io/hng_Api/",
        "github_repo_url": "https://github.com/ZoeSamm/hng_Api.git",
        "status_code": 200
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
