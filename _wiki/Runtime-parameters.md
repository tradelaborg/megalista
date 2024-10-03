These parameters are required in the body of the request to the Dataflow API or as command line parameters for running locally. 

# Expected parameters

|Key Name (Cloud scheduler)|Shell Argument (localrun)|Expected value|
|:---: | :---:| :---:| 
|gcp_project_id|--gcp_project_id|Google Cloud project Id|
|client_id|--client_id|oAuth2 client Id for Google APIs|
|client_secret|--client_secret|oAuth2 client secret for Google APIs|
|refresh_token|--refresh_token|oAuth2 refresh token for Google APIs, obtained through generate_megalist_token.sh|
|access_token|--access_token|oAuth2 access token for Google APIs, obtained through generate_megalist_token.sh|
|setup_sheet_id|--setup_sheet_id|Id of Google Spreadsheet that will be used as configuration engine.|
|developer_token|--developer_token|Google Ads developer token|
|bq_ops_dataset|--bq_ops_dataset|Auxiliary bigquery dataset name used for Megalista operations (dataset needs to exist prior to execution and be hosted in gcp_project_id project)|
|bq_location|--bq_location|Location of bigquery's source dataset used for Megalista (default to US)|
|appsflyer_dev_key|--appsflyer_dev_key|Developer key for AppsFlyer server 2 server API|
