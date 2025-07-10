---
title: # https://www.intercom.com/help/en/articles/10560969-fin-guidance-best-practices Fin Standalone – How it works
document_type: guide
primary_topics: sales, zendesk, salesforce, messaging
last_preprocessed: 2025-06-04
---

# https://www.intercom.com/help/en/articles/10560969-fin-guidance-best-practices Fin Standalone – How it works


### Eoin Nolan • Last updated Oct 30, 2024



### # What is Standalone?


At its simplest, Fin Standalone is just a mapping between Intercom’s conversational system, and a third party conversational system. If a third party has the concept of conversations with comments between admins and users, and an API that lets us read and write these objects, then we can synchronize these into their equivalent objects in Intercom. Having a mirrored version of a conversation from a third party system allows us to run Fin and various other workflow features without these Intercom features needing to care about the original source of the data. In essence, Standalone is a fancy data synchronizer: it’s a layer of glue between Intercom and Zendesk, or Salesforce, etc.


Standalone workspaces are completely separate from the standard Intercom teammate workspace. They have no inbox, all support agents live in the third party tool; they will never modify the conversation via Intercom. Most “inbox” concepts like state (open/closed etc), assignment (assigned to Fin, assigned to Eoin), SLAs, CSAT etc are completely ignored on the Intercom side. This type of functionality is handled in the third party’s system and we don’t attempt to mirror that data to or from Intercom. This greatly reduces the scope and complexity of the data we need to synchronize between the systems.

Once we have a representation of a conversation copied into Intercom, we can run Fin or other automation features like workflows without needing to care about where the original data for the conversation came from. Fin doesn’t care that a conversation was started from a Zendesk Ticket, as long as it receives the data in the right format, it will happily answer questions. The synchronization layer we’ve built for Standalone will simply take its answer and synchronize it back to the third party.

A key aspiration we have with Standalone is that Fin Standalone is just Fin. Any new features built for Fin should just work in a standalone workspace for free. Things like multilingual, tone of voice, email specific formatting should just work out of the box. Even things like Fin performing actions should just work too. We may have to customize the UI for some of the features to hide options that don’t make sense in a standalone workspace (e.g. “close Fin conversations after 3 minutes”) but the core functionality under the hood should be the same.


### # How synchronization works


Today we have three different synchronizers:

Zendesk Tickets – Synchronizes tickets from Zendesk into Intercom using the Zendesk Tickets API. Tickets are typically created via Inbound Email into Zendesk, or via a web form.

Zendesk Messaging – Synchronizes “Sunshine Conversations” into Intercom. Sunshine (formerly smooch.io) is Zendesk’s Messaging platform and has a completely different API to tickets. It also has a different feature set (e.g. in what content it supports)

Salesforce Cases – Synchronizes cases from Salesforce into Intercom using the Salesforce REST API. Cases are typically created using Salesforce’s Email 2 Case automation, or their web form automation Web 2 Case.

We’ll look at each of these in more depth later, but first let’s look at the shared concepts they have.


### # Shared concepts



### # The Standalone::Models::WorkflowReference record


Each integration is treated as its own distinct channel, and each integration has a single workflow which we trigger when a new conversation is synchronized into Intercom.

During setup of a Standalone workspace, we create a Workflow for each of these channels using specific templates in templates/workflows/fin_standalone_* . Each workflow created is linked to the channel it should run for using a WorkflowReference record.


We do not use matching rules to find eligible Workflows to run for a new conversation like we would on a regular Intercom workspace, instead we look up the appropriate workflow for the channel and trigger it using Operator::BotFramework.notify_start_workflow.


### # The Standalone::Models::ExternalReference record


Every integration creates Conversations, ConversationParts, and Users in the Intercom system and we need some way of knowing what records we’ve created in Intercom map to what records from the third party system.

We use the ExternalReference record for this. This polymorphic record allows us to map any record in Intercom to any record in a third party system. It gives us internal_id and internal_type properties and external_id and external_type properties. There are uniqueness constraints to prevent us from mistakenly recreating the same record. The internal_type enum uses the values from our global EntityTypes file, and the external_type enum uses a new set of values from Standalone::Constants::ExternalTypes.

Each integration can create these records in different ways depending on its needs (e.g. the Tickets integration maps ConversationPart to ZendeskComment, whereas the Zendesk Messaging integration chooses to map RenderablePart to SunshineComment) but the concept of needing to map records in Intercom to external records, and ensuring we don’t create duplicate data is the same in all integrations.

# The Standalone::Models::<Zendesk|Sunshine|Salesforce>Integration

Each integration has it’s own record to store specific data needed to run its synchronizer. API Keys are stored on these records and are encrypted using the encrypts method on ActiveRecord. Outside of API keys, these models store information like the ID of the agent in the external system to use as Fin, or the ID of specific channels to run Fin on.

Each integration has a standard state field enum which can be found in Standalone::Constants::IntegrationStates:


### NOT_CONFIGURED – The integration has not been set up at all



### CREATED – The integration has connected to the relevant API


ENABLED – The integration is currently enabled, Fin is running.

PAUSED – The integration was once enabled, and is now paused.

The two Zendesk integrations share some common API configuration, and have separate records for specific Zendesk Tickets and Zendesk Messenger needs.


### # Data Synchronization


All Fin Standalone channels support some form of Data Synchronization, and they all use the same style of UI – the Zendesk version is shown above.


Data Synchronization allows customers to choose specific user data or ticket/case data they want to synchronize to Intercom. The use case is to allow them to power Intercom features like Fin Audience Targeting, or workflow branching using the data they keep in the third party. Some system fields are synchronized by default, e.g. User Email, Conversation title etc.


Data Synchronization is one way. We treat the third party as the source of truth and for simplification of the system we simply read this data into Intercom instead of trying to sync data from our side back (potentially causing data conflicts).

NOTE: The Zendesk Messaging channel allows collecting Name and Email and writing this to Zendesk as this is required for minimum viability of a messenger channel!

At a high level, Data Synchronization works by allowing customers to choose a subset of fields they want to sync, and then creating a CDA or CvDA in Intercom for this data to be written to. Fields from the third party are mapped to their Intercom equivalent using an ExternalReference record, this is how we know where to write specific values when we read them from third party records.

Configuration of these fields is done through these modules:


## Standalone::Salesforce::UserFields



## Standalone::Salesforce::CaseFields



### Standalone::Zendesk::UserFields



### Standalone::Zendesk::TicketFields


These are accessed from the Teammate UI through the Standalone::SalesforceDataController and Standalone::ZendeskDataController.


### # Dummy Admins


We want replies from Agents in the third party system to be synchronized into Intercom using the correct admin name and photo. To cater for this we have the loose concept of a “dummy admin”. These are admin records that are created in Intercom using a special email format: <original email>.hirefin.com where we pull in the admins name and photo too.

We own the hirefin.com domain, and adding this as the email domain for these dummy admins ensures that nobody can access the email associated with them (e.g. to reset the password).


These dummy admins are created with no seat and are hidden from the Teammates list in the UI.


### # The Zendesk Tickets Synchronizer



### # Connection and Setup



When you connect Standalone to your Zendesk workspace you must provide three key pieces of information:


### Your Zendesk subdomain – e.g. mysubdomain.zendesk.com


Your Zendesk Email – Authentication with the API is a combination of Email and Token access.

A Zendesk API Token – Created from the Zendesk Admin page and provided by the customer.

This information is stored on the ZendeskApiIntegration model and is used by Intercom when connecting to the Zendesk API. To access the API, we use the official Zendesk API Ruby client.


### # Choosing an Agent


For the Zendesk Tickets integration to work, we need an Agent in Zendesk for Fin to act as. We do this for two reasons:

Tickets assigned to this agent will be sent to Intercom for processing.

Replies from Fin will appear to the end user as being from the selected agent.

The ID of the agent selected here is stored on the ZendeskTicketsIntegration record as fin_zendesk_user_id.


### # Zendesk Triggers, Webhooks, and Automations


Once an agent is selected, we create a set of Triggers in Zendesk to power the integration. There are 4 triggers in total:

The Resolution Trigger – After synchronizing an answer from Fin, we tag the Zendesk ticket with the current resolution state. This trigger then runs and can mark the ticket as solved. We use a trigger here as it can bypass validation that certain Zendesk workspaces have whereby to close a ticket you must fill out a set of required fields.

The Assignment Trigger – This trigger will assign all new incoming tickets (and not messenger conversations etc) to the agent selected as Fin. It is disabled initially.

The Testing Trigger – To allow our customers to test Fin without going live, we create a trigger that will assign incoming tickets with the subject line “Fin test” to the Fin agent.

The Notify Fin Trigger – This final trigger notifies Intercom via a webhook of any updates to tickets assigned to the Fin agent.

The configuration for this webhook can be found in the Zendesk Admin Settings


When the webhook is created, we make note of the webhook secret and store this on the ZendeskApiIntegration model as webhook_signing_secret

Finally we create an Automation in Zendesk called Fin Failsafe. The purpose of this automation is to prevent tickets getting stuck assigned to the Fin Agent in Zendesk in cases where Intercom is down. The automation is set up to run after 1 hour on tickets assigned to Fin which are “New” or “Open” and have had no updates.


### # Assignment to Fin


We make it optional to enable the Assignment Trigger described above when activating Fin. Many customers may have more complex assignment rules in place already and in those cases we encourage them to assign new tickets to Fin via their existing rules. This option is stored as manage_assignment_trigger on the ZendeskTicketsIntegration record.


### # Receiving new Tickets from Zendesk


When a new ticket is created in Zendesk and assigned to Fin, we receive a webhook payload from Zendesk in the Hooks::ZendeskTicketsController endpoint. This payload contains an App ID code, and a ticket ID, ticket title, and the request has signing headers from Zendesk. We verify the webhook authenticity using the webhook_signing_secret we stored during setup. Invalid webhooks return a 404, and the entire endpoint requires access to the Standalone::FeatureFlags::MAIN feature flag.

Once validated, we enqueue a Standalone::Workers::ZendeskTicketSyncWorker job with the payload.


### # The ZendeskTicketSyncWorker


The ZendeskTicketSyncWorker is called when receiving Ticket updated webhook events from Zendesk, and also directly from the Intercom conversation lifecycle hooks when we update a synced conversation in Intercom.

It therefore has two shapes of arguments:


### Updates from Zendesk pass a zendesk_ticket_id



### Updates from Intercom pass an intercom_conversation_id



### Passing both IDs at once will raise an Argument Error.


The worker sets up a Standalone::Zendesk::TicketSynchronizer with a ZendeskSynchronizationContext object. This object gives the synchronizer enough information to know what ticket to load from Zendesk, what title the ticket has, how many times the job has retried etc.

The worker also applies some debouncing when calling the synchronizer. As we are receiving webhooks from Zendesk for every update to the Ticket it’s possible we’ll receive bursts of webhooks for a single ticket in a very short period of time. We debounce processing of any given ticket to once every 3 seconds. This is done using a Rails cache key with a short expiry, paired with an unless_exists: true write.


### # Inside the Standalone::Zendesk::TicketSynchronizer


The synchronize! method is the main method of the Zendesk Ticket synchronizer.
The first thing we do is load the ticket record from Zendesk using the ZendeskAPI with the ticket_id provided. We then check whether or not the synchronizer is even eligible to run:


### We check that the ticket actually exists in Zendesk.


It checks the ticket_status of the ZendeskApiIntegration for the app.

If the ticket_status is not ENABLED, we check the title of the ticket that was provided directly to see if it is a “Fin Test” ticket.

We check the ticket is not from a Zendesk Channel we don’t support (e.g. “native messaging”)


Once we have determined the ticket should be synchronized, we acquire a lock. This is to protect against attempting to make competing updates to the ticket at the same time, and therefore possibly creating duplicate messages.

Inside the lock we do five main things:


### find_or_create_conversation



### synchronize_zendesk_data_fields



### pull_unsynced_comments_from_zendesk



### push_conversation_to_zendesk



### record_synchronization_state


Let’s look at each of these individually:


### # TicketSynchronizer.find_or_create_conversation


This method is responsible for creating a user record in Intercom, and a conversation in Intercom to represent the Ticket requester and the Ticket itself respectively. If we have already created a conversation for the ticket, we will return the existing user and conversation – any existing conversation can be found by looking up the ExternalReference record for the Zendesk Ticket.


Finding, or creating a new user – in cases where we don’t have a conversation already we need to first find or create a user in Intercom to attach the conversation to. We use the requester ID from Zendesk as the user_id of the Intercom user. This ensures that new tickets from the same Zendesk Requester will use the same user record in Intercom. We do not use email to create or look up the user, this ensures that Zendesk users with the same email are represented separately in the Intercom system. When a user is created, we map it to the Zendesk User through an ExternalReference record.


Once a user is created or found we call the Standalone::Zendesk::UserFields synchronize_fields_to_intercom_user method to ensure any User Field data in Zendesk that the customer wants to synchronize is copied to the Intercom user.

Creating the conversation – Where the conversation does not exist already we create a new UserMessage to represent the first part from the Ticket.

The subject is taken directly from the equivalent field on the Ticket.

The body is passed through a Standalone::Zendesk::EmailBodyCleaner.remove_signature method to perform a rudimentary email signature removal. We had found that email signatures meant not Custom Answers would match when required so this was a first pass at making that perform better.


### The message type is set specifically to :zendesk_ticket.


The channel is set to Channels::Channel::ZendeskTicket. This is a new channel we have added specifically for Zendesk Tickets we sync. It is functionally the same as the Email channel.

As with the User Fields above, we also synchronize Ticket Fields into Intercom Conversation Data Attributes using the Standalone::Zendesk::TicketFields synchronize_fields_to_intercom_conversation method. This only synchronizes Ticket Fields that the customer has specified that they want to update.


Getting the brand right – Zendesk tickets have the concept of a Brand. Intercom similarly has the concept of brands, but it is not well formed throughout the system like it is within Zendesk so we don’t attempt to map brands directly. To enable customers to branch how Fin answers or handles tickets from different brands we have a new system attribute called ‘Zendesk Brand’ which is only visible to customers using Fin Standalone. When a conversation is created for a Zendesk Ticket, we synchronize the current brand into this field.

Starting the Workflow – As mentioned in the WorkflowReference section, every Fin Standalone channel has a single workflow we run when a conversation is created. We do not use Workflow matching.
Once a conversation has been created for the Zendesk Ticket, we look up the WorkflowReference for the Standalone::Constants::IntegrationTypes::ZENDESK_TICKETS integration and manually start it using the Operator::BotFramework.notify_start_workflow method.


### # TicketSynchronizer.synchronize_zendesk_data_fields


After loading or creating the conversation and user, we always synchronize the latest data from the Zendesk User Fields and Ticket Fields to the Intercom user CDAs and conversation CvDAs. This is the only point where we synchronize Zendesk Data to Intercom. We do not try to periodically synchronize data to Intercom (nor do we want to!)

There’s two steps to this: resynchronization of the field config themselves, and writing the actual user or ticket data.

Resynchronization – We want to ensure that the actual configuration of fields from Zendesk are kept up to date in Intercom. For example, if the customer changes the options available for a dropdown field we want that update to flow into Intercom. Rather than updating the fields periodically by polling (there are no triggers we can hook in to), we instead ensure the configurations are up to date during synchronization. However, to prevent outsized API usage and slowdown to synchronization, we only update the CDA and CvDA configurations at most every 6 hours.

We use these methods to keep the CDA and CvDA config up to date:

Standalone::Zendesk::UserFields update_existing_synchronized_fields

Standalone::Zendesk::TicketFields update_existing_synchronized_fields

Writing the data – After resynchronization we write the data to the user and conversation based on the requester and the ticket respectively.

User fields in Zendesk are identified by a string key the same way we identify CDAs in Intercom. E.g. { favourite_fruit => “bananas” }. Ticket Fields are identified by a numeric ID, which is also how we do this for Intercom CvDAs: { "id" => 12345, "value" => "oranges" }.

We use these methods to write the data:

Standalone::Zendesk::UserFields synchronize_fields_to_intercom_user

Standalone::Zendesk::TicketFields synchronize_fields_to_intercom_conversation

For workspaces where no CDAs or CvDAs have been chosen to sync, this operation is a no-op.


### # TicketSynchronizer.pull_unsynced_comments_from_zendesk


The next step of ticket synchronization is to copy over comments from Zendesk. “Comments” in Zendesk refer to anything in the Ticket thread, these could be notes, user replies, admin replies . This process is  pretty straightforward:

Zendesk Tickets have the concept of comments which maps 1:1 to our concept of conversation_parts.

We pull all comments from the ticket via the Zendesk API and loop through them one by one.

‘Private’ comments are skipped. These are Zendesk’s versions of “Private Notes” and we do not need them in Intercom.

We can tell if a comment has already been synchronized by looking up the relevant ExternalReference record. Comments that have already been synchronized are skipped.

If the comment is from a user, we look up the Intercom user via the ticket.requester.id which we would have created in Intercom during the first sync.

If the comment is from a Zendesk Agent, we look up the equivalent dummy admin in Intercom.

Once the sender is determined, we create a comment in the Intercom conversation using the content from the Zendesk Comment. We write the zendesk comment id within the data object on the intercom part for reference.

Finally, we write an ExternalReference record linking the newly created Intercom comment and the Zendesk Comment it came from.

New comment synchronized into Intercom will typically cause the workflow attached to the conversation to progress to a new state. For example, the new comment may be a new user question which would cause the Fin step of the workflow to go generate a new answer.


### # TicketSynchronizer.push_conversation_to_zendesk


After pulling in the latest content from  Zendesk, we then push any unsynced content from the Intercom conversation. Typically there is either new content in the Zendesk Ticket, or new content in the Intercom Conversation – not both at the same time. Regardless, there is no guarantee of ensuring the exact ordering of comments between both systems.

The push_conversation_to_zendesk method does two main things:

copy_intercom_state_to_ticket_object – Applies relevant state to the Zendesk Ticket, e.g. resolution tags are applied, and the ticket status can be changed from new to open.

push_unsynced_comments_to_zendesk – Pushes new comments to the Zendesk Ticket.

#
TicketSynchronizer.copy_intercom_state_to_ticket_object

Knowing when to push changes – We don’t always attempt to synchronize data from Intercom to Zendesk. We only do so if we think there has been a change to the Intercom conversation that actually merits us attempting to sync state. This check occurs in the has_changes_to_push? method.
Internally this checks two things:

Has the conversation had any new parts, not just parts we might sync to Zendesk.

Has the workflow changed its current state (e.g. perhaps it has ended).


The TicketSynchronizer has a synchronization_state_record which records the necessary state from the last sync to let us know if anything has changed. This is essentially the last conversation part ID, and the workflow state timestamp. We can use this data to know whether or not we need to run the sync again given the current state of the conversation.

Why not run the sync every time? We are very sensitive to updating the Zendesk Ticket needlessly as any update to the ticket will cause Intercom’s Ticket Synchronizer to run again. We do not want to get into infinite loops.


### What state is synchronized?


Involvement – If the ticket has been processed in Intercom at all (irrespective of whether Fin has answered or not) we add the FIN_INVOLVED_TAG to the Ticket.

Resolution State – We use the AnswerBot::Private::Models::ResolutionState record for the current conversation to know what tags to apply to the Ticket. Soft resolutions and hard resolutions add the FIN_SOFT_RESOLUTION_TAG and FIN_HARD_RESOLUTION_TAG respectively.

Ticket State – If we don’t think the ticket is resolved, then we mark the ticket either with the Zendesk state “pending” when we are waiting for a user reply, or “open” in cases where Fin is likely thinking of an answer.

Assignment State – Updates to Intercom come from the ticket being assigned to the “Fin Agent” in Zendesk. If the workflow in Intercom has ended, we determine that the ticket in Zendesk should be handed over to the support team in the customer’s Zendesk workspace. We do this handover by setting the assignee_id on the Zendesk Ticket to nil, essentially letting the customer’s Zendesk assignment rules figure out where it should go now. We also apply a FIN_ROUTED_TO_TEAM_TAG at this point too.

Maintaining consistency – The Zendesk Ruby API does not do partial updates to tickets. For example, if you start with a list of tags [a,b,c] and try to add the tag “d”, the API will overwrite the tags list on the remote Ticket with [a,b,c,d]. This means that any tags, or indeed any other state, applied in the background by other Zendesk automations will be overwritten and lost.

To prevent us from overwriting data unintentionally, we make use of the safe_update field on the ticket record provided by the Zendesk Ruby API. This essentially turns the updates we make into conditional updates: for our save call to succeed, the ticket must not have been updated since we loaded it.

If we do encounter a conflict, the save! will fail with a ZendeskAPI::Error::NetworkError 409 error. We rescue these errors and renqueue a synchronization job for 10 seconds from now. Jobs may be retried up to 3 times, otherwise we will raise a Standalone::Errors::RetryLimitReached error.


### TicketSynchronizer.push_unsynced_comments_to_zendesk


Writing comments back to Zendesk is slightly more complex than pulling them in, but the general approach is the same:


### We loop through conversation parts.


If a part has been previously synced we skip it. We use the ExternalReference record to check this.

If the part is from an admin, but not from Fin, we skip it. (It is not expected to have an Admin part that didn’t originate from Zendesk and therefore would have been filtered out by the ExternalReference check)

If the part is a note, we mark the new comment in Zendesk as public: false

When we’ve successfully sent the new comment to the Ticket, create an ExternalReference record.

Batching the conversation parts – This is where the additional complexity comes from. In email conversations, a workflow may create many parts at once. e.g. it may create a few Comment type parts followed by a QuickReplyOptions part. We do not want to send a separate email for every individual part created which would happen if we naively just created comments 1:1 in Zendesk. Instead we need to batch these parts together and create a single comment in Zendesk comprised of the content of multiple Intercom parts (It’s worth stating that this is what we do when sending emails for conversations in a regular Intercom install).
Newly created comments that need to be synchronized are batched by:


### Author type (Bot/Admin/User)



### Author ID



### Is Public? (Is this a note or a comment?)


Once batched, the combined content is sent to Zendesk as a single comment.

What about the ExternalReference in this case?  External References are usually a mapping between a single record in Intercom and a single record in the third party. This batching approach means that we have a case where multiple Intercom records need to be mapped to a single Zendesk part – our uniqueness constraints don’t allow us to have an N →1 mapping (as this would mean we could open ourselves up to mistakenly creating duplicate comments and not knowing about it) so we use an ID Sequencing approach here.

In practice this means we do the following: let’s say we have three Intercom conversation parts, 1, 2, 3. We combined these parts together to create a Zendesk Comment with the ID “abc”. We create the following mappings:


### internal_id external_id 1 “abc” 2 “abc-1” 3 “abc-2”


Essentially, we append the index of the part in the batch to the external ID unless it is the first part of the batch. Keeping this first part as a direct mapping means it is still trivial to identify if a given Zendesk part has been mapped before – e.g. in the above example if I wanted to check “does the Zendesk comment with ID ‘abc’ exist in Intercom?” then it’s still a simple `exists?` call on ExternalReference.

The consistent internal ID mapping also means that if we were to rerun the synchronizer we know exactly what parts were synchronized to Zendesk regardless of whether they were part of a batch or not.


### # TicketSynchronizer.record_synchronization_state


The final step of the ticket synchronizer is to record the current synchronization state. As mentioned before, this is a record that tracks what the current last part ID and last workflow state update are for the Intercom conversation. Recording this allows us to know if any changes have been made to the conversation on the Intercom side for the next time the synchronizer is run.


### # Wrapping up: TicketSynchronizer


At this point the lock on the conversation is released, the workflow should be running in the background, or the ticket should have been handed over and to the support team in Zendesk, ending our involvement in it.


### # The Zendesk Messaging Integration


Zendesk call their messenger offering “Zendesk Messaging” so this is what we refer to it as in the product. Internally, and within all of their docs, the Zendesk Messaging technology is called “Sunshine”. They acquired this from smooch.io so this naming is likely a holdover from that period.


### # Switchboards and Integrations


A key part we need to understand about Sunshine is its Switchboards concept.

Switchboard – A switchboard is the underlying technology that controls who is in control of a given conversation at a given time. For example if Fin was answering a question, the switchboard would say Fin is in control of the conversation. If the user asks to talk to an agent, then the switchboard passes control to the Zendesk Agent Workspace.

Switchboard Integration – Switchboard integrations are the various different things that can control a conversation. We create a Switchboard Integration to represent Fin at the point the customer gives us API access. There are two default switchboard integrations: zd-answerBot (the standard Zendesk Bot flow), and the zd-agentWorkspace (the actual humans who can answer conversations via the Zendesk UI). The Sunshine API allows us to ask the switchboard to pass control of a conversation between any given switchboard integration.

Integration – An “integration” essentially maps to specific channels, e.g. Web messenger, iOS, Android. Zendesk call these “Channels” within their own UI.

Confusingly, there are “custom” integrations which are basically webhook based apps. Fin is created as one of these custom integrations in our customers Zendesk workspace, and this is what shows up in their “Conversations Integrations” settings page.

What is the difference between the Fin Integration and the Fin Switchboard Integration?

Unfortunately due to some unhinged naming conventions in Sunshine this is much less clear than it should be.

Fin Integration – This is essentially the webhook configuration. This tells Sunshine to notify our Rails app when a conversation changes, and the specific topics we care about. Fin Switchboard Integration – This is essentially a token that lets us know whether we are in control of a conversation or not.

When the Fin Integration webhook endpoint gets called in Rails, we are provided with details about the current conversation. These details include the current active switchboard integration ID which may, or may not, be Fin. All of these things combined give us the information needed to know when to actually process a conversation.


### # Connection and Setup



The Zendesk Messaging integration requires a connection to the Zendesk REST API as described in the Zendesk Tickets section. On top of that, we also need a connection to the Zendesk Conversations API. To connect to this the customer must provide three things:


### Their Sunshine App ID



### Their Conversations API Key ID



### Their Secret Key.


The customer can generate a unique set of app id / key id / secret to be used specifically by Fin from the Zendesk Admin → Integrations Settings page.


The keys provided are stored in the ZendeskSunshineIntegration model. To connect to the API we use the Sunshine Conversations Ruby gem. This gem is not hosted anywhere, you must build the gem yourself and reference it in your gemfile that way. We have copied the Sunshine repo to our own Github org (not forked, actually copied) and use our own build actions to package it up and make it available to use in the Intercom Rails app. We will need to keep this up to date in future.

On connection to the Sunshine API, we create set up the Fin Integration using  the Standalone::Zendesk::SunshineSetup module. This does several things:

Create a Fin Integration – Using the Sunshine Integrations API, we create a new custom integration to represent Fin. This Integration is given a webhook URL of https://api.intercom.io/hooks/standalone/zendesk_conversation_event and two webhook topics to subscribe to: 'conversation:create', 'conversation:message'. We also request that the webhook be provided with the full user and full source (e.g. current page)  data.

These custom Integrations are called Conversations Integrations within the Zendesk Admin UI. Our Fin integration is called Intercom Fin AI Agent.

Note the webhook ID and secret – Once the integration is created, we query the Sunshine API’s webhooks endpoint to find the webhook ID and secret for the Fin Integration. All webhook requests from Sunshine provide this token allowing us to verify its authenticity. The ID and secret of the webhook are stored on the SunshineApiIntegration record.

Create a switchboard integration – Finally, we create a switchboard integration to represent Fin so that we can take control of conversations when needed.

Creating these integrations does not change the behavior of the customer’s messenger (i.e. Fin will not start responding unless it is explicitly activated later in setup)



### # Messaging Channels


After connecting to the Conversations API, the customer must choose which channel they want Fin to work with. In Zendesk, you can have multiple brands and each brand can have its own messenger. Some customers want to run Fin only for certain brands leaving the others untouched. We use a combination of the Sunshine integrations API and the Zendesk Brands API to list the channel details here. Currently we only show web channels, but we could theoretically support Android and iOS – and possibly more.

When you select a channel via this UI and hit save we make a note of the selection and store these on the supported_integrations array on the ZendeskSunshineIntegration record for the app. You may only change the supported channels while Fin is not active to protect against the update failing midway and leaving Fin in a broken state. The save action does not change anything with the Sunshine API; the changes to the channels are actually applied when Fin is set live.


### # Testing Fin


We allow customers to test Fin before going live by running the Fin integration in “test mode”. In the test mode UI, the customer first provides a public URL where their messenger is installed. In Rails, we load the HTML for this page and scrape the customer’s Zendesk Messenger Key. This is a public identifier of their messenger, akin to our own App ID Code that you could find on any of our customer’s web pages.

With this key, we open a new window running on a new subdomain: https://standalone.intercom.com/zendesk/preview_messenger/<MESSAGING_KEY>.


On this page we load the customer’s own Zendesk Messenger for them, and set up a new conversation. We append CSP headers to our Rails controller here to allow the Zendesk Messenger to access its own APIs.

In the background when the conversation is opened, the Fin integration receives a webhook telling it that a conversation has started. It can see that the URL is standalone.intercom.com and determines that the customer wants to run in test mode. We then use the Sunshine API to ask the switchboard to pass control to Fin’s switchboard integration, and mark that conversation as being in “test mode”. The customer can then interact with Fin in the messenger without it being enabled anywhere else.


### # Activating Fin


When activating Fin for Zendesk Messenger, we loop through each of the channels the customer selected earlier and enable Fin for the channel.

Every Sunshine Channel  has the concept of a default responder. A default responder is the ID of the switchboard integration that should run when a user starts a conversation (by default this is Zendesk’s Answer Bot). During activation we use the Sunshine API to change the default responder for each selected channel to point at Fin’s switchboard integration at which point Fin will handle new conversations. Conversations that were already in progress will still be handled by whatever was in control of them beforehand.

On deactivation, we set the default responder for channels owned by Fin to be nil. This tells Zendesk to use the overall default setting for the workspace for those channels (usually Zendesk Answer Bot).


### # Receiving Events via Webhook


After connecting to the Sunshine API and setting up the Fin Integration, Intercom will start receiving webhook events for all conversations regardless of whether Fin is enabled or not.


### If Fin is not enabled, the webhook events are ignored.


If Fin is not the active switchboard integration, the webhook events are ignored.

Incoming webhooks are received in the Hooks::StandaloneController and passed to the Standalone::Zendesk::Webhooks::SunshineHandler.

#
Standalone::Zendesk::Webhooks::SunshineHandler

All webhook payloads sent to intercom have a webhook_id, this is the webhook_id we saved during initial setup. At the very start of the Sunshine Handler, we load the  ZendeskSunshineIntegration record  associated with that webhook id and then immediately validate that the webhook secret provided in the payload matches the one that have stored on the integration record.


### A missing integration record will result in a 404.


A mismatch between the provided secret and the stored secret will result in a 403.

Once the payload is verified, we check whether or not the customer is trying to run a test conversation. To be a test conversation the webhook must be:

Previously recorded the conversation_id as a test conversation
OR

Is a conversation:create event (and not a conversation:message event)


### On a URL that matches `standalone.intercom`


On one of the channels the customer had selected during setup.

If we are in test mode, then we make note of the Sunshine conversation ID in the Rails cache. Any further events for this conversation will be handled regardless of the state of the integration.

If we are not in test mode there are some further checks:

We check that the current activeSwitchboardIntegration is the Fin Switchboard Integration.

We check that the Fin has even been enabled for the Zendesk Messenger by inspecting the messenger_state field of the ZendeskApiIntegration record. This must be IntegrationStates::ENABLED for us to process the event.

Finally, if we are valid to process the conversation, we deserialize the webhook payload into SunshinePayload instances and process them.



### # Standalone::Zendesk::Webhooks::SunshinePayload


The SunshinePayload class takes the raw JSON of a sunshine webhook and deserializes into standardized objects so that they are much easier to work with in Rails. All of these objects live in the Webhooks::Sunshine subdirectory.
It has a main deserialize method which returns Sunshine::ConversationEvent objects – these events provide a standardized way for us to process each type of webhook event we receive as each must define a process method.

There are two main supported webhooks:

Sunshine::ConversationCreatedEvent – maps to the conversation:create webhook payload and is responsible for creating conversations in Intercom and starting the Intercom workflow.

Sunshine::ConversationMessageEvent – maps to the conversation:message webhook payload and is responsible for adding new messages to the Intercom conversation

Unsupported webhook topics are deserialized into a Sunshine::UnsupportedEvent object which has a no-op process method. This shouldn’t happen, but customers could theoretically update their Fin integration via the Zendesk UI to add more topics that it fires on.



### # Sunshine::ConversationCreatedEvent.process


When we process a conversation:create event, we do four main things:

Look up or create the user in Intercom based on the Sunshine User ID. User verification is handled entirely by Zendesk through their Messaging authentication. New users are linked to their Sunshine users via an ExternalReference record. We synchronize the user’s name, email, current URL, and geoip data at this point.

With the user set up, we then create a conversation using a NullInitiator. Conversations in Zendesk Messaging are created on messenger open not on the first message from the user. At this point there is no content in the conversation so a null initiator is a good fit here. New conversations in Intercom are linked to their Sunshine counterpart using an ExternalReference record.

Zendesk messaging customers can set data on a Sunshine Conversation using their SDKs. We take that data and synchronize it to the Intercom conversation based on the Data Synchronization setup the customer has chosen as described above in the Data Sync section. As with the Tickets integration, we also synchronize the current Zendesk Brand by default.

Finally, we look up the Intercom Workflow for the Sunshine conversations channel via the WorkflowReference record and invoke it on the Intercom conversation we’ve created.

At this point we will have created a conversation in Intercom and kicked off the relevant workflow – so how do the new Conversation Parts created by that workflow actually get back to the Zendesk Messenger?



### # Standalone::Zendesk::SunshineIntercomEventHandlers


Unlike the Zendesk Tickets integration where we hook into the conversation lifecycle hooks to start syncing data back to Zendesk, the Sunshine integration takes a different approach backed by subscribing to specific events we have added throughout Intercom. These event handlers are responsible for creating new parts in the Sunshine Conversation.

Speed is crucial for the messenger integration and it would not be unusual for the lifecycle hooks to run several seconds after a new comment has been written to the database and this makes the experience feel extremely sluggish. To work around this, we use ActiveSupport::Notifications to emit events exactly at the moment something has happened which we need to respond to.

All events we emit can be found in the Standalone::Events module:

Renderable Part Created – When we create a new renderable part we immediately get notified and handle sending the parts to Sunshine, and ultimately the end user.

Waiting for Team – When the AI engine has determined we need to hand over to the team, either via the quick reply being clicked or the user actually stating it in text, we use the Sunshine Switchboard API to hand the conversation over to Zendesk.

Waiting for Fin – When we’ve send a question off to Fin to think about, we receive this event and show the “Fin is typing” indicator in Zendesk.

Workflow is Finished – When the workflow attached to the conversation ends, we need to handle this. By default we hand the conversation over to the Zendesk Agent workspace.

Note: These events are only emitted and handled if the Intercom app is a standalone app, and if the current conversation has a ExternalReference record.

We set up handlers to these events in two locations:

At the very start of the Workflows engine so that we capture relevant events that occur during the execution of a workflow.


### At the start of handling a Sunshine Conversation Event.


Handlers are memoized per thread to prevent duplicate handling of a single event in cases where we try to set up the handlers multiple times.

# Converting Intercom Parts to Sunshine Parts – The SunshinePartMapper

Before sending messages to Sunshine, we need to take Intercom Renderable Parts and convert them to a format that Sunshine supports. Sunshine Messages support a lot of what Intercom we can render in an Intercom conversation, but it’s not quite a 1:1 mapping so we need to do some transformations. To map an Intercom Renderable Part to it’s sunshine equivalent we have built a Standalone::Zendesk::SunshinePartMapper. This helper takes a RenderablePart and outputs a list of SunshinePart: a helper object we created that provides us with a standard to_sunshine_api_payload method. A single Intercom RenderablePart may map to many SunshinePart based on the constraints of the Sunshine system.

Not all renderable parts are supported, we have chosen a subset that makes sense for the Standalone use case.


QuickReplyOptions – Quick replies are supported and use Sunshine’s “Reply Action” capability. When a quick reply is clicked in the Sunshine messenger, we will receive a conversation:message event in Intercom. To know the Intercom UUID of the quick reply that the user selected, we encode this in the metadata field of the message sent to Sunshine.


BotComment – Bot comments represent the standard non-LLM powered messages that can be sent via a workflow. Sunshine is quite constrained it the content that it supports so we have to do some transformations here:

Images must be sent as their own message, so blocks are chunked and a single Intercom BotComment may become multiple Sunshine Messages.

Inline links are not supported, to handle this we use the preserve_link_urls method of our RenderableContent helper in Intercom. This outputs links like An Example (example.com).

FinAnswer – Answers from Fin have the same link transformations applied as BotComment, but the main difference is that we append on the links to sources using Sunshine’s “Link Buttons” capability. This essentially places a button at the end of the message in the Zendesk Message for every source used.


AttributeCollector – We support collection of Name and Email data, and this can be set up by the customer through editing the workflow for Zendesk Messaging in Intercom. Attribute collectors map to the form message type in Sunshine. Like QuickReplyOptions, we encode the intercom conversation part data as part of the metadata on the Sunshine part. When a user fills in the field in the Zendesk Messenger we will receive a conversation:message event and can load the associated AttributeCollector in the Intercom conversation by using the conversation_part_id in the metadata.


A note on the author of these parts: Unlike Zendesk Tickets, we do not need to choose a specific agent in Zendesk for Fin to act as. The Sunshine API supports passing arbitrary names and avatars to use as the author of a part. The Zendesk messenger will group parts sent by the author.
We have a hardcoded “Fin” author at the moment – but this will likely be made configurable in the future.


Once the Intercom parts have been mapped to their Sunshine equivalents, we send them to Zendesk using our SunshineConversations helper.


### # Standalone::Zendesk::SunshineConversations


The SunshineConversations helper is a the single module in the Rails codebase where we make our Sunshine API calls. It provides us a consistent place and interface to:

create_new_parts – Sends the SunshineParts we create to the API. It also creates ExternalReference records to map the parts we create in Sunshine to their parts in Intercom.

As a single Intercom part can result in multiple Sunshine parts, we use a ID sequencing based approach here to avoid DB index conflicts. This is very similar to what we do for Zendesk Tickets but in the reverse direction – please read that section for more detailed rationale. Let’s say we have an RenderablePart with ID 123 and this maps to Zendesk Parts ‘a’, ‘b’, and ‘c’. We will create a mapping as follows:


### internal_id external_id “123” “a” “123-1” “b” “123-2” “c”


handover_to_agent – Takes the current conversation and hands it over to the zd-agentWorkspace using the Sunshine Switchboard API. Handing over to the agent workspace is what causes a Ticket to be created in Zendesk for the conversation.

handover_to_fin – Takes the current conversation and hands control to Fin. This is used by testing mode to assume control of a conversation, and it is used when the zd-agentWorkspace hands control back to Fin by the agent marking the Ticket in Zendesk as closed.

update_user_name / update_user_email – Used as part of Attribute Collection, uses the Sunshine Users API to update the user details.

start_typing_in_zendesk – Used to show a typing indicator from Fin in the conversation

stop_typing_in_zendesk – Used to hide the typing indicator from Fin.


### # Sunshine::ConversationMessageEvent.process


At this point we’ve covered how conversations get created in Intercom via the ConversationCreatedEvent and how parts created by Intercom get back to Zendesk by mapping them through the SunshinePart mapper and sending them via the Sunshine API.

Now let’s look at how we handle new incoming messages via the conversation:message webhook.

Firstly, we do some checks to ensure we should actually handle the event:

We check if the author of the message is a bot – if so we exit straight away. Usually, these events are sent to Intercom after we have created messages on behalf of Fin; we can just ignore these.

We then check if we have actually created a conversation in Intercom for the current message by looking up the ExternalReference. If no conversation reference is found, we exit – this means that Fin did not handle the conversation:create event for the current conversation (perhaps Fin was turned on after the conversation was started)

Next, we synchronize the data from the Sunshine Conversation to the Intercom Conversation using the same process described in the conversation creation event. Synchronizing on every message ensures any further workflow branching kicked off from the message will have the most up to date data.

We then check whether we have regained control of the conversation – Zendesk Messenger does not (by default) have the same concept of multiple conversations that we have in Intercom. Usually, end users just see one big thread. When a conversation is handed over to the agent in Zendesk, it creates a Ticket. If that Ticket is closed the user can continue their conversation in the messenger as if nothing has changed, this does not reopen the ticket in Zendesk, if the conversation is handed over to the agent again it creates a new ticket. What all this means is that if the Agent in Zendesk closes a ticket that Fin has handed over, Fin will regain control of the conversation the next time the user sends a message – we must then restart the workflow for this conversation otherwise no user messages will be handled.


At this point we can handle the incoming message, of which there are various different types:

Quick Replies – We can determine if the message is a quick reply by looking for the quick_reply_button_id in the message metadata. In this case, we handle the quick reply using the Conversations::QuickReply command

Admin Messages – Admins replying to the conversation via their Zendesk Ticket are supported here. We use their associated Dummy Admin in Intercom as the author in Intercom and use the ConversationsService::Mutator.add_comment method to add the new content.

Form Reply – A form reply maps to our Attribute Collectors. We identify if the incoming message is a form response by looking for type: formResponse. We can extract the required intercom conversation_part_id from the metadata on the message and then call the Conversations::CollectForm to progress the workflow with the value collected.

We then explicitly update the user data via the Sunshine API (note: only name and email supported). This ensures the data gets sent to Zendesk if the conversation is handed over.

User Message – The final case we support is a simple user comment. This is added to the Intercom conversation via the ConversationsService::Mutator.add_comment method.

Finally, we create an ExternalReference record for the intercom conversation part we have created.


### # Wrapping up: Zendesk Sunshine


At this point we’ve covered how:

Conversations get created in Intercom via the conversation:create webhook.

How we respond ASAP to events in the Intercom system by emitting and subscribing to Standalone::Events.

How Intercom conversation parts get translated to Sunshine via the SunshinePartMapper and sent to Sunshine via the SunshineAPI.

How new parts get created in Intercom via the conversation:message webhook.

The Sunshine API is has much less documentation than the Zendesk API and is less well integrated into the Zendesk system (likely because they acquired Smooch rather than built it from scratch). That being said what we have is very functional, but we should watch out for strange gotchas like needing to “regain control” of conversations.
