# Description

Sends hits to a GA Property through Measurement Protocol.

### Selector
**GA_MEASUREMENT_PROTOCOL**

# Requirements

- Google Analytics account id configured in the "Intro" tab.

# Expected Schema

| Column name | Type | Description | Requirement |
| :---: | :---: | :---: | :---: |
| uuid |STRING | Unique event identifier defined by the user used by megalista to deduplicate events before sending | **required** |
|client_id|STRING| | optional*|
|user_id|STRING| | optional*|
|event_category|STRING| |**required****|
|event_action|STRING| |**required****|
|event_label|STRING| |optional|
|event_value|INTEGER| |optional|
|transaction_id|STRING| |**required*****|
|cd1, cd2, cd[n]...|STRING|Any column starting with "cd" with be sent as a custom dimension. The column represents the CD number.|optional|
|cm1, cm2, cm[n]...|STRING|Any column starting with "cm" with be sent as a custom metric. The column represents the CM number.|optional|
|campaign_source|STRING| |optional|
|campaign_medium|STRING| |optional|

*One of **client_id** or **user_id** needs to be sent.

**Required for "event" hit type.

***Required for "transaction" and "item" hit type.

# Metadata

- Metadata 1: GA Property Id
- Metadata 2: "1" if the hit should be non-interactive, "0" otherwise
- Metadata 3: The hit type. Allowed values are "event", "transaction" and "item". Defaults to "event" if none is provided.


# Additional information

If you are using "transaction" or "item" hit types, only the "transaction_id" field is required, but other transaction and item fields are also allowed. See [Enhanced Ecommerce Tracking](https://developers.google.com/analytics/devguides/collection/protocol/v1/devguide#enhancedecom) for more details.

At every request successfully sent, Megalista stores its uuid on a temporary table for 15 days. At every new execution, it consults stored uuids and, in case request has already being sent, it  prevents it to be sent again. As a result, source table should not maintain events for more than 15 days.

**Note**: The UUID value **should not** change for a given line/conversion. If the UUID for a line/conversion changes, this line/conversion would be resent by Megalista, duplicating the data in GA.  
The UUID doesn't have to be a [Universally Unique Identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier), but any value that uniquely identifies a line/conversion. For instance, a "order id" may be a good candidate for the UUID field if the "order id" is unique.