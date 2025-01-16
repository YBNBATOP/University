# Design / Conceptual
Entity types
Attributes
Relationships

ERD can be used but also fact based modelling languages like ORM, NIAM,  FCO-IM that might have better expression possibilities

# Database design

## Logical
Relations
Attributes
Relationships

ERD can be used but no fact based modelling languages
## Physical
Tables
Columns
Foreign Key relationships
Indexes

## Relation and attributes
- Notation of entity type can be used for relations, but add an additional first column to indicate some contraints like PK, FK, UC...
- Relation name: same name as entity type
- Include all the simple (optional and non-optional) attributes
- Put optional attributes in brackets

# Entity type to relation
## Key attribute
### Strong entity type
- Primary key (PK)
	- Choose an identifying attribute or combination of those attributes
	- Prefer a single attribute
	- Prefer an attribute without a meaning
	- In case of combination of attributes: no part of the key is redundant
- Candidate keys: mark as uniqueness constraint (UC/ UCx and x a number)

Weak entity type
- Primary key
	- Take the primary key of all owner entity types (with a many-to-one relationship) and add each as attribute and make it part of the key. If the combination is not identifying take extra identifying attributes as part (should have been modelled at conceptual level). But remember: no part of the key is redundant!
- Candidate key: mark as uniqueness constraint.

## Derived attribute
Is there an added value (ex. performance) to store in table?
- No
	- calculate in code (after fetching)
	- calculate in query (while fetching)
	- calculate with stored procedure or view (while fetching)
- Yes
	- calculate in database trigger (on insert, on update, on delete) to guard consistency but only possible if dependent on values in database

## Composite attribute
- Split in simple atrributes
- Create an extra relation if it can be a concept, split in simple attributes and treat it as an extra entity type (ex. address) with a one to many relationship with the former
- Keep it composite (ex. date json) if the parts are not that important

## Multi-valued attribute
- Create a new relation
- Add that attribute as an attribute of the new relation
- If that attribute is not suited to be part of the key, add an extra meaningless attribute
- Take the primary key of the relation where the multi-valued attribute belonged to and add it as attribute and make it part of the key of the new relation. Together with the other key attribute it will be the primary key.

# Binary relationship
## One-to-many
- The entity type on the one side is the parent entity type
- The entity type on the many side is the child entity type
- Add the primary key of the parent relation as attribute of the child relation and create a foreign key relationship from the child to the parent. Mark the attributes with FKx - x as a number to avoid function if needed.
- Draw an arrow from the foreign key to the prmary key (cfr databases)

## One-to-one both mandatory 
Mandatory participation on both sides of the relationship
- Keep separate relations and choose the primary key of one of the relations as primary key in the other relation where the original will be changed as alternate key (or drop it if not important)
- Keep separate relations and their primary keys but add in one of the relations the primary key as attribute and make it an alternate key
- Database trigger should guard the mandatory on the other side in those cases
- Combine the attributes in one relation and chose one of the keys as primary key and the other as alternate key (or drop it if not important)

## One-to-one mandatory/optional
Mandatory participation on one side of the relationship
- The entity type on the mandatory side is the parent entity type
- The entity type on the optional side is the child entity type

Mandatory participation on one side of the relationship
- Keep separate relations and choose the primary key of the parent relation as primary key in the child relatiomn where the original will be changed as alternate key (or drop it if not important)
- Keep separate relations and their primary keys but add in the child relation the primary key as attribute and make it an alternate key
- Combine the attributes in one relation and chose the key of the parent as primary key and the other as alternate key (or drop it if not important). Make the attributes of the client relation optional

# N-ary relationship
## Many-to-many
- Create a relation
- Add eventual attributes to the relation (normally in crow's foot notation the relationship shoudl should have been already upgraded as an entity type)
- Add the primary key of all related relations as attribute and make the combination the primary key of the relation

# Supertype / Subtype to relation - different mappings
## Supertype / Subtype
- Create one relation for the supertype and one relation per subtype (SP+#SB)
- Create one relation for the supertype with all attributes of the subtypes + flag for indicating each subtype (SP)
- Create one relation for the supertype and one relation for all the attributes of all subtypes + flag for indicating each subtype (SP+SB)
- Create one relation per subtype and add the attributes of the supertype in each relation (#SB)
