const bucketBURL = 'http://my-data-bucket.s3-website-your-region.amazonaws.com/data.json';

// Show frontend content
document.getElementById('bucketA').textContent = 'Frontend content loaded!';

// Fetch data from Bucket B
fetch(bucketBURL)
  .then(r => r.json())
  .then(data => {
    document.getElementById('bucketB').textContent = JSON.stringify(data, null, 2);
  })
  .catch(err => {
    document.getElementById('bucketB').textContent = 'Error fetching Bucket B: ' + err;
  });
