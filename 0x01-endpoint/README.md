# HNGX Backend Assignment Stage 1 🚀

Welcome to the HNGX Backend Assignment Stage 1! In this exciting assignment, you will create and host an endpoint that takes two GET request query parameters and returns specific information in JSON format. Follow this amazing guide to set up and test your endpoint. 😃

## Table of Contents 📋
- [Requirements](#requirements)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Endpoint](#api-endpoint)
- [Testing](#testing)
- [Acceptance Criteria](#acceptance-criteria)

## Requirements 📚
To successfully complete this assignment, your endpoint should meet the following requirements:

- The endpoint should take two GET request query parameters: `slack_name` and `track`. 🚀
- The response should be in JSON format and include the following information:
  - Slack name 😎
  - Current day of the week 📅
  - Current UTC time (with validation of +/-2 minutes) ⏰
  - Track 🛤️
  - GitHub URL of the file being run 🐱‍💻
  - GitHub URL of the full source code 📂
  - Status code of success (`200`) ✅

Here's an example of the expected JSON response format:
```json
{
  "slack_name": "example_name",
  "current_day": "Monday",
  "utc_time": "2023-08-21T15:04:05Z",
  "track": "backend",
  "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
  "github_repo_url": "https://github.com/username/repo",
  "status_code": 200
}
```

## Getting Started 🚀
Follow these steps to set up your endpoint:

### Prerequisites ✅
Make sure you have the following prerequisites installed on your system:

- [Python](https://www.python.org/downloads/) (recommended version 3.6 or higher) 🐍
- [pip](https://pip.pypa.io/en/stable/installing/) (Python package manager) 📦

### Installation ⚙️
1. Clone this repository to your local machine. 🖥️

   ```bash
   git clone https://github.com/DestinedCodes/HNG_X.git
   cd HNG_X
   ```

2. Install the required Python packages using `pip`. 💡

   ```bash
   pip install -r requirements.txt
   ```

## Usage 🏁
To run your endpoint locally, follow these steps:

1. Open a terminal and navigate to the project directory. 📂

2. Run the following command to start the endpoint using Gunicorn. 🚀

   ```bash
   gunicorn endpoint:app
   ```

   This command tells Gunicorn to run the Flask app defined in the `endpoint.py` file.

3. Your endpoint should now be accessible locally at `http://localhost:8000/api`. 🌐

## API Endpoint 🌐
To test your deployed endpoint, use the following URL, and don't forget to add your `slack_name` and `track` parameters:

- [https://hng-x-endpoint.onrender.com/api?slack_name=your_name&track=your_track](https://hng-x-endpoint.onrender.com/api?slack_name=your_name&track=your_track)

## Testing 🧪
Before submission, ensure that your endpoint meets the acceptance criteria:

- Make sure your endpoint is publicly accessible. 🌍
- Test the endpoint using the provided URL or locally by running `gunicorn endpoint:app`. 🚀
- Check the returned JSON against the defined format to ensure it includes all required fields. ✅
- Validate the correctness of each data point in the JSON response. 📊

## Acceptance Criteria ✔️
Your endpoint should meet the following acceptance criteria:

- It should accept two GET request query parameters: `slack_name` and `track`. 🚀
- The response should include the `slack_name` passed as a GET request query parameter. 😎
- The response should display the current day of the week in full (e.g., Monday, Tuesday, etc.). 📅
- The response should return the current UTC time, accurate within a +/-2 minute window. ⏰
- The response should display the track based on the `track` GET parameter passed to the endpoint. 🛤️
- It should include a direct link to the specific file in the GitHub repository being executed. 🐱‍💻
- It should include a link to the main page of the GitHub repository containing the project's entire source code. 📂
- The status code should be `200`. ✅
- The response should adhere to the specified JSON format. 📋

With this guide, you should be well-equipped to complete the HNGX Backend Assignment Stage 1 successfully.
