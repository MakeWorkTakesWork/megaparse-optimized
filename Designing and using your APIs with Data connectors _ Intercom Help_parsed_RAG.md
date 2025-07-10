---
title: Untitled Document
document_type: guide
primary_topics: product
last_preprocessed: 2025-05-26
---


### ================



## 5/26/25, 9:39 PM



### ================


=================================================================

Designing and using your APIs with Data C n ecto Is Intercom Help

=================================================================


### # intercom



### Search for articles...


All Collections > Apps & Integrations > API integration > Set up Data connectors for Fin >
Designing and using your APIs with Data connectors

# Designing and using your APIs with Data
connectors


### [Image: unknown]


Written by Ivan
Updated over 2 weeks ago


### [Image: unknown]



### [Image: unknown]



### Table of contents


Data connectors use APIs to connect to external systems to fetch and/or update existing data.
That's why it's important to keep a couple of things in mind when setting up Data connectors in
Intercom.


### # Using third-party APIs (Shopify, WooCommerce, etc.)


If you're utilizing third-party (not in-house built APIs) with Data connectors in Intercom, you
likely have little to no control over how they work or the response you receive from a request.

That being said, the below guide is still useful guidance, but some sections may not be fully
applicable to your use case.


### Using first-party APIs


aps
ercom.com
ng-an 1d-L g-your- a
ta-connectors


### ===



### 1/6



### ===



### ================



## 5/26/25, 9:39 PM



### ================


=================================================================

Designing and using your APIs with Data C n ecto Is Intercom Help

=================================================================


### # intercom



### Search for articles...


All Collections > Apps & Integrations > API integration > Set up Data connectors for Fin >
Designing and using your APIs with Data connectors

# Designing and using your APIs with Data
connectors


### [Image: unknown]


Written by Ivan
Updated over 2 weeks ago


### [Image: unknown]



### [Image: unknown]



### Table of contents


Data connectors use APIs to connect to external systems to fetch and/or update existing data.
That's why it's important to keep a couple of things in mind when setting up Data connectors in
Intercom.


### # Using third-party APIs (Shopify, WooCommerce, etc.)


If you're utilizing third-party (not in-house built APIs) with Data connectors in Intercom, you
likely have little to no control over how they work or the response you receive from a request.

That being said, the below guide is still useful guidance, but some sections may not be fully
applicable to your use case.


### Using first-party APIs


aps
ercom.com
ng-an 1d-L g-your- a
ta-connectors


### ===



### 1/6



### ===



### ================



## 5/26/25, 9:39 PM



### ================



### Designing and using your APIs with Data C LC Intercom Help


Our engineers have compiled a list of points to note when designing or modifying your existing
APIs to work with Fin and Data connectors in Intercom.


### Authentication and identity considerations


How to secure your users and user input for use in Data connectors

Important: You and/or your security team should carry out a risk assessment and assess
the consequences around any data leakage. Intercom will not and cannot accept any
responsibility or liability for data leaked due to poor authentication and identification
practices of your or third party APIs.


### <



### *



### -


First, we strongly recommend that you enable Identity Verification. Identity verification is the
most important security control to set up. This will prevent malicious actors from impersonating
your users via the Messenger which can lead to them getting access to someone else's
conversations or to execute Data connectors on that user's behalf.


### =======


6
0S
00


### =======


Our team is currently working on a feature that allows you to sign multiple attributes via our
JavaScript API using. JSON Web Tokens JWTS). If you're interested in this feature, feel free to
contact our Support team via Messenger and they'lI be happy to work with you to get this
enabled.

Protectingattributes from updates is most important for the identifying attributes in Data
connectors, when the Data connector surfaces sensitive data or manipulates data.
For example, if your Data connector is making a request to API using "GET
accounts/<accountid>/nvoices then you want to be sure account_id is protected SO the
user can't just enumerate account_ids collecting data. However, if your Data connector is "GET
pizza-order-statustatus/corder.id>' then you might not care about the trustworthiness of
"order_id" and you don't care whether or not you surfaced this info to the right person.

Moreover, you should ensure that the attribute your Data connector uses to uniquely identify
your users (email, for example) is trustworthy. This means that you need to know that you trust
the source of your Data connector's identifying attributes. For example, if your Data connector
identifies the user by user_id, identity verification is signing the user_id attribute or if your Data
connector identifies the user by email or any other attribute, then that attribute is protected,
and it's not collected from the End User without some verification.

nups
ercom.cor
ning -and-usi ing-your-ap W ta-connectors


### ===



### 2/6



### ===



### ================



## 5/26/25, 9:39 PM



### ================



### Designing and using your APIs with Data C LC Intercom Help


Our engineers have compiled a list of points to note when designing or modifying your existing
APIs to work with Fin and Data connectors in Intercom.


### Authentication and identity considerations


How to secure your users and user input for use in Data connectors

Important: You and/or your security team should carry out a risk assessment and assess
the consequences around any data leakage. Intercom will not and cannot accept any
responsibility or liability for data leaked due to poor authentication and identification
practices of your or third party APIs.


### <



### *



### -


First, we strongly recommend that you enable Identity Verification. Identity verification is the
most important security control to set up. This will prevent malicious actors from impersonating
your users via the Messenger which can lead to them getting access to someone else's
conversations or to execute Data connectors on that user's behalf.


### =======


6
0S
00


### =======


Our team is currently working on a feature that allows you to sign multiple attributes via our
JavaScript API using. JSON Web Tokens JWTS). If you're interested in this feature, feel free to
contact our Support team via Messenger and they'lI be happy to work with you to get this
enabled.

Protectingattributes from updates is most important for the identifying attributes in Data
connectors, when the Data connector surfaces sensitive data or manipulates data.
For example, if your Data connector is making a request to API using "GET
accounts/<accountid>/nvoices then you want to be sure account_id is protected SO the
user can't just enumerate account_ids collecting data. However, if your Data connector is "GET
pizza-order-statustatus/corder.id>' then you might not care about the trustworthiness of
"order_id" and you don't care whether or not you surfaced this info to the right person.

Moreover, you should ensure that the attribute your Data connector uses to uniquely identify
your users (email, for example) is trustworthy. This means that you need to know that you trust
the source of your Data connector's identifying attributes. For example, if your Data connector
identifies the user by user_id, identity verification is signing the user_id attribute or if your Data
connector identifies the user by email or any other attribute, then that attribute is protected,
and it's not collected from the End User without some verification.

nups
ercom.cor
ning -and-usi ing-your-ap W ta-connectors


### ===



### 2/6



### ===



## 5/26/25, 9:39 PM


Designing and using your APIs with Data C n necto rs Intercom Help

This prevents malicious actors from being able to, for example, provide someone else's email
address and access an Data connector such as "Get bank statements by email", which would
expose sensitive financial data.

Where possible, we suggest that you do not use email as a primary identifier of fetching data of
your users, but something more random such as a unique, non-guessable user ID.

For performing Identity verification on leads, our team is currently working on a One Time
Password (OPT) feature that will help you verify someone's identity if they're contacting your
support as a lead. If you're interested in this feature, feel free to contact our Support team via
Messenger and they'lI be happy to work with you to get this enabled.


### [Image: unknown]


You should also ensure that the user can't perform Data connectors that they are not
authorized to do, for example, cancel someone else's order by knowing the order ID. This logic
is not handled within Intercom and you/your security team should carry out a risk assessment
and come up with appropriate methods to handle authentication and authorization.


### How to configure your Data connector's API call securely



### 6



## 0S


Intercom currently supports static tokens, HTTP tokens and OAuth (closed beta, contact us via 00
the Messenger for more information on this). Whatever token you use, it is your responsibility tc
make sure it is kept secret and updated if it gets leaked anywhere as soon as possible. As best
practice, we recommend you use OAuth tokens wherever possible.


### # Data considerations


Ideally, the API should only return the data necessary for your Workflow. However, this can be
unrealistic and the API might return a good amount of data that's actually not required to carry
out the Workflow where the Data connector is used.

If you're building APIs from scratch to be exclusively used with Data connectors and Fin
Workflows, you can either:

Build the API in a way that allows you to process business logic of the workflow in one
Data connector - this saves on the number of API calls and bundles the logic into one
place,

Build individual endpoints for, for example, finding orders, getting order details and finally,
refunding the order this is in line with RESTful API best design.principles but requires
multiple API calls to complete one workflow (for example, order refund)


### ===



### 3/6



### ===



### =================================================


nup
ercom.cor
ng -an d-L IS ng-your
ta-connector:


### =================================================



## 5/26/25, 9:39 PM


Designing and using your APIs with Data C n necto rs Intercom Help

This prevents malicious actors from being able to, for example, provide someone else's email
address and access an Data connector such as "Get bank statements by email", which would
expose sensitive financial data.

Where possible, we suggest that you do not use email as a primary identifier of fetching data of
your users, but something more random such as a unique, non-guessable user ID.

For performing Identity verification on leads, our team is currently working on a One Time
Password (OPT) feature that will help you verify someone's identity if they're contacting your
support as a lead. If you're interested in this feature, feel free to contact our Support team via
Messenger and they'lI be happy to work with you to get this enabled.


### [Image: unknown]


You should also ensure that the user can't perform Data connectors that they are not
authorized to do, for example, cancel someone else's order by knowing the order ID. This logic
is not handled within Intercom and you/your security team should carry out a risk assessment
and come up with appropriate methods to handle authentication and authorization.


### How to configure your Data connector's API call securely



### 6



## 0S


Intercom currently supports static tokens, HTTP tokens and OAuth (closed beta, contact us via 00
the Messenger for more information on this). Whatever token you use, it is your responsibility tc
make sure it is kept secret and updated if it gets leaked anywhere as soon as possible. As best
practice, we recommend you use OAuth tokens wherever possible.


### # Data considerations


Ideally, the API should only return the data necessary for your Workflow. However, this can be
unrealistic and the API might return a good amount of data that's actually not required to carry
out the Workflow where the Data connector is used.

If you're building APIs from scratch to be exclusively used with Data connectors and Fin
Workflows, you can either:

Build the API in a way that allows you to process business logic of the workflow in one
Data connector - this saves on the number of API calls and bundles the logic into one
place,

Build individual endpoints for, for example, finding orders, getting order details and finally,
refunding the order this is in line with RESTful API best design.principles but requires
multiple API calls to complete one workflow (for example, order refund)


### ===



### 3/6



### ===



### =================================================


nup
ercom.cor
ng -an d-L IS ng-your
ta-connector:


### =================================================



### ================



## 5/26/25, 9:39 PM



### ================



### Designing and using your APIs with Data C LC Intercom Help


Some considerations that should be included when deciding what and how much data your
API returns include:

Does Fin/Workflow really need all of the provided data in order to complete the steps in
the workflow? For example, if you have a workflow to create an order refund, you probably
only need the details about the order, and not additional data about the specific user's
account.

Data connectors have a timeout of 15 seconds and SO, if the API is taking too long to
respond, it might be a good idea to consider reducing the operations behind it and,
potentially, the amount of data it returns.


### [Image: unknown]


For Data connectors that might take longer time to complete, we suggest you look into
using "Wait for webhook" functionality. instead.

Data connectors can easily access attributes and arrays that are nested 1 to 2 levels deep,
but complex objects that include deeply nested arrays are better suited for processing
with Fin Tasks. If you try to use these types of response objects with an Data connector
you may encounter difficulties. However, Fin Tasks can handle them better.


### 3


Moreover, you should always remove the ability for users to provide malformed data or just
type things.


## 0S



### 00


For example, you should not ask the user to type in their account ID, but present them with
their account IDs (based on a known, secure identifier) and let them pick from a dropdown list.
More on how to collect data from users can be found here.


### # Other considerations


Your API should enforce application-specitic limits, such as capping refunds at a
maximum amount per day.

Ensure your API is idempotent, as Fin may submit the same refund request multiple times.

Implement server-side validation to ensure all inputs adhere to the format specified in your
Data connector.

Apply input sanitization to incoming data, recognizing Al-generated fields that may
contain hallucinated or malicious content.

Use standard HTTP error codes to help Fin respond appropriately. For instance, HTTP
429 or 500 errors may warrant a retry, whereas an HTTP 410 indicates no further
attempts should be made.

Version your API to facilitate seamless migration of Live Fin Data connectors between
versions (e.g., /v1/orders to /v2/orders).


### ===



### Tip



### ===



### =======================================================


aps
tercom.com
ning -an 1d-L us g-your-ap
ta-connectors


### =======================================================



### ===



### 4/6



### ===



### ================



## 5/26/25, 9:39 PM



### ================



### Designing and using your APIs with Data C LC Intercom Help


Some considerations that should be included when deciding what and how much data your
API returns include:

Does Fin/Workflow really need all of the provided data in order to complete the steps in
the workflow? For example, if you have a workflow to create an order refund, you probably
only need the details about the order, and not additional data about the specific user's
account.

Data connectors have a timeout of 15 seconds and SO, if the API is taking too long to
respond, it might be a good idea to consider reducing the operations behind it and,
potentially, the amount of data it returns.


### [Image: unknown]


For Data connectors that might take longer time to complete, we suggest you look into
using "Wait for webhook" functionality. instead.

Data connectors can easily access attributes and arrays that are nested 1 to 2 levels deep,
but complex objects that include deeply nested arrays are better suited for processing
with Fin Tasks. If you try to use these types of response objects with an Data connector
you may encounter difficulties. However, Fin Tasks can handle them better.


### 3


Moreover, you should always remove the ability for users to provide malformed data or just
type things.


## 0S



### 00


For example, you should not ask the user to type in their account ID, but present them with
their account IDs (based on a known, secure identifier) and let them pick from a dropdown list.
More on how to collect data from users can be found here.


### # Other considerations


Your API should enforce application-specitic limits, such as capping refunds at a
maximum amount per day.

Ensure your API is idempotent, as Fin may submit the same refund request multiple times.

Implement server-side validation to ensure all inputs adhere to the format specified in your
Data connector.

Apply input sanitization to incoming data, recognizing Al-generated fields that may
contain hallucinated or malicious content.

Use standard HTTP error codes to help Fin respond appropriately. For instance, HTTP
429 or 500 errors may warrant a retry, whereas an HTTP 410 indicates no further
attempts should be made.

Version your API to facilitate seamless migration of Live Fin Data connectors between
versions (e.g., /v1/orders to /v2/orders).


### ===



### Tip



### ===



### =======================================================


aps
tercom.com
ning -an 1d-L us g-your-ap
ta-connectors


### =======================================================



### ===



### 4/6



### ===



### ================



## 5/26/25, 9:39 PM



### ================


Designing and using your APIs with Data 0 n necto Is Intercom Help

Need more help? Get support from our Community. Forum
Find answers and get help from Intercom Support and Community Experts


### # Related Articles



### [Image: unknown]



### [Image: unknown]



### [Image: unknown]



### ==================



### We run on Intercom



### ==================



### =========



### Resources



### =========



### =======



### Support



### =======


nups
nu tercom.com
1g -an d- ng-your-ap W ta-connectors


### ===



### 5/6



### ===



### ================



## 5/26/25, 9:39 PM



### ================


Designing and using your APIs with Data 0 n necto Is Intercom Help

Need more help? Get support from our Community. Forum
Find answers and get help from Intercom Support and Community Experts


### # Related Articles



### [Image: unknown]



### [Image: unknown]



### [Image: unknown]



### ==================



### We run on Intercom



### ==================



### =========



### Resources



### =========



### =======



### Support



### =======


nups
nu tercom.com
1g -an d- ng-your-ap W ta-connectors


### ===



### 5/6



### ===



## # 5/26/25, 9:39 PM


# Designing and using your APIs with Data C n necto Is Intercom Help


## Product Changes



### Developers



### Blog



### Community



### Academy



### Webinars



### Company



### <



### Home



### About



### =



### a



### =



### Terms



### Privacy



### =====


0S
00


### =====


nups
ercom.cor
ng -an id-usi ng-your-ap W a ta-connectors


### ===



### 6/6



### ===



## # 5/26/25, 9:39 PM


# Designing and using your APIs with Data C n necto Is Intercom Help


## Product Changes



### Developers



### Blog



### Community



### Academy



### Webinars



### Company



### <



### Home



### About



### =



### a



### =



### Terms



### Privacy



### =====


0S
00


### =====


nups
ercom.cor
ng -an id-usi ng-your-ap W a ta-connectors


### ===



### 6/6



### ===

