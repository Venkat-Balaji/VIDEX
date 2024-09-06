from flask import Flask, render_template, request, jsonify
import http.client
import json
import time

app = Flask(__name__)

YOUR_GENERATED_SECRET = "Your API KEY HERE"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        video_url = request.form.get('video_url')

        # Summarization logic using the external API
        data = {
            "data": [
                {
                    "video": video_url,
                    "algorithm": "Inception",
                    "languages": ["en"]
                }
            ]
        }

        headers = {
            "x-api-key": f"token {YOUR_GENERATED_SECRET}",
            "content-type": "application/json",
        }

        connection = http.client.HTTPSConnection("api.scenex.jina.ai")
        connection.request("POST", "/v1/describe", json.dumps(data), headers)

        response = connection.getresponse()
        response_data = response.read().decode("utf-8")
        connection.close()

        if response_data.strip():  # Check if response_data is not empty
            response_json = json.loads(response_data)
            job_id = response_json.get("result", [{}])[0].get("id")

            while True:
                # Check the status of the job
                if job_id:
                    connection.request("GET", f"/v1/jobs/{job_id}", headers=headers)
                    response = connection.getresponse()
                    response_data = response.read().decode("utf-8")
                    connection.close()

                    if response_data.strip():  # Check if response_data is not empty
                        response_json = json.loads(response_data)
                        status = response_json.get("status")

                        if status == "done":
                            # Extract the summary and return it
                            result = response_json.get("result", {})
                            summary = result.get("summary", "")
                            return jsonify({'summary': summary})

                        elif status == "error":
                            return jsonify({'error': 'Error occurred while processing the video.'})

                time.sleep(5)  # Wait for 5 seconds before checking the status again

        else:
            return jsonify({'error': 'Empty response data. Check if the API request was successful.'}), 500

    except Exception as e:
        # Handle exceptions appropriately (e.g., log the error)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
