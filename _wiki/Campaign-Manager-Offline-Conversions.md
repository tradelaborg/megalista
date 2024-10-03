# Description

Uploads Campaign Manager offline conversions to Campaign Manager floodlights (compatible with CM, SA360 and DV360 conversion optimization and CM + DV360 audience creation).

### Selector
**CM_OFFLINE_CONVERSION**

# Requirements

- Profile ID configured in intro
- Floodlight configuration created in CM
- Floodlight activity created in CM
- Campaign Manager API enabled in Google Cloud

# Expected Schema

| Column name | Type | Description | Requirement |
| :--- | :---: | :--- | :---: |
| uuid | STRING | Unique event identifier used by megalista to deduplicate events before sending | **required**|
| gclid |STRING | Click id | optional* |
| dclid |STRING | Click id for Display & Video | optional* |
| mobileDeviceId | STRING | Mobile Advertising ID | optional* |
| encryptedUserId | STRING | Extracted from CM reports | optional* |
| matchId | STRING | Sent to floodlight tag | optional* |
| value | STRING | Total value of the conversion | optional |
| quantity | INT64 | Number of conversions _(Default: 1)_ | optional |
| timestamp | STRING | 2020-04-16T12:00:00.000 _(Default: current timestamp)_ | optional |
| customVariables | ARRAY | Array of u-variable values (stored as `Struct`s) | optional |
| customVariables[].type | [Enum](https://developers.google.com/doubleclick-advertisers/rest/v3.4/Conversion#Type) | String of u-var index, from "U1" to "U100" | optional |
| customVariables[].value | STRING | Value of u-var | optional |

_\* Must have at least one of gclid, dclid, mobileDeviceId, encryptedUserId, matchId._
# Metadata

- Metadata 1: **Floodlight Activity ID**: Can be obtained in the URL for the activity
- Metadata 2: **Floodlight Configuration Id**:  Can be obtained in the URL for the activity

# Additional information
- [Documentation](https://support.google.com/searchads/answer/7384231?hl=en) for offline conversions in Campaign Manager.
- At every request successfully sent, Megalista stores its uuid on a temporary table for 15 days. At every new execution, it consults stored uuids and, in case request has already being sent, it  prevents it to be sent again. As a result, source table should not maintain events for more than 15 days.

# Example BQ data for testing
```
SELECT *
FROM UNNEST(
    ARRAY<STRUCT<
    uuid STRING,
    matchId STRING,
    value STRING,
    quantity INT64,
    customVariables ARRAY<STRUCT<type STRING, value STRING, kind STRING>>>>[
        (generate_uuid(), 'abc', 10, 2, [
            ('U1', '123', 'dfareporting#customFloodlightVariable'),
            ('U2', '456', 'dfareporting#customFloodlightVariable')
        ]),
        (generate_uuid(), 'def', 20, 4, [
            ('U1', '987', 'dfareporting#customFloodlightVariable'),
            ('U2', '654', 'dfareporting#customFloodlightVariable')
        ])
    ])
```

**Note**: The UUID value **should not** change for a given line/conversion. If the UUID for a line/conversion changes, this line/conversion would be resent by Megalista, duplicating the data in Campaign Manager.  
The UUID doesn't have to be a [Universally Unique Identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier), but any value that uniquely identifies a line/conversion. For instance, a "order id" may be a good candidate for the UUID field if the "order id" is unique.