---
title: Untitled Document
document_type: guide
primary_topics: product
last_preprocessed: 2025-05-26
---


### ================



## 5/19/25, 8:27 AM



### ================



### ==================================================



### Fin Task best practices and examples Intercom Help



### ==================================================



### [Image: unknown]



### # intercom



### Search for articles...


All Collections > Fin Al Agent > Train > Fin Task best practices and examples


### # Fin Task best practices and examples


See our best practices and examples when creating Fin Tasks and writing instructions for Fin.

Written by Ivan
Updated this week


### [Image: unknown]



### [Image: unknown]



### [Image: unknown]



### Table of contents


Using Fin Tasks, you can give Fin step-by-step instructions for the task you want it to perform.
We've provided some best practices and examples when writing these instructions for Fin.

Note: Fin Tasks is currently in a closed beta. If you're interested in getting access, please
speak to your Intercom Relationship or Customer Success Manager.


### # Fin Task best practices


Clearly written instructions can make a major difference in how your Fin Task performs.


### General LLM prompting tips


Betore diving into the specitics of Fin Tasks, here are some helpful tips that generally apply
when working with large language models (LLMs):


### ====



### 1/12



### ====


nups
tercom.com
n ar
0539969-fin-t: tas e st practices-and-example:


### ================



## 5/19/25, 8:27 AM



### ================



### ==================================================



### Fin Task best practices and examples Intercom Help



### ==================================================



### [Image: unknown]



### # intercom



### Search for articles...


All Collections > Fin Al Agent > Train > Fin Task best practices and examples


### # Fin Task best practices and examples


See our best practices and examples when creating Fin Tasks and writing instructions for Fin.

Written by Ivan
Updated this week


### [Image: unknown]



### [Image: unknown]



### [Image: unknown]



### Table of contents


Using Fin Tasks, you can give Fin step-by-step instructions for the task you want it to perform.
We've provided some best practices and examples when writing these instructions for Fin.

Note: Fin Tasks is currently in a closed beta. If you're interested in getting access, please
speak to your Intercom Relationship or Customer Success Manager.


### # Fin Task best practices


Clearly written instructions can make a major difference in how your Fin Task performs.


### General LLM prompting tips


Betore diving into the specitics of Fin Tasks, here are some helpful tips that generally apply
when working with large language models (LLMs):


### ====



### 1/12



### ====


nups
tercom.com
n ar
0539969-fin-t: tas e st practices-and-example:


## 5/19/25, 8:27 AM



### Fin Task best practices and examples Intercom Help


Agood prompt is imperative and instructive. Start sentences with a verb and avoid passive
voice.

Leave no room for ambiguity: detailed instruction is better than brief.

For some additional reading, see the introduction topics here.


### # Task scope and organization


While Fin retains a memory of previous steps and actions taken or data stored, you still need to
design tasks with clear boundaries and focused purposes.

When to use a single Fin Task:

All steps are part of a cohesive process with clear progression.


### Later steps depend on earlier steps in a logical sequence.


The entire process shares the same decision criteria and outcomes.

When to consider multiple Fin Tasks:


### For completely separate business processes



### [Image: unknown]



### =



## Z



### =



### You need to create clear checkpoints in a complex workflow


Different stakeholders or teams own different parts of a process


### You want to enable different entry points into a workflow



### Task structure



### Trigger title and description



### Make sure the title is descriptive and not just internal.



### Good practice example: Verify and process refunds



### Bad practice example: Test123


You should write 3-5 sentences to describe when Fin should trigger this task. Be as specific as
possible and make sure to include one or more of the following:

Examples of the types of customer queries that would be answered by this task.


### Key phrases customers might use.


Common scenarios in which triggering this task would be appropriate.

Good practice example:

Use this task if a customer asks to cancel an order or asks for a refund on an order. This task


### ====



### 2/12



### ====


=============================================================

aps
tercom.com
n
539969-hn-tas: < e st practices-and-example:

=============================================================


## 5/19/25, 8:27 AM



### Fin Task best practices and examples Intercom Help


Agood prompt is imperative and instructive. Start sentences with a verb and avoid passive
voice.

Leave no room for ambiguity: detailed instruction is better than brief.

For some additional reading, see the introduction topics here.


### # Task scope and organization


While Fin retains a memory of previous steps and actions taken or data stored, you still need to
design tasks with clear boundaries and focused purposes.

When to use a single Fin Task:

All steps are part of a cohesive process with clear progression.


### Later steps depend on earlier steps in a logical sequence.


The entire process shares the same decision criteria and outcomes.

When to consider multiple Fin Tasks:


### For completely separate business processes



### [Image: unknown]



### =



## Z



### =



### You need to create clear checkpoints in a complex workflow


Different stakeholders or teams own different parts of a process


### You want to enable different entry points into a workflow



### Task structure



### Trigger title and description



### Make sure the title is descriptive and not just internal.



### Good practice example: Verify and process refunds



### Bad practice example: Test123


You should write 3-5 sentences to describe when Fin should trigger this task. Be as specific as
possible and make sure to include one or more of the following:

Examples of the types of customer queries that would be answered by this task.


### Key phrases customers might use.


Common scenarios in which triggering this task would be appropriate.

Good practice example:

Use this task if a customer asks to cancel an order or asks for a refund on an order. This task


### ====



### 2/12



### ====


=============================================================

aps
tercom.com
n
539969-hn-tas: < e st practices-and-example:

=============================================================


### ================



## 5/19/25, 8:27 AM



### ================



### ==================================================



### Fin Task best practices and examples Intercom Help



### ==================================================


will check if the customer is eligible for a cancellation and will proceed with that cancellation,
if applicable.

Bad practice example:
Use this task to cancel.


### [Image: unknown]



### =



## Z



### =



### # Instructions block


The instruction block follows a structured format composed of the following sections..


### ====



### 3/12



### ====


nups
ercom.co:
39969-fin-tas e st practices-and-example:


### ================



## 5/19/25, 8:27 AM



### ================



### ==================================================



### Fin Task best practices and examples Intercom Help



### ==================================================


will check if the customer is eligible for a cancellation and will proceed with that cancellation,
if applicable.

Bad practice example:
Use this task to cancel.


### [Image: unknown]



### =



## Z



### =



### # Instructions block


The instruction block follows a structured format composed of the following sections..


### ====



### 3/12



### ====


nups
ercom.co:
39969-fin-tas e st practices-and-example:


### ==================================================



### Fin Task best practices and examples Intercom Help



### ==================================================



### ================



## 5/19/25, 8:27 AM



### ================



### [Image: unknown]


# 1. Instructions:


### =



## Z



### =


This is a clear, logically-complete, step-by-step plan that Fin should follow. Make sure to cover
all the decision rules that are necessary for Fin to perform the task.

The best and easiest way to formulate these is to follow an "if + else" logic. This logic
guarantees you will always be able to make a decision at any stage and either make progress
towards a solution or have a way out of the process if you are stuck. For our example, this
would look like:

1. If you can determine the order date and it is less than 30 days ago, issue a refund.

1. If you can determine the order date but it is above 30 days ago, tell the customer
Company X's policy does not allow for refunds on purchases more than 30 days into the
past.

1. Else, tell the customer you will escalate to a human member of the support team, and
execute the escalation by doing... (this example assumes escalation logic has been built
into the Fin Task)


### ====



### 4/12



### ====


ntp
ercom.cor
39969-61 in-t SL practices- and-examples


### ==================================================



### Fin Task best practices and examples Intercom Help



### ==================================================



### ================



## 5/19/25, 8:27 AM



### ================



### [Image: unknown]


# 1. Instructions:


### =



## Z



### =


This is a clear, logically-complete, step-by-step plan that Fin should follow. Make sure to cover
all the decision rules that are necessary for Fin to perform the task.

The best and easiest way to formulate these is to follow an "if + else" logic. This logic
guarantees you will always be able to make a decision at any stage and either make progress
towards a solution or have a way out of the process if you are stuck. For our example, this
would look like:

1. If you can determine the order date and it is less than 30 days ago, issue a refund.

1. If you can determine the order date but it is above 30 days ago, tell the customer
Company X's policy does not allow for refunds on purchases more than 30 days into the
past.

1. Else, tell the customer you will escalate to a human member of the support team, and
execute the escalation by doing... (this example assumes escalation logic has been built
into the Fin Task)


### ====



### 4/12



### ====


ntp
ercom.cor
39969-61 in-t SL practices- and-examples


## 5/19/25, 8:27 AM



### Fin Task best practices and examples Intercom Help


If the logic and information Fin needs to access is too open-ended, you should consider
whether you can break down the instructions block into smaller steps with more well-defined,
constrained logic.

You'll also need to identify the input values needed to perform the task. Explicitly state in the
prompt:

What these attributes are and what they can be used for, and how these attributes relate
to the task's broader context.

Whether these attributes are guaranteed to be available (e.g. from a previous step in the
instructions)

o If SO, where they are available or what their value is, by inserting them directly into the
prompt.

o If not, where or how they can be gathered (e.g. from the customer)

1. End this task when:

Briefly define what counts as completion of the task. Specify the conditions under which the
task can be considered to be completed, regardless of it producing a positive or negative
outcome for the customer.


### [Image: unknown]


If possible, you should also include information about any task attributes/attrbutes required by
the task. If the output variable you are trying to fill in is e.g. refund_outcome, add:

When you have the value of the refund_outcome output variable with a status of fdenied,
success orescalation, respectively. No other value is valid.

# 3. Guidance (optional):

Guide how Fin interacts, responds, and behaves during a task by providing clear guidance.
Simply describe any specific behaviors you'd like Fin to follow while performing the steps.


### # Task triggers


Include around 10-30 example queries in task trigger descriptions

When writing a task trigger description, begin with about 10 highly relevant example queries to
ensure the task is recognized correctly. If necessary, you can extend this to 20-30 examples,


### ====



### 5/12



### ====


nups:/
tercom.com 1 n
0539969-f1 in-t tas e st practices-and-example:


## 5/19/25, 8:27 AM



### Fin Task best practices and examples Intercom Help


If the logic and information Fin needs to access is too open-ended, you should consider
whether you can break down the instructions block into smaller steps with more well-defined,
constrained logic.

You'll also need to identify the input values needed to perform the task. Explicitly state in the
prompt:

What these attributes are and what they can be used for, and how these attributes relate
to the task's broader context.

Whether these attributes are guaranteed to be available (e.g. from a previous step in the
instructions)

o If SO, where they are available or what their value is, by inserting them directly into the
prompt.

o If not, where or how they can be gathered (e.g. from the customer)

1. End this task when:

Briefly define what counts as completion of the task. Specify the conditions under which the
task can be considered to be completed, regardless of it producing a positive or negative
outcome for the customer.


### [Image: unknown]


If possible, you should also include information about any task attributes/attrbutes required by
the task. If the output variable you are trying to fill in is e.g. refund_outcome, add:

When you have the value of the refund_outcome output variable with a status of fdenied,
success orescalation, respectively. No other value is valid.

# 3. Guidance (optional):

Guide how Fin interacts, responds, and behaves during a task by providing clear guidance.
Simply describe any specific behaviors you'd like Fin to follow while performing the steps.


### # Task triggers


Include around 10-30 example queries in task trigger descriptions

When writing a task trigger description, begin with about 10 highly relevant example queries to
ensure the task is recognized correctly. If necessary, you can extend this to 20-30 examples,


### ====



### 5/12



### ====


nups:/
tercom.com 1 n
0539969-f1 in-t tas e st practices-and-example:


## 5/19/25, 8:27 AM



### Fin Task best practices and examples Intercom Help


but be mindful of complexity. If the list becomes too long or specific, consider simplifying the
description or transitioning to intent-based triggers to maintain clarity and manageability.


### Use negative examples only when triggering incorrectly


"Do not trigger" examples should only be included if you're observing incorrect triggering
behavior. Negative examples help refine detection by clarifying what Fin should not respond
to, but avoid adding them unless they're addressing a specific problem with misfiring triggers.


### # Task instructions



### Split instructions only when tasks are complex


Use a single structured instruction block when your task is straighttorward or under roughly 10
steps. If the task involves complex logic, significant branching, or becomes difficult to follow,
it's best to split it into multiple instruction blocks for clarity and maintainability.


### Let Fin collect inputs automatically for data connectors



### =



## Z



### =


You don't need to
gather all inputs manually before running a data connector. When
contiguring the data connector, specify the required inputs, and Fin will automatically ask the
customer for any that are missing. This reduces the complexity of your instructions and keeps
interactions more efficient.


### # Task switching is allowed during conversations


Fin is capable of switching tasks mid-conversation. and even switching to informational
answers (from your support content) when the context or customer intent changes. This means
it can exit one task and begin another seamlessly, enabling more dynamic and responsive
interactions based on evolving user needs.


### # API responses are remembered across instruction steps


Fin automatically remembers API responses within the same instruction block. You can refer
back to these results naturally in later steps, such as saying "using the balance returned earlier,"
without needing to repeat or store the data manually.


### No need to save API responses in temporary attributes


There's no requirement to explicitly store API responses in temporary attributes. Fin keeps
track of the data internally, allowing you to reference it directly in subsequent steps using

aps:/ nu tercom.com/h n ar
0539969-hn-tas: < e st practices-and-example:


### ====



### 6/12



### ====



## 5/19/25, 8:27 AM



### Fin Task best practices and examples Intercom Help


but be mindful of complexity. If the list becomes too long or specific, consider simplifying the
description or transitioning to intent-based triggers to maintain clarity and manageability.


### Use negative examples only when triggering incorrectly


"Do not trigger" examples should only be included if you're observing incorrect triggering
behavior. Negative examples help refine detection by clarifying what Fin should not respond
to, but avoid adding them unless they're addressing a specific problem with misfiring triggers.


### # Task instructions



### Split instructions only when tasks are complex


Use a single structured instruction block when your task is straighttorward or under roughly 10
steps. If the task involves complex logic, significant branching, or becomes difficult to follow,
it's best to split it into multiple instruction blocks for clarity and maintainability.


### Let Fin collect inputs automatically for data connectors



### =



## Z



### =


You don't need to
gather all inputs manually before running a data connector. When
contiguring the data connector, specify the required inputs, and Fin will automatically ask the
customer for any that are missing. This reduces the complexity of your instructions and keeps
interactions more efficient.


### # Task switching is allowed during conversations


Fin is capable of switching tasks mid-conversation. and even switching to informational
answers (from your support content) when the context or customer intent changes. This means
it can exit one task and begin another seamlessly, enabling more dynamic and responsive
interactions based on evolving user needs.


### # API responses are remembered across instruction steps


Fin automatically remembers API responses within the same instruction block. You can refer
back to these results naturally in later steps, such as saying "using the balance returned earlier,"
without needing to repeat or store the data manually.


### No need to save API responses in temporary attributes


There's no requirement to explicitly store API responses in temporary attributes. Fin keeps
track of the data internally, allowing you to reference it directly in subsequent steps using

aps:/ nu tercom.com/h n ar
0539969-hn-tas: < e st practices-and-example:


### ====



### 6/12



### ====



## 5/19/25, 8:27 AM



### Fin Task best practices and examples Intercom Help



### simple natural language.



### # Fin Task examples


We have compiled a number of different use case prompts below that can help you shape your
Fin Tasks.


### # Order Refund


Description: The goal of this task is to determine if a refund request made by a customer is
valid, and if SO, process it. By following the below instructions, you will be able to verify and
process a customer's refund request for orders made with Company X.

Step 1: Use Oget.order.details for order with ID Ocollected.order.d to retrieve details for that
order. Then follow the below logic to determine whether the retrieved order can be refunded:

If the order date is more than 30 days older than the present date, inform the customer
you cannot offer a refund because the order was initially made more than 30 days ago.
Set Orefund.Outcome to "denied" and inform the customer of the outcome.


### =



## N



### =


If the order date is less than 30 days older than the present date, proceed to Step 2.

Else, inform the customer you cannot verify whether the order can be refunded and
escalate to a human member of the support team. Set refund.outcome to "escalation"
and inform the customer you have taken this action.

Step 2: Use Oprocess.tems.etung with the order ID Ocollected.order.d to process a refund
for that order. Then gather the response and:

If the refund has succeeded, inform the customer that the refund was processed
successfully. Set Orefund.outcome to "success" and inform the customer of the outcome.

Else, if the refund has failed, inform the customer you were not able to process the refund.
Set Orefund.outcome to l"escalation" and inform the customer you have taken this action.

End this task when: You fill in the value of the Orefund.outcome variable with a status of either
"denied", "success" or "escalation". No other value is valid.

Guidance: Be empathetic when delivering negative news about refund denials. When a refund
is successful, be warm and clear about refund processing timelines.


### ====



### 7/12



### ====


===============================================================

nups: :/
tercom.com
0539969-hn-tas. e st practices-and-example:

===============================================================


## 5/19/25, 8:27 AM



### Fin Task best practices and examples Intercom Help



### simple natural language.



### # Fin Task examples


We have compiled a number of different use case prompts below that can help you shape your
Fin Tasks.


### # Order Refund


Description: The goal of this task is to determine if a refund request made by a customer is
valid, and if SO, process it. By following the below instructions, you will be able to verify and
process a customer's refund request for orders made with Company X.

Step 1: Use Oget.order.details for order with ID Ocollected.order.d to retrieve details for that
order. Then follow the below logic to determine whether the retrieved order can be refunded:

If the order date is more than 30 days older than the present date, inform the customer
you cannot offer a refund because the order was initially made more than 30 days ago.
Set Orefund.Outcome to "denied" and inform the customer of the outcome.


### =



## N



### =


If the order date is less than 30 days older than the present date, proceed to Step 2.

Else, inform the customer you cannot verify whether the order can be refunded and
escalate to a human member of the support team. Set refund.outcome to "escalation"
and inform the customer you have taken this action.

Step 2: Use Oprocess.tems.etung with the order ID Ocollected.order.d to process a refund
for that order. Then gather the response and:

If the refund has succeeded, inform the customer that the refund was processed
successfully. Set Orefund.outcome to "success" and inform the customer of the outcome.

Else, if the refund has failed, inform the customer you were not able to process the refund.
Set Orefund.outcome to l"escalation" and inform the customer you have taken this action.

End this task when: You fill in the value of the Orefund.outcome variable with a status of either
"denied", "success" or "escalation". No other value is valid.

Guidance: Be empathetic when delivering negative news about refund denials. When a refund
is successful, be warm and clear about refund processing timelines.


### ====



### 7/12



### ====


===============================================================

nups: :/
tercom.com
0539969-hn-tas. e st practices-and-example:

===============================================================


## 5/19/25, 8:27 AM



### Fin Task best practices and examples Intercom Help



### Subscription Cancellation Request


Description: The goal of this task is to determine if a subscription cancellation request made by
a customer is valid, and if SO, to process it. By following the instructions below, you will be able
to verify and cancel a customer's subscription for Company X.

Step 1: Use egetsubserpion.0etals for the subscription with ID @collected.subscription.id
to retrieve details for that subscription. Then follow the below logic to determine whether the
retrieved subscription can be canceled:

e If the subscription is still in its minimum commitment period (a 12-month term that has not
yet elapsed):

o Inform the customer that you cannot cancel the subscription at this time because the
subscription is within its commitment period.


### o Set Ocancelaton.Outcome to denied".


If the subscription is eligible for cancellation (it is a month-to-month plan or the
commitment period is over):


### o Proceed to Step 2.


Otherwise, if you cannot determine from the subscription details whether it can be
canceled:


### [Image: unknown]



### =



## Z



### =


o Inform the customer you cannot verify the subscription's cancellation eligibility and
escalate to a human member of the support team.


### o Set ocancelation.Outcome to "escalation".


Step 2: Use Ocancelsubscrption with the subscription ID @collected.subscription.id to
process the cancellation. Then gather the response and:

If the cancellation succeeds:

o Inform the customer that the subscription was canceled successfully.


### o Set Ocancelaton.Qutcome to "success".


If the cancellation fails:

o Inform the customer that you were not able to cancel the subscription and have
escalated the issue.


### o Set ocancelaton.Qutcome to "escalation".


End this task when: You fill in the value of Ocancelation.Outcome with either "denied",
"success", or escalation". No other value is valid.

Guidance: Be matter-of-fact but empathetic when explaining commitment periods. When
successful, confirm clearly what will happen with billing going forward.


### ====



### 8/12



### ====


==============================================================

nups:/y
tercom.com
539969-hn-tas: e st practices- and-examples

==============================================================


## 5/19/25, 8:27 AM



### Fin Task best practices and examples Intercom Help



### Subscription Cancellation Request


Description: The goal of this task is to determine if a subscription cancellation request made by
a customer is valid, and if SO, to process it. By following the instructions below, you will be able
to verify and cancel a customer's subscription for Company X.

Step 1: Use egetsubserpion.0etals for the subscription with ID @collected.subscription.id
to retrieve details for that subscription. Then follow the below logic to determine whether the
retrieved subscription can be canceled:

e If the subscription is still in its minimum commitment period (a 12-month term that has not
yet elapsed):

o Inform the customer that you cannot cancel the subscription at this time because the
subscription is within its commitment period.


### o Set Ocancelaton.Outcome to denied".


If the subscription is eligible for cancellation (it is a month-to-month plan or the
commitment period is over):


### o Proceed to Step 2.


Otherwise, if you cannot determine from the subscription details whether it can be
canceled:


### [Image: unknown]



### =



## Z



### =


o Inform the customer you cannot verify the subscription's cancellation eligibility and
escalate to a human member of the support team.


### o Set ocancelation.Outcome to "escalation".


Step 2: Use Ocancelsubscrption with the subscription ID @collected.subscription.id to
process the cancellation. Then gather the response and:

If the cancellation succeeds:

o Inform the customer that the subscription was canceled successfully.


### o Set Ocancelaton.Qutcome to "success".


If the cancellation fails:

o Inform the customer that you were not able to cancel the subscription and have
escalated the issue.


### o Set ocancelaton.Qutcome to "escalation".


End this task when: You fill in the value of Ocancelation.Outcome with either "denied",
"success", or escalation". No other value is valid.

Guidance: Be matter-of-fact but empathetic when explaining commitment periods. When
successful, confirm clearly what will happen with billing going forward.


### ====



### 8/12



### ====


==============================================================

nups:/y
tercom.com
539969-hn-tas: e st practices- and-examples

==============================================================


## 5/19/25, 8:27 AM



### Fin Task best practices and examples Intercom Help



### # Address Change Request


Description: The goal of this task is to determine if a requested shipping address update for a
customer is valid, and if SO, to process it. By following the instructions below, you will verify and
update the shipping address in Company X's system.

Step 1: Use Oget.customer.prolie by providing the ID ocolected.Customer.e to retrieve the
customer's current account status. Then follow the logic below:

1. If the customer's account is locked or flagged (their account.status is suspected fraud" or
"unpaid balance"):

Inform the customer that you cannot proceed with the address change due to
account restrictions.


### Set address.change.outcome to "denied".


1. If the customer's account is active and eligible for updates:


### Proceed to Step 2.


1. Otherwise, if the system is unable to determine the account status or if there is insufficient
information:

Inform the customer you cannot verify whether the address can be updated and
escalate to a human support
agent.


### [Image: unknown]



### Set Oaddress.change.outcome to "escalation".


Step 2: Use Ovalidate.address by providing the gcolected.new,addies to verify its
authenticity and deliverability. Then follow the logic below:

1. If the new address is not recognized or is outside of Company X's serviceable regions
(address value can only be "United States", "European Union" or "Canada", no other region
is supported):

Inform the customer that the address cannot be serviced or is invalid.


### Set @address.change.outcome to "denied".


1. If the address is recognized and deliverable:


### Proceed to Step 3.


1. If the address validation result is inconclusive or cannot be determined by the system:

Inform the customer you are unable to verify the address at this time and have
escalated the request.


### Set Oaddress.change.outcome to "escalation".


Step 3: Use Oupdate.customer.address by providing both Ocolected.Customer.e and
Ocolected.new,addtres to finalize the address update. Then follow the logic below:

1. If the address update is successtul:

Inform the customer that the address has been updated successtully.

1p
n tercom.com
10539969- 1- as e st practices-and-example:


### ====



### 9/12



### ====



## 5/19/25, 8:27 AM



### Fin Task best practices and examples Intercom Help



### # Address Change Request


Description: The goal of this task is to determine if a requested shipping address update for a
customer is valid, and if SO, to process it. By following the instructions below, you will verify and
update the shipping address in Company X's system.

Step 1: Use Oget.customer.prolie by providing the ID ocolected.Customer.e to retrieve the
customer's current account status. Then follow the logic below:

1. If the customer's account is locked or flagged (their account.status is suspected fraud" or
"unpaid balance"):

Inform the customer that you cannot proceed with the address change due to
account restrictions.


### Set address.change.outcome to "denied".


1. If the customer's account is active and eligible for updates:


### Proceed to Step 2.


1. Otherwise, if the system is unable to determine the account status or if there is insufficient
information:

Inform the customer you cannot verify whether the address can be updated and
escalate to a human support
agent.


### [Image: unknown]



### Set Oaddress.change.outcome to "escalation".


Step 2: Use Ovalidate.address by providing the gcolected.new,addies to verify its
authenticity and deliverability. Then follow the logic below:

1. If the new address is not recognized or is outside of Company X's serviceable regions
(address value can only be "United States", "European Union" or "Canada", no other region
is supported):

Inform the customer that the address cannot be serviced or is invalid.


### Set @address.change.outcome to "denied".


1. If the address is recognized and deliverable:


### Proceed to Step 3.


1. If the address validation result is inconclusive or cannot be determined by the system:

Inform the customer you are unable to verify the address at this time and have
escalated the request.


### Set Oaddress.change.outcome to "escalation".


Step 3: Use Oupdate.customer.address by providing both Ocolected.Customer.e and
Ocolected.new,addtres to finalize the address update. Then follow the logic below:

1. If the address update is successtul:

Inform the customer that the address has been updated successtully.

1p
n tercom.com
10539969- 1- as e st practices-and-example:


### ====



### 9/12



### ====



### ================



## 5/19/25, 8:27 AM



### ================



### # Fin Task best practices and examples Intercom Help



### Set Oaddress.change.outcome to "success".


1. If the address update fails for any reason (a system error or conflicting records):

Inform the customer you have escalated the issue to a human support agent.


### Set @address.change.outcome to "escalation".


End this task when: You fill in the value of the Qaddress.change.outcome variable with a
status of either "denied", "success", or "escalation". No other value is valid.

Guidance: Be clear about which regions are supported. When confirming a successful address
change, remind the customer this will affect all future shipments.


### # Loyalty Points Adjustment


Description: The goal of this task is to determine if a customer's request for a loyalty points
adjustment is valid, and if SO, to carry out that adjustment. By following these instructions, you
will review the customer's loyalty account status, validate the request, and then adjust the
points accordingly in Company X's system.

Step 1: Use Oget.loyalty.prorle with the ID @collected.loyalry.member.o to retrieve the
member's account status. Then follow the logic:


### [Image: unknown]



### =



## N



### =


1. If the loyalty account is inactive, suspended, or flagged for suspicious activity:

Inform the customer that their account is not eligible for a points adjustment at this
time.


### Set Opoints.adjustment.outcome to "denied".


1. If the account is in good standing:


### Proceed to Step 2.


1. Otherwise, if the system cannot determine the account status:

Inform the customer you cannot verify their account and will escalate this matter to a
support specialist.


### Set Opoints.adjustment.outcome to "escalation".


Step 2: Use Caudi_oyaly.activiy by providing Ocollected.loyalrt.member.d and
ocolected.ponts.adjustmenteques to review recent loyalty transactions and see if the
request is justified. Then:

1. If the requested adjustment pertains to a transaction outside the claim window (claim date
is more than 90 days ago):

Inform the customer that the request cannot be granted due to program policies.


### Set Opoints.adustment.outcome to "denied".


1. If the request is valid (for example, points were missed from a recent eligible purchase):


### Proceed to Step 3.



### =====



### 10/12



### =====


auy
ercom.com 1I en/ ar Ey/05990)-m-task e st practices-and-example:


### ================



## 5/19/25, 8:27 AM



### ================



### # Fin Task best practices and examples Intercom Help



### Set Oaddress.change.outcome to "success".


1. If the address update fails for any reason (a system error or conflicting records):

Inform the customer you have escalated the issue to a human support agent.


### Set @address.change.outcome to "escalation".


End this task when: You fill in the value of the Qaddress.change.outcome variable with a
status of either "denied", "success", or "escalation". No other value is valid.

Guidance: Be clear about which regions are supported. When confirming a successful address
change, remind the customer this will affect all future shipments.


### # Loyalty Points Adjustment


Description: The goal of this task is to determine if a customer's request for a loyalty points
adjustment is valid, and if SO, to carry out that adjustment. By following these instructions, you
will review the customer's loyalty account status, validate the request, and then adjust the
points accordingly in Company X's system.

Step 1: Use Oget.loyalty.prorle with the ID @collected.loyalry.member.o to retrieve the
member's account status. Then follow the logic:


### [Image: unknown]



### =



## N



### =


1. If the loyalty account is inactive, suspended, or flagged for suspicious activity:

Inform the customer that their account is not eligible for a points adjustment at this
time.


### Set Opoints.adjustment.outcome to "denied".


1. If the account is in good standing:


### Proceed to Step 2.


1. Otherwise, if the system cannot determine the account status:

Inform the customer you cannot verify their account and will escalate this matter to a
support specialist.


### Set Opoints.adjustment.outcome to "escalation".


Step 2: Use Caudi_oyaly.activiy by providing Ocollected.loyalrt.member.d and
ocolected.ponts.adjustmenteques to review recent loyalty transactions and see if the
request is justified. Then:

1. If the requested adjustment pertains to a transaction outside the claim window (claim date
is more than 90 days ago):

Inform the customer that the request cannot be granted due to program policies.


### Set Opoints.adustment.outcome to "denied".


1. If the request is valid (for example, points were missed from a recent eligible purchase):


### Proceed to Step 3.



### =====



### 10/12



### =====


auy
ercom.com 1I en/ ar Ey/05990)-m-task e st practices-and-example:


### ================



## 5/19/25, 8:27 AM



### ================



### # Fin Task best practices and examples Intercom Help


1. If the audit returns inconclusive results (no matching transaction found or partial data only):

Inform the customer that further investigation is required, and you are escalating the
matter to a human agent.


### Set opoints.aqustment.outcome to "escalation".


Step 3: Use Oadustloyaly.ponts by providing Ocollected.loyalty.member.d and the
@collected.points.aqustment.request amount to finalize the points adjustment. Then:

1. If the points adjustment is processed successfully:

e Inform the customer that their loyalty balance has been updated.


### e Set Opoints.adjustment.outcome to "success".


1. If the adjustment fails due to a system error or contlicting records:

Inform the customer that you were unable to complete the request and have
escalated it for manual review.


### Set Opoints.adjustment.outcome to "escalation".


End this task when: You assign the Opoints.adjustment.outcome a final value of "denied",
"success", or escalation". No other values are valid.

Guidance: When a points adjustment is successful, reference the specific transaction that
generated the points. Be informative about program policies when denying requests.


### [Image: unknown]



### =



## Z



### =



### [Image: unknown]



### [Image: unknown]



### Need more help? Get support from our Community. Forum


Find answers and get help from Intercom Support and Community Experts


### # Related Articles



### [Image: unknown]



### Fin Al Agent explained



### Best practices for using Data connectors with Fin



### Give Fin Tasks betal



### Fin Guidance best practices



### Navigating Fin from setup to deploy


ILL
tercom.com n ar 10539969-mn-ask-best practices-and-example:


### =====



### 11/12



### =====



### ================



## 5/19/25, 8:27 AM



### ================



### # Fin Task best practices and examples Intercom Help


1. If the audit returns inconclusive results (no matching transaction found or partial data only):

Inform the customer that further investigation is required, and you are escalating the
matter to a human agent.


### Set opoints.aqustment.outcome to "escalation".


Step 3: Use Oadustloyaly.ponts by providing Ocollected.loyalty.member.d and the
@collected.points.aqustment.request amount to finalize the points adjustment. Then:

1. If the points adjustment is processed successfully:

e Inform the customer that their loyalty balance has been updated.


### e Set Opoints.adjustment.outcome to "success".


1. If the adjustment fails due to a system error or contlicting records:

Inform the customer that you were unable to complete the request and have
escalated it for manual review.


### Set Opoints.adjustment.outcome to "escalation".


End this task when: You assign the Opoints.adjustment.outcome a final value of "denied",
"success", or escalation". No other values are valid.

Guidance: When a points adjustment is successful, reference the specific transaction that
generated the points. Be informative about program policies when denying requests.


### [Image: unknown]



### =



## Z



### =



### [Image: unknown]



### [Image: unknown]



### Need more help? Get support from our Community. Forum


Find answers and get help from Intercom Support and Community Experts


### # Related Articles



### [Image: unknown]



### Fin Al Agent explained



### Best practices for using Data connectors with Fin



### Give Fin Tasks betal



### Fin Guidance best practices



### Navigating Fin from setup to deploy


ILL
tercom.com n ar 10539969-mn-ask-best practices-and-example:


### =====



### 11/12



### =====



### ================



## 5/19/25, 8:27 AM



### ================



### ==================================================



### Fin Task best practices and examples Intercom Help



### ==================================================



### Did this answer your question?



### [Image: unknown]



### [Image: unknown]



### We run on Intercom



### [Image: unknown]



### =



## Z



### =



### [Table : unknown]



### Support



### Resources



## Product Changes



### Developers



### Blog



### Community



### Webinars



### Academy



### Company



### Home



### About



### Terms



### Privacy



### =====



### 12/12



### =====


nups
ercom.co:
39969-h1 in-tas e st practices-and-example:


### ================



## 5/19/25, 8:27 AM



### ================



### ==================================================



### Fin Task best practices and examples Intercom Help



### ==================================================



### Did this answer your question?



### [Image: unknown]



### [Image: unknown]



### We run on Intercom



### [Image: unknown]



### =



## Z



### =



### [Table : unknown]



### Support



### Resources



## Product Changes



### Developers



### Blog



### Community



### Webinars



### Academy



### Company



### Home



### About



### Terms



### Privacy



### =====



### 12/12



### =====


nups
ercom.co:
39969-h1 in-tas e st practices-and-example:
