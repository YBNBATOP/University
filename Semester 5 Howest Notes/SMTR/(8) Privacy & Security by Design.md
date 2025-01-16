Teacher: Koen Verbeke
For exam - general understanding should be enough
# Data protection by design
You can process personal data if: (lawfulness processing, legal base to process data)
- You've asked nicely = consent
- Its needed for a contract = contractual interest
- legal obligation
- vital interest
- public interest
- legitimate interest

You also have principles:
- lawfulness & transparency
- accountability
- purpose limitation
- data minimisation (very important)

Data protection should always be doable, as in you should pay for what you need and can protect. Mostly we should care about the risks for the **data subject**

GDPR is about protection of data, not privacy.
## DPIA (Data Protection Impact Assessment)
This is the level where we assess the risks for the data subject, by analyzing data and etc.
The whole idea is that we have risks to rights and freedom of the data subject, such as discrimination, fraud, and other things.

There are 3 types of activities that make you do a DPIA.
SA (Supervising authority) provides list of cases where DPIA is obligatory

A DPIA shall in **particular** be required in case of:
- a systematic and extensive evaluation of personal aspects relating to natural persons which is based on automated processing, including profiling, and on which decisions are based that produce legal effects concerning the natural person or similarly significantly affect the natural person
- processing on a large scale of special categories of data referred to in Art. 9(1) or of persoanl data relating to criminal convictions and offences referred to in Art. 10
- A systematic monitoring of a publicly accessible area on a large scale
GBA/APD has its own activities, in case of which you should also do a DPIA
EDPB has 9 criteria, to identify high-risk processing, and means that you should conduct a DPIA.

DPIA execution:
- Four important questions to ask
- In essence, it is a risk analysis

There are also criteria for an acceptable DPIA
# Privacy by design
There are seven foundational principles
- Proactive not Reactive
- Privacy as the default setting
- privacy embedded into design
- full functionality - positive-sum, not zero-sum
- end-to-end security - full lifecycle protection
- visibility and transparency - keep it open
- respect for user privacy - keep it user-centric
## Privacy design strategies
Data oriented strategies

Here we need 8 things, to be remembered for sure (KNOW BY HEART)
- Minimise
	- Limit as much as possible the data you use.
- Split data
	- Separate the processing of personal data as much as possible
- Abstract
	- Limit as much as possible the detail in which personal data is processed
- Hide
	- Protect personal data or make it unlinkable or unobservable
- Inform
	- Inform data subjects about the processing of their personal data in a timely and adequate manner
- Control (data subject has a choice)
- Demonstrate (transparency)
	- Demonstrate you are processing personal data in an appropriate way
- Enforce (use policy)
# Privacy-enhancing technologies (PETs)
## Syntethic data
This is about the usage of data, for example for testing purposes. In this case, it is about having a fake data set, that allows you to make work, without the usage of other things.

This has advantages, but also pitfalls.
If you have bias in your original dataset, you might have some in your synthetic one as well, if you derive from it.
## Hashing & encryption
End-to-end encryption.
## On-device processing 
Advantages:
- Lower bandwidth
- Power saving
- Faster response times
- Increased availability
- Personal data remains on the device
- No extra cost
## FIDO/passkeys
Authentication protocol designed to grant access.
## Anonymisation & pseudonymisation
Anonymising - getting rid of links
Pseudonymise - not diriect link to somebody
### Risks to anonymisation
Singling out - isolate to identify
Linkability - combining datasets to identify
Inference - deduction leads to identification
## PETs in practice
There are a couple of questions before we apply the PET.

This are important to just know they exist for the exam.
# Security by design

# Exercise 
## Synthetic data
Purpose of the application
How the thing is useful
Risks

Instead of anonymising data, they use both the original and synthetic data.
They do test between the both, the results were quite identical. It gives same results, but not.

The outcomes compared with their algorithm were very similar.
The modelling process can be done on this syntethic version, which reduces the risk of data breaches. 
When training, they used the original data, create the synthetic data, and compare them to see the outcome.
It uses k-anonymity to do the anonymisation.
They avoided the biasing, by creating a holdout set for scoring the models. Also used for measuring the accuracy. A holdout set is a subset of the original dataset.

the dataset was a telecom dataset provided by SAS containing the data of 56k customers.

The further trainings cost more money, because you use the original data set. So fur

Risks:
Risks of bias is avoided because we are using holdout sets, to score the models. So when we have the models to create the synthetic data, it will be as accurate as possible.
