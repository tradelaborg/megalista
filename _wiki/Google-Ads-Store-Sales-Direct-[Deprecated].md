-- This connector has been deprecated and replaced by Store Sales Improvements --

# Description

Uploads store sales direct conversions to Google Ads.

### Selector
**ADS_SSD_UPLOAD**

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


# Metadata

- **Conversion Name**: Name of the conversion created on Google Ads	
- **External Upload ID**: This field is deprecated, but please fill in with ANY data (non-spaces) in order to allow for retro-compatibility
- **Should hash**: TRUE or FALSE (DEFAULT=TRUE). Define if you would like Megalista to hash the data before sending. Use false if your data 
is already SHA256 hashed.
- **Currency Code**: Currency code corresponding to the SSD upload (DEFAULT=BRL).
- **Google Ads Account**: Define a Google Ads Account Customer Id to override the Account Id defined in the General Configuration on the "Intro" tab. If the Account Id defined in the General Configuration is a Mcc account, the Mcc account will still be used for authentication, however the override Account Id will be used as the Customer Id (Optional).

# Additional information

Although all columns are optional, it's required that at least email, phone or all mailing fields are present.

More information on Store Sales direct in the [support link](https://support.google.com/google-ads/answer/7620302?hl=en#:~:text=Store%20sales%20(direct%20upload)%20lets,ads%20translate%20into%20offline%20purchases).
