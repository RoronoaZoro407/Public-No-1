  // Add a keyup event listener to the video URL input field
  document.getElementById("video-url").addEventListener("keyup", function() {
    var clearButton = document.getElementById("clear-button");

    // Check if the length of the text is greater than 0
    if (this.value.length > 0) {
      // Show the clear button
      clearButton.style.display = "inline-block";
    } else {
      // Hide the clear button
      clearButton.style.display = "none";
    }
  });

  // Add a click event listener to the clear button
  document.getElementById("clear-button").addEventListener("click", function() {
    // Clear the value of the video URL input field
    document.getElementById("video-url").value = "";
    // Hide the clear button
    this.style.display = "none";
  });