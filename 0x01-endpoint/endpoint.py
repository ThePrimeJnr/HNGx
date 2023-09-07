from flask import Flask, request, jsonify
import datetime
import json

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week
    current_day = datetime.datetime.now().strftime('%A')

    # Get current UTC time
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # GitHub URLs
    github_file_url = "https://github.com/DestinedCodes/HNG_X/blob/master/0X01-endpoint/README.md"
    github_repo_url = "https://github.com/DestinedCodes/HNG_X"

    # Create the JSON response as a Python dictionary
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    # Serialize the response with indentation and set content type
    json_response = json.dumps(response, indent=2)
    
    # Set the content type to 'application/json'
    return json_response, 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run()

