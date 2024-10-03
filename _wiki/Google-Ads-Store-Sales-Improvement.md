# Description

Uploads store sales conversions to Google Ads.

### Selector
**ADS_SSI_UPLOAD**

# Requirements

- Google Ads configured in intro tab
- Store Sales Conversion created in Google Ads
- Google Ads API Enabled in Google Cloud

# Expected Schema

| Column name | Type | Description | Requirement |
| :---: | :---: | :---: | :---: |
| email |STRING | User email | optional* |
| phone |STRING | Phone number in E.164 format | optional* |
| mailing_address_first_name |STRING | | optional* |
| mailing_address_last_name |STRING | | optional* |
| mailing_address_country |STRING | Iso two letter format | optional* |
| mailing_address_zip |STRING | | optional* |
| time | STRING | 2020-04-16T12:00:00.000 | **required** |
| amount | NUMERIC | Value in micros | **required** |
| currency_code | STRING | USD (ISO 4217) | **required** |
| custom_value | STRING | | **required if custom_key is set** |


# Metadata

- **Conversion Name**: Name of the conversion created on Google Ads	
- **Google Ads Account**: Define a Google Ads Account Customer Id to override the Account Id defined in the General Configuration on the "Intro" tab. If the Account Id defined in the General Configuration is a Mcc account, the Mcc account will still be used for authentication, however the override Account Id will be used as the Customer Id (Optional).
- **Should hash**: TRUE or FALSE (DEFAULT=TRUE). Define if you would like Megalista to hash the data before sending. Use false if your data 
is already SHA256 hashed.
- **Custom Key**: In case there is a [custom variable created within Google Ads](https://developers.google.com/google-ads/api/docs/conversions/upload-store-sales-transactions#:~:text=You%20can%20create,to%20your%20business.) (Optional)
- **User Data Consent**: Specifies if data consent was collected: GRANTED | DENIED | UNSPECIFIED (Optional)
- **Ad Personalization Consent**: Specifies if data consent was collected: GRANTED | DENIED | UNSPECIFIED (Optional)

# Additional information

Although all columns are optional, it's required that at least email, phone or all mailing fields are present.

More information on Store Sales in the [support link](https://support.google.com/google-ads/answer/10018944?hl=en&ref_topic=9941533&sjid=4596499919203906174-SA).
