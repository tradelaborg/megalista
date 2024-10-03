# Description

Uploads conversions based on user provided personally identifiable information.

### Selector
**ADS_ENHANCED_CONVERSION_LEADS**

# Requirements

- Google Ads configured in intro tab
- Google Ads Set up for Enhanced Conversions for Leads [[details]](https://developers.google.com/google-ads/api/docs/conversions/upload-identifiers)
- Enhanced Conversions for Leads Conversion created in Google Ads
- Google Ads API Enabled in Google Cloud.

# Expected Schema

| Column name | Type | Description | Requirement |
| :---: | :---: | :---: | :---: |
| uuid |STRING | Unique event identifier defined by the user used by megalista to deduplicate events before sending  | **required** |
| email |STRING | Email provided by user** | **optional** |
| phone |STRING | Phone number provided by user** | **optional** |
| time | STRING | 2020-04-16T12:00:00.000 | **required** |
| amount | STRING | Conversion value | **required** |
| external_attribution_credit | STRING | Credit from External Attribution Data | **optional** |
| external_attribution_model | STRING | External Attribution Model | **optional** |
| consent_ad_user_data | STRING | Consent Status for Ad User Data*** | **optional** |
| consent_ad_personalization | STRING | Consent Status for Ad Personalization*** | **optional** |

** Either email, phone number or both need to be uploaded

*** UNSPECIFIED, UNKNOWN, GRANTED or DENIED

# Metadata

- Metadata 1: **Conversion name**: Name of the created conversion on google ads
- Metadata 2: Google Ads Account (Optional). Define a Google Ads Account Customer Id to override the Account Id defined in the General Configuration on the "Intro" tab. If the Account Id defined in the General Configuration is a Mcc account, the Mcc account will still be used for authentication, however the override Account Id will be used as the Customer Id.
- Metadata 3: TRUE or FALSE (DEFAULT=TRUE). Define if you would like megalista to hash the data before sending. Use false if your data is already SHA256 hashed or if you don't mind sending raw identifiers to Google Ads 

# Additional information

- [Documentation](https://support.google.com/google-ads/answer/11021502?hl=en) for setting up enhanced conversions for leads with Google Tag
- [Documentation](https://support.google.com/google-ads/answer/11347292?hl=en) for setting up enhanced conversions for leads with GTM

# Additional information (2)

At every request successfully sent, Megalista stores the conversion uuid/time pair on a temporary table for 15 days. At every new execution, it consults stored uuid/time(s) and, in case request has already being sent, it  prevents it to be sent again. As a result, source table should not maintain events for more than 15 days.  
Google Ads recognized if the conversion was sent before (Time, PII and amount combination) so conversions are not duplicated.
For multiple form submissions, Google Ads considers the last PII informed by user.