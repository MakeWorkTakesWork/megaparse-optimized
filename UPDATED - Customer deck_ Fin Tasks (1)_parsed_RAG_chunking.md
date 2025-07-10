---
title: Untitled Document
document_type: guide
primary_topics: demo
last_preprocessed: 2025-06-04
---


### # Fin Tasks Beta


Teach Fin to handle complex requests like refunds and cancellations


### # What are Fin Tasks?


Fin Tasks allow customers to automate more complex processes. Such processes usually involve integration with external systems (one or multiple API calls) and complex business logic.

They often have a certain level of business risk: You want some level of control to ensure Fin definitely gets it right

# Example use cases:


### Cancel an order



### Refund a subscription



### Update personal details



### Change a booking



### Troubleshoot a technical issue



### See real use cases from our customers



### How is this different from ‘Fin Actions’



### How is this different from ‘Guidance’


Fin Actions  is great for simple use cases, such as use cases that require Fin to retrieve data e.g. GET Order Status.

However for more complex use cases that involve one or many of:


### Evaluating conditions



### Calling multiple APIs in a sequence


Fin Tasks give you more control and ensures your business logic is followed reliably.

Fin Guidance helps define Fin’s demeanour (e.g tone of voice, answer length, language, style) or general approaches for handling any situation (e.g. when to escalate). It is not meant to be used for Fin to handle more complex processes.


### Why is this better than traditional workflows?


Easier setup with natural language: Set up Fin Tasks effortlessly—no need for complex workflows or decision trees. A simple task description guides Fin’s responses.

Automate processes that required humans: Fin can now handle advanced tasks like troubleshooting or analyzing customer-submitted images—reducing manual workload while delivering fast, intelligent support

More natural, conversational experiences: No more rigid button flows—Fin engages customers conversationally, making interactions smoother and more intuitive.


### # How it works



## # View Demo



### # Customer experience



### # Core features



### # Available today in closed beta



### # Trigger description


Tell Fin when it should trigger the task. This describes the situation Fin should use the task, provide example customer queries, and could also call out situations where Fin should not use this task.


### Example: Use this if a customer asks to cancel their order



### # Instructions block


The instructions block allows you to tell Fin to perform a certain task in natural language. Fin will follow the defined steps, collect necessary data and context from customers, reference help articles, and perform actions as defined in the task.

Example: Check the customers order status and check details about the damage


### # AI-generated task instructions


Use AI to generate instructions from scratch, to help as a starting point for further refinement and adjustment to your own support processes.


### # Actions


Get data from an external system or perform an action e.g. cancel an order.


### # Example: Get orders for customerRefund an order



### # Wait for webhook


Allow Fin to wait for updates in your external systems before proceeding with the next steps of the task.

Example: Wait for identify verification to be complete in external app before proceeding with the task


### # Email verification before running an action


Send a one-time-password to verify someone's’ email address before triggering an action (i.e retrieving or updating data in an external system)


### # Test and preview


Preview and test tasks to understand when a Task is triggered and which steps Fin is following.


## # COMING SOON



### # See Fin’s thinking


See Fin’s thinking in real time so customers always know what’s happening and trust their issue is being handled


### # Get help from an expert


Get help from the Intercom “Tasks Squad” to get set up faster with Tasks.


### # Templates


Set up a Fin Task faster with ready-made templates for common support flows like refunds and account updates.


### # Coming soon



## # COMING SOON



### # Human in the loop COMING SOON


Let Fin get agent approval before proceeding to the next step of the task. If approved, Fin can continue the task.

Example: Let an agent review a refund request before Fin processes it


## # COMING SOON



### # Dynamic Visual UI


Fin can display interactive forms and product selections directly in Messenger—making data collection faster, more accurate, and more delightful for customers.


## # COMING SOON



### # Test specific personas


Test Fin Tasks with realistic user personas - like VIPs or new customers - to catch issues early and ensure every Task works as expected.
