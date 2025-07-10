---
title: Untitled Document
document_type: guide
primary_topics: sales, zendesk, salesforce
last_preprocessed: 2025-05-24
---


## 1/ [P2]Creating a Fin for Salesforce workspace is painful


After trying multiple things and asking people around in #fin-standalone-salesforce-workstream, it seems the best way to create a Fin for Salesforce workspace is to do the following:


### create a Fin for Zendesk workspace self-serve


go to https://intercomrades.intercom.com/admin/standalone/provisioning/


### "remove standalone from workspace"



## then opt it back in but for Salesforce


We should fix this, even if Fin for Salesforce is sales-led only (maybe by adding options in https://intercomrades.intercom.com/billing/my_apps OR in https://intercomrades.intercom.com/admin/standalone/provisioning/)

2/ [P2] Some content refers to Zendesk, but should instead refer to Salesforce

https://app.intercom.com/a/apps/e7lnoryj/knowledge-hub/overview

We probably should have a Syncing articles with Salesforce article under Learn. -Article Plan

3/ [P2] Content ingestion banner showing as successful despite no content. (This probably also happens on Fin for Zendesk workspaces)

4/ [⚠️ P1] Sync from Salesforce doesn’t work at all, and even though it doesn’t work, it marks “Salesforce” as “Enabled” under “Your content”

On my test workspace, I get a 404 Not Found error, but on Peter’s workspace, he gets a 500 error! (I put screenshots/GIFs from both)

404:

EVEN THOUGH I GOT a 404 ERROR, I still see Salesforce Enabled in Your content above 😓and refreshing doesn’t remove it.

500:

5/ [P2] Brian’s test workspace (left) shows a different Sources / Content pages than mine (right)

Probably missing feature flags, but maybe let’s kill these feature flags? It’s confusing 🙏

6a/ [P2] Some of the demo conversations mention Phone, WhatsApp or social channels. We should delete them. (This probably also happens on Fin for Zendesk workspaces)

https://app.intercom.com/a/inbox/e7lnoryj/inbox/shared/all/conversation/215468808938694

6b/ [P2] The Messenger demo conversation has a broken image + wrong link to Messenger install page. (This probably also happens on Fin for Zendesk workspaces)

7/ [P2] Clicking on “Create a snippet” (even without saving or editing the content) creates a snippet. (This probably also happens on Fin for Zendesk workspaces)

8/ [⚠️ P1] “Salesforce” is shown as a source when Snippets are in “Your content”, but not shown otherwise 😅 This might be related to issue 4 above.

When I have snippets, I see both “Snippets (1 of 1)” and “Salesforce” as Enabled.

When I delete that snippet and come back to that page, both are gone. There is no “Salesforce” enabled 😬

20-second GIF to show that:

9/ “Connect to sandbox” errors out on my Salesforce test workspace (probably because I don’t have a sandbox in my Salesforce test workspace).

Video on Slack if that helps: https://intercom.slack.com/files/U1YR4D003/F08MN0NU955/cannot_connect_sandbox.mov

Questions:


### Are we assuming customers have a sandbox?


Should this be “Connect to production” by default? or maybe have both options side by side instead of in a dropdown?

10/ [UX-confusion] Fin Identity: too many options - is that intended?

I managed to connect to production Salesforce (not sandbox). Am I supposed to see all these options under Fin AI Agent Identity?

11/ [UX-confusion] Email-to-case origins: I find that confusing. What does this mean?


### If we know that customers find this clear, then ignore me.


12/ [UX-confusion OR Bug?] My capybara.academy DNS outbound.intercom has a different value in my DNS server (top of screenshot below) than what Intercom wants (bottom of screenshot), but it shows as Authenticated.

13/ [UX-confusion] Clicking on “Intercom Messenger” takes us to different page depending on state of integration

When I click on “Intercom Messenger” in the Deploy page for the first time…


### … I get to this page…


… then I set up the Salesforce integration and might realise that I need content to turn Fin on…

… so I go back and add content, then come back to Deploy, and click on “Intercom Messenger”, but now I see a different page!

14/ [P3] “Intercom Messenger” in the nav bar isn’t clicked when I click on Deploy first and then go Intercom Messenger from the Deploy page.

15/ [P2] Going back to the “Get Started” page shows the welcome survey even though I filled it! Quite annoying.

This is after I filled it once, and finished connecting all of Fin for Salesforce, and after having the Messenger live too so it’s a really weird time to show this again 😅

16/ [P2] We show “Live” near Intercom Messenger’s title but not Salesforce Cases’ title. But they both are live in my test workspace.

17/ [P2] There’s double-scrolling the Salesforce Cases page.
