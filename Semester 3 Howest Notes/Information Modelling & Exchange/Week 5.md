# Modelling issues
## Relations with only identifying attributes
If we want a relation with all possible dates/names of country (where you can choose a valid date/country) then the relation must be kept

If we want a relation with the used dates/names of country the it's possible to drop the relation (dates/country names can be retrieved by querying the corresponding ...)

Nevertheless, it's better that relation Country has a meaningless primary key. As country name should be unique add a uniqueness constraint

The relation Calendar is clearly redundant

## Standard value and exceptional value
All articles are delivered on the same date

Mostly articles are delivered on the same date but exceptions occur. If the deliveryDate of an order detail is not null then the exceptional delivery date is in charge.