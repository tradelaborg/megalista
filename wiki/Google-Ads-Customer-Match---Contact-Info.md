# Description

Creates (if needed) and send user contact information to a Google Ads customer match audience.

### Selector
**ADS_CUSTOMER_MATCH_CONTACT_INFO_UPLOAD**

# Requirements

- Google Ads API token configured as a scheduler parameter (developer_token: XXXXXX)
- Google Ads API Enabled in Google Cloud.

# Expected Schema

| Column name | Type | Description | Requirement |
| :---: | :---: | :---: | :---: |
| email | STRING | | optional |
| phone | STRING | Phone number in E.164 format | optional |
| mailing_address_first_name | STRING | | optional |
| mailing_address_last_name | STRING | | optional |
| mailing_address_country | STRING | Iso two letter format | optional |
| mailing_address_zip | STRING | | optional |

# Metadata

- Metadata 1: audience list name (if it does not exist, it will be automatically created)
- Metadata 2: ADD or REMOVE or REPLACE, if ADD, it will append the entries to the audience, if REMOVE, it will exclude them from the audience, if REPLACE, the audience will be erased before adding the entries into the audience
- Metadata 3: TRUE or FALSE (DEFAULT=TRUE). Define if you would like megalista to hash the data before sending. Use false if your data is already SHA256 hashed or if you don't mind sending raw identifiers to Google Ads
- Metadata 4: Can be left empty
- Metadata 5: Google Ads Account (Optional). Define a Google Ads Account Customer Id to override the Account Id defined in the General Configuration on the "Intro" tab. If the Account Id defined in the General Configuration is a Mcc account, the Mcc account will still be used for authentication, however the override Account Id will be used as the Customer Id. 
- Metadata 6: Consent Status for ad user data (Optional). (UNSPECIFIED, UNKNOWN, GRANTED or DENIED)
- Metadata 7: Consent Status for ad personalization (Optional). (UNSPECIFIED, UNKNOWN, GRANTED or DENIED)

# Additional information

Although all columns are optional, it's required that at least email, phone or all name/address fields are present.
