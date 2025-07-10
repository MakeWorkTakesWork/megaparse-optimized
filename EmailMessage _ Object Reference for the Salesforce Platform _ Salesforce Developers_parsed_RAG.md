---
title: ===============================================================================
document_type: guide
primary_topics: sales, process, salesforce, product
last_preprocessed: 2025-05-26
---

===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### ===============



## 5/26/25,9:31 AM



### ===============



### [Image: unknown]



### # Developers



### Reference I Standard Objects / EmailMessage



### # EmailMessage



## Represents an email in Salesforce.



### # Supported Calls


create(), delete(), describelayout0, describesobjectso, getDeleted0, getupdated0),
query(), retrieve(), search(), undelete(), update(), upsert()


### 0



### # Special Access Rules


EmailMessage is only avallable for orgs that use Emall-to-Case or Enhanced Email, which is
automatically enabled for most customers.

To use reply and forward functionality, FromAddress must specify an email address that exists in
EmaiMessageRelation. with a Relationtype of FromAddress.

The Status field is mostly read-only. You C an change the status only from New to Read.

The HtmlBody and RelatedTOId fields are supported in Classic list views but not in Lightning list
views. In related lists and search results in Lightning Experience, these fields either don't appear,
show blank values, or result in an e

update() is supported when an email record is in Draft status, and IsPrivateprart is false.
It's also supported if the email status is Draft, ISPrivateDrart is true, and CreatedBy is
associated with the current user. When the email record isn't in Draft status, the
sExternallyVisiDle field and custom fields only can be updated.

Set the Update Email Messages user permission for users, such as an Automated Case User, who
run au LC ated processes that modify email message-related records. With the Update Email
Message permission set, users' processes can modify EmalilMessageRelation and
ContentDocumentuink records that are related to an email message that isn't in Draft status. Don't
set this user permission for other users.

Access to an email message depends on the associated object. The user who created the email is
specified in CreatedById and always has access, unless that user is a guest user. Guest users have
read access if the message is marked as IsExternallyvisible.

The object that's used to determine de o differs for Email-to-Case and Enhanced Email.

Email-to-Case -When Email-to-Case is enabled and the email is Case-based (the ParentId
field is Case), access depends on the user's access to the related Case record. If the email
message is a draft, only the in the CreatedById field or - with the Modify All Data
permission can access it.

Enhanced Email-Access is activity-based. The ActivityId field specifies an associated Task
record. You can control access to activity-based objects with the Access Activities permission.
Users with the Modify All Data permission can also acces 55 the message.

When you use the API to insert EmailMessage records in bulk, the sa
C rules apply: acce 55
is based on cases in ParentId fields or by tasks in ActivityId fields. When inserting a single
record, set the createdByld field to the performing the operation or leave it blank.

e.com/docs t. las.en-us.obje ct rei erence.meta/ot re erence/s storce_api_ot ects_cmalmessage .htm


### ====



### 1/16



### ====



### nttps/develr


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### ===============



## 5/26/25,9:31 AM



### ===============



### [Image: unknown]



### # Developers



### Reference I Standard Objects / EmailMessage



### # EmailMessage



## Represents an email in Salesforce.



### # Supported Calls


create(), delete(), describelayout0, describesobjectso, getDeleted0, getupdated0),
query(), retrieve(), search(), undelete(), update(), upsert()


### 0



### # Special Access Rules


EmailMessage is only avallable for orgs that use Emall-to-Case or Enhanced Email, which is
automatically enabled for most customers.

To use reply and forward functionality, FromAddress must specify an email address that exists in
EmaiMessageRelation. with a Relationtype of FromAddress.

The Status field is mostly read-only. You C an change the status only from New to Read.

The HtmlBody and RelatedTOId fields are supported in Classic list views but not in Lightning list
views. In related lists and search results in Lightning Experience, these fields either don't appear,
show blank values, or result in an e

update() is supported when an email record is in Draft status, and IsPrivateprart is false.
It's also supported if the email status is Draft, ISPrivateDrart is true, and CreatedBy is
associated with the current user. When the email record isn't in Draft status, the
sExternallyVisiDle field and custom fields only can be updated.

Set the Update Email Messages user permission for users, such as an Automated Case User, who
run au LC ated processes that modify email message-related records. With the Update Email
Message permission set, users' processes can modify EmalilMessageRelation and
ContentDocumentuink records that are related to an email message that isn't in Draft status. Don't
set this user permission for other users.

Access to an email message depends on the associated object. The user who created the email is
specified in CreatedById and always has access, unless that user is a guest user. Guest users have
read access if the message is marked as IsExternallyvisible.

The object that's used to determine de o differs for Email-to-Case and Enhanced Email.

Email-to-Case -When Email-to-Case is enabled and the email is Case-based (the ParentId
field is Case), access depends on the user's access to the related Case record. If the email
message is a draft, only the in the CreatedById field or - with the Modify All Data
permission can access it.

Enhanced Email-Access is activity-based. The ActivityId field specifies an associated Task
record. You can control access to activity-based objects with the Access Activities permission.
Users with the Modify All Data permission can also acces 55 the message.

When you use the API to insert EmailMessage records in bulk, the sa
C rules apply: acce 55
is based on cases in ParentId fields or by tasks in ActivityId fields. When inserting a single
record, set the createdByld field to the performing the operation or leave it blank.

e.com/docs t. las.en-us.obje ct rei erence.meta/ot re erence/s storce_api_ot ects_cmalmessage .htm


### ====



### 1/16



### ====



### nttps/develr



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### [Table : unknown]



### [Table : unknown]



### 00



### AiAssisted -Email is Al-generated, but sent by human.



### Null-Email is created and sent by human.


e.com/docs t. as s.en-us.oDje re n ence.met: a/ob je re erenc el sforce_api_ob pcts.cmalmesage-ntm


### ====



### 2/16



### ====



### nttps/develr



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### [Table : unknown]



### [Table : unknown]



### 00



### AiAssisted -Email is Al-generated, but sent by human.



### Null-Email is created and sent by human.


e.com/docs t. as s.en-us.oDje re n ence.met: a/ob je re erenc el sforce_api_ob pcts.cmalmesage-ntm


### ====



### 2/16



### ====



### nttps/develr



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================

Salestorce. If the recipient is a contact, lead, or user, add their ID to the
BccIds field instead of adding their email address to the BccAddress
neld. When adding their ID, the email message is automatically
associated with the contact, lead, or user. For an Experience Cloud site
us er who isn't the sender of the email, this field returns null.

You can't send emails unless there's at least one recipient.


### # BccIds



### # Type



### JunctionidList



### [Table : unknown]



### # Properties



### Create, Update



### # Description


A string array of IDs for contacts, leads, and users who were sent a
visually impaired carbon copy of the email message. Each ID is linked to
an EmaillessageRelation record, which represents the relationship 86
between an email message and a Contact, Lead, or User record. For an
Experience Cloud site user who isn't the sender of the email, this list is
empty.
Adding JunctionIdL1st field na an 16 to the fieldsTONulL property
deletes all related junction records. This action can't be undone.


### # CcAddress



### # Type



### string



### # Properties



### Create, Filter, Nillable, Sort, Update



### # Description


A string array of email addresses for recipients who sent a carbon
copy of the email message. Include only email addresses that aren't
associated with Contact, Lead, or User records in Salesforce. Ift the
recipient is a contact, lead, or user, add their ID to the CcIds field
instead of adding their email address to the CcAddr ress held. Then the
email message is automatically associated with the contact, lead, or user.

You can't send emails unless there's at least one recipient.


### # CcIds



### # Type



### JunctionldList



### # Properties



### Create, Update



### # Description


A string array of IDs for contacts, leads, and s who re sent a
carbon copy of the email message. Each ID is linked to an
EmallessageRelation record, which represents the relationship
between an email message and a Contact, Lead, or User record.
Adding a JunctionIdList field to the fleldsTONuLL property
deletes all related junction records. This action can't be undone.

e.com/docs/ at as s.en-us.oDje CL re en ice.meu a/ob je re ereno el storce_apL_ob pcts.cmalmesage-ntm


### ====



### 3/16



### ====



### nttps/develr



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================

Salestorce. If the recipient is a contact, lead, or user, add their ID to the
BccIds field instead of adding their email address to the BccAddress
neld. When adding their ID, the email message is automatically
associated with the contact, lead, or user. For an Experience Cloud site
us er who isn't the sender of the email, this field returns null.

You can't send emails unless there's at least one recipient.


### # BccIds



### # Type



### JunctionidList



### [Table : unknown]



### # Properties



### Create, Update



### # Description


A string array of IDs for contacts, leads, and users who were sent a
visually impaired carbon copy of the email message. Each ID is linked to
an EmaillessageRelation record, which represents the relationship 86
between an email message and a Contact, Lead, or User record. For an
Experience Cloud site user who isn't the sender of the email, this list is
empty.
Adding JunctionIdL1st field na an 16 to the fieldsTONulL property
deletes all related junction records. This action can't be undone.


### # CcAddress



### # Type



### string



### # Properties



### Create, Filter, Nillable, Sort, Update



### # Description


A string array of email addresses for recipients who sent a carbon
copy of the email message. Include only email addresses that aren't
associated with Contact, Lead, or User records in Salesforce. Ift the
recipient is a contact, lead, or user, add their ID to the CcIds field
instead of adding their email address to the CcAddr ress held. Then the
email message is automatically associated with the contact, lead, or user.

You can't send emails unless there's at least one recipient.


### # CcIds



### # Type



### JunctionldList



### # Properties



### Create, Update



### # Description


A string array of IDs for contacts, leads, and s who re sent a
carbon copy of the email message. Each ID is linked to an
EmallessageRelation record, which represents the relationship
between an email message and a Contact, Lead, or User record.
Adding a JunctionIdList field to the fleldsTONuLL property
deletes all related junction records. This action can't be undone.

e.com/docs/ at as s.en-us.oDje CL re en ice.meu a/ob je re ereno el storce_apL_ob pcts.cmalmesage-ntm


### ====



### 3/16



### ====



### nttps/develr



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### ClientThreadioentifier



### Type



### string



### [Table : unknown]


e.com/docs, t. as s.en-us.obje re re ence.meta a/oD re erei sforce_api_ob cts.cmalmessgc.ntm


### ====



### 4/16



### ====



### nttps:/dever



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### ClientThreadioentifier



### Type



### string



### [Table : unknown]


e.com/docs, t. as s.en-us.obje re re ence.meta a/oD re erei sforce_api_ob cts.cmalmessgc.ntm


### ====



### 4/16



### ====



### nttps:/dever



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### [Table : unknown]


e.com/docs t. las.en-us.obje re erence.met. a/ob re re orce_api_ob pcts-.cmalmessagc.ntm


### ====



### 5/16



### ====



### nttps:/dever



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### [Table : unknown]


e.com/docs t. las.en-us.obje re erence.met. a/ob re re orce_api_ob pcts-.cmalmessagc.ntm


### ====



### 5/16



### ====



### nttps:/dever



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### FromAddress



### Type



### email



### [Table : unknown]



### 00


e.com/docs t. as s.en-us.oDje re n ence.met: a/ob re ereno el sforce_api_ob cts.cmalmessgc.ntm


### ====



### 6/16



### ====



### nttps/develr



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### FromAddress



### Type



### email



### [Table : unknown]



### 00


e.com/docs t. as s.en-us.oDje re n ence.met: a/ob re ereno el sforce_api_ob cts.cmalmessgc.ntm


### ====



### 6/16



### ====



### nttps/develr



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### Description


The Internet message headers of the incoming email. Used for


### [Table : unknown]



### 0


e.com/docs t. as s.en-us.oDje
ence.met: a/ob re eren storce_ap_ot cts.cmalmessgc.ntm


### ====



### 7/16



### ====



### nttps:/dever



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### Description


The Internet message headers of the incoming email. Used for


### [Table : unknown]



### 0


e.com/docs t. as s.en-us.oDje
ence.met: a/ob re eren storce_ap_ot cts.cmalmessgc.ntm


### ====



### 7/16



### ====



### nttps:/dever



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### [Table : unknown]



### Defaulted on create, Filter



### ===
* 0


### ===


Only emails with a value in the ParentId field can be made
externally visible in sites.

The Enable Case Feeds in Experience Cloud Sites
organization preference in Setup makes case-related emails,
comments, and updates visible to site members.


### IsOpened



### # Type



### boolean



### # Properties



### Defaulted on create, Filter, Group, Sort



### # Description



### Indicates whether the email has been opened.


e.com/docs t. as s.en-us.obje
ence.met: a/ob je re eren el sforce_api_ob ects.emailmessage. .htm


### ====



### 8/16



### ====



### nttps:/dever



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### [Table : unknown]



### Defaulted on create, Filter



### ===
* 0


### ===


Only emails with a value in the ParentId field can be made
externally visible in sites.

The Enable Case Feeds in Experience Cloud Sites
organization preference in Setup makes case-related emails,
comments, and updates visible to site members.


### IsOpened



### # Type



### boolean



### # Properties



### Defaulted on create, Filter, Group, Sort



### # Description



### Indicates whether the email has been opened.


e.com/docs t. as s.en-us.obje
ence.met: a/ob je re eren el sforce_api_ob ects.emailmessage. .htm


### ====



### 8/16



### ====



### nttps:/dever



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### To see this field, enable email tracking in your org.



### [Table : unknown]



### ==



### 00



### ==


# e.com/docs/ au las.en-us.obje CL re re ence.meta/opje CL re erence el RuRapAN


### ====



### 9/16



### ====



### nttps/develr



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### To see this field, enable email tracking in your org.



### [Table : unknown]



### ==



### 00



### ==


# e.com/docs/ au las.en-us.obje CL re re ence.meta/opje CL re erence el RuRapAN


### ====



### 9/16



### ====



### nttps/develr



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### [Table : unknown]



### 0


e.com/docs, t. as s.en-us.obje re n ence.met: a/ob re cren IC orce_api_oD ect_emaimessage . htm


### =====



### 10/16



### =====



### nttps:/dever



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### [Table : unknown]



### 0


e.com/docs, t. as s.en-us.obje re n ence.met: a/ob re cren IC orce_api_oD ect_emaimessage . htm


### =====



### 10/16



### =====



### nttps:/dever



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================

polymorphic. Polymorphic means a Relatediold is equivalent to the ID
ofa related object.
You must have de 55 to at least o ie entity listed under Reters To to
access RelatedTold.
You can update RelatedToId when IsClienthanaged is set to true.
RelatedtoId and ParentId should have the sam e value when
ParentId is set. You might see unexpected results otherwise.


### [Table : unknown]



### This is a polymorphic relationship neld.



### # Relationship Name



### RelatedTO



### # Relationship Type



### Lookup



### # Refers To


Account, Accreditation, AssessmentindicatorDefinition, As ssessmentTask,
AssessmentlaskContentDocument, AssessmentiaskDenntion,
AssessmentTaskOrde: Asset, AssetrelationsnIp, AssignedResource,
Award, BoardCertfication, BusinessLicense, BusinessMileston e,
BusinessProfile, Campaign, CareBarrier, CareBarierDeterminant
CareBarrierlype, careDeterminant, CareDeterminantlype
CareDiagnosis, Careinterventiontype, CareMetriclarget,
CareObservation, CareObservation/om nponer IL
Care"gmProvHeatthcareProvider, CarePreauth, - re ea
n
CareProgram, areriogamampagn carerrogramen tyRule,
CareProgramenrolee, are -
o e a CL
Larerrogramenroimentcar Da areprogra mGoi arerrogramProduct
CareProgramProvide, areProgram! leamMember
CaePowdetAdherseAction CareProvid tyspec L)
CarPowdeseachabiere a areRegisteredDevte. CareRequest,
CareRequestDrug, carerequestestextension, CareRequestitem,
Carespecialty, Carespecaltylaxonomy Carelaxonomy Case,
Commsubcptonconsens Co ontactEncount:
omactnouneancpan ContactRequest Contract,
coveragebenent, overagesenenuter, redit tMemo, elegatedAccount,
DocumentCheckittem, Enrolimenteligibil ilityCriteria, 16 ealthcareracility,
eatnareactpNetwonk eathcarePayernelwonk
ealtrareractoneradny eaitncareProvider
HealtnarePowidernp. ealtincarePowdeSpecay
HealtincarePowiderliaxon Do y IdentityDocument, Image,
ndivdualAPPicaton Invoice, ListEmail, Location, MemberPlan,
Opportunity, Order, OlherComponentlask PartyConsent,
PersonLifeEvent, PlanBenefit, PlanBenefititem, ProcessException,
Product2, Productitem, ProductReques st PoductRequestuineltem
ProductTransfer, PurchaserPlan, RecelvedDocument, ResourceAbsence,
ReturnOrder, Retumorerunetem ServiceAppointment,
ServiceResource, Shift, Shipment, snipmenuitem, Solution, Visit,
VisitedParty, VolunteerProject, WorkOrder, Workorderuineite m


### 00



### reference



### # Properties



### Create, Filter, Group, Nillable, Sort


e.com/docs t. as s.en-us.oDje
ence.met: a/ob je re erend sI orce_api_ot cts.cmalmessgc.ntm


### =====



### 11/16



### =====



### nttps/develr



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================

polymorphic. Polymorphic means a Relatediold is equivalent to the ID
ofa related object.
You must have de 55 to at least o ie entity listed under Reters To to
access RelatedTold.
You can update RelatedToId when IsClienthanaged is set to true.
RelatedtoId and ParentId should have the sam e value when
ParentId is set. You might see unexpected results otherwise.


### [Table : unknown]



### This is a polymorphic relationship neld.



### # Relationship Name



### RelatedTO



### # Relationship Type



### Lookup



### # Refers To


Account, Accreditation, AssessmentindicatorDefinition, As ssessmentTask,
AssessmentlaskContentDocument, AssessmentiaskDenntion,
AssessmentTaskOrde: Asset, AssetrelationsnIp, AssignedResource,
Award, BoardCertfication, BusinessLicense, BusinessMileston e,
BusinessProfile, Campaign, CareBarrier, CareBarierDeterminant
CareBarrierlype, careDeterminant, CareDeterminantlype
CareDiagnosis, Careinterventiontype, CareMetriclarget,
CareObservation, CareObservation/om nponer IL
Care"gmProvHeatthcareProvider, CarePreauth, - re ea
n
CareProgram, areriogamampagn carerrogramen tyRule,
CareProgramenrolee, are -
o e a CL
Larerrogramenroimentcar Da areprogra mGoi arerrogramProduct
CareProgramProvide, areProgram! leamMember
CaePowdetAdherseAction CareProvid tyspec L)
CarPowdeseachabiere a areRegisteredDevte. CareRequest,
CareRequestDrug, carerequestestextension, CareRequestitem,
Carespecialty, Carespecaltylaxonomy Carelaxonomy Case,
Commsubcptonconsens Co ontactEncount:
omactnouneancpan ContactRequest Contract,
coveragebenent, overagesenenuter, redit tMemo, elegatedAccount,
DocumentCheckittem, Enrolimenteligibil ilityCriteria, 16 ealthcareracility,
eatnareactpNetwonk eathcarePayernelwonk
ealtrareractoneradny eaitncareProvider
HealtnarePowidernp. ealtincarePowdeSpecay
HealtincarePowiderliaxon Do y IdentityDocument, Image,
ndivdualAPPicaton Invoice, ListEmail, Location, MemberPlan,
Opportunity, Order, OlherComponentlask PartyConsent,
PersonLifeEvent, PlanBenefit, PlanBenefititem, ProcessException,
Product2, Productitem, ProductReques st PoductRequestuineltem
ProductTransfer, PurchaserPlan, RecelvedDocument, ResourceAbsence,
ReturnOrder, Retumorerunetem ServiceAppointment,
ServiceResource, Shift, Shipment, snipmenuitem, Solution, Visit,
VisitedParty, VolunteerProject, WorkOrder, Workorderuineite m


### 00



### reference



### # Properties



### Create, Filter, Group, Nillable, Sort


e.com/docs t. as s.en-us.oDje
ence.met: a/ob je re erend sI orce_api_ot cts.cmalmessgc.ntm


### =====



### 11/16



### =====



### nttps/develr



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### [Table : unknown]


ID of the inbound or outbound email messag ge the current email


### [Table : unknown]



### This is only set for Case related Email replies at setup.



### # Relationship Name



### Repy/oEmaiMessage



### Lookup



### EmailMessage



### picklist



### # Properties


Einstein Activity Capture Captured as an entire email
message by Einstein Activity Capture.

Einstein Activity Capture Limited -Captured as
header-only email by Einstein Activity Capture. The sender,
recipients, date, and time of the message e captured, not the
subject or body.

Email Integration App Manual-Captured to track the email
message records created or edited from the mailapp.


### Available in API version 64.0 and later.



### # Properties



### # Description



### 1 (Read)



### 2 (Replied)


e.com/docs t. as s.en-us.oDje re erence.meta a/oD je n eren RpNw


### =====



### 12/16



### =====



### nttps/develr



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### [Table : unknown]


ID of the inbound or outbound email messag ge the current email


### [Table : unknown]



### This is only set for Case related Email replies at setup.



### # Relationship Name



### Repy/oEmaiMessage



### Lookup



### EmailMessage



### picklist



### # Properties


Einstein Activity Capture Captured as an entire email
message by Einstein Activity Capture.

Einstein Activity Capture Limited -Captured as
header-only email by Einstein Activity Capture. The sender,
recipients, date, and time of the message e captured, not the
subject or body.

Email Integration App Manual-Captured to track the email
message records created or edited from the mailapp.


### Available in API version 64.0 and later.



### # Properties



### # Description



### 1 (Read)



### 2 (Replied)


e.com/docs t. as s.en-us.oDje re erence.meta a/oD je n eren RpNw


### =====



### 12/16



### =====



### nttps/develr



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### 3 (Sent)



### 4 (Forwarded)



### [Table : unknown]



### [Image: unknown]



### 0



### Subject field



### HTML Body or Text Body field


As the sender, you can provide the content, or it can be automatically
inserted using predefined values. An email template can also include the
content for these fields


### # Description



### =====



### 13/16



### =====



### nttps:/dever



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### 3 (Sent)



### 4 (Forwarded)



### [Table : unknown]



### [Image: unknown]



### 0



### Subject field



### HTML Body or Text Body field


As the sender, you can provide the content, or it can be automatically
inserted using predefined values. An email template can also include the
content for these fields


### # Description



### =====



### 13/16



### =====



### nttps:/dever



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### [Table : unknown]



### string



### # Properties



### Create, Filter, Nillable, Sort, Update



### # Description


A string array of email addresses for recipients who Ne re sent the email
message. Include only email addresses that aren't associated with
Contact, Lead, or User records in Salesforce. If the recipient is a contact,
lead, or user, add their ID to the ToIds field instead of adding their
email address to the TOAddress field. Then the email message is
automatically associated with the contact, lead, or user.

You can't send emails unless there's at least one recipient.


### # ToIds



### # Type



### JunctionidList



### 0



### # Properties



### Create, Update



### # Description


A string array of IDs for contacts, leads, and users who were sent a
carbon copy of the email message. Each ID is linked to an
EmallessageRelation record, which represents the relationship
between an email message and a Contact, Lead, or User record.
Adding JunctionIdList field no an ne to the fieldsTONulL property
deletes all related junction records. This action can't be undone.


### # Val lidat tedFromAddress



### # Type



### picklist



### # Properties


Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### # Description


A picklist value with either the sender's address, validated org-wide email
addresses that originated the email, or Email-to-Case Routing Address.
Val lida e dF o1 ress isn't suitable for use in Group By or Sort By
statements. Use FromAddress instead.


### # Usage



### EmailMessage is limited to 50 custom fields.


If your org uses Email-to-Case, a cas se is created when an email is sent to one of your company's
addresses. The email, which is related to the case by the ParentID field, is stored as an
EmailMessage record. When u view the email, they see the EmaiMessage record.

If your org use es Enhanced Email, each email is stored as an EmailMessage record and a Task record.
When users view an email, they see the EmailMessage record.

If you would like to change the recipients or contents of an outbound email, don't use automation
tools, like Flows or Apex triggers, to update EmaiMessage records. Unless they are for a draft,

e.com/docs t as s.en-us.oDject rei erence.metayou re erence/s storce_api_ob ects_emaimessage . tm


### =====



### 14/16



### =====



### nttps/develr



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### [Table : unknown]



### string



### # Properties



### Create, Filter, Nillable, Sort, Update



### # Description


A string array of email addresses for recipients who Ne re sent the email
message. Include only email addresses that aren't associated with
Contact, Lead, or User records in Salesforce. If the recipient is a contact,
lead, or user, add their ID to the ToIds field instead of adding their
email address to the TOAddress field. Then the email message is
automatically associated with the contact, lead, or user.

You can't send emails unless there's at least one recipient.


### # ToIds



### # Type



### JunctionidList



### 0



### # Properties



### Create, Update



### # Description


A string array of IDs for contacts, leads, and users who were sent a
carbon copy of the email message. Each ID is linked to an
EmallessageRelation record, which represents the relationship
between an email message and a Contact, Lead, or User record.
Adding JunctionIdList field no an ne to the fieldsTONulL property
deletes all related junction records. This action can't be undone.


### # Val lidat tedFromAddress



### # Type



### picklist



### # Properties


Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### # Description


A picklist value with either the sender's address, validated org-wide email
addresses that originated the email, or Email-to-Case Routing Address.
Val lida e dF o1 ress isn't suitable for use in Group By or Sort By
statements. Use FromAddress instead.


### # Usage



### EmailMessage is limited to 50 custom fields.


If your org uses Email-to-Case, a cas se is created when an email is sent to one of your company's
addresses. The email, which is related to the case by the ParentID field, is stored as an
EmailMessage record. When u view the email, they see the EmaiMessage record.

If your org use es Enhanced Email, each email is stored as an EmailMessage record and a Task record.
When users view an email, they see the EmailMessage record.

If you would like to change the recipients or contents of an outbound email, don't use automation
tools, like Flows or Apex triggers, to update EmaiMessage records. Unless they are for a draft,

e.com/docs t as s.en-us.oDject rei erence.metayou re erence/s storce_api_ob ects_emaimessage . tm


### =====



### 14/16



### =====



### nttps/develr



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================

When a Flow creates an EmailMessage with set values in the audit fields (like CreatedBy and
CreatedDate), any FeedItem automatically created for that EmailMessage will not share the
audit field values.


### # Sample Code-Apex



## This sample logs email activity in Salesforce.


// if En nhancedEmai L Perm is not enabled, continue Logging the email as a task

// if EnhancedEmail Perm is enabled, create an EmailMessage object
EmailMessage emailMessage - new EmallMessageo;
emailMessage.status = '3'; // email was sent
emailMessage. relatedToId 06890000weZGIAT? 11 related to record e.g. an oppo
emailMessage.f fromAddress = 'sender@examp le.c com'; // from address
emailMessage. fromName 'Dan Perkins '; 11 from name
6
emailMessage. subject = 'This is the Subject!'; // email subject
mallMessage.ntalboy chtmlxbodyp<b: eLto</ b>x/body>s/htmb 1/ email body 86
11 Contact, Lead or User Ids of recipients
String [] toIds = new Stringurcee3se00OQOAXCEJIAD:
emailMessage. .toIds toIds;
// additional recipients who don't have a corresponding contact, lead or r id
emailMessage-tohdress emallnotinsalesforcesforceetoexample.com, anotneroneetoexample
insert emailMessage; // insert

// Add Email Message Relation for id of the sender
EmailwessayeRelation emr ne W maluvessagekelationo:
emr. emailMessageId = emalumessage.1d;
emr. relationId = 9859090P00AIVOTAU? 1/ us 56 id of the sender
emr.relationiype - FromAddress';
insert emr;


### # Associated Objects


This object has the following associated objects. If the API version isn't specified, theyre available
in the 0 arT e API versions as this object. Otherwise, they're available in the specified API version and
later.


### # EmalMesgeChangebent (API version 48.0)



### Change events are available for the object.



### # See Also



### Case



## Overview of Salestorce Objects and Fields



### [Table : unknown]


DID THIS ARTICLE SOLVE YOUR ISSUE?
Let us know sO we n improve!

e.com/docs t. as s.en-us.oDje re ence.met: a/ob je re re orce_api_ot cts.cmalmessgc.ntm


### =====



### 15/16



### =====



### nttps/develr



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================

When a Flow creates an EmailMessage with set values in the audit fields (like CreatedBy and
CreatedDate), any FeedItem automatically created for that EmailMessage will not share the
audit field values.


### # Sample Code-Apex



## This sample logs email activity in Salesforce.


// if En nhancedEmai L Perm is not enabled, continue Logging the email as a task

// if EnhancedEmail Perm is enabled, create an EmailMessage object
EmailMessage emailMessage - new EmallMessageo;
emailMessage.status = '3'; // email was sent
emailMessage. relatedToId 06890000weZGIAT? 11 related to record e.g. an oppo
emailMessage.f fromAddress = 'sender@examp le.c com'; // from address
emailMessage. fromName 'Dan Perkins '; 11 from name
6
emailMessage. subject = 'This is the Subject!'; // email subject
mallMessage.ntalboy chtmlxbodyp<b: eLto</ b>x/body>s/htmb 1/ email body 86
11 Contact, Lead or User Ids of recipients
String [] toIds = new Stringurcee3se00OQOAXCEJIAD:
emailMessage. .toIds toIds;
// additional recipients who don't have a corresponding contact, lead or r id
emailMessage-tohdress emallnotinsalesforcesforceetoexample.com, anotneroneetoexample
insert emailMessage; // insert

// Add Email Message Relation for id of the sender
EmailwessayeRelation emr ne W maluvessagekelationo:
emr. emailMessageId = emalumessage.1d;
emr. relationId = 9859090P00AIVOTAU? 1/ us 56 id of the sender
emr.relationiype - FromAddress';
insert emr;


### # Associated Objects


This object has the following associated objects. If the API version isn't specified, theyre available
in the 0 arT e API versions as this object. Otherwise, they're available in the specified API version and
later.


### # EmalMesgeChangebent (API version 48.0)



### Change events are available for the object.



### # See Also



### Case



## Overview of Salestorce Objects and Fields



### [Table : unknown]


DID THIS ARTICLE SOLVE YOUR ISSUE?
Let us know sO we n improve!

e.com/docs t. as s.en-us.oDje re ence.met: a/ob je re re orce_api_ot cts.cmalmessgc.ntm


### =====



### 15/16



### =====



### nttps/develr



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### [Image: unknown]



### [Image: unknown]



### [Image: unknown]



## # DEVELOPER CENTERS


POPULAR RESOURCES
Documentation
Component Library
APIS
Trailhead
Sample Apps
Podcasts
AppExchange


## # COMMUNITY


Heroku
MuleSoft
Tableau
Cloud
Commerce
in  Lightning Design System
Einstein
Quip

Trailblazer Community
Events and Calendar
Partner Community
Blog
Salesforce Admins
Salesforce Architects


### [Image: unknown]



### [Image: unknown]


@ Copyright 2025 Salesforce, Inc. Allrightsreserved. Various trademarks held by their respective owners. Salesforce, Inc.
Salesforce Tower, 415 Mission Street, 3rd Floor, San Francisco, CA 94105, United States

PrivacyInformation IermsofUse Legal UseofCookies Trust Cookie Preferences
@3 Your Privacy.Choices Responsible Disclosure Contact


### ==



### 00



### ==


.com/docs/at!: las.en-us.ob j
en nce.meta a/ 00 n
orce_api_ob pcts-.cmalmessagc.ntm


### =====



### 16/16



### =====



### nttps:/dever



### ===============



## 5/26/25,9:31 AM



### ===============


===============================================================================

EmailMessage Object Reference for the Salesforce Platform Salesforce Developers

===============================================================================


### [Image: unknown]



### [Image: unknown]



### [Image: unknown]



## # DEVELOPER CENTERS


POPULAR RESOURCES
Documentation
Component Library
APIS
Trailhead
Sample Apps
Podcasts
AppExchange


## # COMMUNITY


Heroku
MuleSoft
Tableau
Cloud
Commerce
in  Lightning Design System
Einstein
Quip

Trailblazer Community
Events and Calendar
Partner Community
Blog
Salesforce Admins
Salesforce Architects


### [Image: unknown]



### [Image: unknown]


@ Copyright 2025 Salesforce, Inc. Allrightsreserved. Various trademarks held by their respective owners. Salesforce, Inc.
Salesforce Tower, 415 Mission Street, 3rd Floor, San Francisco, CA 94105, United States

PrivacyInformation IermsofUse Legal UseofCookies Trust Cookie Preferences
@3 Your Privacy.Choices Responsible Disclosure Contact


### ==



### 00



### ==


.com/docs/at!: las.en-us.ob j
en nce.meta a/ 00 n
orce_api_ob pcts-.cmalmessagc.ntm


### =====



### 16/16



### =====



### nttps:/dever

