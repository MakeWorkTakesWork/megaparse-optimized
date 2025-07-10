---
title: Untitled Document
document_type: guide
primary_topics: sales, salesforce, product
last_preprocessed: 2025-05-26
---


### ================



## 5/26/25, 9:42 PM



### ================



### ===========================================



## Salesforce account sync setup Intercom Help



### ===========================================



### [Image: unknown]



### # intercom



### =



### Search for articles...



### <


All Collections > Apps & Integrations > CRM integration > Salesforce app
Salesforce account sync setup


### -



## # Salesforce account sync setup


How to resolve issues related to your Salesforce account sync setup


### [Image: unknown]



### [Image: unknown]


Written by Beth-Ann Sher
Updated over a month ago


### =====


0S
00


### =====



### Table of contents



## V



### # Resolution Steps



### Requirements


The Salestorce App Account sync feature must have all of the following pre-contigured in
order for the sync to run successfully:


### Company feature enabled


Set intercom's company_id with a value that will match to a Salesforce field


### Changes (create / update) to company data in Intercom



## Changes (create / update) to account data in Salestorce



### # Companies Disabled


If a workspace doesn't have company features enabled, a warning is shown in the Salesforce
application settings page.


### ============================================


https
ercom.cor
y 068 a orce-acountsyne-seup


### ============================================



### ===



### 1/5



### ===



### ================



## 5/26/25, 9:42 PM



### ================



### ===========================================



## Salesforce account sync setup Intercom Help



### ===========================================



### [Image: unknown]



### # intercom



### =



### Search for articles...



### <


All Collections > Apps & Integrations > CRM integration > Salesforce app
Salesforce account sync setup


### -



## # Salesforce account sync setup


How to resolve issues related to your Salesforce account sync setup


### [Image: unknown]



### [Image: unknown]


Written by Beth-Ann Sher
Updated over a month ago


### =====


0S
00


### =====



### Table of contents



## V



### # Resolution Steps



### Requirements


The Salestorce App Account sync feature must have all of the following pre-contigured in
order for the sync to run successfully:


### Company feature enabled


Set intercom's company_id with a value that will match to a Salesforce field


### Changes (create / update) to company data in Intercom



## Changes (create / update) to account data in Salestorce



### # Companies Disabled


If a workspace doesn't have company features enabled, a warning is shown in the Salesforce
application settings page.


### ============================================


https
ercom.cor
y 068 a orce-acountsyne-seup


### ============================================



### ===



### 1/5



### ===



### ================



## 5/26/25, 9:42 PM



### ================



### ===========================================



## Salesforce account sync setup Intercom Help



### ===========================================


To rectify, navigate to Settings > Workspace > General and enable. 4 Once this step is
completed, you'll need to ensure companies are being. created in Intercom.


### [Image: unknown]



### <



### # No existing companies



### =====


0S
00


### =====


If company features are enabled, the next requirement would be to create companies in
Intercom using the messenger snippet or through the API. While creating or updating a
company, company_id should be set to the value of the salesforce field used for mapping.


### [Image: unknown]



### [Image: unknown]


Once this step is completed, ensure companies are being created/updated.


### # No Company triggers


https
ercom.com
90680-sales! orce-acountsyne-seup


### ===



### 2/5



### ===



### ================



## 5/26/25, 9:42 PM



### ================



### ===========================================



## Salesforce account sync setup Intercom Help



### ===========================================


To rectify, navigate to Settings > Workspace > General and enable. 4 Once this step is
completed, you'll need to ensure companies are being. created in Intercom.


### [Image: unknown]



### <



### # No existing companies



### =====


0S
00


### =====


If company features are enabled, the next requirement would be to create companies in
Intercom using the messenger snippet or through the API. While creating or updating a
company, company_id should be set to the value of the salesforce field used for mapping.


### [Image: unknown]



### [Image: unknown]


Once this step is completed, ensure companies are being created/updated.


### # No Company triggers


https
ercom.com
90680-sales! orce-acountsyne-seup


### ===



### 2/5



### ===



## 5/26/25, 9:42 PM



## Salesforce account sync setup Intercom Help


This means new companies aren't being created in intercom and existing ones aren't being
updated to trigger the sync to salesforce.

To address this, follow the same steps mentioned in "No existing. companies"


### # No Account triggers


This means accounts aren't being created in salesforce and existing ones aren't being updated
to trigger the sync to Intercom.


### <


To address this, companies need to be created and updated in salesforce, with the desired
mapping field in salestorce matching intercom's company.id




### -



### # Configured but no Identity mappings


If no account identity mappings have been created, this means the selected salesforce field to
map to doesn't match intercom's company.id".

To remedy this for current users, we've sampled some companies and tried to match them to
accounts in salesforce, in order to suggest a field that would lead to mappings.


### =====


0S
0D


### =====



### 9 Tip



### [Image: unknown]


Need more help? Get support from our Community. Forum
Find ansy wers and get help from Intercom Support and Community Experts


### # Related Articles



### [Image: unknown]



### [Table : unknown]



## Salesforce integration troubleshooting and FAQs



## Install Salestorce integration



## Using the Salestorce app in Intercom


# Syncing data between Salesforce accounts and Intercom companies

tl
tercom.cor
y 0680-5 sal orce-acountsyne-seup


### ===



### 3/5



### ===



## 5/26/25, 9:42 PM



## Salesforce account sync setup Intercom Help


This means new companies aren't being created in intercom and existing ones aren't being
updated to trigger the sync to salesforce.

To address this, follow the same steps mentioned in "No existing. companies"


### # No Account triggers


This means accounts aren't being created in salesforce and existing ones aren't being updated
to trigger the sync to Intercom.


### <


To address this, companies need to be created and updated in salesforce, with the desired
mapping field in salestorce matching intercom's company.id




### -



### # Configured but no Identity mappings


If no account identity mappings have been created, this means the selected salesforce field to
map to doesn't match intercom's company.id".

To remedy this for current users, we've sampled some companies and tried to match them to
accounts in salesforce, in order to suggest a field that would lead to mappings.


### =====


0S
0D


### =====



### 9 Tip



### [Image: unknown]


Need more help? Get support from our Community. Forum
Find ansy wers and get help from Intercom Support and Community Experts


### # Related Articles



### [Image: unknown]



### [Table : unknown]



## Salesforce integration troubleshooting and FAQs



## Install Salestorce integration



## Using the Salestorce app in Intercom


# Syncing data between Salesforce accounts and Intercom companies

tl
tercom.cor
y 0680-5 sal orce-acountsyne-seup


### ===



### 3/5



### ===



### ================



## 5/26/25, 9:42 PM



### ================



### ===========================================



## Salesforce account sync setup Intercom Help



### ===========================================


Manually sync people data in bulk using Intercom's Salestorce app


### Did this answer your question?



### [Image: unknown]



### [Image: unknown]



### <



### =



### a



### =



### [Image: unknown]



### =====


0S
00


### =====



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
068 a orce-accoumtsyne-setup


### ===



### 4/5



### ===



### ================



## 5/26/25, 9:42 PM



### ================



### ===========================================



## Salesforce account sync setup Intercom Help



### ===========================================


Manually sync people data in bulk using Intercom's Salestorce app


### Did this answer your question?



### [Image: unknown]



### [Image: unknown]



### <



### =



### a



### =



### [Image: unknown]



### =====


0S
00


### =====



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
068 a orce-accoumtsyne-setup


### ===



### 4/5



### ===



### ================



## 5/26/25, 9:42 PM



### ================



## Salesforce account sync setup Intercom Help



### <



### =



### a



### =



### =====


0S
00


### =====



### ============================================


https
ercom.co:
y 068 a orce-acountsyme-seup


### ============================================



### ===



### 5/5



### ===



### ================



## 5/26/25, 9:42 PM



### ================



## Salesforce account sync setup Intercom Help



### <



### =



### a



### =



### =====


0S
00


### =====



### ============================================


https
ercom.co:
y 068 a orce-acountsyme-seup


### ============================================



### ===



### 5/5



### ===

