---
title: Untitled Document
document_type: guide
primary_topics: sales, zendesk, salesforce, product, messaging
last_preprocessed: 2025-06-04
---


### WHAT WE BUILT Updated Oct 24, 2024


Fin integration with Zendesk and Salesforce [closed beta] aka Fin Standalone Intermission — PM/PMM Patrick Andrews Team Principal Team Release category Beta starts Jul 22, 2024 Full release TBD Plan Separate workspace with P5, only paying for resolutions; seats are discounted Data residency EU, AU, US Sections


### Section 1: Changelog (News item)


Fin now integrates directly with your existing support platform on Zendesk or Salesforce, resolving 50%+ of your volume without migrating platforms. Import your knowledge base and connect Fin to your existing ticketing and messaging channels. When Fin won't be able to resolve, it'll seamlessly hand off to your team in Zendesk or Salesforce.

The integration works with:


### Zendesk tickets (email, forms, etc.)


Zendesk Messaging (Zendesk messenger, social, mobile SDKs, etc.)

Intercom Messenger with hand-off to Zendesk tickets or Salesforce cases


## Salesforce cases (email, forms, etc.)



## Salesforce Messenger


You have full control over when Fin gets involved using Zendesk's/Salesforce's native automation tools. And since all conversations are captured on these platforms, you can report on them there as well.

When using Fin without the rest of the Intercom platform, you only pay 99¢ per resolution — no seats and no minimums.

For now, this integration is available in beta. If you're interested in trying it, talk to us.


### 2 minute demo



## Section 2: Product description/How it works



### # Overview demo (for internal use)



### [Internal] Detailed demo of the integration


The video demos:


### Intercom Messenger with hand-off to Zendesk



### Zendesk Messenger ("headless")



### Zendesk tickets (email)



### Configuration in Intercom



### # Zendesk tickets



### How the integration works


The integration works by synchronizing Zendesk tickets to Intercom conversations. A ticket gets synced when it's assigned to a specified agent in Zendesk (e.g. Fin AI Agent).You can use Zendesk triggers to automatically assign tickets to Fin based on certain conditions.

By default the only user data attributes that get synced are name and email, but you can enable more attributes to synced, so that you can use them to further personalize the customer experience.

When a ticket is synced to Intercom, a workflow—that you can customise—will get triggered and it'll let Fin respond. Fin's response will get synced back to Zendesk. Specifics about the data usage and processing of Fin are the same as in our documentation for a standard Intercom Fin installation.

From an end-user, and Zendesk agent perspective, Intercom powering Fin is not exposed or referenced in any way.


### End-user and agent experience


When a customer send an email or submits a form that will create a ticket in Zendesk. Using Zendesk Triggers the ticket will automatically get assigned to Fin.

For any conversation that gets assigned to Fin, it'll apply the fin-involved tag.

If it knows the answer, Fin will respond and cite the sources it used, mark the ticket as solved, and apply the following tags:

fin-resolved: Fin has resolved the ticket (either soft or hard resolution)

fin-soft-resolution: Fin has resolved the conversation, but the customer hasn't confirmed it.

If the question is ambiguous, Fin will ask clarifying questions and mark the ticket as pending.

If it doesn't have an answer, it'll hand-off the ticket to the team by unassigning itself and marking the ticket as open.

The customer can ask follow-up questions and Fin will again follow the same logic.


### End-user Zendesk


If the customer says that it helped, the “fin-soft-resolution” tag will be removed and “fin-hard-resolution” applied.

If the customer asks to talk to the team, Fin will unassign itself from the ticket, remove the “fin-resolved” and “fin-soft/hard-resolution” tags and apply the “fin-routed-to-team” tag. Using this tag you can create additional Zendesk Triggers to route the ticket further.


### # Zendesk messaging



### How the integration works


Fin connects to Zendesk Messaging through Zendesk’s Sunshine Messaging API. Fin does not work with Zendesk’s classic Chat widget.


Conversations created in the Zendesk Messenger are mirrored to Conversations in Intercom. Users, their name, email, page URL, and geolocation data are also synchronized to Intercom.


When Fin is enabled, it replaces the default Zendesk Answerbot integration you may have enabled. It will not jump into the middle of any in-progress conversations, instead it will handle new conversations from this point.


Conversations with Fin follow the usual Zendesk Messaging semantics: conversations do not appear in the agent workspace unless explicitly handed over, or if the workflow ends. This is the same behavior as Zendesk’s Answerbot flow.


When a conversation is handed over, it will appear in your support team’s queue. Once opened it will create a ticket. Fin will no longer interact in the conversation after it has been handed over.


If the ticket is closed by the support agent, control will be passed back to Fin. If the user asks more questions, the messaging workflow powering Fin will run again. This is also the same behavior as Zendesk’s Answerbot.


Fin can collect Name and Email data and pass this to Zendesk as you would with the default Zendesk Answerbot.


Fin does not control authentication or identity verification – this should be handled through your overall installation of the Zendesk Messenger as described in their documentation.

When you integrate with Zendesk Messaging that means that Fin can work on all channels that are available to you in Zendesk Messaging (e.g. Zendesk Messenger, WhatsApp, mobile SDKs, etc.).


### End-user and agent experience


When the end-user opens the Zendesk Messenger they'll see a greeting from Fin (this can be customized).

After the end-user asks a question, Fin will attempt to answer, citing sources. If the question is ambiguous, Fin will ask clarifying questions. If it's unable to help it'll hand-off the ticket to the team.

Given how Zendesk Messaging works, this conversation won't be visible to agents in Zendesk until the customer asks to talk to the team.

After the customer asks to talk to the team, a new messaging ticket will be created in Zendesk and show up in the queue.


### End-user Zendesk


After an agent takes the conversation they will see the entire conversation history in the thread and can continue the conversation from there.

If the user is offline and their email is known, an email notification will be sent and they will be able to continue the conversation over email.


### # Intercom Messenger with hand-off to Zendesk tickets



### How the integration works


The Intercom messenger integration allows you to install the Intercom Messenger on your site and have new conversations from users be opened directly as tickets in Zendesk. Replies from Agents on Zendesk appear directly in the Intercom messenger.

Functionally it works the same as the tickets integration with some small differences:

When a user starts a conversation in Intercom Messenger we create a conversation in the Intercom system. This conversation is then synchronized into a Ticket in the Zendesk system.

When a user is created via the Intercom Messenger, this user is synchronized into the Zendesk system.


### End-user and agent experience


When the end-user opens the Messenger they'll see a greeting from Fin (this can be customized).

When a customer sends a message that will create a ticket in Zendesk and the intercom-messenger tag will be applied. Using Zendesk Triggers the ticket will automatically get assigned to Fin.

For any conversation that gets assigned to Fin, it'll apply the fin-involved tag.

If it knows the answer, Fin will respond and cite the sources it used, mark the ticket as solved, and apply the following tags:

fin-resolved: Fin has resolved the ticket (either soft or hard resolution)

fin-soft-resolution: Fin has resolved the conversation, but the customer hasn't confirmed it.

If the question is ambiguous, Fin will ask clarifying questions and mark the ticket as pending.

If it doesn't have an answer, it'll hand the ticket off to your team by unassigning itself and marking the ticket as open.

The customer can ask follow-up questions and Fin will again follow the same logic.


### End-user Zendesk


If the customer says that it helped, the “fin-soft-resolution” tag will be removed and “fin-hard-resolution” applied.

If the customer asks to talk to the team, Fin will unassign itself from the ticket, remove the “fin-resolved” and “fin-soft/hard-resolution” tags and apply the “fin-routed-to-team” tag. Using this tag you can create additional Zendesk Triggers to route the ticket further.

If the end-user doesn't have an associated email address, Fin will attempt to collect it (this can be customised via Workflows).


### End-user Zendesk


When the agent replies, it'll show up in the Intercom Messenger.


### End-user Zendesk


If the user is offline and their email is known, an email notification will be sent and they will be able to continue the conversation over email.


## # Salesforce cases



### How the integration works


The integration works by synchronizing Salesforce cases to Intercom conversations. We will synchronize cases created via either email to case or web to case. A case gets synced when it's assigned to a specified agent in Salesforce (e.g. Fin AI Agent). You can use Salesforce Case Assignment rules to assign cases to specific agents in Salesforce.

By default the only user data attributes that get synced are name and email, but you can enable more attributes to be synced, so that you can use them to further personalize the customer experience.

When a case is synced to Intercom, a workflow, that you can customize, will get triggered and it'll let Fin respond. Fin's response will get synced back to Salesforce. Specifics about the data usage and processing of Fin are the same as in our documentation for a standard Intercom Fin installation.

From an end-use, and Salesforce agent perspective, Intercom powering Fin is not exposed or referenced in any way.


### End-user and agent experience


When a customer sends an email or submits a form that will create a case in Salesforce. Using Salesforce's Case Assignment Rules or Flows the case will automatically get assigned to Fin.

For any case that gets assigned to Fin, it'll apply the fin-involved tag.

If it knows the answer, Fin will respond and cite the sources it used, and apply the following tags:

fin-resolved: Fin has resolved the ticket (either soft or hard resolution)

fin-soft-resolution: Fin has resolved the conversation, but the customer hasn't confirmed it.

If the question is ambiguous, Fin will ask clarifying questions.

If it doesn't have an answer, it'll hand-off the ticket to your desired case queue or user.

The customer can ask follow-up questions and Fin will again follow the same logic.


## End-user Salesforce


If the customer says that it helped, the “fin-soft-resolution” topic will be removed and “fin-hard-resolution” applied.

If the customer asks to talk to the team, Fin will assign the case to a specific queue or user of your choice, remove the “fin-soft/hard-resolution” topics and apply the “fin-routed-to-team” topic.


### # Configuration


⚠️ Since this integration is still in closed beta, the design is a bit rough and subject to change.

When using Fin AI Agent with Zendesk or Salesforce, you'll get a separate simplified workspace that only shows features that are relevant for the integration (i.e. the inbox, outbound, contacts, etc. are not available).


### # For Zendesk tickets



### The first thing that you need to do is import knowledge.


You can import knowledge by:


### Syncing your existing Zendesk knowledge base.


Syncing any public URL such as your knowledge base or marketing site.


### Uploading PDFs


Writing or copy/pasting snippets of text directly into Intercom.

You can customize how Fin responds to customers and hands off to your team when it’s unable to help by clicking on “Answer and hand-off”.

At the end of all paths, Fin will unassign itself from the ticket and apply the “routed-to-the-team” tag.

You can tailor the experience further by:


### Creating different branches based on your conditions



### Choosing when Fin answers



### Having Fin send a message



### Providing reply buttons



### Collecting data



### Collecting the customer reply



### Adding internal notes



### Adding an AI generated summary of the conversation


Auto-classifying ticket attributes based on what the customer said (more that here)

To connect to Zendesk you'll need to enter your:


### Zendesk subdomain



### Your Zendesk email



### Your API Token


You can generate a new API token at: Admin Center › Apps & Integrations › Zendesk API.

After connecting to the Zendesk API you'll need to select an identity for the AI Agent on Zendesk. Fin will reply as this agent when a ticket is assigned to it in Zendesk. We suggest creating a new agent for it and making it explicit that it's an AI Agent, rather than a human.

You can create a new agent in Zendesk in:  Admin Center › People › Team members. You can use your own email address by appending “+fin” to the name (e.g. gustavs+fin@intercom.io). You need to use a real email address because you'll need to verify the email address in Zendesk. Make sure to select “Agent” as the role since this account needs to be able to reply to tickets.

Once you've created an account and have verified it, it will be available for selection here:

By default when you set Fin live, we'll create a new trigger in Zendesk that automatically assigns all new tickets to Fin AI Agent (and hence triggers Fin to reply). If you want to have more granular control, you can disable or edit this trigger in the “Auto assign tickets” section. You can also create your own custom triggers in Zendesk that assign tickets to Fin on any condition you choose.

After you've imported content, connected to Zendesk, and selected an identity for AI Agent, the ability to test Fin will get unlocked. You can try Fin by sending an email to the given email address with the subject line “Fin test”.

Once you're ready you can set Fin live to your customers by pressing “Turn Fin on”.


### # For Zendesk Messaging


The configuration for Zenesk Messaging is quite similar to Zendesk tickets. First, you'll need to add some knowledge.

You can import knowledge by:


### Syncing your existing Zendesk knowledge base.


Syncing any public URL such as your knowledge base or marketing site.


### Uploading PDFs


Writing or copy/pasting snippets of text directly into Intercom.

You can configure the greeting your customers will see when they open up the Zendesk Messenger by clicking on “Greeting and hand-off”. From there you can also define what should happen when the user asks to talk to the team.

At the end of all paths the ticket, Fin will unassign itself and apply the “routed-to-the-team” tag.

You can tailor the experience further by:


### Creating different branches based on your conditions



### Choosing when Fin answers



### Having Fin send a message



### Providing reply buttons



### Collecting data



### Collecting the customer reply



### Adding internal notes



### Adding an AI generated summary of the conversation


Auto-classifying ticket attributes based on what the customer said (more that here)

To connect with to Zendesk you'll need expand the “Zendesk” section and enter your:


### Zendesk subdomain



### Your Zendesk email



### Your API Token


If you've already integrated with the Zendesk tickets channel this will already be filled.

You can generate a new API token at: Admin Center › Apps & Integrations › Zendesk API.

Next, you'll need to connect to the Zendesk Conversations API to allow Fin to respond on Zendesk Messaging.

You can generate these API keys at: Admin Center › Apps & Integrations › Conversations API.

Once connected, select on which messaging channels Fin should respond on:

After you've imported content, connected to Zenesk, and selected your desired messaging channels, the ability to test Fin will get unlocked. You can try Fin by entering a URL where your Zendesk Messenger is installed.

Once you're ready you can set Fin live to your customers by pressing “Turn Fin on”.


### # For Intercom Messenger with hand-off to Zendesk


At the moment this integration can only be set up manually by our team. Get in touch with us if you would like to try it (on #fin-standalone-public).


## # For Salesforce cases



### The first thing that you need to do is import knowledge.


You can import knowledge by:


### Syncing your existing Zendesk knowledge base.


Syncing any public URL such as your knowledge base or marketing site.


### Uploading PDFs.


Writing or copy/pasting snippets of text directly into Intercom.

To connect to Salesforce you'll need to create a Connected App, enable OAuth, and generate a consumer key and secret.

To create a Connected App, go to Salesforce settings and search for App Manager.

In the App Manager, click New Connected App on the top right. Once there, enter an app name, API name, and your email address.

To set up OAuth:


### Click on “Enable OAuth Settings”


Add the callback URL https://app.intercom.com/standalone/salesforce/callback (EU or AU workspaces should use their local domain e.g. https://app.eu.intercom.com)

Add the “Full Access (full)” and the “Perform requests at any time (refresh_token, offline_access)” OAuth scopes

Ensure that these checkboxes are ticked:

Require Proof Key for Code Exchange (PKCE) Extension for Supported Authorization Flows


### Require Secret for Web Server Flow



### Require Secret for Refresh Token Flow



### Enable Client Credentials Flow


Save the connected app, then click the Manage button on the next screen.

Click Edit Policies, then on the policies page, make sure Permitted Users is set to “All users may self authorize” and IP Relaxation is set to “Relax IP Restrictions”.

At the bottom of the page, set the Client Credentials flow to run as an admin account by clicking on the “Run as Lookup” icon next to the input field and selecting an admin in the window that appears.

Save your changes, go to the App Manager again, and view the app you just created.

In the OAuth section, click on the “Manage Consumer Details” section.

On the Consumer Details page, you’ll be presented with a consumer key and secret.

Copy those values into the Salesforce panel in Intercom and click “Connect to Salesforce”. Click “Allow” in the window that opens.

After connecting to the Salesforce, you'll need to select an identity for the AI Agent on Salesforce. Fin will reply as this user when a case is assigned to it in Salesforce. We suggest creating a new user for it and making it explicit that it's an AI Agent, rather than a human.

You can use your own email address by appending “+fin” to the name (e.g. gustavs+fin@intercom.io). You need to use a real email address because you'll need to verify the email address in Salesforce. Make sure that “Service Cloud User” is ticked so that Fin can reply to cases.

Once you've created an account and have verified it, it will be available for selection here:

You can customize how Fin responds to customers and hands off to your team when it’s unable to help by clicking on “Answer and hand-off”.

Customize what Fin should do when a case is assigned to it in Salesforce by clicking on “When a case is assigned to Fin in Salesforce”.

You can tailor this experience by:


### Creating different branches based on your conditions



### Choosing when Fin answers



### Having Fin send a message



### Providing reply buttons



### Collecting data



### Collecting the customer reply



### Adding internal notes



### Adding an AI generated summary of the conversation


Auto-classifying ticket attributes based on what the customer said (more that here)

To configure who Fin hands-off to in Salesforce, select a queue or user. In addition to assigning the case to this queue/user, Fin will also apply the “routed-to-the-team” topic.

To test Fin, turn it on and assign a case to the Fin AI Agent in Salesforce.

Once you’re ready for Fin to answer customer questions, use Flows or Case Assignment Rules in Salesforce to automatically assign new cases to Fin.


### # Library



### # Content


The content section lists all content that Fin has access to. The more content it has, the higher its resolution rate.

You can add more content by clicking on the “New content” button and:


### Syncing your existing Zendesk knowledge base.



### Syncing any public URL such as your website.



### Uploading PDFs.


Writing or copy/pasting snippets of text directly into Intercom.


### # Custom answers


Fin is a generative AI Agent, so it'll generate unique answers tailored to the customer's question. But sometimes you may want to have more control on how exactly Fin answers certain questions. Using custom answers you can define exactly how Fin should respond to certain questions.

You can do this by training Fin to recognize certain questions by giving examples of different ways of asking it. Once you've done that, design an exact workflow that Fin should follow when it recognises such a question.


### # Data syncing


To target your content to different audiences, automatically classify tickets (by topic/sentiment/etc), and to create branches in workflows, you'll need to sync your user and ticket data from Zendesk to Intercom.

Click on the “+” icon to select which attributes you want to sync.

For now this is only available for Zendesk, but Salesforce is coming soon.


### # Content targeting


If you want to target some content to specific types of customers (e.g. by region, plan, etc.) you can do that by creating a new audience:

If you're syncing your customer data from Zendesk, you can use that to define the criteria for this audience, for example “Region is Europe”.

To target content to a specific audience, select the desired content in the table, click on “Change audience”, and select the desired audience. By default all content is available for everyone.


### # Auto-classification


You can have more control of how Fin behaves based on what the customer says by having Fin automatically classifying certain attributes about the conversation, such as topic or sentiment, and then using this data to create different branches in your greeting and hand-off workflows.

The way this works is that you define a ticket attribute and describe each of the values in natural language. Then you can trigger an action in a workflow to automatically classify this attribute at any point in the conversation. Once classified, you can use this attribute as a condition to create different branches or pass it on as a note.

To set this up, you'll first need to make sure you have a list-type ticket field in Zendesk that describes the categories you want.

Next, start syncing this ticket attribute by adding it in the Data section.

Click on the attribute to edit the description for each value. Explain to Fin when each of the values should be used in natural language.

After you've done this, you can trigger the auto-classification from a workflow:

And then use this attribute to create conditions in branches or include it in hand-off notes.


### # Reports


Since all tickets/cases that Fin is involved in are captured on Zendesk/Salesforce, you can report on them using your reporting tools directly in Zendesk/Salesforce.

Additionally, there's a Fin Performance report in Intercom where you can see Fin's:


### Involvement



### Deflection rate



### Answer rate



### Resolution rate


Impact over time (answer rate, deflection rate, resolution rate)

Resolution state (confirmed resolution, assumed resolution, routed to the team)


### AI answer resolution rate



### Custom answer resolution rate



### Abandoned rate



### Routed to team rate



### # Usage limits


You can control your costs for Fin by setting up usage limits to alert you or stop Fin when a certain amount of resolutions has been hit within a month.

To do this go to Settings › Billing › Usage limits and click on “Set usage alerts and limits”.


### # Pricing



### Marketing version


When using Fin with the Zendesk or Salesforce integration, you're only charged ¢99 for conversations that Fin resolves — no seats, and no minimums. Read more about how resolutions work.


### Internal version


Category Notes Plans P5 only Motion Sales-led only Price Standalone has the same Resolutions pricing as the rest of Intercom - the base price is $0.99 per Resolution. Seats will be “free” via discounting as described below. How it works We sell a P5 contract and discount expert seats (as many as they require) to be free (i.e. add a 100% discount). This allows us to monetize solely on Resolutions. Fin Standalone workspaces are created through provisioning a workspace through the billing admin and applying a Fin Standalone feature flag. The Fin Standalone workspace prevents the customer from doing anything beyond using Fin with Zendesk or Salesforce (so there’s no risk of misuse). Because the seats are discounted 100%, every Standalone deal has to be routed to Deal Desk for approval.  Deal Desk is aware of this and will work with sellers to ensure approval. Discounts The same Fin discount matrix released Nov 5 also applies to Standalone Overages Overages will work as they normally do.  Any seats usage beyond the contracted amounts will be charged at list price.  To avoid this, sellers should request the Deal Desk to apply Discounted Overages to seats at time of contract. NOTE: Team Billing is launching Discounted Overages in Q4 FY25 (no later than Jan 31, 2025).  Once this has launched, the 100% discount on seats will apply to overage seats as well.  This will remove the need to over contract for seats because customers won’t be billed for any additional teammates they invite.


### # What you can't do


Currently there are some limitations when using Fin with Zendesk or Salesforce:

You can't use the Intercom Messenger for both Fin and Proactive Support.


### # Zendesk API usage


The API key provided to Intercom is stored as an encrypted record in our system.

Intercom uses the API token for the following when configuring the Fin <> Zendesk Integration:

During configuration, you must choose an admin or agent for Fin to reply as. We use the Users API to list Agents and Admins from your Zendesk workspace for you to choose from.

We create five new Zendesk Triggers using the Zendesk Triggers API

A “Fin Test” trigger which looks for incoming Tickets with “Fin Test” in the subject and triggers Fin to run without you having to activate Fin for all your customers.

An optional “Fin” trigger which assigns incoming Tickets to Fin. This is deactivated on creation, and can be optionally enabled when activating Fin. Alternatively, you can assign tickets to Fin through your existing assignment trigger setup.

A “Conversation updated” trigger – for Tickets assigned to Fin, we notify Intercom that a new update has occurred.

A “Resolution” trigger which allows Fin to mark a Ticket as “solved” when it answers the question. Note: This trigger skips filling in any required fields you may have on Tickets.

A “failsafe” trigger – in the rare occurrence that Intercom is down, and tickets are not being processed by Fin, this trigger will unassign tickets from Fin after a period of time to allow your support team to handle them.

When running the integration, Intercom uses the API token for the following:

When a ticket is assigned to Fin, Intercom is notified of an update to the ticket via a webhook. We use the Tickets API to synchronize the Zendesk Ticket data into an Intercom Conversation object that Fin can operate on.

For new conversations we synchronize the end user’s name and the user’s email into a User object in Intercom. You can also optionally synchronize specific User Fields to Intercom by choosing these fields in our setup flow.

We synchronize the Ticket’s comments into equivalent Conversation Part objects in Intercom. You can also optionally synchronize specific Ticket Fields to Intercom.

When new comments or answers are added to the Intercom Conversation by Fin, we use the Tickets API to update the Ticket in Zendesk with Fin’s replies.

If an Agent replies to a conversation while Fin is active, their comments to the end user are synchronized to the Intercom conversation. The agent name and avatar is also synchronized to Intercom so that we can show a correct representation of the conversation within the Intercom workspace.

We make a request to the Zendesk Tickets API for every new update to a Ticket assigned to Fin in Zendesk. This is so that we can correctly mirror the ticket into an Intercom conversation.

Fin will try to update the ticket in Zendesk with a conditional update. This means if another automation in your system (e.g. another Zendesk Trigger) has updated the ticket concurrently, Fin will respect the changes that were made and try to apply it’s own updates after a short delay.

We rate limit our usage of the API to 50 requests per minute. This represents 50% of Zendesk’s minimum API usage allowance. We plan to make this limit configurable.


### Requests over this limit are retried after a delay.


Section 3: [INTERNAL] Troubleshooting guidance Drivers: Eng Required for all releases where applicable


### # Future roadmap


We'll prioritize the roadmap based on customer feedback, in particular customers with very high conversation volume.

Here's what we're considering to add next:


### New integrations



## Intercom Messenger with hand-off to Salesforce



## Salesforce Messenger


We may build more integrations if there's sufficient demand from customers

Bring over more of Fin's capabilities from the standard version of Intercom, such as:


### Actions



### Unanswered questions report



### Read-only inbox for Fin



### CSAT for Fin



### Improved preview and testing experience


Make the standalone version more consistent with the standard version (so that there's less maintenance and we can provide the same functionality in both versions)


## Set up flow



### Library



### Ability to expand



### To the full platform



### To using Fin + Proactive (without the rest of the platform)



### Ability to sign up and get started in a self-serve way



### API usage report



### # Detailed technical overview



### Fin Standalone – How it works

