# Description

Sends [Events](https://developers.google.com/analytics/devguides/collection/protocol/ga4/sending-events?client_type=gtag) or sets [User Properties](https://developers.google.com/analytics/devguides/collection/protocol/ga4/user-properties) into a GA4 Stream (App or Web) through [Measurement Protocol](https://developers.google.com/analytics/devguides/collection/protocol/ga4).

### Selector
**GA_4_MEASUREMENT_PROTOCOL**

# Requirements

- Google Analytics 4 account id configured in the "Intro" tab.

# Expected Schema

## App Event
| Column name | Type | Description | Requirement |
| :---: | :---: | :---: | :---: |
| uuid |STRING | Unique event identifier defined by the user, used by Megalista to deduplicate events before sending | **required** |
|app_instance_id|STRING| A unique identifier for a Firebase app instance. | **required**| 
|name|STRING| The name of the event. | **required**| 
|user_id|STRING| A unique identifier for a user. See [User-ID for cross-platform analysis](https://support.google.com/analytics/answer/9213390) for more information on this identifier. |optional|
|timestamp_micros|NUMBER| A Unix timestamp (in microseconds) for the time to associate with the event. This should only be set to record events that happened in the past. This value can be overridden via user_property or event timestamps. Events can be backdated up to 3 calendar days based on the property's timezone.|optional|  
|parameter_1, parameter_2, ..., parameter_n |STRING| Any other column will be sent as an event parameter.|optional|

## Web Event
| Column name | Type | Description | Requirement |
| :---: | :---: | :---: | :---: |
| uuid |STRING | Unique event identifier defined by the user, used by Megalista to deduplicate events before sending | **required** |
|client_id|STRING| A unique identifier for a client. | **required**| 
|name|STRING| The name of the event. | **required**| 
|user_id|STRING| A unique identifier for a user. See [User-ID for cross-platform analysis](https://support.google.com/analytics/answer/9213390) for more information on this identifier. |optional|
|timestamp_micros|NUMBER| A Unix timestamp (in microseconds) for the time to associate with the event. This should only be set to record events that happened in the past. This value can be overridden via user_property or event timestamps. Events can be backdated up to 3 calendar days based on the property's timezone.|optional|  
|parameter_1, parameter_2, ..., parameter_n |STRING| Any other column will be sent as an event parameter.|optional|

## App User Property
<pre><b>Note</b>: The user property will be sent along a dummy event named <b>user_property_addition_event</b></pre>
| Column name | Type | Description | Requirement |
| :---: | :---: | :---: | :---: |
| uuid |STRING | Unique event identifier defined by the user, used by Megalista to deduplicate events before sending | **required** |
|app_instance_id|STRING| A unique identifier for a Firebase app instance. | **required**| 
|user_id|STRING| A unique identifier for a user. See [User-ID for cross-platform analysis](https://support.google.com/analytics/answer/9213390) for more information on this identifier. |optional|
|timestamp_micros|NUMBER| A Unix timestamp (in microseconds) for the time to associate with the event. This should only be set to record events that happened in the past. This value can be overridden via user_property or event timestamps. Events can be backdated up to 3 calendar days based on the property's timezone.|optional| 
|user_property_1, user_property_2, ..., user_property_n |STRING| Any other column will represent an user property to be set. The name of the column will be used as the name of the user property and the value of the row will be used as the value of the user property.| **required** |

## Web User Property
<pre><b>Note</b>: The user property will be sent along a dummy event named <b>user_property_addition_event</b></pre>
| Column name | Type | Description | Requirement |
| :---: | :---: | :---: | :---: |
| uuid |STRING | Unique event identifier defined by the user, used by Megalista to deduplicate events before sending | **required** |
|client_id|STRING| A unique identifier for a client. | **required**| 
|user_id|STRING| A unique identifier for a user. See [User-ID for cross-platform analysis](https://support.google.com/analytics/answer/9213390) for more information on this identifier. |optional|
|timestamp_micros|NUMBER| A Unix timestamp (in microseconds) for the time to associate with the event. This should only be set to record events that happened in the past. This value can be overridden via user_property or event timestamps. Events can be backdated up to 3 calendar days based on the property's timezone.|optional| 
|user_property_1, user_property_2, ..., user_property_n |STRING| Any other column will represent an user property to be set. The name of the column will be used as the name of the user property and the value of the row will be used as the value of the user property.| **required** |

# Metadata

- Metadata 1: `API Secret` - **Required**. An `API SECRET` generated in the Google Analytics UI. To create a new secret, navigate to:
`Admin > Data Streams > choose your stream > Measurement Protocol > Create`.

- Metadata 2: `Is Event` - **Required**. A boolean indicating if this destination will be used to send an event. Accepted values are `TRUE` or `FALSE`. Must be the opposite of `Metadata 3`, triggers an error otherwise.

- Metadata 3: `Is User Property` - **Required**. A boolean indicating if this destination will be used to set a user property. Accepted values are `TRUE` or `FALSE`. Must be the opposite of `Metadata 2`, triggers an error otherwise.

- Metadata 4: `Non Personalized Ads` - **Required**. A boolean indicating if GA4 should use this event/user property for measurement purposes only. Accepted values are `TRUE` (measurement only) or `False` (measurement and personalized ads). More information can be found on the [Help Center](https://support.google.com/analytics/answer/9494752).

- Metadata 5: `Firebase App ID` - **Required for App Stream**. The Firebase App ID. The identifier for a Firebase app. Found in the Firebase console under: 
`Project Settings > General > Your Apps > App ID.`

- Metadata 6: `Measurement ID` - **Required for Web Stream**. The measurement ID associated with a stream. Found in the Google Analytics UI under:
`Admin > Data Streams > choose your stream > Measurement ID`

# Additional information

At every request successfully sent, Megalista stores its uuid on a temporary table for 15 days. At every new execution, it consults stored uuids and, in case request has already being sent, it  prevents it to be sent again. As a result, source table should not maintain events for more than 15 days.

**Note**: The UUID value **should not** change for a given line/conversion. If the UUID for a line/conversion changes, this line/conversion would be resent by Megalista, duplicating the data in GA.  
The UUID doesn't have to be a [Universally Unique Identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier), but any value that uniquely identifies a line/conversion. For instance, a "order id" may be a good candidate for the UUID field if the "order id" is unique.

For web events that have an array of items, the expected schema of the field in BigQuery must be the type of: JSON.
check the Recommended web events for GA4 for details: https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtag