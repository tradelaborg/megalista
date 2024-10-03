# Description

Creates (if needed) and send mobile device ids to a Google Ads customer match audience.

### Selector
**ADS_CUSTOMER_MATCH_MOBILE_DEVICE_ID_UPLOAD**

# Requirements

- Google Ads API token configured as a scheduler parameter (developer_token: XXXXXX)
- Google Ads API Enabled in Google Cloud.

# Expected Schema

| Column name | Type | Description | Requirement |
| :---: | :---: | :---: | :---: |
|  mobile_device_id | STRING | Mobile device Id identifier (android AdId or IOS IDFA) | **required** |

# Metadata

- Metadata 1: audience list name (if it does not exist, it will be automatically created)
- Metadata 2: ADD or REMOVE or REPLACE, if ADD, it will append the entries to the audience, if REMOVE, it will exclude them from the audience, if REPLACE, the audience will be erased before adding the entries into the audience
- Metadata 3: Can be left empty
- Metadata 4: app_id (i.e. com.mycompany.myapp). If empty, it will use the default app id defined on "Intro" tab
- Metadata 5: Google Ads Account (Optional). Define a Google Ads Account Customer Id to override the Account Id defined in the General Configuration on the "Intro" tab. If the Account Id defined in the General Configuration is a Mcc account, the Mcc account will still be used for authentication, however the override Account Id will be used as the Customer Id.
- Metadata 6: Membership lifespan (Optional, DEFAULT=10000 [Unlimited]). Sets how long in days your customers are kept in a Customer Match segment. It's only applied when creating a new list. 

# Additional information

Don't forget to properly configure your app_id or the audience won't be able to find your users.
