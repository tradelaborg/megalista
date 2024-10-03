# Description

Creates (if needed) and send mobile device ids to a Google Ads customer match audience.

### Selector
**DV_CUSTOMER_MATCH_DEVICE_ID_UPLOAD**

# Requirements

- Display & Video API Enabled in Google Cloud.
- An advertiser created within Display & Video
- An App Id

# Expected Schema

| Column name | Type | Description | Requirement |
| :---: | :---: | :---: | :---: |
|  mobile_device_id | STRING | Mobile device Id identifier (android AdId or IOS IDFA) | **required** |

# Metadata

- Metadata 1: Advertiser Id 
- Metadata 2: Audience list name (if it does not exist, it will be automatically created)
- Metadata 3: TRUE or FALSE (DEFAULT=TRUE). Define if you would like megalista to hash the data before sending. Use false if your data is already SHA256 hashed or if you don't mind sending raw identifiers to Display & Video
- Metadata 4: app_id (i.e. com.mycompany.myapp). If empty, it will use the default app id defined on "Intro" tab

# Additional information

Don't forget to properly configure your app_id or the audience won't be able to find your users.
