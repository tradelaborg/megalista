# Description

Adjusts a previous conversion based on either a gclid/timestamp or an order id.

### Selector
**ADS_OFFLINE_CONVERSION_ADJUSTMENT_GCLID**
or
**ADS_OFFLINE_CONVERSION_ADJUSTMENT_ORDER_ID**

# Requirements

- Google Ads configured in intro tab
- Offline Clicks Conversion created in Google Ads
- Google Ads API Enabled in Google Cloud.

# Expected Schema
Use one of the following according to your use case:
## gclid
| Column name | Type | Description | Requirement |
| :---: | :---: | :---: | :---: |
| gclid |STRING |gclid of the conversion | **required** |
| time | STRING | 2020-04-16T12:00:00.000 (time of the adjustment)| **required** |
| conversion_time | STRING | 2020-04-16T12:00:00.000 (time of the original conversion)| **required** |
| amount | STRING | Conversion value | **optional** |

## order id
| Column name | Type | Description | Requirement |
| :---: | :---: | :---: | :---: |
| order_id |STRING |Order id of the conversion | **required** |
| time | STRING | 2020-04-16T12:00:00.000 (time of the adjustment)| **required** |
| amount | STRING | Conversion value | **optional** |


# Metadata

- Metadata 1: **Conversion name**: Name of the created conversion on google ads
- Metadata 2: Google Ads Account (Optional). Define a Google Ads Account Customer Id to override the Account Id defined in the General Configuration on the "Intro" tab. If the Account Id defined in the General Configuration is a Mcc account, the Mcc account will still be used for authentication, however the override Account Id will be used as the Customer Id. 
- Metadata 3: Either RESTATEMENT or RETRACTION

# Additional information

[Documentation](https://support.google.com/google-ads/answer/7686447?hl=en) for setting up offline conversion adjustments

# Additional information (2)

At every request successfully sent, Megalista stores the conversion glid/time pair or order id on a temporary table for 15 days. At every new execution, it consults stored gclid/time(s) and, in case request has already being sent, it  prevents it to be sent again. As a result, source table should not maintain events for more than 15 days.  
If source tables maintain events for more than 15 days, no duplicated conversion will be registered by Google Ads, but some erros will be logged when Megalista attempt to resend theses conversions.