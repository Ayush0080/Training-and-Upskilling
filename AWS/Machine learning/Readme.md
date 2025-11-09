### Amazon Rekognition


- Amazon Rekognition is an AI-powered image and video analysis service provided by AWS.
It uses deep learning to automatically identify, analyze, and understand visual content — such as objects, faces, people, text, activities, and scenes — in images and videos.


- Key Capabilities of Amazon Rekognition
    | Capability                      | Description                                                | Example                                     |
    | ------------------------------- | ---------------------------------------------------------- | ------------------------------------------- |
    |  **Face Detection**        | Detect faces in an image/video                             | Count how many people are in a photo        |
    |  **Face Recognition**   | Match a face against a collection of known faces           | Authenticate users with facial verification |
    |  **Facial Analysis**          | Identify emotions, age range, gender, and facial landmarks | Detect “happy” or “sad” expressions         |
    |  **Object & Scene Detection** | Identify thousands of common objects/scenes                | “Car”, “Tree”, “Building”, “Beach”, etc.    |
    |  **Text Detection (OCR)**     | Read text in images                                        | Detect text on signboards, license plates   |
    |  **Video Analysis**           | Detect people, activities, or movements in videos          | Identify when a person enters a room        |
    |  **Content Moderation**       | Detect explicit, violent, or inappropriate content         | Filter NSFW or harmful images               |
    |  **Celebrity Recognition**     | Identify famous people in photos or videos                 | Recognize celebrities in media clips        |
    |  **Custom Labels**            | Train your own model for unique objects                    | Detect your company logo, product type      |



### Amazon Kendra

- Amazon Kendra is an intelligent search service powered by machine learning (ML) that helps you find accurate answers from large amounts of unstructured data — such as documents, PDFs, manuals, FAQs, wikis, and websites.

    ```bash
        Data Sources (S3, SharePoint, Confluence)
                    │
                    ▼
            Amazon Kendra Index
                    │
                    ▼
        User Interface / Chatbot / Web App
                    │
                    ▼
        Answers, Passages, or Documents Returned

    ```