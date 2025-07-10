---
title: Untitled Document
document_type: guide
primary_topics: sales, salesforce
last_preprocessed: 2025-05-26
---


### ===============



## 5/26/25,9:31 AM



### ===============


==========================================================================================

Setting up the required permissions for connecting Salesforce Fin by Intercom: Help Center

==========================================================================================


### Ask a question


All Collections > Fin for Salesforce > Setting up the required permissions for connecting Salesforce

# Setting up the required permissions for
connecting Salesforce


### 09



## 0D


This article guides you through setting up the necessary Salesforce permissions for
integrating with your Fin workspace.


### Updated over a month ago



### Table of contents


To power seamless automation and intelligent support experiences, Fin integrates deeply
with your Salesforce instance. This integration requires specific object and field-level
permissions, which allow Fin to create, update, and sync Salesforce cases and related data.

This article will walk you through:


### Why these oermissions are important



### Who needs them



### How to implement them



### A complete reference table of the required permissions



### # Why These Permissions Matter


Fin relies on Salesforce data to create cases, post summaries, read contact information,
and route conversations to agents. Without the proper permissions, Fin may be unable to
interact with your Salestorce environment effectively - resulting in failed syncs, blocked
automations, or limited functionality.

https:/fnai/helple en/
1509 - e ng g-up-L the-re 4u
5- tor-connecting e: or


### ===



### 1/6



### ===



### 0



### ===============



## 5/26/25,9:31 AM



### ===============


==========================================================================================

Setting up the required permissions for connecting Salesforce Fin by Intercom: Help Center

==========================================================================================


### Ask a question


All Collections > Fin for Salesforce > Setting up the required permissions for connecting Salesforce

# Setting up the required permissions for
connecting Salesforce


### 09



## 0D


This article guides you through setting up the necessary Salesforce permissions for
integrating with your Fin workspace.


### Updated over a month ago



### Table of contents


To power seamless automation and intelligent support experiences, Fin integrates deeply
with your Salesforce instance. This integration requires specific object and field-level
permissions, which allow Fin to create, update, and sync Salesforce cases and related data.

This article will walk you through:


### Why these oermissions are important



### Who needs them



### How to implement them



### A complete reference table of the required permissions



### # Why These Permissions Matter


Fin relies on Salesforce data to create cases, post summaries, read contact information,
and route conversations to agents. Without the proper permissions, Fin may be unable to
interact with your Salestorce environment effectively - resulting in failed syncs, blocked
automations, or limited functionality.

https:/fnai/helple en/
1509 - e ng g-up-L the-re 4u
5- tor-connecting e: or


### ===



### 1/6



### ===



### 0



### ===============



## 5/26/25,9:31 AM



### ===============


==========================================================================================

Setting up the required permissions for connecting Salesforce Fin by Intercom: Help Center

==========================================================================================


### # Who Needs These Permissions?


There are two key Salesforce users involved in the integration:

The connected Salesforce user the one linked during integration setup

The user assigned as Fin - the user Fin impersonates when responding, posting, or
taking workflow actions

Both require access to different objects and operations for things to run smoothly.


### # How to Implement the Permissions


The recommended approach is to assign a custom Permission Set in Salestorce:


### 09



## 0D



### 1. Go to Setup * Permission Sets


1. Create a new permission set (e.g., Fin X Salesforce Integration)


### 3. Assign the permissions shown in the table below


1. Assign the permission set to your connected Salestorce user

Make sure the following Salesforce features are also enabled:


### Chatter



### Topics (under Setup * Chatter Settings * Allow Topics)


Feed Tracking (via Setup * Object Manager * [Object] * Feed Tracking)


### Digital Experiences, for some visibility-based fields



## # Required Salesforce Permissions Table



### ==========================================================


https:l/fin.ai
a n -u p-L ne-re
or-conne cting S
2016dd66e


### ==========================================================



### ===



### 2/6



### ===



### ===============



## 5/26/25,9:31 AM



### ===============


==========================================================================================

Setting up the required permissions for connecting Salesforce Fin by Intercom: Help Center

==========================================================================================


### # Who Needs These Permissions?


There are two key Salesforce users involved in the integration:

The connected Salesforce user the one linked during integration setup

The user assigned as Fin - the user Fin impersonates when responding, posting, or
taking workflow actions

Both require access to different objects and operations for things to run smoothly.


### # How to Implement the Permissions


The recommended approach is to assign a custom Permission Set in Salestorce:


### 09



## 0D



### 1. Go to Setup * Permission Sets


1. Create a new permission set (e.g., Fin X Salesforce Integration)


### 3. Assign the permissions shown in the table below


1. Assign the permission set to your connected Salestorce user

Make sure the following Salesforce features are also enabled:


### Chatter



### Topics (under Setup * Chatter Settings * Allow Topics)


Feed Tracking (via Setup * Object Manager * [Object] * Feed Tracking)


### Digital Experiences, for some visibility-based fields



## # Required Salesforce Permissions Table



### ==========================================================


https:l/fin.ai
a n -u p-L ne-re
or-conne cting S
2016dd66e


### ==========================================================



### ===



### 2/6



### ===



### ===============



## 5/26/25,9:31 AM



### ===============


Setting up the required permissions for connecting Salesforce Fin by Intercom: Help Center


## Salesforce



### Fields



### Operations Who



### Why It's



### Object



### Needs It



### Needed



### [Table : unknown]



### <



### *



## 09 0D



### ===



### 3/6



### ===



### nups:/ in.ail e p/



### iodd66e



### tung-up-te-re 4



### or-conne cting -sa



### ===============



## 5/26/25,9:31 AM



### ===============


Setting up the required permissions for connecting Salesforce Fin by Intercom: Help Center


## Salesforce



### Fields



### Operations Who



### Why It's



### Object



### Needs It



### Needed



### [Table : unknown]



### <



### *



## 09 0D



### ===



### 3/6



### ===



### nups:/ in.ail e p/



### iodd66e



### tung-up-te-re 4



### or-conne cting -sa



## 5/26/25,9:31 AM



### [Table : unknown]



### <



### *



## 09 0D


Tip: Fields marked with C (e.g., Finlnvolved c) are custom fields used to track Al

involvement and resolution state. Make sure they're configured in Settings *


## Salesforce Integration.



### Implementation Checklist


Before you go live, make sure to:


### # Assign the custom Fin Integration Permission Set


https:/fnai/helple
150 - e a ng-up-tne-re. 4
tor-conner cting salesorclh.s20tsadsse


### ===



### 4/6



### ===



## 5/26/25,9:31 AM



### [Table : unknown]



### <



### *



## 09 0D


Tip: Fields marked with C (e.g., Finlnvolved c) are custom fields used to track Al

involvement and resolution state. Make sure they're configured in Settings *


## Salesforce Integration.



### Implementation Checklist


Before you go live, make sure to:


### # Assign the custom Fin Integration Permission Set


https:/fnai/helple
150 - e a ng-up-tne-re. 4
tor-conner cting salesorclh.s20tsadsse


### ===



### 4/6



### ===



### ===============



## 5/26/25,9:31 AM



### ===============


==========================================================================================

Setting up the required permissions for connecting Salesforce Fin by Intercom: Help Center

==========================================================================================


### [Image: unknown]



## Enable Chatter, Topics, and Feed Tracking in Salesforce


Confirm visibility for custom fields like Fininvolved C and FinResolutionstate C

Test the integration using a sandbox or non-production environment


## # Helpful Salesforce Docs



### EmailMessage Object Reference



### Feedltem API Reference



## Case Object Guide



### Topic & lopicAssignment Objects



### Did this answer your question?



### [Image: unknown]


https:l/fin.ai
a n -u p-L he-re
or-conne cting S
2016dd66e


### ===



### 5/6



### ===



### ===============



## 5/26/25,9:31 AM



### ===============


==========================================================================================

Setting up the required permissions for connecting Salesforce Fin by Intercom: Help Center

==========================================================================================


### [Image: unknown]



## Enable Chatter, Topics, and Feed Tracking in Salesforce


Confirm visibility for custom fields like Fininvolved C and FinResolutionstate C

Test the integration using a sandbox or non-production environment


## # Helpful Salesforce Docs



### EmailMessage Object Reference



### Feedltem API Reference



## Case Object Guide



### Topic & lopicAssignment Objects



### Did this answer your question?



### [Image: unknown]


https:l/fin.ai
a n -u p-L he-re
or-conne cting S
2016dd66e


### ===



### 5/6



### ===



### ===============



## 5/26/25,9:31 AM



### ===============


# Setting up the required permissions for connecting Salesforce Fin by Intercom: Help Center


### Fin by Intercom: Help Center



### The first Al agent that delivers human-quality service



### =



### <



### =



### =======
* 09
0D


### =======


https:l/fin.ai
a n -u p-L ne-re
or-conne cting S
2016dd66e


### ===



### 6/6



### ===



### ===============



## 5/26/25,9:31 AM



### ===============


# Setting up the required permissions for connecting Salesforce Fin by Intercom: Help Center


### Fin by Intercom: Help Center



### The first Al agent that delivers human-quality service



### =



### <



### =



### =======
* 09
0D


### =======


https:l/fin.ai
a n -u p-L ne-re
or-conne cting S
2016dd66e


### ===



### 6/6



### ===

