# HNGx Backend Assignment Stage 1 🚀

Hello there! Welcome to my journey through the HNGx Backend Assignment Stage 1. In this exciting task, I embarked on creating and hosting an endpoint that takes two GET request query parameters and returns specific information in the magical JSON format. So, let's dive into my adventure and discover how I set up and tested this amazing endpoint. 😃

## Requirements 📚
To successfully complete this assignment, my endpoint had to meet these requirements:

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
Let's start this adventure with the setup:

### Prerequisites ✅
Make sure you have these prerequisites installed on your system:

- Python (recommended version 3.6 or higher) 🐍
- pip (Python package manager) 📦

### Installation and Usage ⚙️
Follow these steps to set up and run the endpoint locally:

1. Clone this repository to your local machine. 🖥️

   ```bash
   git clone https://github.com/DestinedCodes/HNG_X.git
   cd HNG_X/0x01-endpoint
   ```

2. Install the required Python packages using pip. 💡

   ```bash
   pip install -r requirements.txt
   ```

3. Now, it's time to run your endpoint locally: 🚀

   Run the following command to start the endpoint using Gunicorn.

   ```bash
   gunicorn endpoint:app
   ```
   This command tells Gunicorn to run the Flask app defined in the endpoint.py file.

5. Ta-da! Your endpoint is now accessible locally at http://localhost:8000/api. 🌐

## Deployment 🌐
I deployed my endpoint using Render, and it's now globally accessible! You can test it by using the following enchanted URL, and of course, add your `slack_name` and `track` parameters to complete the magic:

- [https://hng-x-endpoint.onrender.com/api?slack_name=your_name&track=your_track](https://hng-x-endpoint.onrender.com/api?slack_name=your_name&track=your_track)

## Testing 🧪
Before the grand submission, I made sure that my endpoint met the acceptance criteria:

- I ensured that my endpoint was publicly accessible. 🌍
- Testing was my favorite part; I tested the endpoint using the provided URL or locally by running `gunicorn endpoint:app`. 🚀
- I carefully checked the returned JSON against the defined format to ensure it included all the required fields. ✅
- I validated the correctness of each data point in the JSON response. 📊

## Acceptance Criteria ✔️
My endpoint successfully met the following acceptance criteria:

- It gracefully accepted two GET request query parameters: `slack_name` and `track`. 🚀
- The response beautifully included the `slack_name` passed as a GET request query parameter. 😎
- The response displayed the current day of the week in full (e.g., Monday, Tuesday, etc.). 📅
- The response returned the current UTC time, accurately within a +/-2 minute window. ⏰
- The response showcased the track based on the `track` GET parameter passed to the endpoint. 🛤️
- I proudly included a direct link to the specific file in the GitHub repository being executed. 🐱‍💻
- I also added a link to the main page of the GitHub repository containing the project's entire source code. 📂
- The status code was `200`. ✅
- The response adhered to the specified JSON format. 📋

With this guide, I hope you'll embark on your own adventure and complete the HNGx Backend Assignment Stage 1 successfully! 🚀✨
