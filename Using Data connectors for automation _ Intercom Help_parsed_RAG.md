---
title: Untitled Document
document_type: guide
primary_topics: sales, zendesk, salesforce, product
last_preprocessed: 2025-05-26
---


### ================



## 5/19/25, 8:26 AM



### ================



### ==================================================



### Using Data COI ecto S for automation Intercom Help



### ==================================================



### [Image: unknown]



### # intercom



### Search for articles...


All Collections > Apps & Integrations > API integration >
Use Data connectors & Custom Objects for automation > Using Data connectors for automation


### # Using Data connectors for automation


Trigger Data connectors automatically with Fin, Workflows, Custom Answers, and macros.


### [Image: unknown]



### [Image: unknown]


Written by Beth-Ann Sher
Updated over a week ago


### [Image: unknown]



### =



## Z



### =



### Table of contents


Data connectors allow you to build no-code integrations to get live data and take actions in
your external systems. Store this response data in Intercom and use it to power Fin and Inbox
automations via workflows and macros.

Using Data connectors allows you to update data in Intercom and send data to external tools
directly from your Inbox.

To use Data connectors for automation, you must have already set up a live Data
connector. If you haven't done SO, refer to our guide on Setting.upa Data connector.


### Using Data connectors with Fin


Enable Fin to resolve customer queries with personalized answers or complex multi-step
processes that require data from external systems.

https:// n tercom.com
a-connectors-lor-automation


### ===



### 1/8



### ===



### ================



## 5/19/25, 8:26 AM



### ================



### ==================================================



### Using Data COI ecto S for automation Intercom Help



### ==================================================



### [Image: unknown]



### # intercom



### Search for articles...


All Collections > Apps & Integrations > API integration >
Use Data connectors & Custom Objects for automation > Using Data connectors for automation


### # Using Data connectors for automation


Trigger Data connectors automatically with Fin, Workflows, Custom Answers, and macros.


### [Image: unknown]



### [Image: unknown]


Written by Beth-Ann Sher
Updated over a week ago


### [Image: unknown]



### =



## Z



### =



### Table of contents


Data connectors allow you to build no-code integrations to get live data and take actions in
your external systems. Store this response data in Intercom and use it to power Fin and Inbox
automations via workflows and macros.

Using Data connectors allows you to update data in Intercom and send data to external tools
directly from your Inbox.

To use Data connectors for automation, you must have already set up a live Data
connector. If you haven't done SO, refer to our guide on Setting.upa Data connector.


### Using Data connectors with Fin


Enable Fin to resolve customer queries with personalized answers or complex multi-step
processes that require data from external systems.

https:// n tercom.com
a-connectors-lor-automation


### ===



### 1/8



### ===



### ================



## 5/19/25, 8:26 AM



### ================



### =====================================================



### Using Data conr lectol S for automation Intercom Help



### =====================================================


1. All you need to do is go to Fin Al Agent > Train > Tasks, click on Manage Data connectors,
and you will be able to connect Fin with your external systems.

1. You can then choose to set a Data connector up from:


### a. A template (using a 3rd party app integration),



### b. An Al recommendation, or



### C. A custom data connector.


1. Once you've set the Data connector live, Fin will be able to use this in conversations to
retrieve data e.g. "Where is my order?"

1. Or, you can give Fin Tasks where the Data connector is used to perform multi-step
processes automatically e.g. "l'd like a refund for my order".


### [Image: unknown]



### =



## Z



### =



### # Using Data connectors in Workflows



### 1. Navigate to Fin Al Agent > Workflows.



### 2. Click New workflow or edit an existing Workflow.


1. From the workflow builder, click the + Add step button and then Collect data. You need to
ensure all the data sent in the request body are collected during or prior to the workflow.


### ===



### 2/8



### ===



### =================================


https
ercom.co
ors-for-automation


### =================================



### ================



## 5/19/25, 8:26 AM



### ================



### =====================================================



### Using Data conr lectol S for automation Intercom Help



### =====================================================


1. All you need to do is go to Fin Al Agent > Train > Tasks, click on Manage Data connectors,
and you will be able to connect Fin with your external systems.

1. You can then choose to set a Data connector up from:


### a. A template (using a 3rd party app integration),



### b. An Al recommendation, or



### C. A custom data connector.


1. Once you've set the Data connector live, Fin will be able to use this in conversations to
retrieve data e.g. "Where is my order?"

1. Or, you can give Fin Tasks where the Data connector is used to perform multi-step
processes automatically e.g. "l'd like a refund for my order".


### [Image: unknown]



### =



## Z



### =



### # Using Data connectors in Workflows



### 1. Navigate to Fin Al Agent > Workflows.



### 2. Click New workflow or edit an existing Workflow.


1. From the workflow builder, click the + Add step button and then Collect data. You need to
ensure all the data sent in the request body are collected during or prior to the workflow.


### ===



### 2/8



### ===



### =================================


https
ercom.co
ors-for-automation


### =================================



### ================



## 5/19/25, 8:26 AM



### ================



### ====================================================



### Using Data connector IS for automation Intercom Help



### ====================================================



### [Image: unknown]


1. Trigger the Data connector. After you've collected all the needed data, click on the + Add
step button again and choose Data connector (using API) then select your Data connector.

1. Specify Data connector fail path. Add a fail path to give users some context in case your Z
Data connector fails to complete.

1. Specify Data connector success path. You'll now be able to display data returned from the
Data connector in your Workflow messages. To do that, add a new message and then click
on the attribute selector 1 button and choose the appropriate attribute you want to show.


### [Image: unknown]



### ===



### 3/8



### ===



### ==================================


http
ercom.co
ors-for-a automation


### ==================================



### ================



## 5/19/25, 8:26 AM



### ================



### ====================================================



### Using Data connector IS for automation Intercom Help



### ====================================================



### [Image: unknown]


1. Trigger the Data connector. After you've collected all the needed data, click on the + Add
step button again and choose Data connector (using API) then select your Data connector.

1. Specify Data connector fail path. Add a fail path to give users some context in case your Z
Data connector fails to complete.

1. Specify Data connector success path. You'll now be able to display data returned from the
Data connector in your Workflow messages. To do that, add a new message and then click
on the attribute selector 1 button and choose the appropriate attribute you want to show.


### [Image: unknown]



### ===



### 3/8



### ===



### ==================================


http
ercom.co
ors-for-a automation


### ==================================



### ================



## 5/19/25, 8:26 AM



### ================



### ======================================================



### Using Data COI nI necto S for automation Intercom Help



### ======================================================



### # Example use case


You can use a Data connector to create a new Jira issue whenever a conversation meets
certain criteria.

For example, you can set up a Workflow that triggers a Data connector to create a new Jira
issue whenever a conversation is tagged with "Feature Request". The Data connector can
automatically populate the issue with the conversation details and assign it to a specific Jira
project.


### # Another example


Here's another example of a Data connector used in Fin Al Agent handover workflow to create
a ticket in Zendesk for agents to respond to via email:


### [Image: unknown]



### =



## Z



### =



### ===



### 4/8



### ===



### =================================


https
ercom.co
ors-for-automation


### =================================



### ================



## 5/19/25, 8:26 AM



### ================



### ======================================================



### Using Data COI nI necto S for automation Intercom Help



### ======================================================



### # Example use case


You can use a Data connector to create a new Jira issue whenever a conversation meets
certain criteria.

For example, you can set up a Workflow that triggers a Data connector to create a new Jira
issue whenever a conversation is tagged with "Feature Request". The Data connector can
automatically populate the issue with the conversation details and assign it to a specific Jira
project.


### # Another example


Here's another example of a Data connector used in Fin Al Agent handover workflow to create
a ticket in Zendesk for agents to respond to via email:


### [Image: unknown]



### =



## Z



### =



### ===



### 4/8



### ===



### =================================


https
ercom.co
ors-for-automation


### =================================



### ================



## 5/19/25, 8:26 AM



### ================



### Using Data connectoi S for automation Intercom Help



### Using Data connectors in macros



### 1. Navigate to Settings > Inbox > Macros.



### 2. Click New macro or edit an existing macro.


1. In the macro configuration, click Add an action and select Data connectors (using API)
from the dropdown men nu.

1. Choose the desired Data connector from the list of available actions.

1. Complete the macro configuration by defining conditions and other settings.


### 6. Save the macro.



### # Example use case


You can use a Data connector to create a task in a project management tool, such as Asana,
Trello or Jira, based on the content of the conversation or the customer's email domain. Then,
you can include this Data connector in a macro to easily create tasks and keep track of
important action items.


### =



## Z



### =



### # Using Data connectors with CMD + K


1. In the Inbox, select a Conversation where you want to apply a Data connector.

1. Press CMD + K (Mac) or Ctrl + K (Windows) to open the command menu.

1. Select Trigger Data connector, type the name of the Data connector you want to use and
select it from the list.

1. The Data connector will be executed, and any resulting data or updates will be applied.


### # Example use case


You can set up a Data connector to create a calendar event in Google Calendar directly from
the Intercom conversation using CMD + K With a high volume of Conversations, this can be
helpful for scheduling meetings with customers and keeping track of important dates.


### # Using Data connectors in the Conversation Part actions


1. In the Inbox, open a Conversation and locate the specific Message for which you want to
trigger a Data connector.

1. Hover over the message and click on the three-dot menu icon that appears.


### ===



### 5/8



### ===


http:
ercom.con
onnectors-for-automation


### ================



## 5/19/25, 8:26 AM



### ================



### Using Data connectoi S for automation Intercom Help



### Using Data connectors in macros



### 1. Navigate to Settings > Inbox > Macros.



### 2. Click New macro or edit an existing macro.


1. In the macro configuration, click Add an action and select Data connectors (using API)
from the dropdown men nu.

1. Choose the desired Data connector from the list of available actions.

1. Complete the macro configuration by defining conditions and other settings.


### 6. Save the macro.



### # Example use case


You can use a Data connector to create a task in a project management tool, such as Asana,
Trello or Jira, based on the content of the conversation or the customer's email domain. Then,
you can include this Data connector in a macro to easily create tasks and keep track of
important action items.


### =



## Z



### =



### # Using Data connectors with CMD + K


1. In the Inbox, select a Conversation where you want to apply a Data connector.

1. Press CMD + K (Mac) or Ctrl + K (Windows) to open the command menu.

1. Select Trigger Data connector, type the name of the Data connector you want to use and
select it from the list.

1. The Data connector will be executed, and any resulting data or updates will be applied.


### # Example use case


You can set up a Data connector to create a calendar event in Google Calendar directly from
the Intercom conversation using CMD + K With a high volume of Conversations, this can be
helpful for scheduling meetings with customers and keeping track of important dates.


### # Using Data connectors in the Conversation Part actions


1. In the Inbox, open a Conversation and locate the specific Message for which you want to
trigger a Data connector.

1. Hover over the message and click on the three-dot menu icon that appears.


### ===



### 5/8



### ===


http:
ercom.con
onnectors-for-automation


### ================



## 5/19/25, 8:26 AM



### ================



### Using Data COI ecto S for automation Intercom Help


1. Select Trigger Data connector from the list of available actions, type the name of the Data
connector you want to use and select it from the list.

1. The Data connector will be executed, and any resulting data or updates will be applied.


### # Example use case


You can set up a Data connector that updates a Salesforce record based on the content of a
specific Conversation Part (message). This can help keep customer information current and
ensure important details are captured in your Customer Relationship Management tool.

Note: Custom Attributes updated by a Data connector using macros and CMD + K
might not be reflected in the Inbox until refreshed.

Logs for your Data connector are kept for 7 days and can be found by opening the Data
connector in Settings > Integrations > Data connectors and then clicking Logs in the top
right corner.


### =



## N



### =



### 9 Tip



### [Image: unknown]


# Need more help? Get support from our Community. Forum
Find ans swers and get help from Intercom Support and Community Experts


### # Related Articles



### # Setting up a Data connector



### Data connectors and Custom Objects FAQs



### Use ticket attributes in Data connectors



### # Fin Data connector FAQs


LL
tercom.con
onnec ctors-for-automation


### ===



### 6/8



### ===



### ================



## 5/19/25, 8:26 AM



### ================



### Using Data COI ecto S for automation Intercom Help


1. Select Trigger Data connector from the list of available actions, type the name of the Data
connector you want to use and select it from the list.

1. The Data connector will be executed, and any resulting data or updates will be applied.


### # Example use case


You can set up a Data connector that updates a Salesforce record based on the content of a
specific Conversation Part (message). This can help keep customer information current and
ensure important details are captured in your Customer Relationship Management tool.

Note: Custom Attributes updated by a Data connector using macros and CMD + K
might not be reflected in the Inbox until refreshed.

Logs for your Data connector are kept for 7 days and can be found by opening the Data
connector in Settings > Integrations > Data connectors and then clicking Logs in the top
right corner.


### =



## N



### =



### 9 Tip



### [Image: unknown]


# Need more help? Get support from our Community. Forum
Find ans swers and get help from Intercom Support and Community Experts


### # Related Articles



### # Setting up a Data connector



### Data connectors and Custom Objects FAQs



### Use ticket attributes in Data connectors



### # Fin Data connector FAQs


LL
tercom.con
onnec ctors-for-automation


### ===



### 6/8



### ===



### ================



## 5/19/25, 8:26 AM



### ================



### ====================================================



### Using Data cor n ecto S for automation Intercom Help



### ====================================================



### Secure Data connectors with One-Time Passcode



### Did this answer your question?



### [Image: unknown]



### [Image: unknown]



### [Image: unknown]



### =



## Z



### =



### We run on Intercom



### [Table : unknown]



### Support



### Resources



## Product Changes



### Developers



### Blog



### Community



### Academy



### Webinars



### Company



### Home



### About



### Terms



### Privacy


https://
tercom.com
tors-for-automation


### ===



### 7/8



### ===



### ================



## 5/19/25, 8:26 AM



### ================



### ====================================================



### Using Data cor n ecto S for automation Intercom Help



### ====================================================



### Secure Data connectors with One-Time Passcode



### Did this answer your question?



### [Image: unknown]



### [Image: unknown]



### [Image: unknown]



### =



## Z



### =



### We run on Intercom



### [Table : unknown]



### Support



### Resources



## Product Changes



### Developers



### Blog



### Community



### Academy



### Webinars



### Company



### Home



### About



### Terms



### Privacy


https://
tercom.com
tors-for-automation


### ===



### 7/8



### ===



### ================



## 5/19/25, 8:26 AM



### ================



### ==================================================



### Using Data COI ecto S for automation Intercom Help



### ==================================================



### [Image: unknown]



### =



## Z



### =



### ===



### 8/8



### ===



### ===================================


https
ercom.co:
tors-for-automation


### ===================================



### ================



## 5/19/25, 8:26 AM



### ================



### ==================================================



### Using Data COI ecto S for automation Intercom Help



### ==================================================



### [Image: unknown]



### =



## Z



### =



### ===



### 8/8



### ===



### ===================================


https
ercom.co:
tors-for-automation


### ===================================

