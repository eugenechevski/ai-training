const AWS = require("aws-sdk");
const c3 = require("c3");

AWS.config.update({
  accessKeyId: "your-access-key-id",
  secretAccessKey: "your-secret-access-key",
  region: "your-region", // Optional if not using the default region
});

const s3Client = new AWS.S3();

const params = {
  Bucket: "your-bucket-name",
  Key: "your-json-file.json",
};

s3Client.getObject(params, (err, data) => {
  if (err) {
    console.error("Error getting object:", err);
  } else {
    const jsonData = JSON.parse(data.Body.toString());

    const chart = c3.generate({
      data: {
        json: jsonData,
        keys: {
          x: "x",
          value: ["y", "z"],
        },
        types: {
          y: "bar",
          z: "line",
        },
      },
      axis: {
        x: {
          type: "timeseries",
          tick: {
            format: "%Y-%m-%d",
          },
        },
      },
    });
  }
});
