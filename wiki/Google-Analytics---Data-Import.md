# Description

Uploads Google Analytics Data import to a GA property.

### Selector
**GA_DATA_IMPORT**

# Requirements

- Google Analytics account id configured in the "Intro" tab.
- Both Google Analytics and Google Analytics Reporting API enabled in Google Cloud.

# Expected Schema

| Column name | Type | Description | Requirement |
| :---: | :---: | :---: | :---: |
| dimension1 | STRING | Custom dimension (1-250) which will be used as match key for the upload | **required** |
| dimension2 | STRING | Custom dimensions to be uploaded | **required** |
| dimension... | STRING | | optional | 

# Metadata

- Metadata 1: GA Property Id
- Metadata 2: Data Import name

# Additional information

- When creating the CSV file for Data Import upload, megalista appends 'ga:' to every bigquery column name so it matches csv expected by GA
- At every execution, the pipeline deletes all previous imported data associated with that data import Name, and then uploads it again to Google Analytics. As a result, we suggest you to use a dedicated data import instance for megalista

