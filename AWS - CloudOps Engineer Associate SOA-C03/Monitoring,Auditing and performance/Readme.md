## CloudWatch Synthetics
- CloudWatch Synthetics lets you proactively monitor your applications by simulating how users interact with them —
even before real users experience issues.

- It does this using canaries  — lightweight scripts that run on a schedule and test your endpoints, APIs, or websites automatically.

- Let’s say you have:

- A website: https://myapp.example.com

- You can create a canary that runs every 5 minutes and:

    - Opens the homepage

    - Checks for the text “Welcome to My App”

    - Measures load time

    - Takes screenshots

    - Stores results in Amazon S3 & CloudWatch Logs


##### CloudWatch Synthetics Canary Blueprints
- Heartbeat Monitor – load URL, store screenshot and an HTTP archive file
- API Canary – test basic read and write functions of REST APIs
- Broken Link Checker – check all links inside the URL that you are testing
- Visual Monitoring – compare a screenshot taken during a canary run with a baseline 
screenshot
- Canary Recorder – used with CloudWatch Synthetics Recorder (record your 
actions on a website and automatically generates a script for that)
- GUI Workflow Builder – verifies that actions can be taken on your webpage (e.g., test a webpage with a login form )  



## AWS CloudTrail

- Provides governance, compliance and audit for your AWS Account
- CloudTrail is enabled by default!
- Get an history of events / API calls made within your AWS Account by:
    - Console
    - SDK
    - CLI
- AWS Services
- Can put logs from CloudTrail into CloudWatch Logs or S3
- A trail can be applied to All Regions (default) or a single Region.
- If a resource is deleted in AWS, investigate CloudTrail first