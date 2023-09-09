from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week (full name)
    current_day = datetime.datetime.utcnow().strftime('%A')

    # Get current UTC time with +/-2 minute validation
    current_time = datetime.datetime.utcnow()  # Current UTC time
    current_time -= datetime.timedelta(minutes=2)  # Subtract 2 minutes
    current_time_str = current_time.strftime('%Y-%m-%dT%H:%M:%SZ')  # Format as ISO 8601

    # GitHub URLs
    github_file_url = 'https://github.com/ZoeSamm/hng_Api/blob/main/file_name.ext'
    github_repo_url = 'https://github.com/ZoeSamm/hng_Api'

    # JSON response
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_time_str,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

