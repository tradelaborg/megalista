### To manually schedule daily/hourly runs, go to Cloud Scheduler:

Click on create job
* Add a name and frequency as desired
* For target set as HTTP
* Configure a POST for url: https://dataflow.googleapis.com/v1b3/projects/${YOUR_PROJECT_ID}/templates:launch?gcsPath=gs://${BUCKET_NAME}/templates/megalista, replacing the params with the actual values
* For a sample on the body of the request, check https://github.com/google/megalista/blob/main/cloud_config/scheduler_sample.json
* Use a Service Account with the following minimum roles:
  * Cloud Dataflow Service Agent
  * Dataflow Admin
  * Storage Objects Viewer
* Scope: https://www.googleapis.com/auth/cloud-platform