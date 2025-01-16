We will see how to model a inheritance.
If you do not know how to model something, then sometimes you can skip it.

There are diffrent versions of inheritance:
- Single inheritance
- Hierarchical inheritance
- Multilevel inheritance
- Multiple inheritance

## Inheritance notation in ERD
To show that an entity inherits from a super entity, then we just use a triangle from the super entity.

Imagine having a Type **Game**, then you can have a class/entity type **FamilyGame**, **PuzzleGame**.

## Inheritance constraints
We might need, sometimes, for an attribute to be  a part of 2 entity types (like a game might be both a Puzzle and Family Game). This is also shown as a triangle of a entity type, and then we just add the **(mandatory)** text inside, which will mean that the entity should be a part of at least one of the other entity set. Vice-versa, it might be **(optional)**.
As well we can have **{or}** if it should include at least in one of the types.
As well, we can have **{and}**, if an entity is included in both of them.

# Advice
Sometimes when working on the ERD, we should make sure whether something we are talking about is a part of UoD (a system as a whole), or an entity type.

Sometimes we need to make a difference betweek a concept and something that "can be touched". Although, this does not always relate to every situation when modelling.

Sometimes, if an attribute is the same for different entites from an entity set, then we can say it is a part of UoD. Like imagine a subscription price. If it is the same for every member, then we can include it in UoD. If not, then things are different.

Sometimes it is also very important who inherits from who. Imgine you have an entity class BoardGame, Category, and a PuzzleGame, RiddleGame etc. Then each game type will inherit from the **BoardGame** entity, and **not the Category** one.

