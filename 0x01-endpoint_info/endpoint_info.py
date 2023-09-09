from flask import Flask, request, jsonify
import datetime
import json

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    try:
        # Get query parameters
        slack_name = request.args.get('slack_name')
        track = request.args.get('track')

        # Check if both parameters are missing
        if not slack_name and not track:
            raise ValueError("slack_name and track are required")

        # Check if slack_name is missing
        if not slack_name:
            raise ValueError("slack_name is required")

        # Check if track is missing
        if not track:
            raise ValueError("track is required")

        # Get current day of the week
        current_day = datetime.datetime.now().strftime('%A')

        # Get current UTC time
        utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

        # Use environment variables for URLs
        github_file_url = "https://github.com/DestinedCodes/HNGx/blob/master/0x01-endpoint_info/endpoint_info.py"
        github_repo_url = "https://github.com/DestinedCodes/HNGx"

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

        # Serialize the response with indentation
        json_response = json.dumps(response, indent=2)
        
        # Set the content type to 'application/json'
        return json_response, 200, {'Content-Type': 'application/json'}
    except Exception as error_message:
        # Handle errors and return an appropriate response
        error_response = json.dumps({"error": str(error_message)})
        return error_response, 400, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run()
