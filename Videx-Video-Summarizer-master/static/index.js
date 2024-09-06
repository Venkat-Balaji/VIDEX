function summarizeVideo() {
    var videoUrl = document.getElementById("video-url").value;
    var summarizeButton = document.getElementById("summarize-button");
    var loaderContainer = document.getElementById("loader-container");
    var resultContainer = document.getElementById("result-container");
    var summaryText = document.getElementById("summary-text");

    // Show loader
    loaderContainer.style.display = "flex";
    // Disable button during processing
    summarizeButton.disabled = true;

    // Use AJAX to submit the form data to the Flask endpoint
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/summarize", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    xhr.onload = function () {
        // Hide loader
        loaderContainer.style.display = "none";
        // Enable button after processing
        summarizeButton.disabled = false;

        if (xhr.status === 200) {
            // Process the response
            var response = JSON.parse(xhr.responseText);

            if (response.summary) {
                // Display the summary
                resultContainer.style.display = "block";
                summaryText.textContent = response.summary;
            } else if (response.error) {
                // Display the error message
                alert("Error: " + response.error);
            }
        } else {
            console.log("Error: " + xhr.statusText);
        }
    };

    xhr.send("video_url=" + encodeURIComponent(videoUrl));
}
