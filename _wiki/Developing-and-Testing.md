## Running Megalista

We recommend first running it locally and make sure that everything works.
Make some sample tables on BigQuery for one of the uploaders and make sure that the data is getting correctly to the destination.
After that is done, upload the Dataflow template to GCP and try running it manually via the UI to make sure it works.
Lastly, configure the Cloud Scheduler to run Megalista in the frequency desired and you'll have a fully functional data integration pipeline.

### Running locally
Make sure to have Google Cloud SDK installed (https://cloud.google.com/sdk/docs/install).  
After following the steps above, run `gcloud auth application-default login` to have your user being used to access GCP resources.

```bash
python3 megalista_dataflow/main.py \
  --runner DirectRunner \
  --developer_token ${GOOGLE_ADS_DEVELOPER_TOKEN} \
  --setup_sheet_id ${CONFIGURATION_SHEET_ID} \
  --setup_json_url ${CONFIGURATION_JSON_URL} \
  --setup_firestore_collection ${CONFIGURATION_FIRESTORE_COLLECTION}
  --refresh_token ${REFRESH_TOKEN} \
  --access_token ${ACCESS_TOKEN} \
  --client_id ${CLIENT_ID} \
  --client_secret ${CLIENT_SECRET} \
  --bq_ops_dataset %{BQ_OPS_DATASET} \
  --bq_location %{BQ_DATASET_LOCATION} \
  --project ${GCP_PROJECT_ID} \
  --region us-central1 \
  --temp_location gs://{$GCS_BUCKET}/tmp
```
Only set one configuration parameter (`setup_sheet_id`, `setup_json_url` or `setup_firestore_collection`).

#### Manually executing pipeline using Dataflow UI
To execute the pipeline, use the following steps:
- Go to **Dataflow** on GCP console
- Click on *Create job from template*
- On the template selection dropdown, select *Custom template*
- Find the *megalista* file on the bucket you've created, on the templates folder
- Fill in the parameters required and execute