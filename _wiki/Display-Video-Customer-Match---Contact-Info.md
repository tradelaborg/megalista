# Description

Creates (if needed) and send user contact information to a Display & Video customer match audience.

### Selector
**DV_CUSTOMER_MATCH_CONTACT_INFO_UPLOAD**

# Requirements
- Display & Video API Enabled in Google Cloud
- An advertiser created within Display & Video

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

- Metadata 1: Advertiser Id 
- Metadata 2: Audience list name (if it does not exist, it will be automatically created)
- Metadata 3: TRUE or FALSE (DEFAULT=TRUE). Define if you would like megalista to hash the data before sending. Use false if your data is already SHA256 hashed or if you don't mind sending raw identifiers to Display & Video
- Metadata 4: ""
- Metadata 5: ""
- Metadata 6: Consent Status for ad user data (Optional). (UNSPECIFIED, UNKNOWN, GRANTED or DENIED)
- Metadata 7: Consent Status for ad personalization (Optional). (UNSPECIFIED, UNKNOWN, GRANTED or DENIED)


# Additional information

Although all columns are optional, it's required that at least email, phone or all name/address fields are present.
