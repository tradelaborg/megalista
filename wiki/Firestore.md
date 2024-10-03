To configure using Firestore (recommended for use with web interface - WIP):
 - Verify that the Firestore API is enabled on Google Cloud (see the APIs section)
 - Create a [collection](https://firebase.google.com/docs/firestore/data-model) in Firestore, with the name of your choice
 - Inside the collection, create a Firestore document named "account_config", and provide Account IDs for Google Ads, Analytics, CM360, etc. See schema below.
 - Inside the collection, create separate Firestore documents for each Source/Destination pair. See schema below.

#### Firestore document schemas

**account_config document schema:**

| Field name  | Description  |
|---|---|
| google_ads_id | Google Ads account ID (customer ID) used by default |
| mcc_trix  | TRUE/FALSE. Indicates whether the Google Ads account is an MCC (parent account) or not |
| google_analytics_account_id | Google Analytics account ID |
| campaign_manager_account_id | Google Campaign Manager account ID |
| app_id | Android/iOS app ID for Google Ads or Appsflyer used by default |

**Source+Destination document schema:**

Universal parameters (mandatory for any upload type):
| Field name  | Description  |
|---|---|
| active | yes/no. Enables or disables scheduled uploads for the Source/Destination pair |
| bq_dataset | Name of the souce Big Query dataset |
| bq_table | Name of the source Big Query table |
| source | BIG_QUERY. Data source for the uploads. |
| source_name | Display-only name for the source, shown on logs. Example: "Top spending customers" |
| destination_name | Display-only name for the destination, shown on logs. Example: "Customer match" |

Google Ads conversions
| Field name  | Description  |
|---|---|
| gads_conversion_name | Name of the Google Ads conversion registered on the platform |
| type | ADS_OFFLINE_CONVERSION |

Google Ads Store Sales Direct
| Field name  | Description  |
|---|---|
| gads_conversion_name | Name of the Google Ads conversion registered on the platform |
| gads_external_upload_id | External upload ID |
| type | ADS_SSD_UPLOAD |

Google Ads Customer Match - Contact
| Field name  | Description  |
|---|---|
| gads_audience_name | Name of the Google Ads audience registered on the platform |
| gads_operation | ADD/REMOVE. Indicates whether the user list should be added or removed from the audience |
| gads_hash | TRUE/FALSE. Enables hashing on data |
| gads_account | (Optional) Google Ads account ID (Customer ID). Overlaps the default account ID in the account_config document |
| type | ADS_CUSTOMER_MATCH_CONTACT_INFO_UPLOAD |

Google Ads Customer Match - Mobile
| Field name  | Description  |
|---|---|
| gads_audience_name | Name of the Google Ads audience registered on the platform |
| gads_operation | ADD/REMOVE. Indicates whether the user list should be added or removed from the audience |
| gads_account | (Optional) Google Ads account ID (Customer ID). Overlaps the default account ID in the account_config document |
| gads_app_id | (Optional) Android/iOS app ID for Google Ads. Overlaps the default app ID in the account_config document  |
| type | ADS_CUSTOMER_MATCH_MOBILE_DEVICE_ID_UPLOAD |

Google Ads Customer Match - User ID
| Field name  | Description  |
|---|---|
| gads_audience_name | Name of the Google Ads audience registered on the platform |
| gads_operation | ADD/REMOVE. Indicates whether the user list should be added or removed from the audience |
| gads_account | (Optional) Google Ads account ID (Customer ID). Overlaps the default account ID in the account_config document |
| gads_hash | TRUE/FALSE. Enables hashing on data |
| type | ADS_CUSTOMER_MATCH_USER_ID_UPLOAD |

Google Analytics - Measurement Protocol
| Field name  | Description  |
|---|---|
| google_analytics_property_id | Google Analytics property ID (UA) |
| google_analytics_non_interaction | 1/0. Indicates whether the event is a non-interaction hit |
| type | GA_MEASUREMENT_PROTOCOL |

Google Analytics - Data Import
| Field name  | Description  |
|---|---|
| google_analytics_property_id | Google Analytics property ID (UA) |
| google_analytics_data_import_name | Name of the data import set in Google Analytics |
| type | GA_DATA_IMPORT |

Google Analytics - User List
| Field name  | Description  |
|---|---|
| google_analytics_property_id | Google Analytics property ID (UA) |
| google_analytics_view_id | Google Analytics view ID in the property selected |
| google_analytics_data_import_name | Name of the data import set in Google Analytics |
| google_analytics_user_id_list_name | Name of the user ID list |
| google_analytics_user_id_custom_dim | User ID custom dimension |
| google_analytics_buyer_custom_dim | Buyer custom dimension |
| type | GA_USER_LIST_UPLOAD |

Campaign Manager
| Field name  | Description  |
|---|---|
| campaign_manager_floodlight_activity_id | Floodlight activity ID |
| campaign_manager_floodlight_configuration_id | Floodlight configuration ID |
| type | CM_OFFLINE_CONVERSION |

Appsflyer S2S events
| Field name  | Description  |
|---|---|
| appsflyer_app_id |  |
| type | APPSFLYER_S2S_EVENTS |