---
title: USER: I would like to build an application like Wappalyzer, but more focused on identifying customer management technologies, like CRM (i.e. salesforce, hubspot, dynamics), help centers/help desk (zendesk, freshdesk), chatbot and CX ai agents (ada ai agent, zendesk ai agent, agentforce on salesforce service cloud).
document_type: guide
primary_topics: sales, process, zendesk, salesforce
last_preprocessed: 2025-05-28
---

USER: I would like to build an application like Wappalyzer, but more focused on identifying customer management technologies, like CRM (i.e. salesforce, hubspot, dynamics), help centers/help desk (zendesk, freshdesk), chatbot and CX ai agents (ada ai agent, zendesk ai agent, agentforce on salesforce service cloud).


### Can you brainstorm off the below foundation?


Below is a practical redesign of each stage in the Wappalyzer-style pipeline so it can **zero-in on CRM, help-desk, support, and customer-engagement stacks** (e.g., Salesforce Service Cloud, Zendesk, Intercom, Freshdesk, HubSpot, Kustomer, Gorgias, Helpscout).


### ---



### ## 1  Fingerprint repository — upgrade the rule set


| Addition                                                               | Why it matters                                                             | Example rule (pseudo-JSON)                                     |                | | ---------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------- | -------------- | | **Widget-snippet regexes** for chat, ticket, and knowledge-base embeds | These tools expose tell-tale JS, CSS, or iframe URLs.                      | `"script": "https?://widget\\.intercom\\.io/widget/[a-z0-9]+"` |                | | **Cookie &amp; localStorage names**                                        | Many platforms drop IDs (e.g., `_zendesk_session`, `hubspotutk`).          | `"cookies": "_zendesk_session"`                                |                | | **CNAME &amp; A-record patterns** for support sub-domains                  | A domain like `support.example.com` often CNAMEs to `example.zendesk.com`. | `"dns": "CNAME.*\\.zendesk\\.com"`                             |                | | **API end-point regexes** captured in XHR trace                        | Modern SPAs call `https://example.zendesk.com/api/v2/...`.                 | `"xhr": "/api/v[12]/tickets"`                                  |                | | **SPF/DKIM DNS look-ups**                                              | Salesforce, HubSpot, etc. add `include:_spf.salesforce.com` to DNS.        | `"dns": "include:_spf\\.salesforce\\.com"`                     |                | | **Email web-form action targets**                                      | Hidden `&lt;form action="https://.../submit_ticket"&gt;`.                        | `"html": "&lt;form[^&gt;]+submit_ticket"`                            |                | | **Job-posting keywords** (optional enrichment)                         | Public careers pages leak “we use Zendesk” etc.                            | \`"html": "experience with (Zendesk                            | ServiceNow)"\` |


### Organise new techs into fine


grained categories:


## `"CRM" → "Salesforce", "HubSpot" …`



### `"Help Desk"` → "Zendesk", "Freshdesk" …



### `"Customer Engagement"` → "Intercom", "Drift" …



### ---



### ## 2  Content acquisition — collect richer artefacts



### 1. *



### # Multi



### # origin crawl**



### Start with the main URL,



### then automatically branch


to likely support hubs: `support.`, `help.`, `kb.`, `status.`, `/help`, `/hc`, `/desk`, `/tickets`, `/knowledge`. 2.


### # **Headless‐browser interaction script



### **



### After initial load,



### # **click elements



### ** that match chat



### launcher CSS classes (`.intercom



### launcher`, `.zE


...`) or “Contact Support” buttons to trigger widgets and XHRs.


### Record



### # **full network waterfall



### # ** (XHR URLs, websocket hosts). 3.



### # **DNS &amp; SMTP harvest



### **


Query A/CNAME/MX/TXT records once per domain; cache results for 24 h. 4.


### # **Optional: WHOIS &amp; LinkedIn mini



### scraper



### # ** for enrichment (detect “Zendesk Administrator” roles).



### ---



### ## 3  Detection engine — upgrade scoring logic


```python score = Σ(location_weight * pattern_confidence) # Boost rules tagged `crm_core`, `helpdesk_core` if tech in ["Zendesk", "Salesforce Service Cloud"]: score *= 1.25            # bias toward these verticals # Penalise stale signals (e.g., CDN-cached JS &gt; 1 year old) if asset_age &gt; 365: score *= 0.8 ```


### # **Cross


evidence fusion:

** recognise that `support.example.com` CNAMEs to `example.zendesk.com`


### and


the main site loads the Zendesk widget → raise confidence dramatically.


### # **Version inference from API headers



### ** (e.g., `x



### zendesk



### origin



### server: lion` → maps to v3.0).



### ---



### # ## 4  Post



### # processing tweaks


| Rule                                                                                                 | Purpose | | ---------------------------------------------------------------------------------------------------- | ------- | | **Implies** `SaaS Hosting → AWS` (don’t double-count infra)                                          |         | | **Excludes** “Freshdesk” vs. “Freshservice” when both match but only one is customer-facing          |         | | **Requires** “Intercom Messenger” *requires* “Intercom Platform” (ensures full stack attribution)    |         | | **Confidence decay** if only DNS evidence but no page-level artefact (could be unused legacy domain) |         |


### ---



### # ## 5  Delivery surfaces



### # **Bulk enrichment API



### ** returns an



### # **`apps: {crm: ..., helpdesk: ..., engagement: ...}`


** block with confidence %, version, and evidence list (widget, DNS, cookie).


## # **Sales



### ops CSV export



### # ** pre


columns for ICP work: `crm_name`, `crm_version`, `helpdesk_name`, `engagement_name`, `intercom_present (Y/N)`.


### ---



### # ## 6  Advanced tricks for harder targets


| Challenge                                              | Strategy                                                                               | | ------------------------------------------------------ | -------------------------------------------------------------------------------------- | | **Widgets behind consent banners**                     | Re-crawl after auto-accepting cookies via JS injection.                                | | **Shadow DOM encapsulation**                           | Use Chrome DevTools Protocol `DOM.getFlattenedDocument`.                               | | **First-party proxying** (chat JS served from own CDN) | Hash &amp; compare script content against known vendor hashes (Shannon entropy + SimHash). | | **Server-side only ticketing** (no widget)             | Correlate SPF/DKIM, LinkedIn job titles, and `robots.txt` links to `/hc/`, `/tickets`. |


### ---



### ### Putting it into practice


1. **Extend the JSON fingerprints** with 200-plus CRM/help-desk-specific patterns. 2. **Embed a Selenium/Puppeteer flow** that opens the chat bubble and waits for network calls. 3. **Run DNS → page → interaction sweep**; pipe artefacts to updated detector. 4. **Store enriched results**; surface in your prospecting dashboards to filter by Zendesk vs. Salesforce Service Cloud vs. Intercom footprints.

These tweaks convert a general web-tech scanner into a *precision instrument* for **customer-service stack intelligence**, giving sales or competitive-intel teams the detail they need to tailor pitches—or, in your case, to spot where Fin can replace or augment an existing toolset.


### ----------------------------------


CLAUDE:


### # Thought process



### # 9s


The user is interested in building a specialized application similar to Wappalyzer, but focused specifically on customer management technologies. They've provided a comprehensive document that outlines a practical redesign of a Wappalyzer-style pipeline targeted at CRM, help-desk, support, and customer-engagement stacks.

Let me analyze what they've provided and brainstorm extensions and improvements to this foundation. The document covers:

1. Fingerprint repository upgrades 2. Content acquisition improvements 3. Detection engine enhancements 4. Post-processing rules 5. Delivery surfaces 6. Advanced techniques for harder targets


### ⠀


They're particularly interested in:


## CRM systems (Salesforce, HubSpot, Dynamics)



### Help centers/help desk (Zendesk, Freshdesk)


Chatbot and CX AI agents (Ada AI Agent, Zendesk AI Agent, Agentforce on Salesforce Service Cloud) I should brainstorm:

1. Additional detection patterns for AI agents specifically 2. New data sources and detection methods 3. Architecture and implementation approaches 4. Competitive differentiation strategies 5. Business model considerations 6. Technical challenges and solutions

``` scratchpad[CONTEXT_ANALYSIS] - Building a Wappalyzer-style tool specialized for customer management tech detection - Focus areas: CRM, help desk, chatbots, CX AI agents - Foundation provided covers detection patterns, crawling strategies, and delivery methods - Need to extend focus on AI agent detection (Ada, Zendesk AI, Agentforce, etc.)

[METHODOLOGY] - Analyze current foundation and identify gaps - Brainstorm AI-specific detection patterns - Propose architectural improvements - Consider business/competitive positioning - Address technical challenges unique to AI agent detection

[KEY_FINDINGS] - AI agents often have subtle fingerprints compared to traditional tools - Need deeper behavioral analysis beyond static pattern matching - Real-time interaction required to trigger AI responses - Privacy/ethical considerations for automated interactions

[SYNTHESIS] Multiple enhancement vectors available focusing on AI agent specialization </thinking>

This is an excellent foundation! Let me brainstorm extensions and improvements, particularly for detecting modern AI agents and chatbots:


### # ## 🎯 AI Agent Detection Enhancements


### 1. **AI-Specific Fingerprints** ```javascript // AI Agent Detection Patterns { "ada_ai": { "script": "https?://.*\\.ada\\.support/", "websocket": "wss?://.*\\.ada\\.support/", "cookies": "ada_.*", "localStorage": "ada_session_.*", "dom": "data-ada-.*|ada-embed|ada-button" }, "zendesk_answer_bot": { "script": "answer_bot.*\\.zdassets\\.com", "xhr": "/api/v2/answer_bot/", "headers": "x-zendesk-answer-bot-.*" }, "salesforce_agentforce": { "script": "agentforce.*\\.force\\.com", "xhr": "/services/data/.*/sobjects/AgentWork", "cookies": "sfdc-agentforce.*" }, "intercom_fin": { "xhr": "/messenger/web/fin/.*", "localStorage": "intercom-fin-.*", "headers": "x-intercom-fin-version" } } ```


### ### 2. *



### # Behavioral Detection Strategies**


``` &]:odd:bg-bg-500/10">Detection MethodPurposeImplementation&]:odd:bg-bg-500/10">Response Time AnalysisAI agents respond faster than humansMeasure chat response latency patterns&]:odd:bg-bg-500/10">Natural Language PatternsAI has consistent formatting/structureAnalyze message consistency scores&]:odd:bg-bg-500/10">Capability ProbingTest for AI-specific featuresSend specific queries that trigger AI responses&]:odd:bg-bg-500/10">Widget Mutation ObservationAI widgets have unique DOM behaviorsTrack dynamic element changes&]:odd:bg-bg-500/10">Network Traffic PatternsAI makes predictable API callsMonitor request sequences ```


### ### 3. *



### # Multi



### # Stage Detection Pipeline**


``` pythonclass CustomerStackDetector: def __init__(self): self.stages = [ DNSReconStage(),      # Quick DNS/CNAME checks StaticAnalysisStage(), # HTML/JS fingerprinting InteractionStage(),    # Trigger widgets/chats BehavioralStage(),     # AI behavior analysis EnrichmentStage()      # LinkedIn/job posting scan ]

# async def detect(self, domain):


### signals = {}


# for stage in self.stages:


### # signals.update(await stage.analyze(domain))



### # return self.score_and_classify(signals)



### ```



### ### 4. *



### # Advanced AI Agent Detection**



### # Conversational Probes:**


``` javascriptconst AI_PROBE_MESSAGES = [ "What are your business hours?",  // Common AI training "Can you help me with [RANDOM_PRODUCT]?", // Tests knowledge boundaries "Tell me a joke", // Many AIs have this disabled "What's 2+2?", // Simple computation test "Transfer to human agent" // Triggers handoff behavior ]; ```


### # Response Analysis:**


Typing indicators (AI often shows consistent "typing" duration)

Message structure (AI tends to use bullet points, numbered lists)


### Emoji usage patterns


Response time distribution (AI: consistent, Human: variable) ### 5.


### # **Extended Data Sources



### **


``` &]:odd:bg-bg-500/10">SourceValueCollection Method&]:odd:bg-bg-500/10">Status PagesOften list integrationsCrawl status.*.com, /status&]:odd:bg-bg-500/10">API DocumentationReveals tech stackScan /api, /developers, docs.*&]:odd:bg-bg-500/10">Customer ReviewsMention support toolsParse G2, Capterra, TrustRadius&]:odd:bg-bg-500/10">Security HeadersPlatform-specific headersAnalyze x-powered-by, custom headers&]:odd:bg-bg-500/10">Job Postings"Experience with [Tool]"Indeed, LinkedIn job API&]:odd:bg-bg-500/10">SSL CertificatesSubdomain enumerationCertificate Transparency logs&]:odd:bg-bg-500/10">Robots.txtHidden admin pathsParse for /admin, /agent, /support ```


### ### 6. *



### # Architecture Considerations**


``` yamlarchitecture: data_pipeline: - crawler: type: "headless_cluster" browsers: ["Chrome", "Firefox", "Safari"] interaction_scripts: true - analyzer: ml_models: - text_classifier: "identify_ai_responses" - pattern_matcher: "tech_fingerprints" rules_engine: "yaml_based" - storage: primary: "PostgreSQL" cache: "Redis" embeddings: "Pinecone"  # For AI response similarity

# api_design:


### # /detect/single



### # Real



### # time single domain



### # /detect/bulk



### # Batch processing



### # /monitor/changes



### # Track stack changes



### # /enrich/contacts



### # Find decision makers



### ```



### ### 7. *



### # Competitive Differentiation**



### # Unique Features:**


1. **AI Personality Detection** - Identify which LLM powers the agent 2. **Integration Mapping** - Show how tools connect (Salesforce ↔ Zendesk) 3. **Migration Readiness Score** - How easy to replace current stack 4. **Cost Estimation** - Estimate their current spend 5. **Performance Benchmarking** - Response times, resolution rates


### ⠀



### ### 8. *



### # Privacy



### # Conscious Design**


``` pythonclass EthicalCrawler: def __init__(self): self.respect_robots = True self.rate_limit = RateLimiter(max_per_minute=10) self.interaction_limits = { 'chat_messages': 3,  # Max probe messages 'form_submissions': 0,  # Never submit real forms 'session_duration': 60  # seconds } ```


### ### 9. *



### # Business Model Extensions**


``` &]:odd:bg-bg-500/10">TierFeaturesTarget User&]:odd:bg-bg-500/10">Free API100 lookups/month, basic detectionDevelopers&]:odd:bg-bg-500/10">Sales ProUnlimited + CRM integration + alertsSales teams&]:odd:bg-bg-500/10">EnterpriseCustom fingerprints + API + white-labelTech vendors&]:odd:bg-bg-500/10">IntelligenceCompetitor tracking + market analysisStrategy teams ```


### ### 10. *



### # Technical Challenges & Solutions**



### # **Challenge: Shadow DOM & Iframes**


``` javascript// Solution: Multi-context execution async function detectInAllContexts(page) { const contexts = await page.frames(); for (const frame of contexts) { try { await frame.evaluate(detectionScript); } catch (e) { // Cross-origin frames will fail } } } ```


### # Challenge: Anti



### # Bot Measures**



### Rotate user agents intelligently



### Use residential proxies for hard targets



### Implement human



### like interaction patterns



### Respect rate limits and implement backoff ### 11.



## # **AI



### Specific Enrichment



### **



### ```



### # sql-



### # Track AI adoption trends



### # CREATE TABLE ai_agent_adoption (



### domain VARCHAR(255),



### detected_date DATE,



### ai_platform VARCHAR(100),



### previous_platform VARCHAR(100),



### confidence_score FLOAT,



### # evidence JSONB



### );



### # Alert on platform changes



### # CREATE TRIGGER platform_change_alert



### # AFTER UPDATE ON company_tech_stack



### # WHEN NEW.helpdesk_platform != OLD.helpdesk_platform;



### ```



### ### 12. *



### # Future



### # Proofing**



### # **Plugin Architecture



### # ** for new AI platforms



### # **ML Model Updates



### ** for evolving AI behaviors



### # **Community Contributions



### # ** for fingerprint rules



### # **Webhook System



### # ** for change notifications



### # **GraphQL API


** for flexible data queries This specialized approach would give you a significant edge over general

purpose tools like Wappalyzer, particularly for sales teams targeting companies that might benefit from modern AI customer service solutions like Fin.


### -------------------------------------------------------


USER: So, why don't you do a test run on the company cooperators.ca

See what you can find using the tools at your disposal, start with brave-search, then run an mcp-linkup search-web, and utilize the firecrawl capabilities to explore the site and nested sites to find whatever intel you can.


### ---------------------------------


CLAUDE:

I'll analyze cooperators.ca to identify their customer management technologies. Let me start with a broad search to understand the company.Let me search more specifically about The Co-operators Group:Now let me do a deeper search using mcp-linkup to find more specific information about their technology:Now let me directly analyze the Co-operators website using firecrawl. First, let me map their site to find relevant URLs:Let me scrape the main contact page and online services pages to look for technology indicators:Let me check their online services page for more technology indicators:Let me analyze their client care page to look for any support technology indicators:Let me do a deep research to find more comprehensive information about their technology stack:## Summary: The Co-operators Customer Support Technology Analysis

Based on my comprehensive analysis of The Co-operators' website and digital footprint, here are my findings:

# ### Current Technology Indicators Found:

1. **No Direct Evidence of Major Support Platforms** - No Zendesk implementation detected - No Salesforce Service Cloud indicators found - No Intercom, Freshdesk, or other common helpdesk widgets present - No visible chat bot or AI agent technology

1. **What They Are Using:** - **Traditional Support Channels:** - Phone-based support with different numbers for various services - Email support through specific addresses (client_service_support@cooperators.ca, etc.) - Web forms for various services

# **Online Services Portal:


### **



### Custom



### built online services platform for policy management



### Self



### service capabilities for customers to manage accounts



### Appears to be a proprietary system rather than a third



### party platform



### # **Third


Party Services Identified:


### **



### ARAG Legal Solutions Inc. (for Legal Assistance Helpline)



### Analytics tools (Yahoo Analytics, Bing tracking)



### Content delivery networks for static assets


1. **Technology Infrastructure:** - The website appears to use a custom-built system - No identifiable CRM or helpdesk JavaScript libraries detected - No chat widget scripts or customer service platform indicators - Forms submit to internal endpoints rather than third-party services

# ### Key Insights:

1. **Legacy Approach:** The Co-operators appears to be using a more traditional, internally-managed customer support approach rather than modern SaaS platforms like Zendesk or Salesforce Service Cloud.

1. **Modernization Opportunity:** The deep research report indicates that the insurance industry, including companies like The Co-operators, is in transition from legacy systems to modern platforms. However, based on the current website analysis, they haven't yet implemented these visible customer-facing technologies.

1. **Internal Systems:** They likely use internal CRM and support systems that aren't exposed through their public-facing website, which is common for large insurance companies with established infrastructure.

# ### Recommendation for Fin.ai:

The Co-operators represents a significant opportunity for Fin.ai's solutions because: - They currently lack visible modern AI-powered customer service technology - Their traditional phone/email support model could benefit from AI automation - The insurance industry trend toward platforms like Zendesk and Salesforce Service Cloud suggests they may be evaluating such solutions - Their large customer base (as a major Canadian insurer) would benefit from AI-driven efficiency improvements

This makes them an ideal prospect for Fin.ai's AI agent solutions, whether as a standalone implementation or integrated with a future helpdesk platform migration.

USER (ME): conduct a comprehensive search of their customer support reputation as it stands. Are they renowned, or losing customers and opportunities for lack of response? Check any and all sources that might bring forth relevant intel, forums, cx websites, blogs, linkedin, whatever you can. Use the same tools as before.

Thought process3sThe user wants me to conduct a comprehensive search on The Co-operators' customer support reputation. I should look for:


| Customer | Forums | Blogs | LinkedIn | Any |
| --- | --- | --- | --- | --- |
| ### I'll | use multiple | search | tools to | gather this intelligence. |
| I'll conduct | a comprehensive | search | to investigate | The Co-operators' customer support reputation. Let me search multiple sources for relevant intelligence. |
| { `count`: | 15, `query`: | `\"The | Co-operators\" | insurance customer service reviews complaints Canada` } |
| Title: | The Co-operators | Reviews | | Read | Customer Service Reviews of cooperators.ca Description: Do you agree with <strong>The</strong> <strong>Co</strong>-<strong>operators</strong>&#x27;s TrustScore? Voice your opinion today and hear what 79 <strong>customers</strong> have already said. URL: https://ca.trustpilot.com/review/cooperators.ca |
| Title: | r/AskACanadian | on Reddit: | Anyone | can share their experience with the insurance company The co-operators? Description: Their price is the best but saw some bad <strong>reviews</strong>, although almost all <strong>insurance</strong> companies are in similar situations. Are they bad? URL: https://www.reddit.com/r/AskACanadian/comments/12i36g0/anyone_can_share_their_experience_with_the/ |
| Title: | The Co-operators | Group Limited | - Ombuds | Office | BBB Complaints | Better Business Bureau Description: View <strong>complaints</strong> of <strong>The</strong> <strong>Co</strong>-<strong>operators</strong> Group Limited - Ombuds Office filed with BBB. BBB helps resolve disputes with <strong>the</strong> <strong>services</strong> or products a business provides. URL: https://www.bbb.org/ca/on/guelph/profile/insurance-companies/the-co-operators-group-limited-ombuds-office-0107-1194627/complaints |
| Title: | Service | Review | Panel - | The Co-operators Description: A panel of client volunteers. As a <strong>co</strong>-<strong>operative</strong>, we’re closely connected to our clients and focused on serving you better. URL: https://www.cooperators.ca/en/client-care/service-review-panel |
| Title: | The Co-operators | Home Insurance | Quotes | & Reviews | LowestRates.ca Description: Get the best home <strong>insurance</strong> quote from <strong>The</strong> <strong>Co</strong>-<strong>operators</strong> today! Compare coverage options &amp; find the lowest rates available! Instant. Online. Free. URL: https://www.lowestrates.ca/insurance/home/the-co-operators |
| Title: | Consumer | information | Description: | <strong>The</strong> <strong>Co</strong>-<strong>operators</strong> is committed to the fair treatment of consumers. This is embedded in the organization’s <strong>co</strong>-<strong>operative</strong> values, culture, and ethics. URL: https://www.cooperators.ca/en/client-care/consumer-information |
| Title: | The Co-operators | Reviews | | Read | Customer Service Reviews of cooperators.ca | 2 of 4 Description: Do you agree with <strong>The</strong> <strong>Co</strong>-<strong>operators</strong>&#x27;s TrustScore? Voice your opinion today and hear what 78 <strong>customers</strong> have already said. URL: https://www.trustpilot.com/review/cooperators.ca?page=2 |


Title: The Co-operators | BBB Business Profile | Better Business Bureau Description: Not BBB Accredited. <strong>Insurance</strong> <strong>Services</strong> Office in Langley, BC. See BBB rating, <strong>reviews</strong>, <strong>complaints</strong>, and more. URL: https://www.bbb.org/ca/bc/langley/profile/insurance-services-office/the-co-operators-0037-125134

Title: Co-Operators General Insurance Review & Complaints: Auto, Home, Life & Business Insurance (2025) | ExpertInsuranceReviews.com Description: Premiums Claims Feedback Financial Strength One of the more recognizable names in the Canadian <strong>insurance</strong> industry, <strong>The</strong> <strong>Co</strong>-<strong>Operators</strong> is a full-<strong>service</strong> <strong>insurer</strong> covering both personal and commercial lines. As a <strong>co</strong>-<strong>operative</strong>, <strong>the</strong> company is owned by its member organizations, and profits are shared ... URL: https://www.expertinsurancereviews.com/co-operators-general/

Title: Concerns and Complaints Description: At <strong>The</strong> <strong>Co</strong>-<strong>operators</strong>, we aim to provide the best client experience. Your honest feedback will help us continue to provide you with quality <strong>services</strong> and products. URL: https://www.cooperators.ca/en/client-care/compliments-concerns

Title: Complaint Resolution Process - The Co-operators Description: If you have a concern relating to the processing of your claim, here are the steps to guide you through <strong>the</strong> <strong>complaints</strong> resolution process. URL: https://www.cooperators.ca/en/insurance/travel/claims/complain-process

Title: The Co-operators Reviews: What Is It Like to Work At The Co-operators? | Glassdoor Description: 659 <strong>The</strong> <strong>Co</strong>-<strong>operators</strong> <strong>reviews</strong>. A free inside look at company <strong>reviews</strong> and salaries posted anonymously by employees. URL: https://www.glassdoor.ca/Reviews/The-Co-operators-Reviews-E18308.htm

Title: The Co-operators Car Insurance Reviews - RateLab.ca Description: Consumer <strong>complaints</strong> against the company include difficulty contacting <strong>customer</strong> <strong>service</strong> and issues with handling claims. BBB (Better Business Bureau): <strong>The</strong> <strong>Co</strong>-<strong>operators</strong> is accredited by the BBB and is rated A+. There are few <strong>customer</strong> <strong>reviews</strong> available on the website of the BBB. We value your feedback and would love to hear about your experience with <strong>The</strong> <strong>Co</strong>-<strong>operators</strong> auto <strong>insurance</strong>. If you are a <strong>customer</strong> of <strong>The</strong> <strong>Co</strong>-<strong>operators</strong> <strong>in</strong> <strong>Canada</strong>... URL: https://www.ratelab.ca/reviews/car-insurance-reviews/the-co-operators/

Title: The Co-operators Group Limited - Ombuds Office | BBB Business Profile | Better Business Bureau Description: Not BBB Accredited. <strong>Insurance</strong> Companies in Guelph, ON. See BBB rating, <strong>reviews</strong>, <strong>complaints</strong>, and more. URL: https://www.bbb.org/ca/on/guelph/profile/insurance-companies/the-co-operators-group-limited-ombuds-office-0107-1194627

Title: Co-operators Car Insurance Review, Cost, Contact 2025 Description: Our updated <strong>Co</strong>-<strong>operators</strong> car <strong>insurance</strong> <strong>review</strong> - Coverage, cost, phone number, &amp; more. Compare free car <strong>insurance</strong> quotes using our free tool. URL: https://hellosafe.ca/en/car-insurance/co-operators

Good initial results. Let me check the Trustpilot reviews more closely and search for Reddit discussions and other forums.


### {



### `url`: `https://ca.trustpilot.com/review/cooperators.ca`,



### # `formats`: [



### # `markdown`



### ],



### # `onlyMainContent`: true



### }


# ![](https://x.adroll.com/attribution/trigger?fpc=16b8b80f8e41bb25203eb8ce99222710&advertisable_eid=6U7APKK4E5F45KVW4MS4AL&conversion_type=PageView&conversion_value=0.00&currency=USC&flg=1&pv=3120094920.848082&arrfrr=https%3A%2F%2Fca.trustpilot.com%2Freview%2Fcooperators.ca)

# ![](https://d.adroll.com/cm/b/out?adroll_fpc=16b8b80f8e41bb25203eb8ce99222710

# 1748481570283&flg=1&pv=3120094920.848082&arrfrr=https%3A%2F%2Fca.trustpilot.com%2Freview%2Fcooperators.ca&advertisable=6U7APKK4E5F45KVW4MS4AL)![](https://d.adroll.com/cm/bombora/out?adroll_fpc=16b8b80f8e41bb25203eb8ce99222710

# 1748481570283&flg=1&pv=3120094920.848082&arrfrr=https%3A%2F%2Fca.trustpilot.com%2Freview%2Fcooperators.ca&advertisable=6U7APKK4E5F45KVW4MS4AL)![](https://d.adroll.com/cm/experian/out?adroll_fpc=16b8b80f8e41bb25203eb8ce99222710

# 1748481570283&flg=1&pv=3120094920.848082&arrfrr=https%3A%2F%2Fca.trustpilot.com%2Freview%2Fcooperators.ca&advertisable=6U7APKK4E5F45KVW4MS4AL)![](https://d.adroll.com/cm/g/out?adroll_fpc=16b8b80f8e41bb25203eb8ce99222710

# 1748481570283&flg=1&pv=3120094920.848082&arrfrr=https%3A%2F%2Fca.trustpilot.com%2Freview%2Fcooperators.ca&advertisable=6U7APKK4E5F45KVW4MS4AL)![](https://d.adroll.com/cm/index/out?adroll_fpc=16b8b80f8e41bb25203eb8ce99222710

# 1748481570283&flg=1&pv=3120094920.848082&arrfrr=https%3A%2F%2Fca.trustpilot.com%2Freview%2Fcooperators.ca&advertisable=6U7APKK4E5F45KVW4MS4AL)![](https://d.adroll.com/cm/l/out?adroll_fpc=16b8b80f8e41bb25203eb8ce99222710

# 1748481570283&flg=1&pv=3120094920.848082&arrfrr=https%3A%2F%2Fca.trustpilot.com%2Freview%2Fcooperators.ca&advertisable=6U7APKK4E5F45KVW4MS4AL)![](https://d.adroll.com/cm/n/out?adroll_fpc=16b8b80f8e41bb25203eb8ce99222710

# 1748481570283&flg=1&pv=3120094920.848082&arrfrr=https%3A%2F%2Fca.trustpilot.com%2Freview%2Fcooperators.ca&advertisable=6U7APKK4E5F45KVW4MS4AL)![](https://d.adroll.com/cm/o/out?adroll_fpc=16b8b80f8e41bb25203eb8ce99222710

# 1748481570283&flg=1&pv=3120094920.848082&arrfrr=https%3A%2F%2Fca.trustpilot.com%2Freview%2Fcooperators.ca&advertisable=6U7APKK4E5F45KVW4MS4AL)![](https://d.adroll.com/cm/outbrain/out?adroll_fpc=16b8b80f8e41bb25203eb8ce99222710

# 1748481570283&flg=1&pv=3120094920.848082&arrfrr=https%3A%2F%2Fca.trustpilot.com%2Freview%2Fcooperators.ca&advertisable=6U7APKK4E5F45KVW4MS4AL)![](https://d.adroll.com/cm/pubmatic/out?adroll_fpc=16b8b80f8e41bb25203eb8ce99222710

# 1748481570283&flg=1&pv=3120094920.848082&arrfrr=https%3A%2F%2Fca.trustpilot.com%2Freview%2Fcooperators.ca&advertisable=6U7APKK4E5F45KVW4MS4AL)![](https://d.adroll.com/cm/taboola/out?adroll_fpc=16b8b80f8e41bb25203eb8ce99222710

# 1748481570283&flg=1&pv=3120094920.848082&arrfrr=https%3A%2F%2Fca.trustpilot.com%2Freview%2Fcooperators.ca&advertisable=6U7APKK4E5F45KVW4MS4AL)![](https://d.adroll.com/cm/triplelift/out?adroll_fpc=16b8b80f8e41bb25203eb8ce99222710

# 1748481570283&flg=1&pv=3120094920.848082&arrfrr=https%3A%2F%2Fca.trustpilot.com%2Freview%2Fcooperators.ca&advertisable=6U7APKK4E5F45KVW4MS4AL)![](https://d.adroll.com/cm/x/out?adroll_fpc=16b8b80f8e41bb25203eb8ce99222710

# 1748481570283&flg=1&pv=3120094920.848082&arrfrr=https%3A%2F%2Fca.trustpilot.com%2Freview%2Fcooperators.ca&advertisable=6U7APKK4E5F45KVW4MS4AL)

Looks like you’re in the United States. [Go to the American Trustpilot site](https://www.trustpilot.com/review/cooperators.ca)


### # [![The Co


operators logo](https://consumersiteimages.trustpilot.net/business


### units/5c7e2ed4b62d9a000147ac53



### 198x149


# 1x.jpg)](http://cooperators.ca/?utm_medium=company_profile&utm_source=trustpilot&utm_campaign=logo_click)

# [Visit website](http://cooperators.ca/?utm_medium=company_profile&utm_source=trustpilot&utm_campaign=domain_click)


### Unclaimed profile



### # # The Co



### # operatorsReviews79


# ![TrustScore 1.5 out of 5](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.5.svg)


### 1.6


# [Insurance Agency](https://ca.trustpilot.com/categories/insurance_agency)

[Write a review](https://ca.trustpilot.com/evaluate/cooperators.ca) [Visit website](http://cooperators.ca/?utm_medium=company_profile&utm_source=trustpilot&utm_campaign=domain_click)

# [Write a review](https://ca.trustpilot.com/evaluate/cooperators.ca)


### # ![](https://businessunitprofile



### # cdn.trustpilot.net/businessunitprofile



### # consumersite/public/trustpilot



### # shield.svg)


Companies on Trustpilot can’t offer incentives or pay to hide any reviews.


### ## See what reviewers are saying


![Rated 1 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.svg)

I’ve acquired a new vehicle and was needing car insurance. I’ve been calling everyday for a week, and been put on waiting 7h each day, and after trying to reach them by email, they suggested that i need to look for another insurance.

0 proficiency, 0 service, I don’t recommend wasting your time with them! See more

![Rated 1 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.svg)

If I could leave 0 stars, I would have. If you are looking into home or auto insurance, I beg you to look elsewhere and not make the mistake I did. They are just awful, they increase premiums every year without cause or the ability to detail the reasons behind the increases. They are incredibly slow to respond during any actual claim processes and will find any way they can to either not provide coverage or provide the bare minimum. Their 'trusted' contractor list is full of poorly reviewed contractors who seem as crooked as cooperators are. Please go elsewhere, you will thank me later.See more

![Rated 1 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.svg)

I am 58 years old and have never made a claim in my life. Recently struck a wild turkey while driving. Cooperators have been completely negligent in addressing the repair. Phone calls and emails are not responded to. I WILL be dropping Cooperators as soon as my term is finaished. AVOID AT ALL COSTSSee more

![Rated 1 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.svg)

Raised my premium approx a month later then cut my insurance off due to nonpayment( false). NOW COOPERATORS will not fix thier mistake. I've never had any driving infractions but have to pay the premiums of a convicted dui driver. This company does not deserve your money find a better more reputable company. Shame on you Cooperators.See more


### See all 79 reviews



### # ## Company details


1. [Insurance Agency](https://ca.trustpilot.com/categories/insurance_agency)

1. [Insurance Broker](https://ca.trustpilot.com/categories/insurance_broker)

1. [Insurance Company](https://ca.trustpilot.com/categories/insurance_company)


### #### Information provided by various external sources


The Co-operators Group Limited, founded in 1945, is a Canadian insurance co-operative owned by 44 members including co-ops, credit union centrals and representative farm organizations.


### # ## Contact info



### Macdonell Street 130, N1H 3T9, Guelph, Canada


[cooperators.ca](http://cooperators.ca/?utm_medium=company_profile&utm_source=trustpilot&utm_campaign=domain_click)


### 1.6



### #### Bad


# ![TrustScore 1.5 out of 5](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.5.svg)


### # 79 reviews



### 5



### # star



### 4



### # star



### 3



### # star



### 2



### # star



### 1



### # star


[How this company uses Trustpilot](https://ca.trustpilot.com/review/cooperators.ca/transparency)


### ## People also looked at


[![Sonnet Insurance logo](https://consumersiteimages.trustpilot.net/business-units/5e4e0b7438d2d60001f5dc90-198x149-1x.jpg)\\ \\ **Sonnet Insurance** \\ www.sonnet.ca\\ \\ ![TrustScore 4 out of 5](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-4.svg)\\ \\ 4.2\\ \\ (5K)](https://ca.trustpilot.com/review/www.sonnet.ca)

[![Intact Insurance logo](https://consumersiteimages.trustpilot.net/business-units/5d4b5bfe45db820001f73109-198x149-1x.jpg)\\ \\ **Intact Insurance** \\ intact.ca\\ \\ ![TrustScore 1.5 out of 5](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.5.svg)\\ \\ 1.4\\ \\ (145)](https://ca.trustpilot.com/review/intact.ca)

[![belairdirect logo](https://consumersiteimages.trustpilot.net/business-units/60ca694b2357330001889bcc-198x149-1x.jpg)\\ \\ **belairdirect** \\ www.belairdirect.com\\ \\ ![TrustScore 1.5 out of 5](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.5.svg)\\ \\ 1.3\\ \\ (63)](https://ca.trustpilot.com/review/www.belairdirect.com)

[![tdinsurance.com logo](https://consumersiteimages.trustpilot.net/business-units/6197f7e2f570db422b2ef730-198x149-1x.jpg)\\ \\ **tdinsurance.com** \\ tdinsurance.com\\ \\ ![TrustScore 1.5 out of 5](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.5.svg)\\ \\ 1.3\\ \\ (105)](https://ca.trustpilot.com/review/tdinsurance.com)

[![squareone.ca logo](https://consumersiteimages.trustpilot.net/business-units/640bff96a1a5464aeb00a411-198x149-1x.jpg)\\ \\ **squareone.ca** \\ squareone.ca\\ \\ ![TrustScore 2 out of 5](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-2.svg)\\ \\ 1.9\\ \\ (39)](https://ca.trustpilot.com/review/squareone.ca)

[![Wawanesa Insurance logo](https://consumersiteimages.trustpilot.net/business-units/5c8abaf717f74e00010403d1-198x149-1x.jpg)\\ \\ **Wawanesa Insurance** \\ www.wawanesa.com\\ \\ ![TrustScore 1.5 out of 5](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.5.svg)\\ \\ 1.5\\ \\ (31)](https://ca.trustpilot.com/review/www.wawanesa.com)

[![Max Insurance  logo](https://consumersiteimages.trustpilot.net/business-units/62632c173965f59c10b1bf0a-198x149-1x.jpg)\\ \\ **Max Insurance** \\ maxinsurance.ca\\ \\ ![TrustScore 4.5 out of 5](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-4.5.svg)\\ \\ 4.7\\ \\ (426)](https://ca.trustpilot.com/review/maxinsurance.ca)

[![Desjardins Group logo](https://consumersiteimages.trustpilot.net/business-units/5da3f84effa5b70001ecf97d-198x149-1x.jpg)\\ \\ **Desjardins Group** \\ desjardins.com\\ \\ ![TrustScore 1.5 out of 5](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.5.svg)\\ \\ 1.3\\ \\ (104)](https://ca.trustpilot.com/review/desjardins.com)


### # More filters



### # Most recent



### # #### Top mentions


# customer servicestaffservicemistakepricecancellationcontactresponse timepaymentrecommendation


### # 2 days ago


![Rated 1 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.svg)

# [**Terrible service really don’t care…**](https://ca.trustpilot.com/reviews/6834f31bb4264113682cc8a1)

Terrible service really don’t care about existing customers let alone new customers


### Don’t call them or if you don’t wanna be on a 7 hour + hold



### # Date of experience:*



### May 26, 2025



### # UsefulShare



### # 5 days ago


![Rated 1 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.svg)

[**I’ve acquired a new vehicle and was…**](https://ca.trustpilot.com/reviews/6830bdf60dd33b37f191a5e0)

I’ve acquired a new vehicle and was needing car insurance. I’ve been calling everyday for a week, and been put on waiting 7h each day, and after trying to reach them by email, they suggested that i need to look for another insurance.

0 proficiency, 0 service, I don’t recommend wasting your time with them!


### # Date of experience:*



### May 23, 2025



### # Useful1Share



### # 6 days ago


![Rated 1 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.svg)


### [*



### # Terrible!*


# ](https://ca.trustpilot.com/reviews/682f3a8fb92ed57c2c16561c)

I am 58 years old and have never made a claim in my life. Recently struck a wild turkey while driving. Cooperators have been completely negligent in addressing the repair. Phone calls and emails are not responded to. I WILL be dropping Cooperators as soon as my term is finaished. AVOID AT ALL COSTS


### # Date of experience:*



### May 22, 2025



### # Useful1Share



### May 20, 2025


![Rated 1 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.svg)

[**I took a day from work today just to…**](https://ca.trustpilot.com/reviews/682d07e8b7239c1bbdbd76c4)

I took a day from work today just to call and have a quote for car insurance but I really had a bad experience that would say to everyone not to waste time on these people as they don’t respond to the call after waiting for 4 hours and it’s not only today I called them before as well with no response. I am really disappointed and angry at the same time.


### # Date of experience:*



### May 20, 2025



### # Useful1Share



### May 16, 2025


![Rated 1 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.svg)


### [*



### # Hello*


# ](https://ca.trustpilot.com/reviews/6827c77caa5356bdcc037780)


### # Hello



### I am a customer with cooperator from day one in Quebec


And I am telling you do not use cooperator there service is worst every year they make

There on laws internally when it come to reclamation when you ask where it is in the police they reply it is internal P policy

Please stay away don’t thing they are cheap they are more expensive and they are not worth musch when you have damage I am in the middle of changing to another insurance


### My name is Michel I am one of there customer since 2009



### # Date of experience:*



### May 16, 2025



### # Useful1Share



### May 16, 2025


![Rated 1 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.svg)

[**If I could leave 0 stars I would**](https://ca.trustpilot.com/reviews/6827a0c3b824cb5910c87be0)

If I could leave 0 stars, I would have. If you are looking into home or auto insurance, I beg you to look elsewhere and not make the mistake I did. They are just awful, they increase premiums every year without cause or the ability to detail the reasons behind the increases. They are incredibly slow to respond during any actual claim processes and will find any way they can to either not provide coverage or provide the bare minimum. Their 'trusted' contractor list is full of poorly reviewed contractors who seem as crooked as cooperators are. Please go elsewhere, you will thank me later.


### # Date of experience:*



### May 16, 2025



### # Useful1Share



### May 15, 2025


![Rated 1 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.svg)

[**Raised my premium approshame on you cooperatorsx a month later…**](https://ca.trustpilot.com/reviews/68261579d15f82b9d80475e5)

Raised my premium approx a month later then cut my insurance off due to nonpayment( false). NOW COOPERATORS will not fix thier mistake. I've never had any driving infractions but have to pay the premiums of a convicted dui driver. This company does not deserve your money find a better more reputable company. Shame on you Cooperators.


### # Date of experience:*



### May 15, 2025



### # UsefulShare



### May 9, 2025


![Rated 1 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.svg)

[**Too expensive , premium increasing year over year , poor customer service**](https://ca.trustpilot.com/reviews/681e9a1c916bc2dc4c8d93d9)

Too expensive, Customer service always involves a long wait time. The representatives themselves are polite and having lack of knowledge , doing mistakes, you have to double check after your call is finished . However, the company’s overall service is disappointing. My insurance premium increases every single year, and the explanation is always the same: “inflation in your area. It’s becoming increasingly frustrating and unreasonable.


### # Date of experience:*



### May 10, 2024



### # UsefulShare



### May 5, 2025


![Rated 1 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.svg)


### [*



### # Very expensive*


# ](https://ca.trustpilot.com/reviews/6818e26475e1a607fd8c1e8e)

Very expensive insurance I was paying 209 dollars a month now they want 279 a month say good by im going to be calling them Thursday highway Robbery these guys


### # Date of experience:*



### May 05, 2025



### # UsefulShare



### Apr 26, 2025


![Rated 1 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.svg)

[**Never think of buying auto insurance…**](https://ca.trustpilot.com/reviews/680d7d74c8933b4befa02528)

Never think of buying auto insurance from cooperators. very expensive. Even non- responsive when we call them. They don't care about the customers. Ultimately I had to cancel my insurance and I had to pay one month premium as penalty... very horrible experience.


### # Date of experience:*



### April 09, 2025



### # UsefulShare



### See if a website is trustworthy without leaving the page



### # ![](https://cdn.trustpilot.net/brand



### # assets/4.3.0/logo



### # black.svg)


# [Get Chrome extension](https://chrome.google.com/webstore/detail/trustpilot


### # reviews


# rating/dimkjjladgaekdlfebknbaooicmfalke?utm_source=trustpilot&utm_medium=cpp_promotion&utm_campaign=cpp_promotion)


### Apr 22, 2025


![Rated 3 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-3.svg)

# [**Rental from my own pocket**](https://ca.trustpilot.com/reviews/680797a16e30295395820450)

Rental coverage with a limit of $1500.00 accordingly to my contract. Rental for 18 days paid by the insurance: $581.72. I had to pay another 8 days from my pocket, $258.55. Disappointing!


### # Date of experience:*



### March 17, 2025



### # UsefulShare



### # Updated Apr 21, 2025


![Rated 1 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.svg)

# [**Know the details of any policy, especially seniors!**](https://ca.trustpilot.com/reviews/680118a7f8b1fa2614db9107)

I had insurance policies for 2 cars and life insurance for myself costing $203 a month for a policy for $25,000 should I die. I have to die and my wife would receive $25K. No one explained to me that this was an Infinity Policy, nor my gracious Branch Manager. A few weeks ago, I advised my Branch Manager that I would like to surrender the policy and receive whatever monies accrued. The Branch Manager forwarded a form to be signed by me and my wife.

My Branch forwarded the policy to his Head Office and I was advised that I would not receive zero dollars. I asked whether I could cancel my surrender and continue to pay. I received a eletter from Cristina Chobot -To: MS


### # Cc: Elizabeth Davidson



### # Subject: CL 001256927 RANJIT



### # Hi


Regrettably, we were unable to reinstate the policy, both owners assigned off and agree to the terms of the surrender form.

The surrender form is clearly states that “You may not be eligible for insurance coverage in the future. If you want insurance coverage after the date of this cancellation, you must submit a new application, and your insurability will be assessed as of the date of your new application.”


### Please advise your clients.



### # Sincerely



### # Christina Chobot


Christina Cobot short changed us for over $20,000 to benefit Cooperators instead of advising us not to surrender our policy. We were cheated, Shame on you Christina Cobot!

As a Senior, in my opinion, Christina Cobot does not know the fundamentals of customer service and customer retention. I would not conduct any new business with the Cooperators. It was a cash grab.


### # cc Robert Wessling, John Harvie



### # Date of experience:*



### April 13, 2025



### # UsefulShare



### # Updated Mar 24, 2025


![Rated 1 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.svg)


### [*



### Never trust the co



### operators*


# ](https://ca.trustpilot.com/reviews/67e1786ba18c17ce206787cc)


### I had insurance for 6 months with the Co-operators


I had a 2004 Pontiac GT which needed an inspection, but wasn’t able to find someone in time… so they cancelled my insurance and tried taking more money out of my account for the cancellation, without telling me first…. 🤦‍♀️

On another note, I did try calling them and was on hold for 1.5 hours before someone answered and said the sales department was closed…. Then called the next day and was on hold for 2.5 hours, will never be coming back.


### # Date of experience:*



### March 23, 2025



### # UsefulShare



### Mar 11, 2025


![Rated 1 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.svg)


### [*



### Calls never answered.*


# ](https://ca.trustpilot.com/reviews/67d0b5f3a383c9b7b05e0772)

They don't have enough staff to attend customers phone calls. Spent total of 13 plus hours to get a quote but no luck.They never attend the call,just keep it on hold and wasting customers time.I will not be looking for a part of these pathetic insurance company and will discourage others from doing business with this unprofessional company. It's 2025 and still they don't have the call back option or enough staff to handle the customers. Worst insurance company ever.


### # Date of experience:*



### March 11, 2025



### # UsefulShare



### See 1 more review by Arun



### Mar 10, 2025


![Rated 1 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.svg)


### [*



### Forever is not enough*


# ](https://ca.trustpilot.com/reviews/67cf4a34388208e519d44fdb)

There should be an option for a negative rating for the Co-operators insurance company. If you are looking for FOREVER, this is the company you should call, you’ll be put on hold for forever! Wasting your weeks calling them for a quote. Customer service rating is below ZERO.


### # Date of experience:*



### March 10, 2025



### # UsefulShare



### Mar 10, 2025


![Rated 1 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.svg)

[**Customer service is very bad.**](https://ca.trustpilot.com/reviews/67cf4551234b07f4124e0560)

Customer service is very bad.. 20 days ago I went to South Trail branch of Calgary to get an insurance quote, they told me that they do not receive customers in the office without an appointment.. The appointment was made on 10/3, they took my name and phone number.. When I went for the appointment, the system had changed to phone and they do not receive customers, knowing that my name and phone number are registered with them.. I was not contacted. Notified of the change.. I took a leave from work and traveled a long distance to get there.. Currently on the phone for more than an hour, it is a waste of time


### # Date of experience:*



### March 08, 2025



### # UsefulShare



### Mar 1, 2025


![Rated 1 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.svg)


### [*



### # Crap company*


# ](https://ca.trustpilot.com/reviews/67c31a3b3fc91329496a3a01)


| Customer | The | They’re | The | Getting |
| --- | --- | --- | --- | --- |
| ### # Date | of experience:* |  |  |  |

### March 01, 2025



### # UsefulShare



### Feb 26, 2025


![Rated 1 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-1.svg)


### [*



### # Absolutely terrible experience*


# ](https://ca.trustpilot.com/reviews/67bf38d7d18a592949d3709e)

Absolutely terrible experience. This insurance company gladly took my money but disappeared the moment I actually needed them. They find every excuse to deny claims, have the worst customer service, and couldn’t care less about their clients. Stay far away unless you enjoy getting scammed.


### # Date of experience:*



### # February 25, 2025



### # UsefulShare



### Feb 1, 2025


![Rated 5 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-5.svg)


### [*



### Chris is awesome*


# ](https://ca.trustpilot.com/reviews/679e3c2837b6ebf6837f6a57)

I dealt with Chris today and it’s safe to say that he is the one i’d like to deal with everytime. He was so patient and went through everything in depth and was so helpful. Chris is awesome.


### # Date of experience:*



### # February 01, 2025



### # UsefulShare



### Jan 23, 2025


![Rated 5 out of 5 stars](https://cdn.trustpilot.net/brand-assets/4.1.0/stars/stars-5.svg)

[**I want to give my highest rate to…MAYA Hanna**](https://ca.trustpilot.com/reviews/67925fa7d6a2df62277ddf11)

I want to give my highest rate to Co-operators insurance. Also, I would like to rate my nice adjustor " Maya Hanna" 10/ 10 for her wonderful customer service and for being such an amazing caring, and professional adjustor. GREAT INSURANCE!!


### # Date of experience:*



### # January 16, 2025



### # UsefulShare



### ### Is this your company?


Claim your profile to access Trustpilot’s free business tools and connect with customers.

[Get free account](https://business.trustpilot.com/signup?locale=en

# CA&utm_medium=consumer&utm_source=claim_company_button&utm_campaign=consumer_cta&website=cooperators.ca&country=CA)


### # ### The TrustpilotExperience



### #### We're open to all


[Anyone](https://help.trustpilot.com/s/article/Who-can-write-a-review-and-when?language=en) can write a Trustpilot review. People who write reviews have ownership to edit or delete them at any time, and they’ll be displayed as long as an [account is active](https://help.trustpilot.com/s/article/Whats-the-retention-period-of-reviews?language=en).


### #### We champion verified reviews


Companies can ask for reviews via automatic invitations. Labeled Verified, they’re about genuine experiences.

# [Learn more](https://help.trustpilot.com/s/article/How-do-reviews-get-on-Trustpilot?utm_campaign=verified&utm_content=verified_tooltip&utm_medium=referral&utm_source=transparency_page&language=en) about other kinds of reviews.


### #### We fight fake reviews


We use dedicated people and clever technology to safeguard our platform. Find out how we [combat fake reviews](https://ca.trustpilot.com/trust/combating-fake-reviews).


### #### We show the latest reviews


Learn about Trustpilot’s [review process](https://help.trustpilot.com/s/article/The-journey-of-reviews-on-Trustpilot?language=en).


### #### We encourage constructive feedback


Here are [8 tips for writing great reviews](https://help.trustpilot.com/s/article/8-tips-for-writing-great-customer-reviews?language=en).


### #### We verify reviewers


Verification can help ensure [real people](https://help.trustpilot.com/s/article/Verify-your-identity-with-photo-ID?language=en) are writing the reviews you read on Trustpilot.


### #### We advocate against bias


Offering incentives for reviews or asking for them selectively can bias the TrustScore, which goes [against our guidelines](https://help.trustpilot.com/s/article/Who-can-write-a-review-and-when?language=en).


### [Take a closer look](https://ca.trustpilot.com/trust)



### [are you human?](https://ca.trustpilot.com/end



### # of



### # the



### # line)



### # reCAPTCHA



### Recaptcha requires verification.


# [Privacy](https://www.google.com/intl/en/policies/privacy/) \


### [Terms](https://www.google.com/intl/en/policies/terms/)



### protected by *



### # reCAPTCHA**


# [Privacy](https://www.google.com/intl/en/policies/privacy/) \


### [Terms](https://www.google.com/intl/en/policies/terms/)

