import http.client
import json
import time

YOUR_GENERATED_SECRET = "Your API KEY HERE"

data = {
    "data": [
        {
            "video": "https://firebasestorage.googleapis.com/v0/b/causal-diffusion.appspot.com/o/uploads%2Fchunks%2FlquspRrVQTR5MbKhCCav1S3Amdo1%2F1700505599788%2Fdemo2.mp4?alt=media&token=ddec25d1-76bf-441f-ad51-d27b3427f7e2",
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
    print("Raw Response Data:", response_data)  # Print the raw response data for diagnosis
    response_json = json.loads(response_data)
    job_id = response_json.get("result", [{}])[0].get("id")
    print(f"Job ID: {job_id}")

    while True:
        # Check the status of the job
        if job_id:
            connection.request("GET", f"/v1/jobs/{job_id}", headers=headers)
            response = connection.getresponse()
            response_data = response.read().decode("utf-8")
            connection.close()

            if response_data.strip():  # Check if response_data is not empty
                print("Raw Status Response Data:", response_data)  # Print the raw status response data for diagnosis
                response_json = json.loads(response_data)
                status = response_json.get("status")

                if status == "done":
                    # Save the summary to a text file
                    result = response_json.get("result", {})
                    summary = result.get("summary", "")
                    with open("summary.txt", "w", encoding="utf-8") as file:
                        file.write(summary)
                    print("Summary saved to 'summary.txt'")
                    break
                elif status == "error":
                    print("Error occurred while processing the video.")
                    break

        time.sleep(5)  # Wait for 5 seconds before checking the status again
else:
    print("Empty response data. Check if the API request was successful.")
