---
title: Untitled Document
document_type: guide
primary_topics: sales, salesforce, product
last_preprocessed: 2025-05-26
---


### =================



## 5/26/25, 9:30. AM



### =================



### ========================================================



## Set up Fin for Salesforce a Fin by Intercom: Help Center



### ========================================================



### Ask a question



### <


All Collections > Fin for Salesforce > Set up Fin for Salesforce cases


## # Set up Fin for Salesforce cases


How to configure and customize Fin to handle cases on Service Cloud.


### Updated in the last hour



### Table of contents



### 09



### # Setup



### 00



### # Add knowledge


To set Fin up to handle Salesforce cases, the first thing you need to do is add your content
to train Fin. Go to Deploy> Salesforce cases and select Add knowledge.


### =========================


https:l/fin.ai
orce-cases


### =========================



### ====



### 1/16



### ====



### =================



## 5/26/25, 9:30. AM



### =================



### ========================================================



## Set up Fin for Salesforce a Fin by Intercom: Help Center



### ========================================================



### Ask a question



### <


All Collections > Fin for Salesforce > Set up Fin for Salesforce cases


## # Set up Fin for Salesforce cases


How to configure and customize Fin to handle cases on Service Cloud.


### Updated in the last hour



### Table of contents



### 09



### # Setup



### 00



### # Add knowledge


To set Fin up to handle Salesforce cases, the first thing you need to do is add your content
to train Fin. Go to Deploy> Salesforce cases and select Add knowledge.


### =========================


https:l/fin.ai
orce-cases


### =========================



### ====



### 1/16



### ====



### =================



## 5/26/25, 9:30. AM



### =================



## Set up Fin for Salesforce a Fin by Intercom: Help Center



### [Image: unknown]



### <



### -


# You can add knowledge by:

Syncing.any.public URL such as your knowledge base or marketing site.


### Uploading. PDFS.



### =====



### 09 00



### =====


Writing. or copypastngsnppets of text directly into Intercom.


### # Integration


First you will need to choose whether you want to connect your Sandbox (testing) or
Production (Live, customer facing).


### [Image: unknown]


To connect to Salesforce you'll need to create a Connected App and enable OAuth, and
generate a consumer key and secret (see detailed instructions below).


### =======================


https://fin.ai
ce-cases


### =======================



### ====



### 2/16



### ====



### =================



## 5/26/25, 9:30. AM



### =================



## Set up Fin for Salesforce a Fin by Intercom: Help Center



### [Image: unknown]



### <



### -


# You can add knowledge by:

Syncing.any.public URL such as your knowledge base or marketing site.


### Uploading. PDFS.



### =====



### 09 00



### =====


Writing. or copypastngsnppets of text directly into Intercom.


### # Integration


First you will need to choose whether you want to connect your Sandbox (testing) or
Production (Live, customer facing).


### [Image: unknown]


To connect to Salesforce you'll need to create a Connected App and enable OAuth, and
generate a consumer key and secret (see detailed instructions below).


### =======================


https://fin.ai
ce-cases


### =======================



### ====



### 2/16



### ====



### =================



## 5/26/25, 9:30. AM



### =================


Set up Fin for Salesforce
Fin by Intercom: Help Center


### [Image: unknown]



### =



### <



### =



### # Create a Connected App


To create a Connected App, go to Salestorce settings and search for "App Manager"! In the
App Manager, click New Connected App on the top right and choose "Create a
Connected App"


### /



### [Image: unknown]



### : -



### 09



### 00


Once there, enter an app name, API name, and your email address.


### =======================


https://fin.ai
ce-cases


### =======================



### ====



### 3/16



### ====



### =================



## 5/26/25, 9:30. AM



### =================


Set up Fin for Salesforce
Fin by Intercom: Help Center


### [Image: unknown]



### =



### <



### =



### # Create a Connected App


To create a Connected App, go to Salestorce settings and search for "App Manager"! In the
App Manager, click New Connected App on the top right and choose "Create a
Connected App"


### /



### [Image: unknown]



### : -



### 09



### 00


Once there, enter an app name, API name, and your email address.


### =======================


https://fin.ai
ce-cases


### =======================



### ====



### 3/16



### ====



### =================



## 5/26/25, 9:30. AM



### =================



## Set up Fin for Salesforce a S Fin by Intercom: Help Center



### [Image: unknown]



### <



## # Set up OAuth



### 09



### 00


# Next, set up OAuth for your Connected App:

1. Under "API (Enable OAuth Settings)" select the Enable OAuth Settings checkbox.

1. Then add the callback URL:


### httpslapp.intercom.com/standalone. salesforce/calback


(For EU or AU workspaces use your local domain e.g. ntps/app.eu.ntercom.com,

1. Under "Select oAuth Scopes" Add the following 2 options:


### "Full Access (full)"


"Perform requests at any time (refresh_token, offline_access)

1. Ensure the following checkboxes are ticked:

Require Proof Key for Code Exchange (PKCE) Extension for Supported
Authorization Flows


### Require Secret for Web Server Flow



### Require Secret for Refresh Token Flow



### Enable Client Credentials Flow



### =======================


https://fin.ai
ce-cases


### =======================



### ====



### 4/16



### ====



### =================



## 5/26/25, 9:30. AM



### =================



## Set up Fin for Salesforce a S Fin by Intercom: Help Center



### [Image: unknown]



### <



## # Set up OAuth



### 09



### 00


# Next, set up OAuth for your Connected App:

1. Under "API (Enable OAuth Settings)" select the Enable OAuth Settings checkbox.

1. Then add the callback URL:


### httpslapp.intercom.com/standalone. salesforce/calback


(For EU or AU workspaces use your local domain e.g. ntps/app.eu.ntercom.com,

1. Under "Select oAuth Scopes" Add the following 2 options:


### "Full Access (full)"


"Perform requests at any time (refresh_token, offline_access)

1. Ensure the following checkboxes are ticked:

Require Proof Key for Code Exchange (PKCE) Extension for Supported
Authorization Flows


### Require Secret for Web Server Flow



### Require Secret for Refresh Token Flow



### Enable Client Credentials Flow



### =======================


https://fin.ai
ce-cases


### =======================



### ====



### 4/16



### ====



### =================



## 5/26/25, 9:30. AM



### =================



## Set up Fin for Salesforce a S Fin by Intercom: Help Center



### [Image: unknown]



### <


# Save the Connected App, then click the Manage button on the next screen.


### 09



### 00



### [Image: unknown]


Click Edit Policies, then on the policies page under OAuth Policies, make sure Permitted
Users is set to "All users may self authorize" and IP Relaxation is set to "Relax IP
Restrictions"


### ============================


https://fin.ai/
t-u
ce-cases


### ============================



### ====



### 5/16



### ====



### =================



## 5/26/25, 9:30. AM



### =================



## Set up Fin for Salesforce a S Fin by Intercom: Help Center



### [Image: unknown]



### <


# Save the Connected App, then click the Manage button on the next screen.


### 09



### 00



### [Image: unknown]


Click Edit Policies, then on the policies page under OAuth Policies, make sure Permitted
Users is set to "All users may self authorize" and IP Relaxation is set to "Relax IP
Restrictions"


### ============================


https://fin.ai/
t-u
ce-cases


### ============================



### ====



### 5/16



### ====



### =================



## 5/26/25, 9:30. AM



### =================



## Set up Fin for Salesforce a Fin by Intercom: Help Center



### [Image: unknown]



### <



### ========


33
05
00


### ========


At the bottom of the page, set the Client Credentials flow to run as an admin account by
clicking on the "Run as Lookup" icon next to the input field and selecting an admin in the
window that appears.


### =========================


https:l/fin.ai
orce-cases


### =========================



### ====



### 6/16



### ====



### =================



## 5/26/25, 9:30. AM



### =================



## Set up Fin for Salesforce a Fin by Intercom: Help Center



### [Image: unknown]



### <



### ========


33
05
00


### ========


At the bottom of the page, set the Client Credentials flow to run as an admin account by
clicking on the "Run as Lookup" icon next to the input field and selecting an admin in the
window that appears.


### =========================


https:l/fin.ai
orce-cases


### =========================



### ====



### 6/16



### ====



### =================



## 5/26/25, 9:30. AM



### =================



## Set up Fin for Salesforce a Fin by Intercom: Help Center



### [Image: unknown]



### <



### -


Save your changes, then go to the App Manager again, and view the app you just created
using the dropdown menu next to it.


### =====


09
00


### =====



### =========================


https:l/fin.ai
orce-cases


### =========================



### ====



### 7/16



### ====



### =================



## 5/26/25, 9:30. AM



### =================



## Set up Fin for Salesforce a Fin by Intercom: Help Center



### [Image: unknown]



### <



### -


Save your changes, then go to the App Manager again, and view the app you just created
using the dropdown menu next to it.


### =====


09
00


### =====



### =========================


https:l/fin.ai
orce-cases


### =========================



### ====



### 7/16



### ====



### =================



## 5/26/25, 9:30. AM



### =================



## Set up Fin for Salesforce a Fin by Intercom: Help Center



### [Image: unknown]



### <



### =====


Y
*
* ### =====


# In the API (Enable OAuth Settings) section, click on Manage Consumer Details.


### =====


09
00


### =====



### [Image: unknown]



### =================================


nups:/ in.ai
+4 t-up- n-
ce-cases


### =================================



### ====



### 8/16



### ====



### =================



## 5/26/25, 9:30. AM



### =================



## Set up Fin for Salesforce a Fin by Intercom: Help Center



### [Image: unknown]



### <



### =====


Y
*
* ### =====


# In the API (Enable OAuth Settings) section, click on Manage Consumer Details.


### =====


09
00


### =====



### [Image: unknown]



### =================================


nups:/ in.ai
+4 t-up- n-
ce-cases


### =================================



### ====



### 8/16



### ====



### =================



## 5/26/25, 9:30. AM



### =================



### ========================================================



## Set up Fin for Salesforce a Fin by Intercom: Help Center



### ========================================================


On the Consumer Details page, you'll be presented with a consumer key and secret, you
can save these for later.


### # Al Agent identity


After connecting to Salesforce, you should be able to select an identity from the Fin Al
Agent Identity dropdown in Deploy > Salesforce Cases.


### [Image: unknown]



### <


Fin will reply as this user when a case is assigned to it in Salesforce. We recommend
creating a new user for it and making it explicit that it's an Al Agent, rather than a human.


### =======


:
05
00


### =======


You can use your own email address by appending "+fin" to the name (e.g.
dean-ingeampyo. You need to use a real email address because you'll need to verify
the email address in Salesforce. Make sure that "Service Cloud User" is ticked SO that Fin
can reply to cases.


### =========================


https:l/fin.ai
orce-cases


### =========================



### ====



### 9/16



### ====



### =================



## 5/26/25, 9:30. AM



### =================



### ========================================================



## Set up Fin for Salesforce a Fin by Intercom: Help Center



### ========================================================


On the Consumer Details page, you'll be presented with a consumer key and secret, you
can save these for later.


### # Al Agent identity


After connecting to Salesforce, you should be able to select an identity from the Fin Al
Agent Identity dropdown in Deploy > Salesforce Cases.


### [Image: unknown]



### <


Fin will reply as this user when a case is assigned to it in Salesforce. We recommend
creating a new user for it and making it explicit that it's an Al Agent, rather than a human.


### =======


:
05
00


### =======


You can use your own email address by appending "+fin" to the name (e.g.
dean-ingeampyo. You need to use a real email address because you'll need to verify
the email address in Salesforce. Make sure that "Service Cloud User" is ticked SO that Fin
can reply to cases.


### =========================


https:l/fin.ai
orce-cases


### =========================



### ====



### 9/16



### ====



### =================



## 5/26/25, 9:30. AM



### =================



## Set up Fin for Salesforce a Fin by Intercom: Help Center



### [Image: unknown]



### <



### # Answer and hand-off



### =====


09
00


### =====


You can customize how Fin responds to customers and hands off to your team when it's
unable to help in the Workflow section of your Deploy menu by clicking on Manage
Answer and hand-off.


### [Image: unknown]


# You can tailor this experience by:


### Creating different branches based on your conditions.



### Choosing when Fin answers.


https:/fin.ai/hel Ip/
1420 t-u
orce-cases


### =====



### 10/16



### =====



### =================



## 5/26/25, 9:30. AM



### =================



## Set up Fin for Salesforce a Fin by Intercom: Help Center



### [Image: unknown]



### <



### # Answer and hand-off



### =====


09
00


### =====


You can customize how Fin responds to customers and hands off to your team when it's
unable to help in the Workflow section of your Deploy menu by clicking on Manage
Answer and hand-off.


### [Image: unknown]


# You can tailor this experience by:


### Creating different branches based on your conditions.



### Choosing when Fin answers.


https:/fin.ai/hel Ip/
1420 t-u
orce-cases


### =====



### 10/16



### =====



### =================



## 5/26/25, 9:30. AM



### =================



### ========================================================



## Set up Fin for Salesforce a Fin by Intercom: Help Center



### ========================================================



### Having Fin send a message.



### Providing reply buttons.



### Collecting data.



### Collecting the customer reply.



### Adding internal notes.



### Adding an Al generated summary of the conversation.


Auto-classifying ticket attributes based on what the customer said. coming soon


### [Image: unknown]



### <



### 09



## O0


# Once you've finished customizing the workflow, click Save changes.


### # Email-to-Case Origins


To configure which case origins Fin should treat as email to case, select all of the channels
that apply in the Email-to-Case origins dropdown


### [Image: unknown]



### ==========================


https:// in.ai
oI ce-cases


### ==========================



### =====



### 11/16



### =====



### =================



## 5/26/25, 9:30. AM



### =================



### ========================================================



## Set up Fin for Salesforce a Fin by Intercom: Help Center



### ========================================================



### Having Fin send a message.



### Providing reply buttons.



### Collecting data.



### Collecting the customer reply.



### Adding internal notes.



### Adding an Al generated summary of the conversation.


Auto-classifying ticket attributes based on what the customer said. coming soon


### [Image: unknown]



### <



### 09



## O0


# Once you've finished customizing the workflow, click Save changes.


### # Email-to-Case Origins


To configure which case origins Fin should treat as email to case, select all of the channels
that apply in the Email-to-Case origins dropdown


### [Image: unknown]



### ==========================


https:// in.ai
oI ce-cases


### ==========================



### =====



### 11/16



### =====



### =================



## 5/26/25, 9:30. AM



### =================


Set up Fin for Salesforce
Fin by Intercom: Help Center


### Then click Save to update your configured channels.



### # Email Domain Verification


Next, verify your email domain to ensure that emails sent from Fin are delivered
successtully.

Go to Channels > Salesforce cases and click + Add email domain below the "Email
Domain Verification" section. You'll need to enter:

Display name: This is the name that will appear as the sender of your emails.

Email address: A domain that you're using to receive inbound cases in Salesforce.


## - JA



### - -



### [Image: unknown]



### 09



### 00


Click Add email to save, you will receive a green pop up banner confirming that your email
domain has been added.


### # Test and go live


To test Fin, go to Channels > Salesforce cases and select Turn Fin on at the bottom of the
page, then assign a case to the "Fin Al Agent" you created in Salesforce.

Fin won't be live to your customers immediately, Fin will only respond to tickets assigned to
it. Once you're ready for Fin to answer customer questions, use Flows or Case Assignment
Rules in Salesforce to automatically assign new cases to Fin.


### =======================


https://fin.ai
ce-cases


### =======================



### =====



### 12/16



### =====



### =================



## 5/26/25, 9:30. AM



### =================


Set up Fin for Salesforce
Fin by Intercom: Help Center


### Then click Save to update your configured channels.



### # Email Domain Verification


Next, verify your email domain to ensure that emails sent from Fin are delivered
successtully.

Go to Channels > Salesforce cases and click + Add email domain below the "Email
Domain Verification" section. You'll need to enter:

Display name: This is the name that will appear as the sender of your emails.

Email address: A domain that you're using to receive inbound cases in Salesforce.


## - JA



### - -



### [Image: unknown]



### 09



### 00


Click Add email to save, you will receive a green pop up banner confirming that your email
domain has been added.


### # Test and go live


To test Fin, go to Channels > Salesforce cases and select Turn Fin on at the bottom of the
page, then assign a case to the "Fin Al Agent" you created in Salesforce.

Fin won't be live to your customers immediately, Fin will only respond to tickets assigned to
it. Once you're ready for Fin to answer customer questions, use Flows or Case Assignment
Rules in Salesforce to automatically assign new cases to Fin.


### =======================


https://fin.ai
ce-cases


### =======================



### =====



### 12/16



### =====



### =================



## 5/26/25, 9:30. AM



### =================


Set up Fin for Salesforce
Fin by Intercom: Help Center


### [Image: unknown]



### <



### -



### # How it works


When a customer sends an email or submits a form, that will create a case in Salesforce.
Using Salesforce's Case Assignment Rules or Flows, the case will automatically get
assigned to Fin.


### =====


09
00


### =====



### =========================


https:l/fin.ai
orce-cases


### =========================



### =====



### 13/16



### =====



### =================



## 5/26/25, 9:30. AM



### =================


Set up Fin for Salesforce
Fin by Intercom: Help Center


### [Image: unknown]



### <



### -



### # How it works


When a customer sends an email or submits a form, that will create a case in Salesforce.
Using Salesforce's Case Assignment Rules or Flows, the case will automatically get
assigned to Fin.


### =====


09
00


### =====



### =========================


https:l/fin.ai
orce-cases


### =========================



### =====



### 13/16



### =====



### =================



## 5/26/25, 9:30. AM



### =================



## Set up Fin for Salesforce as S Fin by Intercom: Help Center



### [Image: unknown]



### <



### ===


*
* ### ===



### =====


09
00


### =====


# For any case that gets assigned to Fin, it'll apply the fin-involved topic.

If Fin has relevant knowledge available to answer, Fin will respond and cite the sources it
used, and apply the following tags:

fin-resolved: Fin has resolved the ticket (either soft or hard resolution).

fin-soft-resolution: Fin has resolved the conversation, but the customer hasn't
confirmed it.


### =========================


https:l/fin.ai
orce-cases


### =========================



### =====



### 14/16



### =====



### =================



## 5/26/25, 9:30. AM



### =================



## Set up Fin for Salesforce as S Fin by Intercom: Help Center



### [Image: unknown]



### <



### ===


*
* ### ===



### =====


09
00


### =====


# For any case that gets assigned to Fin, it'll apply the fin-involved topic.

If Fin has relevant knowledge available to answer, Fin will respond and cite the sources it
used, and apply the following tags:

fin-resolved: Fin has resolved the ticket (either soft or hard resolution).

fin-soft-resolution: Fin has resolved the conversation, but the customer hasn't
confirmed it.


### =========================


https:l/fin.ai
orce-cases


### =========================



### =====



### 14/16



### =====



### =================



## 5/26/25, 9:30. AM



### =================



## Set up Fin for Salesforce a Fin by Intercom: Help Center



### [Image: unknown]



### <



### -



### Learn more about how Fin resolutions are defined.



### 33



### 09



### 00


If the question is ambiguous, Fin will ask clarifying questions. If Fin doesn't have an answer
it'll hand-off the ticket to your desired case queue or user. Customers can ask follow-up
questions and Fin will follow the same process.

If the customer says that it helped, the fin-soft-resolution topic will be removed and
fin-hard-resolution applied.

If the customer asks to talk to the team, Fin will assign the case to a specific queue or user
of your choice, remove the fin-soft/hard-resolution' topics and apply the "fin-routed-
to-team" topic.

https:l/fin.ai
orce-cases


### =====



### 15/16



### =====



### =================



## 5/26/25, 9:30. AM



### =================



## Set up Fin for Salesforce a Fin by Intercom: Help Center



### [Image: unknown]



### <



### -



### Learn more about how Fin resolutions are defined.



### 33



### 09



### 00


If the question is ambiguous, Fin will ask clarifying questions. If Fin doesn't have an answer
it'll hand-off the ticket to your desired case queue or user. Customers can ask follow-up
questions and Fin will follow the same process.

If the customer says that it helped, the fin-soft-resolution topic will be removed and
fin-hard-resolution applied.

If the customer asks to talk to the team, Fin will assign the case to a specific queue or user
of your choice, remove the fin-soft/hard-resolution' topics and apply the "fin-routed-
to-team" topic.

https:l/fin.ai
orce-cases


### =====



### 15/16



### =====



### =================



## 5/26/25, 9:30. AM



### =================



## Set up Fin for Salesforce a Fin by Intercom: Help Center



### [Image: unknown]



### <



### =====


05
00


### =====



### [Image: unknown]



### Did this answer your question?



### [Image: unknown]



### Fin by Intercom: Help Center



### The first Al agent that delivers human-quality service



### =========================


https:l/fin.ai
orce-cases


### =========================



### =====



### 16/16



### =====



### =================



## 5/26/25, 9:30. AM



### =================



## Set up Fin for Salesforce a Fin by Intercom: Help Center



### [Image: unknown]



### <



### =====


05
00


### =====



### [Image: unknown]



### Did this answer your question?



### [Image: unknown]



### Fin by Intercom: Help Center



### The first Al agent that delivers human-quality service



### =========================


https:l/fin.ai
orce-cases


### =========================



### =====



### 16/16



### =====

