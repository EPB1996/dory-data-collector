# Dory Backend

## Setting Up a Virtual Environment

To create and activate a virtual environment, follow these steps:

1. Create a virtual environment:

   ```sh
   uv venv
   ```

2. Activate the virtual environment:
   - On Linux or macOS:
     ```sh
     source .venv/bin/activate
     ```
   - On Windows:
     ```sh
     .venv\Scripts\activate
     ```

## Install dependencies

1. Install Uvicorn:

   ```sh
   uv sync
   ```

2. Run the FastAPI application:
   ```sh
   uv run uvicorn app.main:app --reload
   ```

This will start the FastAPI server, and you can access it at `http://127.0.0.1:8000`.

## Fast deploy

Create service account with access to firestore

```sh
gcloud iam service-accounts create dory-data-collector-sa --display-name "Dory Data Collector Service Account"

gcloud projects add-iam-policy-binding sandbox-ebaumgartner \
   --member "serviceAccount:dory-data-collector-sa@sandbox-ebaumgartner.iam.gserviceaccount.com" \
   --role "roles/datastore.user"

```

```sh
gcloud run deploy dory-data-collector --port 8080 --source . --region europe-west9 --service-account dory-data-collector-sa@sandbox-ebaumgartner.iam.gserviceaccount.com --max-instances 1 --min-instances 0 --memory 256Mi --cpu 1
```
