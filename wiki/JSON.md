 To configure using JSON:
 - Make a copy of the [JSON template](https://github.com/google/megalista/tree/main/cloud_config/configuration_sample.json)
 - Provide Account IDs for Google Ads, Analytics, CM360, etc.
 - Configure Sources and Destinations, separating entries with commas
 - Connect Sources to Destinations in the "Connections" field
 - Save and upload this JSON file to a Google Cloud Storage bucket (default bucket options are fine)
 - Make note of the files's gsutil URI in the Cloud Storage UI: `gs://`**mybucketname/myconfig.json**

As an alternative, you may:
 - Configure using the [Google Sheets approach](https://github.com/google/megalista/wiki/Google-Sheets)
 - In the sheet `JSON`, in the cell `A2`, you can find the content of a JSON file that reflects the contents of the spreadsheet (configuration that has been just edited)
 - Copy the cell
 - Paste in a text editor
 - Remove the double quotes that exist in the beginning and the end of the text
 - Replace two double quotes (`""`) by one double quote (`"`) on the whole text
 - Save and upload this JSON file to a Google Cloud Storage bucket (default bucket options are fine)
 - Make note of the files's gsutil URI in the Cloud Storage UI: `gs://`**mybucketname/myconfig.json**
