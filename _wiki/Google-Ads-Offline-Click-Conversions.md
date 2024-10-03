# Description

Uploads gclid based offline conversions to Google Ads.

### Selector
**ADS_OFFLINE_CONVERSION**

# Requirements

- Google Ads configured in intro tab
- Offline Clicks Conversion created in Google Ads
- Google Ads API Enabled in Google Cloud.

# Expected Schema

| Column name | Type | Description | Requirement |
| :---: | :---: | :---: | :---: |
| gclid |STRING |Gclid of the conversion | **required** |
| time | STRING | 2020-04-16T12:00:00.000 | **required** |
| amount | STRING | Conversion value | **required** |
| external_attribution_credit | STRING | Credit from External Attribution Data | **optional** |
| external_attribution_model | STRING | External Attribution Model | **optional** |
| consent_ad_user_data | STRING | Consent Status for Ad User Data** | **optional** |
| consent_ad_personalization | STRING | Consent Status for Ad Personalization** | **optional** |

** UNSPECIFIED, UNKNOWN, GRANTED or DENIED

# Metadata

- Metadata 1: **Conversion name**: Name of the created conversion on google ads
- Metadata 2: Google Ads Account (Optional). Define a Google Ads Account Customer Id to override the Account Id defined in the General Configuration on the "Intro" tab. If the Account Id defined in the General Configuration is a Mcc account, the Mcc account will still be used for authentication, however the override Account Id will be used as the Customer Id. 

# Additional information

[Documentation](https://support.google.com/google-ads/answer/7012522?hl=en) for setting up offline conversions tracking

# Additional information (2)

At every request successfully sent, Megalista stores the conversion glid/time pair on a temporary table for 15 days. At every new execution, it consults stored gclid/time(s) and, in case request has already being sent, it  prevents it to be sent again. As a result, source table should not maintain events for more than 15 days.  
If source tables maintain events for more than 15 days, no duplicated conversion will be registered by Google Ads, but some erros will be logged when Megalista attempt to resend theses conversions.