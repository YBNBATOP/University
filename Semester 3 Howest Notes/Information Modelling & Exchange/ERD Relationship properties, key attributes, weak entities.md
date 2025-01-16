# Relationships
## Participation
Participation of a relationship - the participation constraint of a relationship specifies the number of instances of an entity type that can participate in a relationship

We can have: 
- **partial** participation: an entity **may** take part in the relationship
- **total** participation: every entiry **must** take part in the relationship

In general words - it shows us the minimum amount of values it can have. For example, a student must have at least 1 course.
## Cardinality
The cardinality of a relationship is a constraint on a relationship indicating how many instances of an entity type can relate to one instance of another entirty type

For relationships with two roles, this can be:
- one to one
- one to many/many to one
- many to many
In general words - it shows the maximum amount of values it might have

## Participation vs Cardinality
The participation of a relationship defines the minimum number of related entities on a relationship (0 or 1), the cardinality of a relationship defines the maximum number of related entities on a relationship (1 or more)

## Attribute of a relationship
Sometimes it is not enough to just specify it, so that is why we might sometimes need to upgrade a relationship to an entity type, especially if we got more than 1 attribute.





# Key attributes
A key attribute is an attribute in ER diagrams twhose vlaues are constant and distinct for each individual entity in an entity set.

Sometimes there is a need for multiple attributes to uniquely identify entities in an entity set

There may be more than one attribute composing the key: the combination of those attributes are unique for each individual entity of an entity type and no attribute in the combination is obsolete. One attribute in that composition is called partial key attribute.

# Weak entity
If the existence of an entity depends on the existence of another entity, we say the entity is a weak entity

A partial key, also knows as discriminator, is the set oof attributes which can uniquely identify weak entities that are related to the same owner entity

An entity that cannot be uniquely identified by its own attributes and relies on the relationship with one or more other (strong) entities. A weak entity needs another (strong) entity to be uniquely identifiable.

The identity of a weak entity is composed of its own partial key and the key of the related strong entity.

A weak entity has always a many to one weak relationship with a strong entity. The weak entity has full participation in the relationship. The strong entity can be full or partial participation.
A weak entity must be related to one or more strong entities.



