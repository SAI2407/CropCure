
## Crop-Cure: Plant Disease Detection System

Crop-Cure is an intelligent system designed to assist farmers and gardeners by automatically detecting plant diseases from leaf images. It uses a two-stage deep learning model to first verify if an uploaded image contains a leaf, and if so, then analyzes it for signs of common diseases.

## Features

*   **Leaf Detection:** Intelligently verifies that the uploaded image is a plant leaf, reducing false diagnoses from irrelevant images.
*   **Disease Analysis:** Current model is finely tuned for potato cultivation, delivering accurate detection for major diseases including Late Blight, Early Blight, and Healthy leaf classification.
*   **Image Preprocessing:** Automatically handles image resizing and formatting to meet model requirements.


**Try the Live Demo here:** [Crop-Cure on Hugging Face Spaces](https://huggingface.co/spaces/Sai240723/CropCure)

You can download the docker image of **CropCure** here : [Crop-Cure Image in DockerHub](https://hub.docker.com/repository/docker/saiteja367/cropcure/general)


Following is the **CropCure** architecure.



<img width="877" height="685" alt="image" src="https://github.com/user-attachments/assets/8a149f6a-61f9-4a81-89b2-bb7b5018414b" />



