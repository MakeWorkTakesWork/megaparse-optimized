---
title: Untitled Document
document_type: guide
primary_topics: sales, process, demo, zendesk, salesforce, product, messaging
last_preprocessed: 2025-07-08
---


### # Executive Summary


The case hand-off between Salesforce Service Cloud and AI customer experience (CX) platforms (e.g.

Intercom Fin, Ada) is breaking down due to a few critical integration gaps. In particular, misconfigured

routing rules, context loss during bot-to-human transitions, and unreliable API handshakes are causing

support cases to fall through the cracks. We identify three root-cause hypotheses — covering assignment

logic conflicts, conversation continuity failures, and integration connectivity lapses — and propose

validation tests for each. We then outline two viable solution architectures (a native Salesforce AppExchange

package vs. an external middleware orchestrator, plus a hybrid event-driven approach) to remediate these

issues. Finally, we present a phased 6–12 month plan with resource needs, a dual-path go-to-market

(AppExchange and direct enterprise pilots), and a roadmap to ensure compliance (GDPR, HIPAA, etc.) and

position the venture for a strategic acquisition by a major CX vendor. The plan emphasizes a seamless AI-to- human handoff that preserves context and follows business rules, restoring trust in automated support


### while laying the groundwork for scale.



### 1. Problem Hypotheses & Validation Plan



### # Hypothesis



### # Why It’s Plausible



### # How to Test



### # Success Metric (Pass/



### # Fail Criteria)



### # H1: Assignment/



### # Routing Conflict



### # – Case



### # assignment rules



### # and automation



## in Salesforce are



### # misrouting or



### dropping AI-



### handled cases.



### Fin/Ada are supposed



### to follow existing case



### # assignment rules



### 1



### If rules aren’t triggered



### # or a rule conflict



### reassigns the case (e.g.



### # default owner takeover



### # on updates



### 2



### # ), the AI



### # agent never actually



### gets or keeps the case.



### This would stall the



### # bot’s involvement or



### # prematurely hand off



### # to humans



### # unexpectedly.



### .



### # Simulation: Create test



### cases that should go to



### the AI (e.g. with a specific



### # origin or keyword).



### # Monitor whether the case



### owner is correctly set to



### # the Fin/Ada queue or user.



### Update a case via API and



### # check if assignment rules



### # fire unintentionally (e.g.



### owner flips to default)



### 2



## # Also review Salesforce



### # Setup for multiple active



### # rules or triggers that



### might conflict.



### .



### Pass: 100% of test



### cases intended for AI



### are assigned to the AI



### # bot user/queue and



### # remain so until handoff.



### # No unexpected owner



### # changes on case


# updates.<br>- Fail:


### Some cases bypass the



### AI queue or get



### reassigned (owner =



### # default or human



### # queue) without proper



### # triggers.



### =



### 1



### =



### # Hypothesis



### # H2: Context &



### # Continuity Loss –



### # Conversation



### # context



### (transcripts,



### # customer info)



### isn’t preserved



### when handing off from AI to human



### agents, leading to



### # duplicate or



### # incomplete cases.



### # Why It’s Plausible



### # A smooth AI-to-human



### handoff requires



### preserving full context



### 3



### . If the bot fails to



### # attach the conversation



### transcript or uses a



### # new case instead of



### updating the existing



### one, agents might see



### an empty or duplicate



### case. Ada’s integration,



### # for example, explicitly



### # transfers conversation details into the



## # Salesforce Case



### 4



### # . Fin



### likewise promises to



### # “structure every



### # answer” with full



### # context



### 5



### # . Any gap



### here forces customers



### to repeat themselves,



### undermining CX.



### # How to Test



### # End-to-End Dry Run: Trigger



### # the AI agent on a sample



### inquiry that escalates.



### Verify the resulting



## # Salesforce case contains



### # the full chat/email


# history (e.g. in the Case Description or as attached EmailMessage


### # records) and relevant



### # customer data (contact



### link, subject, etc.). Check if



### # a single case persists



### # through the bot and



### # human stages (vs. multiple



### # case records for one



### # issue). Survey support



### agents if they needed to



### ask the customer to repeat



### # information.



### =



### 2



### =



### # Success Metric (Pass/



### # Fail Criteria)



### Pass: The case visible



### # to a human agent



### includes the AI’s



### # conversation transcript



### # and customer info, with



### # no need for the



### # customer to re-explain.



### Only one case exists per



### # customer issue (no



### # duplicate case


# sprawl).<br>- Fail:


### Important context is



### missing (empty



### # description or no chat



### log), or a new case is



### created upon handoff



### (duplicate), causing



### # agents or customers to



### # backtrack.



### # Hypothesis



### # Why It’s Plausible



### # How to Test



### # Success Metric (Pass/



### # Fail Criteria)



### # As an external app, the



### # AI agent relies on



### Pass: The integration



## # Salesforce API calls. If


# Health Check & Log Audit:


### detects lost connectivity



### # the OAuth token



### Intentionally revoke the



### # (e.g. token expiration)



### # disconnects or



## Salesforce OAuth token or



### # and alerts or retries



### # expires, the



### simulate an API error, then



### # promptly; case creation



### # integration halts



### 6



### .



### # observe Fin/Ada behavior



### # resumes after re-auth.



### # H3: Integration



### # Connectivity



### # Lapse – The



## # Salesforce–AI



### # integration



### # sometimes fails



### # (due to



### authentication,



### # API limits, or field



### mapping errors),



### causing Fin/Ada



### to stop creating



### # or updating cases.



### # Indeed, Intercom notes



### that if the token is



### manually removed or



### expired, “the



### integration will stop



## working” hitting Salesforce API



### 7



### . Similarly,



### call limits would pause



### # case sync



### 8



### # . Field



### mismatches (missing



### required fields or



### changed API names)



### can also cause case-



### # creation attempts to



### – does it log errors or



### # attempt reconnection?



### Check the integration’s



### # admin console (Intercom’s



### # or Ada’s) for error logs or



### health status flags (Intercom provides a



### # health check UI for errors



### 11



### # ). Also, review



## # Salesforce API usage logs



### during peak times to see if



### limits were hit. Field



### # Mapping Test: Temporarily



### remove or hide a



### # No sustained drop in



### # case creation rate



### during testing. Field



### # mapping issues



### # produce clear errors



### that can be caught in testing.<br>- Fail: The



### AI fails to create or



### # update cases with no



### # immediate alert (silent



### failure). Error logs show



### # authentication failures



### # or API limit errors



### coinciding with times



### silently fail



### 9



### 10



### .



## # Salesforce field the



### when cases were



### # These issues would



### integration expects (e.g.



### # dropped. Integration



### # manifest as Fin not



### Contact Email) and see if



### requires manual re-auth



### creating cases at all (as



### the case creation fails with



### # far too often (e.g. token



### # some Intercom



### # an error.



### # issues more than



### customers have



### # quarterly).



### reported).



### 2. Deep Technical Analysis



## # 2.1 Salesforce Service Cloud Integration Points


Salesforce Service Cloud provides multiple integration hooks that the AI hand-off solution must leverage or

# adjust:



Case Object & Assignment Rules: Inbound support issues (from email, web, chat) typically create a Case record. Assignment Rules then route the case to a queue or user. Fin’s design relies on this:

when a case arrives, if it matches criteria, an assignment rule can auto-assign it to the “AI agent”


### # user or queue for Fin



### 12



### 13


. This is how Fin “picks up the case” initially. Our analysis found that if

the REST API creates/updates a case without proper headers, Salesforce may still fire assignment


### # rules by default



### 14


. This can lead to unexpected re-routing – for example, when Fin updates a case

(to post an answer or close it), Salesforce might re-run assignment rules, potentially changing the

owner to a default user if no rule matches the update criteria


### 2



### . Such behavior can break the



### =



### 3



### =










intended flow (the case might leave the Fin queue mid-process). The integration must therefore carefully manage assignment rule execution, using the Sforce-Auto-Assign header or explicit


### rule control on API calls to prevent unwanted reassignments



### 14



### 2



### .


Salesforce User & Permissions: Fin or Ada will connect to Salesforce via a Connected App (OAuth),

typically under a dedicated integration user. That user needs permissions to read/write Cases, Case

Comments, Email Messages, Knowledge Articles, etc. If the OAuth token for that user is revoked or


### expires, no API calls go through



### 6



### . We discovered common admin actions (like removing an


installed package or changing the integration user’s password) can invalidate the token,


### immediately halting case sync



### 7


. Additionally, Salesforce allows only a limited number of active


### # OAuth tokens per user (usually 5)



### 15



### – if exceeded, new logins fail. A robust integration should


monitor token health and perhaps use a dedicated “API Only” user to avoid human interference.

Case Fields and Objects: The integration maps conversational data to Salesforce fields. For email- based cases, typically the incoming email becomes a Case.Description or a child EmailMessage record. Ada’s guidance, for instance, suggests putting the chat transcript into a


### # field like Case Reason or Description



### 16



### (though “Reason” is a picklist in standard SF, so a custom


text field might be used instead). Fin likely does something similar – e.g., attach the Q&A or

summary to the Case as a comment or in the Description. The Contact or Lead linkage is also

critical: the case should be associated with the correct customer record. If the customer’s email/

name isn’t passed correctly, the case may come in without a Contact, making human follow-up

harder. We must verify that Fin/Ada are populating key fields (Subject, Contact, Description, etc.) and

not violating any required-field constraints. (Intercom’s standard Salesforce app, for example,

requires certain fields like Email, LastName on Leads to exist


### 9



### – by analogy, Fin’s case integration



### might expect specific fields to be present.)


Omni-Channel / Live Agent (Chat) Integration: For real-time chat handoffs, Salesforce’s Live Agent

or Omni-Channel interface is involved. Ada’s “Glass” integration, for example, connects to Salesforce


### # Live Chat APIs



### 17



### 18


. In such cases, a Session Transfer occurs rather than creating a new case: the

bot joins a live chat session and then hands it to an agent in Salesforce. Key integration points are

the Live Agent REST API or the Messaging API for Salesforce. Any solution working with chat must

handle session IDs, agent availability, and queue selection. The failure modes here include chats not

transferring (customer stuck with bot), or transcripts not carrying over into the chat for the agent.

This requires ensuring the Live Agent “Handoff” API call (or external chat API) is invoked with all


### needed context (visitor ID, chat transcript snippet, etc.).


Platform Events & Apex Triggers: Salesforce provides an event-driven option to respond to case

changes. For instance, one could create an Apex trigger on Case insert to notify the AI service (via

callout or Platform Event) that a new case needs AI attention. Or use a Platform Event published

when a case is ready for bot handling, which external subscribers (the AI service or a middleware)

can listen to. Platform Events are designed for exactly these cross-system real-time updates

They avoid constant polling and API calls, by letting Salesforce “publish” an event (e.g. “Case Created

with Category X”) that the AI can subscribe to. Our analysis indicates this would reduce API usage

and timing issues – instead of the AI querying Salesforce repeatedly (“any new case for me?”),


## Salesforce would push a notification out immediately



### 20



### 21



### . This aligns with a more scalable


architecture, but requires building the event publishing logic in Salesforce (declaratively or via Apex)

and ensuring the external side can receive and auth to the event stream.


### =



### 4



### =



### 19



### .


In summary, the Salesforce side offers robust plumbing (assignment rules, events, APIs) but needs careful

configuration. The case assignment rules must be tuned so that cases meant for AI reliably go to the AI

agent (and stay assigned until handed off). Custom Apex or Flow logic may be needed to plug gaps — for

example, to attach transcripts, or to override assignment on case closure to avoid reopening by a rule.


### # 2.2 Intercom Fin / Ada API Workflows


Both Intercom Fin and Ada act as AI “agent” layers that sit on top of traditional ticketing systems.

Understanding their workflows clarifies where the hand-off could break:



Intercom Fin Workflow: Fin is an AI agent that connects with external helpdesks like Salesforce via


### # OAuth and APIs



### 22


. Once connected, Fin can handle cases across channels – e.g. email cases and


### chat – directly within Service Cloud



### 23


. The Fin workflow in Salesforce likely goes as follows:



Case Ingestion: A new case enters Salesforce (via email-to-case, web form, etc.) and triggers normal

assignment. If configured, an assignment rule sets the case owner to a Fin Queue or User. Fin’s

documentation confirms it “picks up the case based on your assignment rules”


### 12



### # . In practice, this


means Fin’s backend is either polling Salesforce or subscribed to events for cases assigned to it.



AI Response Generation: Fin retrieves relevant data: it will pull the case description, related

knowledge articles (it “learns all your support content from your Help Center instantly”


### 24



### # ), and the



### # conversation history if any



### 5


. Using its AI engine (likely a large language model tuned on the

knowledge base), Fin formulates an answer. This answer is then pushed into Salesforce – either as a

public reply (email sent to customer) or a comment on the case. For email cases, Fin would use

Salesforce’s EmailMessage API to send an email from the case, or possibly leverage a “Fin

Messenger” component. (The help doc mentions Fin working with “Salesforce In-App Messaging”


### # and legacy LiveAgent for chat



### 25



### .)





| Customer | Interaction | Loop: | The | Fin’s |
| --- | --- | --- | --- | --- |
| Fin can | optionally | auto-close | the case. | Fin has a feature to “auto-close if resolved when the |

### customer confirms”



### 26


– meaning if the customer indicates the answer solved their problem, Fin will

call Salesforce to set the Case Status = Closed and perhaps tag it (e.g. add a “Fin Resolved” tag). Indeed, Fin applies specific tags like fin-soft-resolution or similar to categorize resolution

outcomes (soft vs. confirmed) – these tags help in reporting


### 26



### . If the customer says the answer


didn’t help or asks for a human, Fin should then proceed to handoff.



Handoff to Human: Fin’s workflow configuration allows a “handover to your team” step


### 27



### 28



### # . At


this point, Fin needs to transition the case to a human agent seamlessly. Likely it will do one or more

of: set a Case field (like escalate flag), change the Case Owner to a human queue, and post a final

message (“Handing you over to a human agent now”). The case remains in Salesforce; the human

agent is notified via their Service Console (possibly using Omnichannel if configured for that queue).

Fin’s promise is that this happens “directly in your Service Cloud workspace”


### 1



### # , i.e., the agent just



### sees the case in their queue with the full thread.


Throughout this, Fin must adhere to “using your existing automations and reports”


### 1



### . This implies it tries


not to bypass Salesforce conventions: e.g., it will follow whatever Case Assignment Rules and email

templates exist. However, our investigation shows that if those automations aren’t designed with an AI

agent in mind, conflicts arise (as in H1). For example, a workflow might automatically close cases after 3

days of no activity – if Fin is the owner, such a rule could prematurely close an active AI conversation. Part of


### =



### 5



### =


the solution might be adjusting or disabling certain automations when Fin is involved (for instance, filtering


### # them out by owner = Fin).




Ada Integration Workflow: Ada’s platform similarly integrates with CRMs to escalate conversations.

Ada provides a no-code builder to configure handoffs. For Salesforce, Ada can create Cases and also

integrate into Salesforce Chat. The Case creation flow (from Ada’s email handoff) is roughly:



Escalation Trigger: The Ada chatbot decides a human is needed (perhaps user asked for an agent or


### the bot confidence is low).




Metadata Fetch: Ada suggests using a “Fetch Chat Metadata” step to gather the conversation


### # transcript, summary, user info into variables



### 29



### 30



### . This ensures the full context is captured in text



### # form.




Create Case via API: Ada then uses its Salesforce Action integration to Create a Case with those


### # details



### 31


. The configuration has fields for Case Subject, Description, etc., and one maps the

captured transcript into a Case field (Ada’s docs suggest using “Case Reason” or a custom field for


### # the transcript text)



### 16


. Attachments can also be passed (they mention handling file attachments via


### # a token)



### 32


. This is done via Salesforce’s REST API in the background. If successful, Salesforce


### # returns a Case ID.




Confirmation & Handoff Continuation: Ada can send an automated “standby” message to the user

like “We’re connecting you to an agent” and possibly provide the case number or reference. Ada’s

workflow ends here, handing control to Salesforce. From that point, the user and the human agent

communicate typically over email (if it was an email channel) or the agent might reach out by

whatever channel the case is configured for. One important nuance: Ada’s guide notes that “Human

Agents will need to use a different email address than the AI Agent for responding”


### 33



### # . This implies


that if the AI was using, say, support@company.com to send replies, the human should not also use

that or it could confuse the thread. In practice, this could mean the AI uses a specific alias (like

bot@company.com) and the human uses the standard support address, or vice versa. If not handled,

an email thread might route back to the bot unintentionally. This is exactly the type of detail where

integration can fail – using a single mailbox for both AI and human caused loops or missed


### # messages.


For live chat, Ada’s “Glass” integration effectively bridges the chatbot with Salesforce’s live agent. Ada

maintains the chat UI, but behind the scenes it connects via Salesforce Live Agent APIs so that when a

human takes over, the conversation in Ada’s interface is relayed to the Salesforce Console. Ada Glass was

introduced to solve “interrupted conversations and misunderstandings” during bot-to-live transitions


### 3



### # . It


ensures the customer doesn’t have to switch interfaces and the agent gets the chat history. The live agent

handoff requires configuring chat deployment IDs, org IDs, and agent skills in Salesforce


### 34



### 18



### # , essentially


pre-wiring the routing so that the right agent pool is engaged. If any of those IDs or settings are wrong, the


### handoff will fail (user might just get stuck or dropped).




Common Failure Points in Workflows: Both Fin and Ada ultimately rely on correct mapping of

conversation data to case data and a timely trigger of the handoff. We identified a few likely failure

# points:



Failure to Create Case: Fin’s early access integration had reports of not creating cases when expected

(as hinted by community posts where “FIN creates cases for each conversation, but that’s not

happening anymore…”). This could happen if Fin’s API call to Salesforce failed silently (token expired


### =



### 6



### =


or missing field causing a validation error). Ada’s case creation could similarly fail if required fields

(like Contact Email) are blank or if the SF API user lacks permission. In either case, the user’s request

may just vanish unless the platform notifies them of an error (Ada does have an “Error Fallback”


### # message configuration



### 35


, which suggests sending a message if the handoff API call fails). Fin’s

integration should have something similar (perhaps sending “Sorry, we’re unable to connect to an


### agent right now” if case creation fails).




Delay or Race Condition: If there’s a delay in the AI picking up the case, the customer might send

multiple follow-ups. Without proper handling, this could spawn multiple cases or confuse the AI. For

example, if Fin uses the first email to create the case, but the customer emails again before Fin

responds, Salesforce might attach the second email to the same case (which is good) – but Fin might

not have seen it yet or might treat it as a new query. The integration has to handle ongoing updates.

Ideally Fin should be subscribed to case updates too, not just creation, so it can react to new


### # customer replies on an open case.




Improper Closure Loop: Fin auto-closing cases is convenient, but if the customer later replies “Actually

it’s not fixed,” does a new case get made, or can the closed case reopen? Typically email-to-case can

reopen closed cases if configured, or create new. If Fin closed it with a special status (maybe “Solved by AI”), we might need a rule to reopen on customer reply. Otherwise, those follow-ups might go

nowhere. This is a corner case that needs addressing in the Salesforce config (e.g. a Case Auto-

Response rule or trigger to reopen AI-closed cases on customer reply).



Context Not Visible to Agents: Perhaps Fin answered and the customer still wasn’t satisfied. When the

agent opens the case, they should see what Fin already told the customer (to avoid repeating steps).

Fin likely logs its Q&A as an Email Message on the case or a Case Comment. If that logging fails, the

agent essentially starts from zero with the user, who then feels the agent is disconnected. Ensuring

that every AI interaction is written back to the case (via the API) is critical for continuity. Fin’s promise

that “all cases Fin is involved in are captured on Salesforce” for reporting


### 36



### suggests they do log


those answers. We should verify that these are stored perhaps as Case Comments (with a specific

marker that AI wrote it) or as part of the case description update.

In essence, the external AI platforms have to choreograph with Salesforce via API calls at key moments:

case creation, AI response, and handoff. Each API call (create, update status/owner, add comment) is a

potential point of failure if not handled exactly right. Our solution will likely introduce a transaction

manager or robust error-handling around these calls (e.g., retry logic, post-failure alerts) to ensure no


### conversation is dropped even if one call fails.



### # 2.3 Bottleneck & Failure Mapping


Bringing the above together, we map the end-to-end case flow and highlight where breakdowns occur:


### 1.


Case Originates – (Email or Chat arrives to support):


### 2.


Salesforce creates a Case (via Email-to-Case or API from Ada).


### 3.



### Assignment Rule intended to assign to AI fires.



### 4.


Failure Point: If no assignment rule matches (or it’s deactivated), the case might go to a default queue

instead of Fin. The AI never sees it, and the customer waits indefinitely for a bot response that never


### comes.



### 5.


Mitigation: Define a clear assignment rule: e.g. “If Case Origin = Email and Subject contains ‘[Fin]’ or

custom field indicates AI eligible, assign to Fin Bot User”. Ensure this rule is active and atop others.

Include a final rule entry “Do not reassign owner” to prevent default owner takeover


### 37



### .



### =



### 7



### =



### 6.



### 7.



### 8.



### 9.



### 10.



### 11.



### 12.



### 13.



### 14.



### 15.



### 16.



### 17.



### 18.



### 19.


AI Picks Up Case – (Fin/Ada receives new case notification):

Fin (for example) retrieves case details via API. It may also update the case to indicate it’s working


### # (e.g., change Status to “In Progress – AI”).


Failure Point: OAuth token issues here will prevent Fin from reading the case. Similarly, if required

fields are missing (say Contact email not on case), Fin might lack context to answer.

Mitigation: Monitor API auth. The integration should have a lightweight “heartbeat” check (e.g.,

periodic GET on a known test case) – if it fails, trigger re-auth flow or alert an admin. Also ensure the

case creation process always sets needed fields (maybe use a before-save trigger to default any


### missing info so Fin has what it needs).


AI Responds to Customer – (Fin generates answer and attempts to respond through Salesforce):

For email: Fin calls Salesforce API to send an email reply (creating an EmailMessage linked to

Case). For chat: Fin hands off the chat session or posts a message via the messaging API.

Failure Point: If the email send fails (e.g., Salesforce sending limits, or missing email address), the

customer gets nothing. Also, as noted earlier, Salesforce might re-run assignment rules on this Case

update (because sending an EmailMessage via API can trigger a case update event). This could


### reassign the case away from Fin mid-stream .



### 2


Mitigation: Use the Sforce-Auto-Assign=false header on any case update API calls from Fin to


### # suppress re-running assignment rules



### 14



### . Also ensure the From address used is correct (if the org


uses a specific support address, Fin’s message should use it to thread properly). Possibly integrate

with Salesforce’s “Einstein Bots” or Messaging framework for a more native approach (but that’s a


### # larger scope).



| Customer | Iterate |
| --- | --- |
| The reply | comes into Salesforce (as another EmailMessage on the case if email thread, or chat |
| message). | Fin should detect this and either answer again or decide to escalate if it can’t handle the |
| ### # new | query. |
| Failure | Point: Fin might not realize the conversation continued if it isn’t listening for updates. Or if the |
| case got | reassigned due to the prior step, Fin might not see the update at all. This is a “drop” |
| scenario: | the customer asks something, but Fin is no longer attending the case and no human is |
| ### # either. |  |
| Mitigation: | Maintain case ownership with Fin until it explicitly hands off. We might implement a |
| custom | field like “AI_In_Progress__c” as a flag. As long as that’s true, assignment rules or other |
| triggers | shouldn’t snag the case. Only when Fin sets “AI_In_Progress = false (handoff)” should normal |


routing resume. This acts as a latch to keep the case with Fin during multi-turn exchanges.

AI Decides to Handoff – (AI cannot resolve, triggers escalation):

Fin will update the case to mark handoff: possibly by changing the Case Owner to a human queue

(like Tier1 Support), setting Status = “New” or “Open” again, and adding an internal note “Handoff

from Fin – unresolved query about X”. Ada’s approach is similar: it creates the case and then it’s


### essentially “unattended” by the bot, awaiting human.



### =



### 8



### =



### 20.



### 21.



### 22.



### 23.



### 24.



### 25.



### 26.



### 27.



### 28.



### 29.


Failure Point: The actual transfer might not notify the human agents. E.g., if Case Owner is changed

to a Queue but no one’s subscribed to that queue or Omni-Channel not configured, the case just sits.

Or if the Status isn’t updated, some agents might overlook it in their views. Another pitfall: If Fin

forgets to update priority or category, the case might land in a general backlog instead of the urgent

channel it needs (especially if the user was already frustrated).

Mitigation: As part of handoff, have the integration set a clear signal on the case: e.g. Status =

“Escalated to Human”, Priority = High (if user is upset or it’s a VIP – the AI could determine this from

sentiment or business rules). Also, send a notification – possibly an automated @ mention or email

to the support team alias – indicating an AI handoff occurred. In Salesforce, an Apex trigger could

detect “if Owner changed from FinQueue to SupportQueue, then post a Chatter @mention to

SupportManagers” etc., or simply rely on Omni-Channel routing alerts if configured.

Human Agent Takes Over – (Agent opens case and reviews history):

The agent sees the conversation thread in the Case’s email feed or chat transcript, including everything Fin already said. The agent then continues the communication with the customer (either


### in the same email thread or chat session).


Failure Point: If the agent cannot see what Fin did (due to missing transcript or not having access to

Fin’s knowledge base context), they might repeat questions or give an inconsistent answer. Also, if

any part of Fin’s answer was incorrect or against policy, the agent needs to know to correct it


### proactively. Without visibility, that’s impossible.


Mitigation: Ensure 100% of AI interactions are logged on the case. For email, every Fin reply is

already an EmailMessage on the case. For chat, Fin’s messages should appear in the chat transcript

that the agent can read (likely accomplished via Ada Glass or Intercom’s Messenger integration).

Additionally, consider a “Summary” field: Fin could post a private comment like “AI Summary:


| Customer | Fin | Article | Customer |
| --- | --- | --- | --- |
| escalating.” | This gives | the agent | a quick brief. Such a summary could even be put in a custom Case |
| ### # field | or the | Description | for easy reference |

### 38



### . Modern AI like Fin can generate conversation


summaries easily, and indeed Fin’s workflow builder lists “Summarize the conversation with AI” as an


### # option



### 27


. Utilizing that would speed up agent ramp-up in the ticket.

Post-Handoff Resolution & Reporting – (Case eventually closed by human, data recorded):

The case is solved by the agent and closed. Management might want to report on AI vs human performance. If Fin added tags (like fin_deflected , fin_escalated ) or used a field to mark

resolution type, we can report how many cases Fin fully solved vs. handed off. Fin’s own dashboard


### provides “routed to team rate” and “AI resolution rate”



### 39



### 40



### using the data logged.


Failure Point: Without consistent tagging or status codes, we can’t measure success. Also, if the agent

doesn’t follow the process (e.g., forgets to close the case or remove the AI flag), it may skew data or


### leave cases hanging open.


Mitigation: Implement automation to enforce data consistency. For example, if an agent closes a case

that Fin touched, ensure a “Resolution Type” field is set to either “Resolved by AI”, “Resolved by

Human (AI assist)”, or “Resolved by Human (no AI)” as appropriate. This can be done via a required

field in the closing process or a trigger that checks tags. These data will not only aid acquisition

discussions (proving the value of the AI integration) but also help identify any remaining failure

patterns (e.g., if “AI escalate” cases have a longer handle time, etc.).


### =



### 9



### =


In mapping these steps, the key bottleneck emerges around steps 2–4: the handoff logic in the middle

(between AI and Salesforce) is brittle. Routing rules misfire, causing ownership ping-pong; the API

integration can drop or duplicate messages; and error handling is insufficient. Therefore, our solution will

squarely target that middle layer – either by reinforcing it within Salesforce (managed package with robust

triggers/flows) or by externalizing it (middleware that coordinates between Salesforce and the AI, ensuring


### each step succeeds before moving on).



### 3. Solution Architectures


We propose and evaluate three architecture approaches to solve the integration breakdown, each with

# distinct implementation strategies:


### # A. Managed Package Fix (Native AppExchange Package)


Overview: Build a Salesforce managed package that installs into Service Cloud, providing custom objects,

Apex classes, and Lightning components to streamline the AI handoff. This package acts as an intermediary

within Salesforce: catching new cases, invoking the AI, and orchestrating the handoff all inside the

Salesforce environment. It would be listed on AppExchange for easy deployment. Key features of this

# approach:



In-App Case Router: Use Apex Triggers or Flows on Case creation to detect which cases should go to

AI (based on configurable criteria: e.g., Case Topic, Customer Tier, or a checkbox “Handle by AI”).

Instead of relying solely on standard Assignment Rules, the package could provide a custom routing

logic to assign the case to a placeholder “AI Holding” queue and signal the external AI via a Platform

Event. This eliminates misfires from Assignment Rules (we essentially bypass or augment them with



our logic). Platform Event Bridge: Define a custom Platform Event AI_Case_Request__e (published when a case needs an AI response) and AI_Case_Response__e (for AI to respond back). Salesforce can

publish an event with case details as soon as a case qualifies for AI. The external AI (Fin/Ada) subscribes to AI_Case_Request__e in real-time, processes the query, then publishes an AI_Case_Response__e with the answer or a flag to escalate. The managed package includes an Apex trigger that listens for AI_Case_Response__e and updates the case (posting the AI answer

into the case feed, or reassigning ownership to a human queue if escalated). This design is fully

event-driven and decouples the systems; no polling is needed and the context is carried in the

event payload (case Id, question, relevant article IDs, etc.). Salesforce Ben describes that Platform

# Events support exactly this kind of real-time Salesforce-to-external communication


### 19



### .




Lightning Component for Agent View: The package can include a Lightning component for the

Salesforce Console that displays AI context. For example, if an agent opens a case that was handled

by Fin, a side panel could show “AI Interaction Summary” – listing what Fin answered, confidence

scores, etc. This is mostly a value-add to improve agent experience and was a common ask in early

AI integrations (agents want to know what the bot did before they stepped in). We could also allow

agents to trigger the AI on-demand via a Quick Action (e.g., “Get AI Suggestion” button, which uses

Fin to draft an answer for the agent to review). This keeps humans in control but leverages AI where


### needed, making the product more attractive.




Pros: Everything stays within Salesforce’s security and UI – data residency is ensured (customer data

isn’t stored outside Salesforce except transiently in the AI service), and admins can configure it with

clicks (assignment criteria, etc.). AppExchange distribution gives credibility and easier installation for


### ==



### 10



### ==


customers. Also, being in-org allows using Salesforce’s robust logging and permission system to


### # monitor the integration.




Cons: Development complexity is high – requires advanced Salesforce development (Apex, LWC,

packaging). We must pass Salesforce Security Review, which takes ~4-6 weeks


### 41



### # and demands


thorough remediation of any security issues. Another challenge: each AI vendor (Fin, Ada, etc.) may

require different API handling – the package might need to handle multiple AI providers or we

maintain separate package versions. Inflexibility could be an issue: any update to logic requires

package upgrade. Also, heavy use of Apex and events will count against org limits (but those are


### high-volume platform events if properly licensed).



### # B. Middleware Orchestrator (External Cloud Service)


Overview: Develop an external integration service (middleware) that sits between Salesforce and the AI

platforms. Think of it as a “case traffic controller” running on a cloud platform (e.g. AWS, GCP, Heroku)

that uses APIs to communicate with both sides. It offloads the logic from Salesforce into an independent

# app. Key elements:



Streaming Listener & API Client: The orchestrator uses Salesforce’s Streaming API (CometD) or the newer Pub/Sub API to subscribe to Case events. For instance, it can subscribe to Case object

creation events or a custom Platform Event (similar to approach A, but the event consumption

happens in the external service). When it gets a signal of a new case for AI, it calls the respective AI’s

API. For Intercom Fin, since a direct API was not publicly available yet (Fin’s “API integration” is in


### closed beta



### 42


), the middleware might instead use browser automation or a pseudo-user to

interface with Fin… but this is not ideal. More likely, we’d partner with Intercom’s APIs or use their

official integration endpoints (perhaps the middleware triggers Fin via an Intercom endpoint or

GraphQL). Ada, on the other hand, has a REST API and OAuth that could be used to create cases or

send messages – but Ada mostly expects to initiate the handoff from its side. So, our middleware

might primarily be useful for Fin, or for other AI bots that have APIs.



Unified Case Handoff Logic: The middleware can implement the business rules in one place: e.g., “If

case is from VIP customer, bypass Fin and assign human immediately” or “If Fin’s confidence < 50%

on first reply, auto-escalate without waiting for customer ask.” These kinds of intelligent routing

decisions could be layered on top of Fin/Ada’s capabilities. Essentially, the service could become an

AI Orchestration Engine that uses not just one AI but potentially multiple: (for example, try Fin first,

but if Fin can’t answer, try a secondary knowledge base, etc., before going to a human). This goes

beyond the immediate scope but is a selling point for scalability.



Audit & Logging: As a standalone app, we can maintain detailed logs of every interaction (API

request/response) in our own database. This is useful for debugging when something goes wrong

(whereas in Approach A, we’d rely on Salesforce debug logs or Intercom logs which are harder for

end-users to parse). We can also build an admin UI in this middleware to show integration health,

recent handoffs, etc., which could be accessed by the support ops teams.



Pros: High flexibility in development tech stack (we can use Python/Node/Java, integrate with

multiple APIs easily). We are not constrained by Salesforce governor limits, so complex processing or

retries can be done freely. Deployment updates are in our control (no need for customer to upgrade

a package). This could scale to integrate not just Salesforce<->Intercom, but potentially Salesforce<-

>(any AI CX platform) and even extend to Zendesk or others, making it a broader SaaS offering. Also,

by owning the middleware, we have more control for implementing advanced features like caching

knowledge, or even injecting other AI (our own LLM) if Fin fails.


### ==



### 11



### ==




Cons: Requires robust security and compliance since it will handle possibly sensitive case data

outside of Salesforce. We must ensure encryption in transit and at rest, and likely get certifications

(SOC 2, etc.) sooner or later to reassure enterprise clients. Additionally, customers might be hesitant

to put an extra link in their support chain – any downtime in our service could disrupt their case flow.

We need high availability engineering (with monitoring, failover strategies). From a business

perspective, an external service means a separate login and management, which some Salesforce-

centric admins may resist; it might be seen as more complex than an AppExchange app. Finally,

convincing Salesforce-focused buyers might be easier with an AppExchange badge than a

standalone SaaS – although we can mitigate this by eventually pursuing Salesforce ISV partnership


### for credibility, even if the core is external.


# C. Native Enhancement via Platform Events (Hybrid Approach)

Overview: This approach is somewhat a blend: utilize Salesforce native event-driven mechanisms and

minimal external code, leveraging more of Salesforce’s own capabilities like Flow and Einstein Platform

Services. The idea is to reduce reliance on heavy packages or constant API polling, using out-of-the-box

# integration where possible:



Salesforce Flow Orchestration: We can create a Flow (or Apex) that, when a case is created,

publishes a Platform Event (as in Approach A). Instead of an external service subscribing directly, we

might use something like MuleSoft Anypoint or Salesforce’s own Integration Services to

subscribe and call Fin/Ada. (Salesforce might prefer you use MuleSoft, but that could be overkill/

expensive for clients; however, for a customer already owning it, it’s an option). Alternatively, use a Heroku worker subscribed to events (blurring into Approach B). The key difference here is we try to

# utilize Platform Events for real-time and maybe Salesforce External Services or Named

Credentials to call the Fin/Ada API from within Salesforce. Salesforce can make outbound REST calls,

so conceivably an invocable Apex action could call Intercom’s API directly. If Fin exposes a REST endpoint like POST /finAnswer with question and context, we could hit that from Salesforce. This

would keep the integration logic mostly in Salesforce, but avoid storing state externally.



Platform Event for Handoff to Agent: On the flip side, we can have Fin (or our minimal

middleware) publish a handoff event that Salesforce listens to, which triggers a Flow to assign the

case to a human. This way, even if Fin can’t directly reassign owners via API, the event listener can do

it internally with full Salesforce context. For example, Fin’s system could make a single call to an API endpoint we host that simply publishes AI_Case_Escalate__e with CaseId – Salesforce receives

that and a Flow changes the owner and notifies agent. This is a cleaner separation of concerns.



Leverage Salesforce Einstein if needed: Since Salesforce is heavily pushing its own AI (Einstein,


### # Agentforce



### 43


), our solution could optionally integrate Einstein for backup. For instance, if Fin fails

to answer, maybe an Einstein Article recommendation or next-best action could be triggered to assist

the human agent. While not core to solving the integration gap, this demonstrates forward-looking

design and could make us attractive to Salesforce (for acquisition) since we complement their AI


### ecosystem rather than solely relying on third-party.




Pros: Event-driven architecture is scalable and decoupled, reducing errors from missed signals or

race conditions. Using mostly declarative tools (Flow) can simplify maintenance for customers and

avoid too much custom code. Also, platform events can handle high volumes (with the High Volume

Events edition, millions of events per day) which is future-proof for scaling. This approach also

inherently solves the polling problem and reduces API calls (Salesforce is broadcasting changes


### # instead of the AI polling repeatedly)



### 20



### 21



### .



### ==



### 12



### ==




Cons: Still requires writing some Apex/Flow to glue things, and understanding event order nuances.

Relying on event delivery means we must build idempotency (e.g., if two events fire or an event is

out-of-order, handle gracefully). Debugging across systems can be tricky. Additionally, this doesn’t

eliminate the need for an external component entirely – Fin/Ada need to consume events and

produce responses. If those platforms don’t natively support Salesforce events, we’ll have to

implement a subscriber (which is basically a small middleware anyway). So this might reduce the

amount of code but not completely remove external pieces. Also, if customers are not on

Performance/Unlimited editions, some event or API capabilities may be limited.

To aid comparison, here is a summary of Pros & Cons of the main two paths (Managed Package vs.

Middleware), with the Platform Events hybrid considered as a technique that can apply to both:


### # Approach



### # Pros



### # Cons



### Native UX & Security: Runs entirely



### # A. Managed



### # Package



### # (Native SF App)


in Salesforce; data stays in org, leveraging built-in security model.

# <br>- AppExchange Trust:


### Customers can install via



### # AppExchange, after rigorous security



### # review (a plus for enterprise



### # credibility). <br>- Low external



### # dependencies: No additional servers



### to maintain; works offline from



## Salesforce’s perspective (no internet



### dependency except to call AI APIs).



### # <br>- Deep Integration: Can use



## Salesforce features (Omni-Channel,



### # Knowledge, Flows) to enhance AI



### Development Complexity: Requires



## # Salesforce-specific expertise (Apex, LWC)



### and navigating governor limits. <br>-



### # Release Cycle: Updating managed



### packages is slower; bug fixes require



### package version upgrades by clients. <br>-



### # Initial Overhead: Security review (4–6+



### # weeks)



### 41



## # and Salesforce ISV registration



### needed before launch. <br>- Limited



## Cross-Platform: Designed for Salesforce-



### first; harder to extend to other CRMs



### # without separate builds.



### # handoff in ways external apps might



### not easily do.



### ==



### 13



### ==



### # Approach



### # Pros



### # Cons



### Data Residency/Compliance: Customer



### Flexible & Agile: Can iterate rapidly



## data leaves Salesforce; need strong



### # in a modern tech stack (Node/Python/



### # encryption, GDPR compliance, possible



### # etc.), integrate with multiple AI



### # data center localization (EU, US, etc.) to



### providers in one codebase. <br>- Rich



### satisfy enterprise policies. <br>- Uptime



## Processing: Unlimited control over



### Responsibility: We must maintain 24/7



### # B. Middleware



### # Orchestrator



### # (External



### # Service)



### # retries, logging, and complex logic



### (no SF limits). <br>- Multi-Platform



### Potential: Could evolve to support



### Zendesk, ServiceNow, etc., expanding



### # market and acquisition appeal



### # high availability; any outage or slowness



### directly impacts customers’ support


# operations. <br>- Integration Overhead:


### Requires setup of Connected App, OAuth,



### # and trust from SF org to our service; some



## beyond just Salesforce. <br>-



### clients may prefer an in-house app over a



### # Independent Scaling: Scales on



## third-party server in the loop. <br>- Sales


cloud infrastructure; can handle spikes better by queuing, etc.,

Motion: Slightly harder sell to Salesforce- centric buyers; might need more effort to


### without impacting SF performance.



### # demonstrate security and ROI vs. an



### # AppExchange native solution.


Recommendation: We can actually combine the strengths of these approaches by delivering a

lightweight managed package that handles Salesforce-specific pieces (UI components, event publishing,

custom fields for AI status) while the heavy lifting (AI calls, routing brain) lives in the middleware. This way,

the package serves as a connector (and gives us AppExchange presence), and the cloud service does the

sophisticated orchestration. Many Salesforce ISVs use this hybrid model (managed package + cloud service)

to balance security with flexibility. We should, in the next phase, decide on the exact division of labor

between package and cloud, but a likely split: Salesforce package for event triggers and UI; cloud for AI

communication and decisioning. This also positions us well to be acquired either by a Salesforce (they could

absorb the package and connect it to Einstein) or by an AI vendor (who might utilize the cloud hub to plug


## # into Salesforce and other systems).



### 4. 6‑to‑12‑Month Roadmap


A phased roadmap is outlined below, assuming we start in Month 0. It covers the investigation, build,

testing, and go-to-market preparation. This timeline is aggressive but feasible with a lean team, focusing

first on an MVP integration fix, then iterating towards a full AppExchange launch by year’s end.


### ==



### 14



### ==



### # Month



### 0-1



### 2



### 3-4



### # Milestone &



### # Focus



### # Deep Discovery



### # & Design



### # <br>(Weeks



### 1-4)<br>-



### # Research &



### # Hypothesis



### # Validation



### # Prototype



### # Development



### # (Spike)



### # <br>(Weeks



### 5-8)<br>- Build



## # small PoC for



### # critical path



### # MVP Build –



### # Core



### # Integration



### # <br>(Weeks



### 9-16)<br>-



### Develop the



### # Minimum Viable



## # Product focusing



### on fixing the



### # handoff loop



### # Owner



### # (Primary



### # Responsible)



### # Founder/



### # Architect



### # (Intercom AE



### # as PM) +



## # Salesforce



### # Consultant



## # Salesforce



### # Developer +



### # Backend



### # Engineer



### # Backend/API



### # Engineer



### # (lead), SF



### Developer,



### # Part-time SF



### # Admin for



### # config



### # Key Deliverables & Metrics



### # – Conduct stakeholder interviews (incl. ex-Intercom



### engineers, pilot customers) to validate the three



### hypotheses in real scenarios. <br>– Detailed technical



### design document covering data flow diagrams, object



### models, and API touchpoints. <br>– Decision on core



### architecture (Package vs Middleware or hybrid) based



### on discovery (include a risk analysis). <br>– Initial



### product requirements and user stories drafted (e.g.



### “As a support manager, I want AI-resolved cases auto-



### closed with proper tags”).


– Salesforce Dev Org setup with dummy Service Cloud and a trial Intercom Fin or Ada instance for


### testing. <br>– Basic prototype that creates a case via



### API and receives an AI answer: for example, a script



### that simulates Fin’s behavior on a new case (since Fin



### API might not be open, use a mock LLM service).



### <br>– Validate connectivity: demonstrate an OAuth



### flow working, a Platform Event subscription working



### externally, and a case being updated via API from



### # external service. <br>– Internal demo of the prototype



### solving a sample case end-to-end (with logs).



### # <br>(Success = confirmation that our approach can



### # technically work, and identification of any showstoppers



### # early.)



### # – Case Routing Engine implemented: e.g., an Apex



### trigger or Flow that publishes an event or calls out to


assign case to AI. <br>– Middleware Service (if used):


## Set up cloud functions to handle event ingestion and



### call AI API (use Fin’s API if available or a placeholder).



### # <br>– Bi-directional Communication: The AI’s



### response (real or mock) comes back and updates the



### Case (adds comment/reply, reassigns owner if



### needed). <br>– Basic error handling and logging in


# place: e.g., retry logic if API call fails, and a status field


### on Case (like “AI_Status__c” with values “Pending AI”,



### “AI Completed”, “Escalated”). <br>– Unit tests in Apex



### # (for triggers) and integration test scripts for the



### # service. <br>– Internal Alpha release: Use test cases



### to ensure an AI response or a controlled handoff flows



### # through. Confirm no infinite loops or ownership



### # thrash.



### ==



### 15



### ==



### # Month



### 5



### 6-7



### # Milestone &



### # Focus



### # Pilot with



### # Friendly User(s)



### # <br>(Weeks



### 17-20)<br>-



### # Iterate with real-



### # world input



## # Product



### # Refinement &



### # Hardening



### # <br>(Weeks



### 21-28)<br>-



### # Incorporate



### feedback,



### # expand features



### # Owner



### # (Primary



### # Responsible)



### # PM/Founder +



### # Solutions



### # Engineer, Pilot



### # Customer



### # Admin



### UX Designer,



### SF Dev,



### Backend Dev,



### # QA Engineer



### # Key Deliverables & Metrics



### # – Identify 1-2 pilot customers (mid-market companies



### open to trying the solution on sandbox orgs). Possibly



### the user (AE) can leverage past contacts. <br>– Deploy



### MVP to pilot sandbox: Configure it for their org



### (assignment rules or criteria, connect their Fin/Ada).



### <br>– Collect pilot feedback on: Does AI pick up cases



### reliably? Are agents getting context? Any breakdown



### observed? <br>– Fix high-priority issues on the fly



### (Month 5 will include rapid patch releases to pilots).



### # <br>– Success criteria: e.g., a target that Fin/Ada



### # handles at least 50% of applicable cases in pilot


without human intervention, and hand-offs occur within SLA (say <30 seconds delay). Metrics gathered


### and analyzed.



### – UX improvements: Build the Lightning component



### for agent view (if decided), polish any pilot UX pain



### (like unclear status labels, etc.). Possibly design a



## simple dashboard in Salesforce for admins to see AI vs



### # human metrics. <br>– Performance tuning: Ensure



### the event handling and API calls are non-blocking (use



### # asynchronous processing where possible). Test with



### volume (simulate hundreds of cases). <br>– Security



### # & Compliance checks: Conduct an internal security



### review of code (Apex scan using Checkmarx,



### # penetration test of the middleware API). Address any



### data privacy concerns (e.g., ensure we’re not storing



### PII unnecessarily in logs). <br>– Expand integration to



### cover edge cases found in pilot: e.g., if pilot needs



### support for attachments or multi-lingual content,



### # address those. <br>– By end of Month 7, codebase



### should be Beta-ready for broader use, and



### documentation drafted (admin guide, setup



### # instructions).



### ==



### 16



### ==



### # Month



### 8



### 9



### # Milestone &



### # Focus



### # AppExchange



### # Prep & ISV



### # Review



### # <br>(Weeks



### 29-32)<br>-



### # Formalize



### # packaging and



### begin security



### # review



### # GTM Plan



### # Finalization



### # <br>(Weeks



### 33-36)<br>-



## # Marketing, Sales



### # prep pre-launch



### # Owner



### # (Primary



### # Responsible)



### # SF Developer



### # (Package



### Lead),



### # Founder/PM



### # Marketing



### # Lead



### # (contractor or



### founder),



## # Sales Advisor



### # Key Deliverables & Metrics



## # – Package creation: Convert the Salesforce



### # components into a Managed Package (namespace



### registration, packaging org setup). <br>– Thorough



### QA in a fresh test org by installing the package and



### connecting to the cloud service – ensure nothing is



### # environment-specific. <br>– Prepare Security Review



### documentation: architecture diagrams, data flow,



## # responses to Salesforce’s security questionnaire



### (covering how we handle authentication, encryption,



## # etc.). <br>– Submit package for Salesforce Security



### Review around week 32. (Expect ~4-6 weeks


. <br>– Meanwhile, set up required turnaround) legal agreements: join Salesforce Partner Program,


### 41



### ensure we have a Business Org for the AppExchange



### # listing.



### # – Create product name, branding, and an



### # AppExchange listing draft (copy, screenshots from



### pilot usage, value prop statements). <br>– Website



### and collateral: launch a landing page describing the



### solution and capturing leads. Include a whitepaper or



### case study from pilot if possible. <br>– Pricing strategy



### determined: e.g., per-case or per-user pricing, or



### # value-based (maybe a flat enterprise license). For



### initial GTM, maybe keep it simple (free pilot, then



## subscription). <br>– Reach out to press or Salesforce



### # AppExchange marketing channels for potential



## # feature (perhaps a blog on SalesforceBen or similar



### about AI handoff solutions, to build awareness). <br>–



### # Identify target companies (mid-market SaaS



### companies, etc.) and start warming up contacts for



### # post-launch demos.



### ==



### 17



### ==



### # Month



### # Milestone &



### # Focus



### # Owner



### # (Primary



### # Responsible)



### # Key Deliverables & Metrics



### – Assuming Security Review feedback is returned by



### # now: address any required fixes or clarifications. (If



### issues are minor, we can get approval by end of Month



### 10. If major issues, might extend into Month 11.)



### <br>– Beta launch: Open up the product to a few



### # Beta Launch &



### Founder/PM,



### # more customers beyond the pilot (perhaps via a



### # AppExchange



### # Customer



### private listing or just by providing package and service



### 10



### # Security Result



### # Success (early



### access). Provide high-touch support to ensure



### # <br>(Weeks



### # hire or



### # successful integration. <br>– Begin formal training



### 37-40)



### # founder)



### materials: user guides for support agents and admins,



### # maybe short video tutorials on setup and how the AI


handoff works. <br>– Start collecting testimonials or quantified results from pilot/beta (e.g., “reduced


### human case load by X%”). These will feed GTM



### # materials.



### # – AppExchange Listing Go-Live (target around month



### 11 if security review passed): The app becomes



### publicly available. Coordinate a marketing push with



## this: e.g., a blog post on Salesforce AppExchange blog,



### a webinar showcasing the integration (perhaps co-



## hosted with a pilot customer or with a Salesforce AE



## who sees value). <br>– Sales outreach: Leverage



### Intercom/Fin networks – since the AE has connections,



### reach out to companies who struggled with Fin or Ada



### integration and offer our solution. Also engage



### 11-12



### # Public Launch &



### # Growth



### # <br>(Weeks



### 41-52)



### Founder/CEO,



## # Sales &



### # Partnerships



### # Lead



## Salesforce solution engineers who might refer clients



### needing better bot integration. <br>– OEM/Tech



### # Partnerships: By month 12, initiate talks with



### # potential partners: e.g., Intercom product team (pitch



### that our integration could be an official add-on for



## Fin), or Salesforce (if they have interest in improving AI



### handoff, position our metrics). Possibly also approach



### # other AI CX vendors like Ada or Forethought to



### support their platform in our integration hub –



### broadening commercial opportunities. <br>– KPI



### tracking: set targets such as: 5 customer orgs



### deployed by end of year, >90% AI handoff success rate



### # in those orgs, and a pipeline of prospects for next



### # year. Use these to measure success and guide



### whether to pursue further funding or strategic sale.


This roadmap anticipates a fairly quick timeline to MVP (roughly 4 months) to start proving value, and a

polished product by 6-8 months, with commercialization in months 9-12. It aligns with the goal of being


### ==



### 18



### ==


acquisition-ready in about a year: by then we aim to have real customers, an AppExchange presence, and

data demonstrating that we solved the hand-off breakdown problem.


### 5. GTM & Commercial Paths


To turn this technical solution into a viable venture, we’ll pursue a multi-pronged Go-To-Market strategy,

tailored to enterprise CX technology buyers:



AppExchange Launch Strategy: Achieving AppExchange listing is central to our credibility. We will

list the solution in the Service Cloud category, emphasizing “Seamless AI Agent Handoff for Service

Cloud” as the key value. The listing should highlight compatibility with Intercom Fin, Ada, and

potentially other AI bots – capturing searches for those terms. Salesforce’s AppExchange marketing

programs (like AppExchange Demo Jam, etc.) can give visibility. We’ll use AppExchange’s PRU (Partner

Referral Unit) leads if available, and ensure we gather and display a couple of 5-star customer

reviews early (perhaps from pilot users). Given that AppExchange deals often involve Salesforce AEs,

we will network within Salesforce – for example, with Service Cloud specialists – so that when their

customers ask about chatbot integrations, they point them to our app.



Direct-Sale Pilot Path: In parallel, we’ll do direct sales/pilots especially where AppExchange process

might be slow. The mid-market/enterprise support leaders are our targets – likely VPs of Customer

Support or Support Operations managers who have implemented AI bots. We’ll approach companies

known to use Intercom Fin or Ada (or similar like Zendesk Answer Bot, Salesforce Einstein Bot) and

who also use Salesforce (many do). The value pitch: “Reduce AI integration headaches and rescue

dropped cases – our tool ensures your AI and Salesforce work in lockstep, with full context and

compliance.” We can offer a free 30-day pilot in their sandbox to prove the value. For direct sales, we

need to be prepared to handle objections about data security – we’ll have documentation ready on

our architecture and possibly be willing to sign a NDA/DPAs for pilot. If pilots succeed, converting to

paid contracts (annual SaaS license or subscription) will follow. These direct wins not only bring

revenue but also validate product-market fit and create champions who can reference us.



OEM / Strategic Partnership Path: We keep open the avenue that a larger player might want to

incorporate our solution. There are two likely angles:



CX Platform Vendors: Intercom itself might realize that instead of building deep Salesforce

integration fixes in-house, partnering or acquiring us is faster. Ada or other chatbot companies could

similarly see us as a way to instantly improve their Salesforce story. Our plan is to remain vendor-

agnostic enough to be appealing to multiple parties, but if one shows strong interest (say Intercom

wants exclusivity), we evaluate that strategically. Early on, we can engage with Intercom’s

partnership team (leveraging the user’s insider knowledge and contacts) to show what we’re doing.

If they see we’re enhancing Fin adoption for Salesforce customers, they might support or co-market


### rather than compete.




Salesforce and AppExchange Partners: Salesforce might consider our functionality as a gap filler


### # until their native Agentforce matures



### 44



### . Being on the AppExchange and demonstrating success


with Service Cloud could make us an acquisition target for Salesforce (especially if we integrate

multiple third-party AI – it gives Salesforce an “agnostic” solution for customers using non-Einstein

AI). We should also connect with Salesforce’s ISV partner managers to explore co-selling

opportunities: Salesforce sales teams will be more likely to introduce us if it helps them close Service


### ==



### 19



### ==


Cloud deals (for example, if a customer is concerned that adopting Fin means leaving Salesforce UI,

we provide a remedy, helping the Salesforce AE keep the account).



OEM Model: As an alternative to outright acquisition, a larger company might OEM our solution –

e.g., include it as part of their product offering. For instance, Ada could bundle our connector with

their enterprise package, paying us a licensing fee. This could significantly expand reach with

minimal sales effort on our side. Thus, we’ll design our licensing such that it’s possible to do an OEM

# deal (e.g., modular architecture, white-label capability).



Marketing & Thought Leadership: We will produce content that addresses the pain we solve – e.g.,

blog posts or webinars on “Best Practices for AI-to-Human Handoff in Customer Support” featuring

our solution. Citing industry stats (like Gartner numbers on AI in support) and our pilot results will

build credibility. This content serves both to educate the market and gently promote our product.

# Posting on communities (Salesforce Trailblazer, Intercom Community, Reddit r/salesforce) with

helpful insights (not just ads) will also get the attention of practitioners who experienced these


### # integration issues.




Target Customer Profile: We focus on mid-market and enterprise Service Cloud customers (200+

agent orgs, likely). These teams have volume where AI assistance matters, and complexity where

integration issues are felt painfully. Within those companies, we target Support Operations or CRM

admins who are tasked with making Salesforce talk to their AI tools – these individuals directly feel

the frustration of broken handoffs and will be our internal champions. For enterprise deals, also

involve the IT integration team and Compliance officers early to navigate security approval (we’ll

# arm ourselves with documentation and possibly a security assessment ready).



Pricing Strategy: For initial pilots, free or deeply discounted to get in the door. Long term, a

subscription model likely based on number of AI-assisted cases or agents. For example, if a

company has 100 agents and Fin is deflecting 1000 cases/month, the value is high – pricing could be

$X per month per 1000 AI-handled cases or $Y per agent seat (though per-case aligns value better).

We should also consider aligning pricing with the AI vendor’s pricing (Intercom charges $0.99 per


### # resolution



### 45


; if we ensure those resolutions happen smoothly, we might price at, say, $0.20 per AI

resolution as a facilitation fee). However, we’ll remain flexible and in early deals likely do custom

quotes until a standard emerges. The goal is to show ROI: if our solution prevents, say, 50 dropped

handoffs a month, that might save many hours of agent time and some customer churn – easily


### justifying a few thousand dollars a month in large orgs.


In summary, our GTM has a dual focus: leveraging the Salesforce ecosystem (AppExchange, ISV

channels) to gain trust and scale, and direct solution selling to companies suffering the AI-SF integration

pain. This dual approach maximizes early traction. As we grow, we will decide whether to remain a stand-

alone integration provider or to align closely with a bigger platform for acquisition; our strategy keeps both

paths open, ensuring we build value either as an independent business or as an attractive tech acquisition.


### 6. Resource & Budget Matrix


Delivering this plan will require a nimble team with a mix of Salesforce-specific skills and general integration

expertise, plus some supporting roles for business and compliance. Below is a resource plan outlining roles,

whether they’re full-time (FTE) or contract, rough cost estimates, and when they should come on board:


### ==



### 20



### ==



### # Role



## # Salesforce



### # Developer/



### # Architect



### # Backend



### # Integration



### # Engineer



## # Salesforce



### # Administrator/



### # Consultant



## # Product



### # Manager /



### # Domain Expert



### # (Founder AE)



### # QA Engineer



### # Type (FTE/



### # Contract)



### # 1 FTE (or



### # Lead



### # Contract)



## # 1 FTE



## # 0.5 FTE



### (could be



### # contract



### # part-time)



## # 1 FTE



### # Contract (as



### needed,



## ~0.5 FTE



### # equivalent)



### # Est. Annual



### # Cost (Range)



### $120k – $150k



### (salary) <br>+



### # benefits



### $110k – $140k



### ~$60k (for



### # part-time)



### # – (Founder’s



### # draw)



### $70k – $90k



### # (pro-rated)



### ==



### 21



### ==



### # Start



### # Month



### # Month



### 1



### # Month



### 2



### # Month



### 1



### # Month



### 0



### # Month



### 4



### # Key Responsibilities



### Own the design of the managed



## package, Salesforce data model,



### and integration points. Develop



### # Apex triggers, Flows, and Lightning



### # components. Ensure code passes



### # security review. Deep knowledge of



### # Service Cloud required.



### Build and maintain the



### # middleware/orchestration service



### (if applicable). Develop event



### # subscribers, API clients for Fin/Ada.


# Handle cloud infrastructure (deployment, monitoring). Should


### be well-versed in REST APIs, OAuth,



### # and scaling services.



### Configure and test the solution in



## # various Salesforce org scenarios.



### Advise on assignment rule setup,



## # Salesforce best practices. During



### # pilots, assist customers in



### # installation and configuration. Also



### helps with writing knowledge base



### # docs for setup.



### # Define product requirements and



### use cases (leveraging first-hand



### # knowledge of the Fin integration



### issues). Liaise with pilot customers,



### translate their needs into features.



### Also doubles as Solution



### Architect, ensuring the solution



### # addresses real root causes.



### Develop test plans covering end-to-



### end use cases: new case flows,



### various edge cases (reassignments,



### # token expiry). Perform regression



### testing on package and cloud



### # service before each release. Also



## # test in different Salesforce



### # environments (Sandbox, different



### # versions) for compatibility.



### # Role



### # UI/UX Designer



### # DevOps/Cloud



### # Engineer



### # Security/



### # Compliance



### # Officer



### # Marketing &



### # Communications



### # Lead



### # Type (FTE/



### # Contract)



### # Contract



### # (project-



### based)



### 0.5 FTE (or shared with



### # backend



### # engineer)



### # Contract/



### # Advisor



### # (fractional)



### # Contract



### # (fractional)



### # Est. Annual



### # Cost (Range)



### $5k – $10k



### # (one-time for



### # initial design)



### $80k – $100k



### # (pro-rated)



### ~$15k (for



### # consultation)



### $50k (for 6-



### # month



### # engagement)



### ==



### 22



### ==



### # Start



### # Month



### # Month



### 5



### # Month



### 3



### # Month



### 6



### # Month



### 8



### # Key Responsibilities


# Design any user-facing elements:


### the agent console component UI,



### # admin settings pages, and overall



### flow (ensuring it’s intuitive for SF



### admins). Since our product is more



### backend, this may be a small



### engagement focusing on usability



### of whatever interface we expose.



## Set up and maintain cloud


# infrastructure for the middleware:


### CI/CD pipelines, logging systems,


security of the cloud environment, auto-scaling. If using a simpler


### # serverless approach, this role



### # ensures smooth deployment and



### monitoring. Could be a part-time



### role or handled by the Backend



### Eng initially, then formalized as we



### # onboard customers.


Review the solution for compliance:


### # GDPR, HIPAA (if health data



### # possible), and AppExchange



### security readiness. Help prepare



### # documentation for Security Review



### # and later for any enterprise



### # security assessments. This person



### ensures encryption keys, data



### # retention policies, and access



### controls are in place. Possibly an



## # external consultant with Salesforce



### # security expertise.



### # Develop marketing materials



### # (website, AppExchange listing



### # content, press releases). Plan



### launch campaigns. Could be a



### freelancer or agency specializing in



### B2B SaaS marketing. Not needed



### until product is nearing launch



### # readiness.



### # Role



### # Type (FTE/



### # Contract)



### # Est. Annual



### # Cost (Range)



### # Start



### # Month



### # Key Responsibilities



### Once the product is ready to sell, a



### sales lead to drive deals and



### # manage partnerships. Ideally



## # Sales/



### # Partnerships



### # Director



### # 1 FTE (or



### could hire



### # Month 10)



### $120k +



### # commission



### # Month



### 10



### # someone with enterprise sales



## # experience in SaaS or Salesforce



### # ecosystem. Month 10 hire means



### # founder handles sales in early



### pilots; this role comes to accelerate



### commercial traction and handle



### # pipeline by public launch.



### # Ensures pilot and early customer


# success: onboarding, training, first- line support for issues. Also


### # monitors the system for any live



### # Customer



### # Success/Support



### # Rep



## # 1 FTE



### $70k – $90k



### # Month



### 10



### # problems and coordinates with



### engineering to resolve. Starting



### # around launch ensures new



### customers get white-glove



### # treatment. (Prior to this, the PM/



### founder likely covers these tasks



### # with pilot users.)


Budget Notes: In the first 6 months, our core expenses are a Salesforce dev and a backend dev (plus

founder sweat equity). That’s roughly $20k/month in developer salaries. Add part-time admin and QA

around mid-point, plus cloud hosting (maybe $500-$1000/month on AWS in early stage), and we’re looking

at a burn of perhaps $30k/month by month 6. By months 10-12, hiring sales and success roles increases

burn but hopefully by then we have either revenue from pilot conversions or investment. The total 12-

month budget might be on the order of $500k–$800k, which could be seed-funded or bootstrapped with

initial customer deals. We should plan for some contingency funds for things like security certifications or


### legal fees (e.g., getting contracts reviewed, etc.).


This lean team assumes each person is fairly experienced to reduce management overhead (e.g., the

Salesforce dev is senior enough to architect without a separate architect role). We also leverage fractional

experts (security, marketing) instead of full hires to save cost and get specialized skills only when necessary.


### 7. Risk & Compliance Checklist


Launching an integration in the enterprise CX space comes with various risks and compliance obligations.

Below is a checklist addressing these and our plans to mitigate them:

❏ Salesforce Security Review Compliance: Ensure no hard-coded credentials, SQL/SOQL injection vulnerabilities, or insecure use of APIs in our code. Use Salesforce Security Scanner (Checkmarx) . Prepare a detailed penetration test report for our external service and


### ==



### 23



### ==


address any issues (Salesforce will want to see we handle external calls securely too). We will follow

Salesforce’s secure coding guidelines (e.g., bulkifying triggers, respecting user permissions in Apex). • ❏ Data Privacy (GDPR/CCPA): Our system processes personal data (customer inquiries, possibly contact info). We must have a Data Processing Addendum ready for customers, outlining how we

use and protect data. For GDPR: implement capabilities to delete or anonymize data upon request –

e.g., if a customer triggers a Salesforce GDPR delete, our service should also delete any cached

transcripts. We’ll avoid storing any more PII than necessary; ideally, most data stays in Salesforce,

and any transient data in our system is purged after use. If we log conversation content for

debugging, ensure logs are ephemeral or sanitized. • ❏ Data Residency & Localization: For European clients, data may need to stay in EU. If our cloud service is multi-region, we should allow processing in the region matching the customer (could use

an EU data center for EU customers). Alternatively, offer a deployment option where the middleware

could run in the customer’s own cloud or a private instance if needed (for highly regulated orgs). We

need to be clear about where our servers are hosted and possibly get certifications like EU-US Data

Privacy Framework compliance or rely on Standard Contractual Clauses for data transfer. • ❏ HIPAA and Sensitive Data: If targeting any healthcare or fintech clients, our system might need to be HIPAA compliant when handling PHI, or PCI compliant if handling any payment info in support

cases. While not our initial target, we should design encryption and access control with these in

mind. Mark fields that may contain sensitive info and ensure they’re encrypted at rest. Possibly

obtain a HIPAA compliance audit if we land a healthcare pilot (or at least be ready to sign a Business

Associate Agreement, which means we attest to protecting health data according to HIPAA rules). • ❏ Access Control & Authentication: Only authorized staff should have access to production systems. Use SSO/MFA for our internal tools. The integration between Salesforce and our service

must use OAuth securely – we should never store the SF username/password, only the OAuth token

(encrypted). For connecting to Intercom/Ada, similarly use their OAuth keys securely. Implement

proper token rotation and secure storage (e.g., AWS Secrets Manager for any keys). Also consider an

audit log in our system for any admin actions (like if someone from our team accesses a customer’s

data for support, it’s logged). • ❏ Intellectual Property & Licensing: Ensure any third-party libraries (open source) we use in our middleware have permissive licenses to avoid IP issues if we’re acquired. E.g., avoid strong copyleft

licenses that could complicate inclusion in a larger product. All code developed by contractors needs

to be under IP assignment to the company. Also watch out for Salesforce’s restrictions: since we’re

on AppExchange, we need to comply with their terms (e.g., not replicating core functionality in

unsupported ways, not storing certain Salesforce data outside without disclosure, etc.). We will get

legal advice on AppExchange partnership terms. • ❏ AppExchange Security & Privacy Listing: When listing, we must disclose what data we access and where it goes. Our listing will need a Security & Compliance section: we’ll state that we access

case data and possibly contact info to pass to the AI, that data is transmitted securely (TLS1.2+), and

stored temporarily in our cloud (if at all). We should also list compliance measures like encryption

and that we don’t store customer data long-term. This transparency is important for trust. • ❏ Scalability & Rate Limits: A risk is hitting Salesforce API limits (they check this in security review too). Using Platform Events reduces API calls, but if we do use REST calls, ensure we use bulk APIs or

composite calls to minimize call count. Also implement back-off strategies if approaching limits. For

our own service, implement rate limiting per client to prevent a malfunction on one side (like an

infinite loop of case updates) from flooding either system. • ❏ Failure Contingency: Have a clear fallback plan if our service is down or Fin/Ada is down. For example, if our middleware cannot reach Fin, perhaps we immediately re-route the case to human to


### ==



### 24



### ==


avoid black hole. Document this behavior and make sure customers are okay with it (most would

prefer a safe failover to human rather than nothing). From compliance view, also consider SLAs –

eventually we’ll need to offer uptime guarantees; we should start monitoring from day 1 (set up

alerts for any failures in event processing or API calls so we can proactively respond). • ❏ Legal: Salesforce Contract and Exit: Joining Salesforce’s partner program entails legal agreement. Also, if acquisition is a goal, keep legal hygiene: all software should have clear

ownership, any customer data belongs to customer, etc. If we integrate deeply with Intercom’s API,

ensure we’re not violating their terms of service (e.g., if they have a clause against using Fin outside

approved ways, get an OK or partnership with them). We might run things by Intercom’s legal if

needed to avoid later issues. • ❏ Auditability: Enterprises may ask for audits. We should be prepared to undergo security audits or provide materials like penetration test results, architecture diagrams, etc. Aligning early with

common standards (SOC 2 Type I by end of year maybe) will make these conversations smoother. For

instance, by Month 12, we might not have full SOC 2 yet, but we can at least state we are working


### towards it and have basic policies in place.


By diligently following this checklist, we aim to reduce the risk of security incidents or compliance blockers

that could derail customer deals. Early attention to these items is essential for mid-market and enterprise

trust, and also makes us a more attractive acquisition target (since any acquiring company will do due


### # diligence on these aspects).



### 8. Next‑Step Action Items (0‑30 Days)


In the immediate term (the first month), here are concrete actions to get this initiative off the ground and

# on track:



# Kickoff Technical Investigation: Schedule in-depth discussions with two key groups: (1) A

Salesforce Service Cloud expert (possibly a Salesforce Certified Technical Architect or someone who’s

integrated bots before) to review our hypotheses on assignment rules and event approaches; (2) An

Intercom/Ada technical contact or former colleague who knows the internals of Fin’s integration (to

gather insight on where it commonly fails). These talks will refine our approach and might surface


### # gotchas early.




Set Up Dev Infrastructure: Create a Salesforce Developer Org (or scratch org via Salesforce DX) for

development. Also, set up a private Git repository and a basic CI pipeline (we can use GitHub Actions

or Bitbucket pipelines) so that any Apex code or external code changes trigger automated tests.

Additionally, register for an Intercom Fin trial or demo environment (if possible) – since Fin is early

access, we might use Intercom’s developer APIs to simulate as needed. For Ada, see if a developer

sandbox is available to test case handoff (or use their documentation and perhaps reach out to their


### # support for a trial).




Reproduce the Issue in a Controlled Env: Write a small script or use Workbench (Salesforce tool) to

simulate the scenario: e.g., use Salesforce API to create a Case and then update it to add a Case

Comment, and observe assignment rule behavior. Basically, confirm Hypothesis H1 by experiment:

does adding an Email-to-Case update via API trigger reassignment? Document this with evidence

(screenshots or logs) to have a solid understanding. Also simulate token issues: connect an org via

OAuth then manually disconnect it and see how Intercom behaves (maybe check Intercom logs if

accessible). This hands-on validation will guide where to focus coding efforts.


### ==



### 25



### ==




Design Review & Architecture Decision: Within 2-3 weeks, conduct an internal design review (the

founder, the SF dev, maybe an advisor). Decide on the architecture (likely leaning hybrid). Sketch out

a high-level diagram of the solution (Case → Trigger → Event → Middleware → AI → response). Identify the components to be built in Salesforce vs externally. This will serve as a blueprint for


### # development sprints.




Preliminary Contact with Salesforce ISV Partner Team: It’s worth reaching out early to

Salesforce’s ISV program managers to express intent to build this solution. They can provide

guidance on security review prep and perhaps early feedback. Initiating the partnership sign-up now

can save time later (there are steps like getting a namespace, etc., which we can do in parallel). Also,

inquire if any similar solutions exist on AppExchange to ensure we differentiate (a quick scan


### suggests not specific to Fin/Ada, but good to confirm).




Legal Setup: Formally register the new venture (if not already done) to be able to enter partnerships

and NDAs. Also, if not yet available, draft a basic NDA to use when talking to pilot customers or

anyone we need to share sensitive info with. Although a lawyer isn’t needed full-time now, having

templates ready expedites collaboration with design partners or pilot customers (who may want an



NDA). Pilot Customer Pipeline: Start identifying and gently approaching potential pilot customers. The

user, being an ex-Intercom AE, likely has contacts at companies that tried Fin. Reach out informally:

“We’re exploring a solution to improve Fin’s Salesforce integration – can I chat with your support lead

about their experience?” These conversations can both validate our understanding and pave the way

for them to try our solution in a month or two. Aim to have at least one committed pilot design


### # partner by end of 30 days.




# Set Up Project Management & Communication: Establish our internal project tracking (whether

that’s JIRA, Trello, or GitHub issues). Outline the user stories for the MVP. Also set up a Slack (or

Teams) for the team and include any external advisors. Having these structures in place early will


### keep the development organized as new folks join.




Compliance Prep: Start a security checklist document mapping out how we’ll address each item in

section 7. For example, list out all places where data is stored and ensure encryption for each; decide

on an encryption library for the external service; check if Salesforce Shield (platform encryption) is

needed or if standard TLS is enough since data stays mostly in SF. Initiating these discussions in the

first month means we won’t scramble last-minute for security review.

By executing these action items in the first 30 days, we will move from concept to concrete execution with

momentum. This sets the foundation for the subsequent development and gives confidence to

stakeholders (and potential investors or customers) that the project is being managed methodically with an


### # eye on both technical success and business viability.



### # Appendices


A. Reference APIs & Objects - Salesforce Case Object: Key fields – OwnerId (will be set to Fin’s user or queue for AI cases), Status , Priority , Origin (could mark if came from Bot vs. Human), SuppliedEmail (customer email from web form), Description (initial issue text, may contain AI summary after handoff). Also CaseComment and EmailMessage child objects for threaded communication. - Assignment Rules: Use of AssignmentRuleHeader in API calls to control behavior AssignmentRuleHeader.useDefaultRule=false on any updates Fin performs to prevent re-routing.


### 14



### . We’ll likely use


Intercom Fin API: Not publicly documented in detail (as Fin is beta). Presumably OAuth with Intercom


### ==



### 26



### ==


credentials, then some endpoint like POST /salesforce/case/{id}/answer or Fin might subscribe to

SF events through a connected app. Since Fin’s doc says “connect via OAuth”


### 22



## , it might use Salesforce


APIs behind scenes rather than expose its own. If Fin’s closed API isn’t accessible, we emulate via Intercom’s

existing APIs (Intercom has Conversation APIs, but Fin working on cases might not expose those externally).

We may rely on Fin’s built-in behavior triggered by assignment rules as currently. (Hence the event/

middleware might just monitor and ensure SF side is synced, rather than directly calling Fin’s AI.)

Ada API: Ada offers REST endpoints for creating cases or sending data to external systems. Ada’s “Actions”

likely correspond to invoking Salesforce REST API (Create Case) as described


### 31



### . For chat, Ada uses


streaming APIs (long polling to Live Agent). In our solution, if supporting Ada, we might not need to use Ada

APIs at all – Ada already creates the case and we ensure it’s handled. But if we want to integrate deeply, we

could use Ada’s API to signal back when agent picks up, etc. - Platform Events: Custom Platform Event example definition: AI_Case_Update__e with fields: CaseId,

Action (enum: “answer”, “escalate”), AnswerText, AnswerSource, Confidence, etc. Published by AI or by

middleware after getting AI answer. Subscriber in Salesforce (Apex trigger) uses the data to update the case

(e.g., add CaseComment with AnswerText if action=answer, or change owner if action=escalate).

Sample API Payloads: - Salesforce REST create Case (used by Ada or by our middleware):


### # POST /services/data/v57.0/sobjects/Case



### {



### "Origin": "Web",



### "Subject": "ADA: Support Request",


"Description": "User question: 'How do I reset my password?' \n[Transcript ID


### 12345]",



### "SuppliedName": "Jane Doe",



### "SuppliedEmail": "jane@example.com",



### "Status": "New",



### # "Priority": "Medium"



### }


(Note: Ada might populate a custom field with full transcript if Description is too short or use Case Feed


### # items.)


Fin auto-closing Case via API (pseudo-code):


### # PATCH /services/data/v57.0/sobjects/Case/500xx0000001234



### {



### "Status": "Closed",


"Reason": "Solved by AI", // custom or standard field indicating


### # resolution



### "ClosedDate": "2025-07-08T18:30:00Z"



### }


Fin likely also adds a tag, which could be implemented as a Case RecordType or a checkbox (we might create a custom field Closed_by_AI__c = true ).

Platform Event publish from Flow (pseudo):


### ==



### 27



### ==


In a Flow, after Case creation, create an AI_Case_Request__e record with fields: CaseId = {!NewCase.Id},

Subject = {!NewCase.Subject}, DescriptionSnippet = LEFT({!NewCase.Description}, 200). The external system


### will pick up this event via CometD.



### # B. Sample Case Routing Flow


# (Textual flowchart of a new case through our system):


### 1.


New Case Created in Salesforce (Origin e.g. “Email” from support@company.com). It enters as


### # Status “New”, Owner “Unassigned”.



### 2.


Trigger: Case to AI? – Our package’s trigger/flow runs: checks case criteria (e.g., if no attachments and issue type is FAQ, send to AI). It publishes AI_Case_Request__e and sets Case Owner to a

temporary “AI Processing” queue or a dummy user to indicate it's with AI (to avoid standard assignment). It also updates a field AI_Status__c = 'Pending' .


### 3.


AI Service Receives Event – The middleware (or Fin’s system) gets the event with case details. It calls

AI engine (Intercom Fin) with the question. Fin uses knowledge base and returns an answer: “To

reset your password, click Forgot Password on the login page.” along with a flag (e.g., confident


### 4.


enough). AI Response Event – The middleware publishes AI_Case_Response__e (CaseId, AnswerText,


### 5.


Action=”answer”, Confidence=95%). Salesforce Updates Case – Our Apex trigger on AI_Case_Response__e fires: it finds the Case by

Id. It creates a Case Comment or EmailMessage on that case with the AnswerText (visible to

customer if email). It updates Case Status to “Working” and Owner remains AI for now. It sets AI_Status__c = 'Answered' .


### 6.


Customer Receives Answer – The answer is sent out (via Salesforce email). Customer reads it. Two

# possibilities:

a. Issue Resolved: Customer is satisfied or does not reply within say 48 hours. We have a

background job or Fin signals “no response, assume solved.” Then a final event or workflow triggers closure: Case Status -> “Closed”, AI_Status__c = 'Resolved' , maybe populate Case Resolution


### field “Solved by AI” and auto-close.


b. Not Resolved: Customer replies “That didn’t work”. Salesforce attaches that reply to the Case (EmailMessage). Our system detects a new EmailMessage on a case where AI_Status__c = 'Answered' . This triggers another event to AI or simply the middleware sees it via API. Fin now


### 7.


either gives a second answer or decides “I can’t handle this”. Suppose it decides to escalate. Escalation – Fin/middleware publishes AI_Case_Response__e with Action=”escalate”. Our SF

trigger handles it: changes Case Owner to “Tier1 Support Queue”, Status “New” (or “Escalated”), and

maybe posts an internal comment “AI could not resolve – handing over to agent.” Also, notifies via email/Slack (if integrated) that an escalation happened. Sets AI_Status__c = 'Escalated' .


### 8.


Agent Takes Over – A support agent picks up the case from the queue. They see the full thread:

initial customer query, AI answer, customer follow-up. They respond accordingly and eventually


### resolve the case, closing it with standard procedures.



### 9.


Reporting – Later, admin reports show: Case X was AI answered then escalated. Case Y was fully

solved by AI. Fin’s own dashboard can also reflect resolution rates based on tags/fields we set


### 40


# C. Citation Index (Key sources referenced):


## 1. Intercom Fin for Salesforce capabilities 1


– Confirms Fin follows SF assignment rules and can handoff to


### # team in Service Cloud.



### 2. Fin integration overview 5



### 27


– Notes Fin resolving cases with conversation history and offering


### ==



### 28



### ==



### .



### workflows like handover and summarize conversation.



### 3. Ada documentation on email handoff 32



## – Describes Ada creating Salesforce cases with conversation


details and need for separate agent email addresses to avoid conflicts.


## 4. Salesforce StackExchange/Medium article 2



### – Explains the Assignment Rule header default


behavior causing unexpected owner reassignments on API updates, which is a likely root cause of our


### observed routing issues.



### 5. Intercom integration troubleshooting 6


# – Points out OAuth token removal stops integration and that

only 4 OAuth tokens per user are allowed, highlighting a cause for integration outages.


## 6. SalesforceBen on Platform Events 19


# – Emphasizes real-time integration capability with external systems

via Platform Events, supporting our event-driven architectural choice.


## 7. Salesforce Security review timeline 41


– Notes the ~4-6 week security review process, informing our


### # roadmap timing.



### 8. TechTarget on Ada Glass 3


– Articulates the importance of smooth chatbot-to-human transitions to

avoid customer frustration (context preservation), reinforcing our hypothesis on context loss.

1. Intercom community snippet tags (like fin-soft-resolution ), informing our design of resolution tracking. 26

1. Intercom community snippet tags (like fin-soft-resolution ), informing our design of resolution tracking. 26

Each of these sources has been used to validate specific claims or provide context for our solution design.

By grounding our analysis in documented evidence and real user experiences, we ensure our plan

addresses the actual issues and aligns with best practices in the Salesforce and AI integration landscape.


### 1



### 24



### 42



### 45



### Fin for platforms explained | Intercom Help


# https://www.intercom.com/help/en/articles/10118495-fin-for-platforms-explained


### 2



### 14



### 37


Case Assignment Rules getting fired on REST API Record Updates in Salesforce | by Sai Sri Ram


### # Naraharisetty | Medium


# https://medium.com/@saisriram_61508/case-assignment-rules-getting-fired-on-rest-api-record-updates-in-


### # salesforce-70a5820326b8



### 3


Ada looks to improve chatbot handoff with AI-powered Ada Glass | TechTarget

# https://www.techtarget.com/searchcustomerexperience/news/252465487/Ada-looks-to-improve-chatbot-handoff-with-AI-


### # powered-Ada-Glass



### 4



### 16



### 29



### 30



### 31



### 32



### 33



### 35



### 38



### # Email handoffs | Ada | Documentation


# https://docs.ada.cx/docs/channels/email/email-configuration/email-handoffs


### 5



### 12



### 13



### 22



### 23



### 25



### 27



### 28



### 36



### 39



### 40


# How Fin integrates with Salesforce | Fin by Intercom: Help Center

# https://fin.ai/help/en/articles/10614065-how-fin-integrates-with-salesforce


### 6



### 7



### 8



### 9



### 10



### 11



### 15


# Salesforce integration troubleshooting and FAQs | Intercom Help

# https://www.intercom.com/help/en/articles/1047665-salesforce-integration-troubleshooting-and-faqs


### 17



### 18



### 34



### # Ada Glass configuration | Ada | Documentation


# https://docs.ada.cx/docs/handoffs/salesforce/salesforce-chat/ada-glass-configuration


### 19



### 20



### 21



## # Salesforce Platform Events: Explained | Salesforce Ben



### # https://www.salesforceben.com/salesforce-platform-events/



### 26



### # Need help for building FIN AI Agent - Intercom Community


# https://community.intercom.com/fin-ai-agent-59/need-help-for-building-fin-ai-agent-10401


### ==



### 29



### ==



### 41



### 46



## # Salesforce Security Review: Updates and Tips for Passing


# https://magicfuse.co/blog/how-to-pass-salesforce-appexchange-security-review


### 43



### 44


# AI Agents Are Smart - Handing Off To Humans Makes Them Smarter


### # https://www.salesforce.com/blog/agent-to-human-handoff/



### ==



### 30



### ==

