---
title: ===========================================================================
document_type: guide
primary_topics: sales, salesforce, product, messaging
last_preprocessed: 2025-05-26
---

===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### ================



## 5/26/25, 9:32 AM



### ================



### [Image: unknown]



### [Image: unknown]



### Reference I Standard Objects / FeedItem



### # Feedltem


FeedItem represents an entry in the feed, such as changes in a record feed, including text posts,
link posts, and content posts. This object is availabl le in API version 21.0 and later. This object
replaces FeedPost.


### # Supported Calls


create(), delete(), describesObjects0, describeLayouto, getDeleted0), getupdated0),
query0), retrieve(), search0), update(), upsert()


### 0



### # Special Access Rules


You can delete all feed items you created. To delete feed items you didn't create, you must
have on ne of these permissions:


### Modify All Data


Modify All Records on the feed item's parent object, for example, Account for a feed
item on an account feed


### Moderate Chatter



### Note


Users with the Moderate Chatter permission can delete only the feed items
and comments that they can see.

Only users with this permission can delete items in unlisted groups.

Guest users can't insert system field values for Chatter feeds. Even if you try to assign the
Caninserfedsptemfiets permission to a Guest User, the permission isn't granted.

Only users with the Modify All Data permission can delete a feed item of Type TrackedChange.

If the context user has the Insert System Field Values for Chatter Feeds user permission, the create
field property is available on CreatedBy and CreatedDate system fields. During migration, the
context user can set these fields to the original post's author and creation date. The fields can't be
updated after migration.


### # Fields



### [Table : unknown]



### [Image: unknown]



### Field Name



### BestCommentId



### reference


nttps/develr
e.com/docs t. as s.en-us.oDje CL re erence.meta a/oD re crer IC orce_api_ob jects_teedite em.htm


### ====



### 1/16



### ====


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### ================



## 5/26/25, 9:32 AM



### ================



### [Image: unknown]



### [Image: unknown]



### Reference I Standard Objects / FeedItem



### # Feedltem


FeedItem represents an entry in the feed, such as changes in a record feed, including text posts,
link posts, and content posts. This object is availabl le in API version 21.0 and later. This object
replaces FeedPost.


### # Supported Calls


create(), delete(), describesObjects0, describeLayouto, getDeleted0), getupdated0),
query0), retrieve(), search0), update(), upsert()


### 0



### # Special Access Rules


You can delete all feed items you created. To delete feed items you didn't create, you must
have on ne of these permissions:


### Modify All Data


Modify All Records on the feed item's parent object, for example, Account for a feed
item on an account feed


### Moderate Chatter



### Note


Users with the Moderate Chatter permission can delete only the feed items
and comments that they can see.

Only users with this permission can delete items in unlisted groups.

Guest users can't insert system field values for Chatter feeds. Even if you try to assign the
Caninserfedsptemfiets permission to a Guest User, the permission isn't granted.

Only users with the Modify All Data permission can delete a feed item of Type TrackedChange.

If the context user has the Insert System Field Values for Chatter Feeds user permission, the create
field property is available on CreatedBy and CreatedDate system fields. During migration, the
context user can set these fields to the original post's author and creation date. The fields can't be
updated after migration.


### # Fields



### [Table : unknown]



### [Image: unknown]



### Field Name



### BestCommentId



### reference


nttps/develr
e.com/docs t. as s.en-us.oDje CL re erence.meta a/oD re crer IC orce_api_ob jects_teedite em.htm


### ====



### 1/16



### ====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### # Properties



### Filter, Group, Nillable, Sort



### # Description


The ID of the comment marked as best answer on a question post.


### This isa a relationship field.



### # Relationship Name



### BestComment



### Relationship Type



### Lookup



### # Refers To



### FeedComment



### Body



### 00



### # Type



### textarea



### # Properties



### Create, Nillable, Sort, Update



### # Description


The body of the feed item. Required when Type is TextPos st or
AC dy al ancedTextPost. Optional when Type is ContentPost or LinkPost.

Although a value for Body isn't required for the ContentPost type, an
attachment is required. It an attachment isn't present, the type changes to
TextPost or AdvancedTextPost, depending on the API version.
TextPost and AdvancedTextPost do require a value for Body.


### # Tip


See the SR1C chl6 e C field for a list of HTML tags
supported in the body of rich text posts.


### # CommentCount



### # Type



### int



### # Properties



### Filter, Group, Sort



### # Description



### The number of comments as ssociated with this feed item.



### # Tip


In a feed that supports pre-moderation, CommentCount
isn't updated until a comment is published. For example,
say that you comment on a post that already has , e
published comment and your comment triggers
moderation. Now there are two comments on the post, but


### Mopiaainlrmhn


nttps/develr
e.com/docs, t. as s.en-us.obje re re ence.met: a/


### ====



### 2/16



### ====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### # Properties



### Filter, Group, Nillable, Sort



### # Description


The ID of the comment marked as best answer on a question post.


### This isa a relationship field.



### # Relationship Name



### BestComment



### Relationship Type



### Lookup



### # Refers To



### FeedComment



### Body



### 00



### # Type



### textarea



### # Properties



### Create, Nillable, Sort, Update



### # Description


The body of the feed item. Required when Type is TextPos st or
AC dy al ancedTextPost. Optional when Type is ContentPost or LinkPost.

Although a value for Body isn't required for the ContentPost type, an
attachment is required. It an attachment isn't present, the type changes to
TextPost or AdvancedTextPost, depending on the API version.
TextPost and AdvancedTextPost do require a value for Body.


### # Tip


See the SR1C chl6 e C field for a list of HTML tags
supported in the body of rich text posts.


### # CommentCount



### # Type



### int



### # Properties



### Filter, Group, Sort



### # Description



### The number of comments as ssociated with this feed item.



### # Tip


In a feed that supports pre-moderation, CommentCount
isn't updated until a comment is published. For example,
say that you comment on a post that already has , e
published comment and your comment triggers
moderation. Now there are two comments on the post, but


### Mopiaainlrmhn


nttps/develr
e.com/docs, t. as s.en-us.obje re re ence.met: a/


### ====



### 2/16



### ====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================

the count says there's only one. In a moderated feed,
comments aren't counted until approved by an admin or
someone with Can Approve Feed Post and Comment or


### [Table : unknown]



### 00


nttps/develr
e.com/docs t. as s.en-u: us.obje re n ence.meta a/oD je re erence e/ sforce_apLobyects_feeditem.htm


### ====



### 3/16



### ====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================

the count says there's only one. In a moderated feed,
comments aren't counted until approved by an admin or
someone with Can Approve Feed Post and Comment or


### [Table : unknown]



### 00


nttps/develr
e.com/docs t. as s.en-u: us.obje re n ence.meta a/oD je re erence e/ sforce_apLobyects_feeditem.htm


### ====



### 3/16



### ====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### [Table : unknown]



### 00


nttps:/dever
e.com/docs t. las.en-us.obje re erence.met. a/o 00 re
I orce_api_ob jects._feeditem.htm


### ====



### 4/16



### ====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### [Table : unknown]



### 00


nttps:/dever
e.com/docs t. las.en-us.obje re erence.met. a/o 00 re
I orce_api_ob jects._feeditem.htm


### ====



### 4/16



### ====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### [Table : unknown]



### =



### 0



### =



### ====



### 5/16



### ====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### [Table : unknown]



### =



### 0



### =



### ====



### 5/16



### ====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### This is a polymorphic relationship field.



### Relationship Name



### [Table : unknown]



### [Table : unknown]


Though the <br> tag isn't supported, you can use
<p>6nbspi</p> to create lines.

nttps/develr
e.com/docs t. as s.en-us.oDje re erence.meta a/ob
I RePLA.EdIeNNn


### ====



### 6/16



### ====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### This is a polymorphic relationship field.



### Relationship Name



### [Table : unknown]



### [Table : unknown]


Though the <br> tag isn't supported, you can use
<p>6nbspi</p> to create lines.

nttps/develr
e.com/docs t. as s.en-us.oDje re erence.meta a/ob
I RePLA.EdIeNNn


### ====



### 6/16



### ====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### [Table : unknown]



### [Image: unknown]


The <img> tag is accessible only through the API and must reference
files in Salesforce similar to this example: <img
src-"sfdc://069B0000000omj h"></ img>


### 0


In API version 35.0 and later, the system replaces special
* ar racters in rich text with escaped HTML. In API version
34.0 and prior, all rich text appears as a plain-text
representation.


### reterence


nttps:/dever
e.com/docs t. las.en-us.obje C re erence.met. a/o 00 re
I orce_api_ob jects._feeditem.htm


### ====



### 7/16



### ====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### [Table : unknown]



### [Image: unknown]


The <img> tag is accessible only through the API and must reference
files in Salesforce similar to this example: <img
src-"sfdc://069B0000000omj h"></ img>


### 0


In API version 35.0 and later, the system replaces special
* ar racters in rich text with escaped HTML. In API version
34.0 and prior, all rich text appears as a plain-text
representation.


### reterence


nttps:/dever
e.com/docs t. las.en-us.obje C re erence.met. a/o 00 re
I orce_api_ob jects._feeditem.htm


### ====



### 7/16



### ====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### LikeCount



### Type



### int



### [Table : unknown]



### 00


NetworkId-The ID of the Experience Cloud site in which the
FeedItem is available. If left empty, the feed item is only available in
the default Experience Cloud site.

Only feed items with a Group or User parent can set a NetworkId or
null value for NetworkScope.

Fori feed items with a record parent, can set NetworkScope only
to ALINetworKS.

nttps:/dever
e.com/docs t. as s.en-us.obje
ence.metayop je re ereno el storce_apL_oD ojects feeditem.htm


### ====



### 8/16



### ====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### LikeCount



### Type



### int



### [Table : unknown]



### 00


NetworkId-The ID of the Experience Cloud site in which the
FeedItem is available. If left empty, the feed item is only available in
the default Experience Cloud site.

Only feed items with a Group or User parent can set a NetworkId or
null value for NetworkScope.

Fori feed items with a record parent, can set NetworkScope only
to ALINetworKS.

nttps:/dever
e.com/docs t. as s.en-us.obje
ence.metayop je re ereno el storce_apL_oD ojects feeditem.htm


### ====



### 8/16



### ====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### to a specific account.



### This isa polymorphic relationship field.



### # Relationship Name


Parent
Relationship Type
Lookup
Refers To
Account, Accreditation, Activationlargetz ActhatontgintogAcess
APiAnomalyèventstore. AssessmentindicatorDefinition, Assessmentiask,
AsessmentlaskContentDocument, AsesmentiassDefntion
Asesmentasandemnton Assessmentiaskorder, Asset,
AssetRelationship, AssignedResource, Award, BoardCertfication,
Businesslicense, BusinessMlestone, BusinessProfile, Campaign, CareBarrier,
CareBarierDeterminant, CareBarrierlype, CareDeterminant,
CareDeterminantlype, CareDiagnosis, Careinterventionlype,
CareMetriclarget, Ca areopservation a are eObserationComponent,
CarePgmP ProvHe eal althcareProvider, arePreaut n CarePreauthiten n
a areProgram, - areProgramCampag rePogamegbnyaue
a areProgramEnrolee, CareProgram mEnrolleeProduct,
arerogemenoimencand CareProgramGoa, areProgramProduct
CareProgramProvide arerrogramieamMemp et
a areP ToWdeTACVetseActIon. careProviderracin y Specialty,
Careproviderse DI r CareRegisteredDevice CareRequest,
CareRequestDrugs areRequestextenson CareRequest.tem, Carespecialty,
carespectaltylaxonomy carelaxonomy Case, odeSet, CollaborationGroup,
commsuDscrption CommSubs rptionChannettype,
Commubcptonconent Commsupscrptontiming
Consumptionschnedule Contact, contactencounte,
Comactnouneancpan ContentDocume Contract, coveragebenent,
coveragebenehttem Coenuasumgvenson CreditMemo,
CreditMemoLin e Dashboard, Dasnpoaracor ponent, DataStream,
DelegatedAccount, Documentcneckistte m EngagementCh anne ell Type,
r nhancedLetterhead, EnrolmenttigiDiitycnitena Event, HealthcareFacility,
eatnarelactyNelwos eatncarelayeretwonx
eaticarePacttonefaciy HeathcareProvider, HealtncarePovidernp:
eatmacrowoespecay Peatfdreowdeisorom, Identifier, Image,
IndwidualApplication, Invoice, InvoiceLin e, Lead, Location, Marketsegment,
MaretsegmentActmation MemberPlan, Messagingsession,
MktCalculatedinsight, OperatingHours, Opportunity, Order, Orderltem,
OtherComponentask PartyConsent, Personeducation, Personlanguage,
PersonLifeEvent, e ersonName, Planbenent, lanBenefititem, Product2,
ProductrumilmentLocation. Productitem, Productitemiransaction,
ProductRequest,  roductkequestuineitem, ProductRequired, ProductTransfer,
ProfileSkill, Pronieskillndorsement, Pronleskiluser, Prowdersearchsynclog
PurchaserPlan, PurchaserPlanAs n, Received cumer nu Report,
ReportAnomayeventstor e ResourceA Abse enc e, Resourcerrererence.
Returnorder, RetumOrderlinelten m, erviceAppointment ServiceResource,
serviceResourceskl, ServiceTerritory, ServicelertoMember
ervitelemoyworkype eson-pcangvension Shift, Shipment,
Shipmentitem, Site, SkillRequirement, SocialPost, Solution, Task,
TheatDetectionfedback Topic, User, Visit, VisitedParty, Visitor, VoiceCall,
VolunteerProject, WorkBadgeDehntion, WorkOrder, WorkOrderuneitem,
Worklype, WorklypeGroup, WokypecroupMembet


### 86


nttps/develr
e.com/docs/ au las.en-us.obje CL re n ence.meta/op, jo re re IC ord ce_api


### # t6 em.htm



### ====



### 9/16



### ====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### to a specific account.



### This isa polymorphic relationship field.



### # Relationship Name


Parent
Relationship Type
Lookup
Refers To
Account, Accreditation, Activationlargetz ActhatontgintogAcess
APiAnomalyèventstore. AssessmentindicatorDefinition, Assessmentiask,
AsessmentlaskContentDocument, AsesmentiassDefntion
Asesmentasandemnton Assessmentiaskorder, Asset,
AssetRelationship, AssignedResource, Award, BoardCertfication,
Businesslicense, BusinessMlestone, BusinessProfile, Campaign, CareBarrier,
CareBarierDeterminant, CareBarrierlype, CareDeterminant,
CareDeterminantlype, CareDiagnosis, Careinterventionlype,
CareMetriclarget, Ca areopservation a are eObserationComponent,
CarePgmP ProvHe eal althcareProvider, arePreaut n CarePreauthiten n
a areProgram, - areProgramCampag rePogamegbnyaue
a areProgramEnrolee, CareProgram mEnrolleeProduct,
arerogemenoimencand CareProgramGoa, areProgramProduct
CareProgramProvide arerrogramieamMemp et
a areP ToWdeTACVetseActIon. careProviderracin y Specialty,
Careproviderse DI r CareRegisteredDevice CareRequest,
CareRequestDrugs areRequestextenson CareRequest.tem, Carespecialty,
carespectaltylaxonomy carelaxonomy Case, odeSet, CollaborationGroup,
commsuDscrption CommSubs rptionChannettype,
Commubcptonconent Commsupscrptontiming
Consumptionschnedule Contact, contactencounte,
Comactnouneancpan ContentDocume Contract, coveragebenent,
coveragebenehttem Coenuasumgvenson CreditMemo,
CreditMemoLin e Dashboard, Dasnpoaracor ponent, DataStream,
DelegatedAccount, Documentcneckistte m EngagementCh anne ell Type,
r nhancedLetterhead, EnrolmenttigiDiitycnitena Event, HealthcareFacility,
eatnarelactyNelwos eatncarelayeretwonx
eaticarePacttonefaciy HeathcareProvider, HealtncarePovidernp:
eatmacrowoespecay Peatfdreowdeisorom, Identifier, Image,
IndwidualApplication, Invoice, InvoiceLin e, Lead, Location, Marketsegment,
MaretsegmentActmation MemberPlan, Messagingsession,
MktCalculatedinsight, OperatingHours, Opportunity, Order, Orderltem,
OtherComponentask PartyConsent, Personeducation, Personlanguage,
PersonLifeEvent, e ersonName, Planbenent, lanBenefititem, Product2,
ProductrumilmentLocation. Productitem, Productitemiransaction,
ProductRequest,  roductkequestuineitem, ProductRequired, ProductTransfer,
ProfileSkill, Pronieskillndorsement, Pronleskiluser, Prowdersearchsynclog
PurchaserPlan, PurchaserPlanAs n, Received cumer nu Report,
ReportAnomayeventstor e ResourceA Abse enc e, Resourcerrererence.
Returnorder, RetumOrderlinelten m, erviceAppointment ServiceResource,
serviceResourceskl, ServiceTerritory, ServicelertoMember
ervitelemoyworkype eson-pcangvension Shift, Shipment,
Shipmentitem, Site, SkillRequirement, SocialPost, Solution, Task,
TheatDetectionfedback Topic, User, Visit, VisitedParty, Visitor, VoiceCall,
VolunteerProject, WorkBadgeDehntion, WorkOrder, WorkOrderuneitem,
Worklype, WorklypeGroup, WokypecroupMembet


### 86


nttps/develr
e.com/docs/ au las.en-us.obje CL re n ence.meta/op, jo re re IC ord ce_api


### # t6 em.htm



### ====



### 9/16



### ====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### [Table : unknown]



### 00



### # Properties



### Create, Filter, Group, Nillable, Sort



### # Description



### The revision number of the feed item.


Specifies whether this feed item is published and visible to all who can
the feed. This field is available in API version 37.0 and later.


### Published -The item's visible to all with ac to the teed.


PendingReview: -The item's visible to its author and users who see
the item and have View All Data or Can Approve Feed Post and
Comment permission. Some people can delete and edit the item.
They include the author and users who see the item and have Can
Approve Feed Post and Comment or Modify All Data permission.


### # Note


These permissions don't apply when you retrieve
feed items using SOQL. To filter out Pending Review
feed items you must add an explicit clause.

Some actions are blocked when a feed item is pending review:


### Comment



### Like and unlike



### Mopiaainlrmhn


nttps:/dever
e.com/docs, t. as s.en-us.obje re re ence.met: a/c ol


### =====



### 10/16



### =====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### [Table : unknown]



### 00



### # Properties



### Create, Filter, Group, Nillable, Sort



### # Description



### The revision number of the feed item.


Specifies whether this feed item is published and visible to all who can
the feed. This field is available in API version 37.0 and later.


### Published -The item's visible to all with ac to the teed.


PendingReview: -The item's visible to its author and users who see
the item and have View All Data or Can Approve Feed Post and
Comment permission. Some people can delete and edit the item.
They include the author and users who see the item and have Can
Approve Feed Post and Comment or Modify All Data permission.


### # Note


These permissions don't apply when you retrieve
feed items using SOQL. To filter out Pending Review
feed items you must add an explicit clause.

Some actions are blocked when a feed item is pending review:


### Comment



### Like and unlike



### Mopiaainlrmhn


nttps:/dever
e.com/docs, t. as s.en-us.obje re re ence.met: a/c ol


### =====



### 10/16



### =====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### [Table : unknown]


Isolated -The item is visible only to admins. After an item is isolated,
the author no longer has view or edit ace The admin user can edit,
view, and delete isolated feed items.


### string



### # Properties



### Create, Filter, Group, Nillable, Sort, Update



### # Description


The title of the feed item. When the Type is LinkPost, the LinkUrl is the
URL and this held is the link na The Title neld can be updated on posts
of Type QuestionPost.


### -



### 0



### # Type



### # Properties



### Create, Filter, Group, Nillable, Restricted picklist, Sort



### # Description


The type of feed item. Except for ContentPost, LinkPost,
QuestionPost, and TextPost, all the FeedItem types listed here are
system-generated. In most situations, we recommend that you don't create
system-generated fields using Apex or our APIS. One exception is during
Chatter data migrations, which can require admins to migrate system-
generated post types.

ActivityEvent -indirectly generated event when a S6 er or the API
adds a Task associated with a feed-enabled parent record (excluding
email tasks on cases). Also 00 rs when a user or the API adds or
updates a Task or Event associated with a record (excluding email
and call logging).

For a recurring Task with CaseFeed disabled, one event is generated
for the series only. For d recurring Task with CaseFeed enabled, events
are generated for the series and each occurrence.

AdvancedTextPost -created when user posts group
an nouncement and, in Lightning Experience as of API version 39.0
and later, when user shares a post.


### AnnouncementPost -Not used.



### ApprovalPost -generated when a user submits an approval.



### BasicTemp lateFeedItem -Not used.



### CanvasPost -a post made bya ca IV as app posted on a feed.


Collaboratiomtroupcreated -generated when a us creates a
public group.


### clawnatiorogplaraive -Not used.



### ContentPost -a post with an attached file.


nttps/develr
e.com/docs t. as s.en-us.oDje re re ence.met: a/o 00 n rer sforce.api_obyects._feeditem.htm


### =====



### 11/16



### =====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### [Table : unknown]


Isolated -The item is visible only to admins. After an item is isolated,
the author no longer has view or edit ace The admin user can edit,
view, and delete isolated feed items.


### string



### # Properties



### Create, Filter, Group, Nillable, Sort, Update



### # Description


The title of the feed item. When the Type is LinkPost, the LinkUrl is the
URL and this held is the link na The Title neld can be updated on posts
of Type QuestionPost.


### -



### 0



### # Type



### # Properties



### Create, Filter, Group, Nillable, Restricted picklist, Sort



### # Description


The type of feed item. Except for ContentPost, LinkPost,
QuestionPost, and TextPost, all the FeedItem types listed here are
system-generated. In most situations, we recommend that you don't create
system-generated fields using Apex or our APIS. One exception is during
Chatter data migrations, which can require admins to migrate system-
generated post types.

ActivityEvent -indirectly generated event when a S6 er or the API
adds a Task associated with a feed-enabled parent record (excluding
email tasks on cases). Also 00 rs when a user or the API adds or
updates a Task or Event associated with a record (excluding email
and call logging).

For a recurring Task with CaseFeed disabled, one event is generated
for the series only. For d recurring Task with CaseFeed enabled, events
are generated for the series and each occurrence.

AdvancedTextPost -created when user posts group
an nouncement and, in Lightning Experience as of API version 39.0
and later, when user shares a post.


### AnnouncementPost -Not used.



### ApprovalPost -generated when a user submits an approval.



### BasicTemp lateFeedItem -Not used.



### CanvasPost -a post made bya ca IV as app posted on a feed.


Collaboratiomtroupcreated -generated when a us creates a
public group.


### clawnatiorogplaraive -Not used.



### ContentPost -a post with an attached file.


nttps/develr
e.com/docs t. as s.en-us.oDje re re ence.met: a/o 00 n rer sforce.api_obyects._feeditem.htm


### =====



### 11/16



### =====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================

CreatedRecordEvent generated when a user creates a record from
the publisher.

DasmboarctompmentAlert -generated when a dashboard metric
or gauge exceeds a user-defined threshold.

DashboardComponentSnapshot -created when a user posts a
dashboard snapshot on a feed.


### LinkPost a post with an attached URL.



### PollPost a poll posted on a feed.


ProfileskillPost -generated when skill is added to a user's
Chatter profile.


### QuestionPost -generated when a user posts a question.



### ReplyPost -generated when Chatter Answers posts a reply.


RypplePost-generated when a user creates a Thanks badge in WDC.


### TextPost -a direct text entry on a feed.



## G


TrackedChange a change or group of changes to a tracked held.


### 0


UserStatus -automatically generated when a user adds a post.
Deprecated.

The following values appear in the Type picklist for all feed objects but apply
only to CaseFeed:

AttachArticleEvent generated event when a user attaches an
article to a cas se.

CallLogPost -generated ev e t when a user logs call for a case
through the user interface. CTI calls also generate this event.

CaseCommentPost -generated event when a user adds a case
comment for a a e object.

ChangestatusPost -generated event when a user changes the
status of a case.

ChatTranscriptPost generated event when Chat transcript is
saved to a case.

EmallMessageEvent -generated event when an email related to a
case object is sent or received.

FacebookPost -generated when a Facebook post is created from a
case. Deprecated.

MilestoneEvent -generated when a case milestone is completed or
reaches violation status.


### SocialPost-generated when a social post is created from a a



### # Note


If you set Type to ContentPost, also specify
contentData and ContentrileName


### Visibility



### Type



### picklist



### # Properties


Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### # Description


nttps/develr
e.com/docs t. as s.en-us.oDje
ence.meta a/oD je re erence/s SIC orce_api ot jects feeditem.htm


### =====



### 12/16



### =====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================

CreatedRecordEvent generated when a user creates a record from
the publisher.

DasmboarctompmentAlert -generated when a dashboard metric
or gauge exceeds a user-defined threshold.

DashboardComponentSnapshot -created when a user posts a
dashboard snapshot on a feed.


### LinkPost a post with an attached URL.



### PollPost a poll posted on a feed.


ProfileskillPost -generated when skill is added to a user's
Chatter profile.


### QuestionPost -generated when a user posts a question.



### ReplyPost -generated when Chatter Answers posts a reply.


RypplePost-generated when a user creates a Thanks badge in WDC.


### TextPost -a direct text entry on a feed.



## G


TrackedChange a change or group of changes to a tracked held.


### 0


UserStatus -automatically generated when a user adds a post.
Deprecated.

The following values appear in the Type picklist for all feed objects but apply
only to CaseFeed:

AttachArticleEvent generated event when a user attaches an
article to a cas se.

CallLogPost -generated ev e t when a user logs call for a case
through the user interface. CTI calls also generate this event.

CaseCommentPost -generated event when a user adds a case
comment for a a e object.

ChangestatusPost -generated event when a user changes the
status of a case.

ChatTranscriptPost generated event when Chat transcript is
saved to a case.

EmallMessageEvent -generated event when an email related to a
case object is sent or received.

FacebookPost -generated when a Facebook post is created from a
case. Deprecated.

MilestoneEvent -generated when a case milestone is completed or
reaches violation status.


### SocialPost-generated when a social post is created from a a



### # Note


If you set Type to ContentPost, also specify
contentData and ContentrileName


### Visibility



### Type



### picklist



### # Properties


Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### # Description


nttps/develr
e.com/docs t. as s.en-us.oDje
ence.meta a/oD je re erence/s SIC orce_api ot jects feeditem.htm


### =====



### 12/16



### =====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================

Specifies whether this feed item is available to all users or internal users only.
This field is available in API version 26.0 and later, if digital experiences is
enabled for your org.
Visibility can have the following values:

ALlUsers -The feed item is available to all user rs who have permission
to see the feed item.

InternalUsers: -The feed item is available to internal users only.

Note the following exceptions for Visibility:

For record posts, Visibility is set to In t er alUsers for all
internal users by default.


### External us can set Visibility only to AlLUsers.



### Visibility can be updated on record posts.


The Update property is supported only for feed items posted on
records.


### 0



### # Usage


When a feed item's Isclosed field is set to true, some actions are blocked and others are
blocked to most users. This table sets out the actions that are blocked when a feed item is
closed.


### Action



### Availability on a Closed Conversation



### [Table : unknown]



### erence el Moepiaaslseman


nttps:/dever
e.com/docs t. as s.en-us.obje CL rei erence.meta/ob


### =====



### 13/16



### =====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================

Specifies whether this feed item is available to all users or internal users only.
This field is available in API version 26.0 and later, if digital experiences is
enabled for your org.
Visibility can have the following values:

ALlUsers -The feed item is available to all user rs who have permission
to see the feed item.

InternalUsers: -The feed item is available to internal users only.

Note the following exceptions for Visibility:

For record posts, Visibility is set to In t er alUsers for all
internal users by default.


### External us can set Visibility only to AlLUsers.



### Visibility can be updated on record posts.


The Update property is supported only for feed items posted on
records.


### 0



### # Usage


When a feed item's Isclosed field is set to true, some actions are blocked and others are
blocked to most users. This table sets out the actions that are blocked when a feed item is
closed.


### Action



### Availability on a Closed Conversation



### [Table : unknown]



### erence el Moepiaaslseman


nttps:/dever
e.com/docs t. as s.en-us.obje CL rei erence.meta/ob


### =====



### 13/16



### =====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### [Table : unknown]



### [Image: unknown]


This Apex example shows how to add a feed item with an attachment to a lead using API
version 36.0 and later. First, post a feed item.


### =


//create and insert post
FeedItem post new FeedItem();
post.Body 'HelloThere';
post.ParentId D_UF.LEADENTITY?
post.Title = 'FileName' ';
insert post;


### 0



### Then insert the attachment.


//create and associate a content attachment to the post
reedAttachment feedAttacl hi ent ne ew FeedAttachment0;
esattacmemt.festatiyla = post.Id;
feedAt ttachment.Recordid D0F.OMEVERSON :
eecAttachment.Title = 'FileName';
fee,Attachment.lype = CONTENT';
insert feedAttachment;

If you're using API version 23.0 or later and have View All Data permission, you can directly
query for a Feeditem. The following example returns the 20 most recent feed items.

SELECT ID, CreatedDate, CreatedById, Createdby.FirstName, Createdby.LastName
(SELECT ID, FieldName, OldValue, NewValue FROM FeedTrackedChanges ORDER BY
FROM FeedItem
WHERE CreatedDate > LAST_MONTH
ORDER BY CreatedDate DESC

Ify you're using an earlier API version than version 23.0, query Feeditem objects through a
feed (such as AccountFeed or OpportunityFeed). The following example returns all feed
items for a given account, ordered by date descending:


## E


SELECT Id, Type, FeedItem. Body
FROM AccountFeed
WHERE ParentId Ac ccountId ORDER BY CreatedDate DESC

nttps/develr
e.com/docs t. as s.en-us.oDje re ence.met: a/ob je re re I orce_apL_oD Djects, _leedite em.htm


### =====



### 14/16



### =====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### [Table : unknown]



### [Image: unknown]


This Apex example shows how to add a feed item with an attachment to a lead using API
version 36.0 and later. First, post a feed item.


### =


//create and insert post
FeedItem post new FeedItem();
post.Body 'HelloThere';
post.ParentId D_UF.LEADENTITY?
post.Title = 'FileName' ';
insert post;


### 0



### Then insert the attachment.


//create and associate a content attachment to the post
reedAttachment feedAttacl hi ent ne ew FeedAttachment0;
esattacmemt.festatiyla = post.Id;
feedAt ttachment.Recordid D0F.OMEVERSON :
eecAttachment.Title = 'FileName';
fee,Attachment.lype = CONTENT';
insert feedAttachment;

If you're using API version 23.0 or later and have View All Data permission, you can directly
query for a Feeditem. The following example returns the 20 most recent feed items.

SELECT ID, CreatedDate, CreatedById, Createdby.FirstName, Createdby.LastName
(SELECT ID, FieldName, OldValue, NewValue FROM FeedTrackedChanges ORDER BY
FROM FeedItem
WHERE CreatedDate > LAST_MONTH
ORDER BY CreatedDate DESC

Ify you're using an earlier API version than version 23.0, query Feeditem objects through a
feed (such as AccountFeed or OpportunityFeed). The following example returns all feed
items for a given account, ordered by date descending:


## E


SELECT Id, Type, FeedItem. Body
FROM AccountFeed
WHERE ParentId Ac ccountId ORDER BY CreatedDate DESC

nttps/develr
e.com/docs t. as s.en-us.oDje re ence.met: a/ob je re re I orce_apL_oD Djects, _leedite em.htm


### =====



### 14/16



### =====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### Provide the ParentId for API version 22.0 and earlier.


A feed item of type UserStatus is automatically created when a u adds a post to update
the status. You can't explicitly create a feed item of type UserStatus.

The Feeditem object doesn't support aggregate Tunctions in queries.

If the context user has the Insert System Field Values for Chatter Feeds user permission, the
create field property is available on CreatedBy and CreatedDate system fields. During
migration, the context us t can set these fields to the original post's author and creation
date. The fields can't be updated after migration.


### The size limit for an attachment on a feed is 2 GB.


You can't use the content fields to update or delete the content.


### You can't filter or update the content fields.


Deleting a feed item via the API also deletes the associated content. Likewise, undeleting a
feed item restores associated content.


### 86



### # Note


This object is hard deleted. It isn't sent to the Recycle Bin.

After uploading to a feed, it's possible for an attachment or document to be deleted, marked
private, or hidden by sharing rules. In this case, all content fields in a FeedItem object appear
as null in a SOQL query.

You can't explicitly create or delete a reedirackedcnange record.

Imagine that you insert a feed item or feed comment of Type Cont tentPost on a User or
Group to create a file. Then the NetworkScope field value of the feed item is passed to the
file.

Ify you use an Apex trigger to modify the Body of a Feeditem object, all mentions hyperlinks
are converted to plain text. The mentioned us e ers don't get email notifications.

Ify you insert rich text into the feed item body, make sure that the case of the opening and
closing HTML tags matches. For example, <b>This is bold text</B> generates an Cl IC DI.

To check file sharing with Apex triggers, write triggers on or ntentDocumenttink instead of
Feeditem. For an example, see contentDocumentuink.

In API version 36.0 and later, us e FeedAttachment to attach or
content items to
feed item. As a result of support for multiple attachments through FeedAttachment, all fields
related to content attachments have been removed. These fields re: contentData,
contentDescription contentrlleName, ContentSize, and ContentType.

For all API versions of FeedItem, you can't query a FeedItem object using the System
Modstamp filter.

When you use the Feeditem object to create a record-triggered flow, and the flow tries to
update a field on the parent record, the field may not update in the UI until the page is
retreshed.

DID THIS ARTICLE SOLVE YOUR ISSUE?
Let us know SO we can improve!


### Share your feedback


nttps/develr
e.com/docs t. as s.en-us.oDje re ence.met: a/ob re
I orce_apL_oD Djects, _leedite em.htm


### =====



### 15/16



### =====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


### Provide the ParentId for API version 22.0 and earlier.


A feed item of type UserStatus is automatically created when a u adds a post to update
the status. You can't explicitly create a feed item of type UserStatus.

The Feeditem object doesn't support aggregate Tunctions in queries.

If the context user has the Insert System Field Values for Chatter Feeds user permission, the
create field property is available on CreatedBy and CreatedDate system fields. During
migration, the context us t can set these fields to the original post's author and creation
date. The fields can't be updated after migration.


### The size limit for an attachment on a feed is 2 GB.


You can't use the content fields to update or delete the content.


### You can't filter or update the content fields.


Deleting a feed item via the API also deletes the associated content. Likewise, undeleting a
feed item restores associated content.


### 86



### # Note


This object is hard deleted. It isn't sent to the Recycle Bin.

After uploading to a feed, it's possible for an attachment or document to be deleted, marked
private, or hidden by sharing rules. In this case, all content fields in a FeedItem object appear
as null in a SOQL query.

You can't explicitly create or delete a reedirackedcnange record.

Imagine that you insert a feed item or feed comment of Type Cont tentPost on a User or
Group to create a file. Then the NetworkScope field value of the feed item is passed to the
file.

Ify you use an Apex trigger to modify the Body of a Feeditem object, all mentions hyperlinks
are converted to plain text. The mentioned us e ers don't get email notifications.

Ify you insert rich text into the feed item body, make sure that the case of the opening and
closing HTML tags matches. For example, <b>This is bold text</B> generates an Cl IC DI.

To check file sharing with Apex triggers, write triggers on or ntentDocumenttink instead of
Feeditem. For an example, see contentDocumentuink.

In API version 36.0 and later, us e FeedAttachment to attach or
content items to
feed item. As a result of support for multiple attachments through FeedAttachment, all fields
related to content attachments have been removed. These fields re: contentData,
contentDescription contentrlleName, ContentSize, and ContentType.

For all API versions of FeedItem, you can't query a FeedItem object using the System
Modstamp filter.

When you use the Feeditem object to create a record-triggered flow, and the flow tries to
update a field on the parent record, the field may not update in the UI until the page is
retreshed.

DID THIS ARTICLE SOLVE YOUR ISSUE?
Let us know SO we can improve!


### Share your feedback


nttps/develr
e.com/docs t. as s.en-us.oDje re ence.met: a/ob re
I orce_apL_oD Djects, _leedite em.htm


### =====



### 15/16



### =====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


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


nttps:/dever
.com/docs/at!: las.en-us.ob j
en nce.meta a/ D0 re
I orce_api_ob jects._feeditem.htm


### =====



### 16/16



### =====



### ================



## 5/26/25, 9:32 AM



### ================


===========================================================================

FeedItem Object Reference for the Salesforce Platform Salesforce Developers

===========================================================================


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


nttps:/dever
.com/docs/at!: las.en-us.ob j
en nce.meta a/ D0 re
I orce_api_ob jects._feeditem.htm


### =====



### 16/16



### =====

