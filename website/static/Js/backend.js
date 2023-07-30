// Add click event listener to download button
document.getElementById("download-btn").addEventListener("click", function() {
    var videoUrl = document.getElementById("video-url").value;
    if (videoUrl !== "") {
        downloadVideo(videoUrl);
    }
});

// Function to initiate the download process
function downloadVideo(url) {
    var downloadResult = document.getElementById("download-result");
    downloadResult.innerHTML = "Downloading...";

    // Send POST request to download endpoint
    fetch('/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: url })
    })
    .then(response => {
        // Check if response is successful
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Handle response data
        if (data.status === 'success') {
            downloadResult.innerHTML = "Download completed! Filename: " + data.filename;
        } else if (data.status === 'error') {
            downloadResult.innerHTML = "Error: " + data.message;
        } else {
            throw new Error('Invalid response data');
        }
    })
    .catch(error => {
        // Handle any errors that occur during the download process
        downloadResult.innerHTML = "Error: " + error.message;
    });
}
