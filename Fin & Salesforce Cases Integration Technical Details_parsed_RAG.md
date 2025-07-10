---
title: Untitled Document
document_type: guide
primary_topics: sales, salesforce
last_preprocessed: 2025-05-24
---


## # Fin & Salesforce Cases Integration



### # Technical Details



### # Core design


The Fin <> Salesforce Cases integration works by periodically synchronizing a Salesforce Case into an Intercom Conversation data model. This is the exact same set of data models that powers Fin in a standard Intercom installation.

The Fin system runs as if running on a standard Intercom installation. It does not have direct access to data in your Salesforce account.

As Fin replies, its answers and questions are synchronized back into the original Salesforce Case.

Specifics about the data usage and processing of Fin are the same as in our documentation for a standard Intercom Fin installation.

From an end-user, and Salesforce agent perspective, the Intercom conversation model powering Fin is not exposed or referenced in any way.


### # API Token Access


The connected app secret provided to Intercom is stored as an encrypted record in our system.

When configuring the connected app, we try to minimize the permissions we get on your Salesforce integration. Currently, we only require the “Manage user data via the API (api)” and the “Perform requests at any time (refresh_token, offline_access)” scopes.


### # API Usage


Intercom uses the connected app for the following when configuring the Fin <> Salesforce Integration:

During configuration, you must choose an admin or agent for Fin to reply as, as well as a user or queue to handover to when Fin cannot help. We query the User object via the REST API to get a list of users for the workspace. We exclude certain types of users (e.g. guest users) as they cannot be assigned to cases.

We also query for queues, via the Group object in the REST API, that are setup to handle case objects and add them to the list of handover options.

When running the integration, Intercom uses the connected app for the following:

We poll intermittently, either looking for new cases assigned to the user assigned to be your AI agent in Salesforce, or updates to cases that we already know about.

When we find a new case or an update to a case that is assigned to the selected agent, we synchronise the case via the REST API into an Intercom conversation object, and then we pass that conversation to Fin if required. Once Fin replies, we create the reply in the Salesforce case via the API.

If the case was initiated by an email, we directly email the response to the end user. Note that you will need to validate your email domain with Intercom before we can send emails on behalf of your organization.

If we determine that the end user would like to speak to a human, we re-assign the case to the designated handover user or queue via the REST API.


### # API Usage and Rate Limits


As Salesforce does not natively support webhooks, we are required to poll for tickets periodically. Currently we do this every minute, so at a minimum, we will make 1,440 calls to the Salesforce API on your behalf (60 times an hour over 24 hours).

We look for any cases that have been updated in the last two minutes (we can’t absolutely guarantee the poller runs once per minute so we added a small buffer to the window), so we aren’t pulling all the cases all of the time.

When we do find a case that has been updated, we make up to around 10 requests via the API to select case feed items, create new comments from Fin, reassign the case and add topics to the case.
