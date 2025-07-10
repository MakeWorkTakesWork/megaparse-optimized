---
title: Untitled Document
document_type: guide
primary_topics: sales, poc, process, demo, evaluation, zendesk, salesforce
last_preprocessed: 2025-05-19
---


## Fin Standalone Sales, Set Up & POC Process



## Sales & POC Process


Stage Overview Driver Supporting Discovery High level pitch and gather customer context, goals and suitability AE n/a Demo Live Fin demo trained on their content demonstrated in ZD or SF environment SE AE (always) PM (if required product is early e.g. SFDC) Set up Hand held set up session and discussion to align on success criteria for POC SE AE (always) PM (if required product is early e.g. SFDC) POC & evaluation PoC evaluation plan to guide and support customers through properly evaluating Fin and achieving success. Supported with regular meetings and clear communication channels (e.g. shared slack) SE AE (always) PM (‘if required product is early e.g. SFDC’
OR
‘for AAA/AA or >50k convo per month accounts’ ) Commercial Contract and commercial negotiation. AE n/a


### Important notes


AE/ SEs should continue to include PM earlier in the process (eg. from demo) when a customer requires Fin SA features that are early in the development cycle e.g. Salesforce, Intercom Messenger channel and soon API.

PM should only be brought into support the POC phase if A) the customer requires features early in development cycle (similar to above) OR B) it’s a priority account defined by AAA/AA or >50k convo per month

Certain accounts will also quality also for a swarm (see details below)


## Demo



### Prep



## You need a paid-for Zendesk and Salesforce account


Create new Intercom workspace for both ZD and SF and apply the correct feature flags


### Create a demo web page to host the different messengers


Chris Murphy/ Brian Deeley have context on how to set this up


### Guidance



### Pre-train Fin on prospect content



## Demo Fin live in Zendesk or SFDC environment


Pre-prepare relevant questions for the demo using Chat GPT to generate hard question against their knowledge base

The demo should cover: 1) how Fin works in platform channels; 2) how the integration works and 3) the key Fin features

Tailor the demo based on the customers context e.g. show Fin on the channels they use and if we know they have a lot of action questions, ensure this is demoed properly


## Set up process


Invite customer to 1h set up & PoC kick off call that has two goals

Guiding the customer through setting up the integration so they start testing

Aligning the success criteria and plan for the PoC & evaluation process (see below)

Create them a workspace from billing admin - extend trial for 6-8 weeks

Apply the relevant Fin Standalone feature flags - the following base flags will apply all the required flags. Be aware that if your account has the standalone-base feature flag, any new feature flag will not get automatically applied


### fin-standalone-base (USA)



### fin-standalone-base (EU)


For Salesforce customers, also enable: team-standalone-fin-standalone-salesforce

[if using ZD tickets/SF cases] Send customer email ahead to get them to create admin in Zendesk/ SF (see example below)

Add yourself to their workspace (via billing admin) and add import their content


### Invite them to the workspace


In set up meeting, 1) guide them through set up steps ie. inputting API keys etc and 2) confirm success criteria and PoC plan


### Example email (step 4)



### 
```
Hey folks,

```


Great to meet last week and looking forward to getting you set up with Fin on Zendesk tomorrow.

Ahead of the call, it would be ideal if you could create an account for Fin on Zendesk so that it can reply to your customers. You can do this via Admin Center › People › Team members. Give it a name (e.g. Fin AI Agent) and an email (you can use your own email and append “+fin” e.g. akshay.joshi+fin@cloudinary.com). An Agent seat will be sufficient and make sure to confirm the email address after you create it (you'll need to be signed out of Zendesk to do it). You can also upload the attached image as a profile photo if you'd like.

To connect to Zendesk you'll also need to generate API keys for the Zendesk API and Conversations API, so it's important that someone on the call tomorrow has an admin seat.


## PoC & Evaluation Process


‘Evaluation’ is the process we guide prospects through in their PoC to ensure they properly and fairly evaluate Fin and are able to achieve their success criteria which ultimately drives the buying decision.

Brian Deeley is working on standardised template and approach for how to run Fin evaluation in PoCs but in general we should be getting clear on the customers success criteria and then guiding them through a structured step by step process to properly test Fin.

Fin Standalone PoC Template:


### Google Sheet


Customer Context: PoC objective: Contacts: Communication channels/ Meeting cadence: Timeline: Optional phases Content optimisation Guidance Actions Additional channels Overall Fin Performance


## Services Team & Swarms


A newly created Services Group (part of Team Fin; led by Diego Ballona) has been created to support our most critical Fin opportunities.

For such opportunities, a swarm playbook is followed where a dedicated swarm team (R&D, RAD, GTM and senior leaders) will lead the customer through their consideration, evaluation and deployment process ensuring all their product needs are met, they evaluate Fin effectively, and ultimately, ensures we do whatever it takes to win the deal.

Account qualification: 100k conversation per month OR AAA account OR DG compete OR Parahelp compete OR Sierra compete. SLT approves.

Swarms driven by the Services Team are available to all Fin opportunities including Fin Standalone.

The Fin SA team should flag with Diego if we think an opportunity should be considered for a swarm.
