var url = "https://s3.amazonaws.com/your-bucket-name/your-file.json";

var chart = c3.generate({
  bindto: "#chart",
  data: {
    url: url,
    mimeType: "json",
    type: "line", // Replace with your desired chart type
  },
});

chart.on("error", function (error) {
  console.error("Error loading JSON from S3:", error);
  // Display a user-friendly error message
});
