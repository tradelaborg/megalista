# All version updates:

Please remember to reinstall requirements in [requirements.txt](https://github.com/google/megalista/blob/main/megalista_dataflow/requirements.txt) using pip, as the versions of the dependencies can have changed.

# From v4.x to v4.3:

This version introduced resend controls for Google Ads Offline Conversion.  
If you're using this connector, you'll se a new table created in the Ops Dataset in Bigquery for each source table used in this conector.  
This new table will have the gclid/time pairs for each Ads Offline Conversion successfully sent to the Google Ads API.  
It's recommended that the source tables for Ads Offline Conversions be changed to have a "where clause" limiting the appearance of each line for the maximum of 15 days, since the sent data is only retained for this period (for saving storage costs).  
A column with conversion date, for instance, would be a good candidate to be used in this clause.  
More details in the [connector page](https://github.com/google/megalista/wiki/Google-Ads-Offline-Conversions).

# From v3.0 to v4.0:

The main change in this version is the migration from the deprecated Adwords API to the new Google Ads API. Your existing developer tokens should work normally. 

If you made changes to the [Google Ads Uploaders](https://github.com/google/megalista/tree/main/megalista_dataflow/uploaders/google_ads), please review the changes regarding this new version. Otherwise, just update past the tag and you'll be using the new API.

# From v2.0 to v3.0:

The main code change in v3.0 is the update to the 2.27 version of Apache Beam which has the native implementation for side inputs in BigQuery sources. This incurred in a major refactor in the [megalista_dataflow/main.py](https://github.com/google/megalista/blob/main/megalista_dataflow/main.py) as well as the introduction of the [megalista_dataflow/sources/batches_from_executions.py](https://github.com/google/megalista/blob/main/megalista_dataflow/sources/batches_from_executions.py) source. 
If you have no customization in the main pipeline file or the [BaseBoundedSource](https://github.com/google/megalista/blob/main/megalista_dataflow/sources/base_bounded_source.py), just update past the v3.0 tag and it should present no issues.

# Previous versions to v2.0:

The main code change in v2.0 from previous versions is the usage of the configuration spreadsheet as the source of truth for the enabled uploaders. To update, migrate your custom executions in [megalista_dataflow/main.py](https://github.com/google/megalista/blob/main/megalista_dataflow/main.py) to spreadsheet according to instructions on README.md. 

If updating to the latest revision, also be sure to check the [JsonConfigurationSource](https://github.com/google/megalista/blob/main/megalista_dataflow/sources/json_execution_source.py) if you rather use it than the spreadsheet configuration.

# Migrating from other sources:

If your code wasn't sourced from GitHub, please swap to this repo using:

`git remote set-url origin https://github.com/google/megalista.git`

