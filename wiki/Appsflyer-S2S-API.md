# Description

Send server to server events to AppsFlyer. 

### Selector 
**APPSFLYER_S2S_EVENTS**

# Requirements
- Appsflyer dev token configured as a scheduler parameter (appsflyer_dev_key: XXXXXX)
- Auxiliar bigquery dataset defined as a scheduler parameter (bq_ops_dataset: XXXX)

# Expected Schema

| Column name | Type | Description | Requirement |
| :---: | :---: |  :---: | :---: |
| uuid | STRING | Unique event identifier used by megalista to deduplicate events before sending. | **required** |
| appsflyer_id | STRING | Details on Appsflyer S2S documentation | **required** |
| customer_user_id | STRING | 1* | optional |
| ip | STRING | 1* | optional |
| device_ids_idfa | STRING | 1* | optional |
| device_ids_advertising_id | STRING | 1* | optional |
| device_ids_amazon_aid | STRING | 1* | optional |
| device_ids_oaid | STRING | 1* | optional |
| device_ids_imei | STRING | 1* | optional | 
| event_eventName | STRING | 1* | **required** |
| event_eventCurrency | STRING | 1* | optional |
| event_eventTime | DATETIME (UTC) | 1* | optional |
| event_eventValue | STRING | 1* | optional | 

1* - Details on [Appsflyer S2S documentation](https://support.appsflyer.com/hc/pt/articles/207034486-Server-to-server-events-API-for-mobile-S2S-mobile-)

# Metadata
- Metadata 1: app_id (i.e. com.mycompany.myapp)

# Additional Information
At every request successfully sent, Megalista stores its uuid on a temporary table for 15 days. At every new execution, it consults stored uuids and, in case request has already being sent, it  prevents it to be sent again. As a result, source table should not maintain events for more than 7 days.

**Note**: The UUID value **should not** change for a given line/conversion. If the UUID for a line/conversion changes, this line/conversion would be resent by Megalista, duplicating the data in Appsflyer.  
The UUID doesn't have to be a [Universally Unique Identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier), but any value that uniquely identifies a line/conversion. For instance, a "order id" may be a good candidate for the UUID field if the "order id" is unique.