---
title: Untitled Document
document_type: guide
primary_topics: sales, salesforce
last_preprocessed: 2025-05-24
---


### # ==Group==


A set of User records. ==Group==s are sets of users. They can contain individual users, other ==group==s, the users in a particular role or territory, or the users in a particular role or territory plus all the users below that role or territory in the hierarchy.


### # Supported Calls


create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), search(), retrieve(), update(), upsert()


### # Special Access Rules


Authenticated internal and external users can access this object.


### # Fields


Field Details Description * Type textarea Properties Create, Filter, Nillable, Sort, Update Description* The description of the ==group==. This field is available in API version 62.0 and later. DefaultDivision * Type picklist Properties Create, Defaulted on create, Filter, ==Group==, Restricted picklist, Sort, Update Description* This record’s default division. Only applicable if divisions are enabled. DeveloperName * Type string Properties Create, Filter, Group, Nillable, Sort, Update Description The name of the object in the API. This name can contain only underscores and alphanumeric characters, and must be unique in your org. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. In managed packages, this field prevents naming conflicts on package installations. With this field, a developer can change the object’s name in a managed package and the changes are reflected in a subscriber’s organization. This name is unique by group type and corresponds to Group Name in the user interface. This field is available in API version 24.0 and later. When creating large sets of data, always specify a unique DeveloperName for each record. If no DeveloperName is specified, performance may slow while Salesforce generates one for each record. Only your Salesforce org’s internal users can access this field. DoesIncludeBosses * Type boolean Properties Create, Defaulted on create, Filter, ==Group==, Sort, Update Description* Indicates whether records shared with users in this ==group== are also shared with users higher in the role hierarchy (true) or not (false). This field is only available for public ==group==s. This field corresponds to the Grant Access Using Hierarchies checkbox in Setup. This field is available in API version 18.0 and later. DoesSendEmailToMembers * Type boolean Properties Create, Defaulted on create, Filter, ==Group==, Sort, Update Description* Indicates whether the email is sent (true) or not sent (false) to the ==group== members. The email is sent to queue members as well. Email * Type email Properties Create, Filter, ==Group==, Nillable, Sort, Update Description* Email address for a ==group== of type Case. Applies only for a case queue. Name * Type string Properties Create, Filter, ==Group==, idLookup, Sort, Update Description Required. Name of the ==group==. Corresponds to Label * on the user interface. OwnerId * Type reference Properties Filter, ==Group==, Sort Description ID of the user who owns the ==group==. This is a polymorphic relationship field. Relationship Name Owner Relationship Type Lookup Refers To Organization, User QueueRoutingConfigId * Type reference Properties Create, Delete, Query, Retrieve, Update Description* The ID of the queue routing configuration associated with the queue. RelatedId * Type reference Properties Filter, ==Group==, Nillable, Sort Description Represents the ID of the associated ==group==s. For ==group==s of type “Role,” the ID of the associated UserRole. The RelatedId field is polymorphic. This is a polymorphic relationship field. Relationship Name Related Relationship Type Lookup Refers To User, UserRole Type * Type picklist Properties Create, Filter, ==Group==, Restricted picklist, Sort Description* Required. Type of the ==group==. One of the following values:  * AllCustomerPortal—Public ==group== that includes all Customer Portal or Customer Community Plus users. This type is only available when a Customer Portal or a Customer Site is enabled for your org. * ChannelProgram==Group==—Public ==group== for partners in a channel program.   * Collaboration==Group==—Chatter ==group==. * Manager— Public ==group== that includes a user’s direct and indirect managers. This ==group== is read-only.   * ManagerAndSubordinatesInternal— Public ==group== that includes a user and the user’s direct and indirect reports. This ==group== is read-only.    * Organization—Public ==group== that includes all the User records in the organization. This ==group== is read-only.    * Participant—Compliant Data Sharing ==group== that includes internal users who have the Use Compliant Data Sharing permission. A ==group== can contain other participant ==group==s only, or a ==group== can contain both internal users with the Use Compliant Data Sharing permission and other participant ==group==s. This value is only available when Compliant Data Sharing is enabled for your org.    * PRMOrganization—Public ==group== that includes all the partners in an organization that has the partner site or portal feature enabled.   * Queue—Public ==group== that includes all the User records that are members of a queue.    * Regular—Standard public ==group==. When you create() a ==group==, its type must be Regular, unless a partner site or portal is enabled for the organization, in which case the type can be Regular or PRMOrganization.    * Role—Public ==group== that includes all the User records in a particular UserRole.    * RoleAndSubordinates—Public ==group== that includes all the User records in a particular UserRole and all the User records in any subordinate UserRole. The availability of this value depends on the type of org, org creation date, release update enforcement status, and whether digital experiences is enabled. For more information, see this knowledge article . * RoleAndSubordinatesInternal—Public ==group== that includes all the User records in an internal UserRole, excluding customer and partner roles, and all the User records in any subordinate internal UserRole. The availability of this value depends on the type of org, org creation date, release update enforcement status, and whether digital experiences is enabled. For more information, see this knowledge article .  * SharingRecordColl==Group==—Public ==group== that has access to a SharingRecordCollection. * Territory—Public ==group== that includes all the User records in an organization that has the territory feature enabled.  * TerritoryAndSubordinates—Public ==group== that includes all the User records in a particular UserRole and all the User records in any subordinateUserRole in an organization that has the territory feature enabled.Only Personal, Regular, and Queue can be used when creating a ==group==. The other values are reserved.


### # Usage



### Unlike users, this object can be deleted.


Only public ==group==s are accessible via the API. Personal ==group==s are not available.

In API version 34.0 and later, you can query a ==group== using Related.Name to retrieve the ==group==’s name. Related.Name is supported for public ==group==s, user roles, territories, manager ==group==s, and user names.

In API version 13.0 and later, if you delete a public ==group==, it is deleted even if it has been used in sharing, consistent with the behavior for UserRole. In versions before 13.0, such sharing prevents the record from being deleted.


### # See Also



### ==Group==Member



## Overview of Salesforce Objects and Fields

