# Logging
Analyse imformation:
- Downtime
- Performance
- Bugs
- Attacks

The issue can be anywhere in the infrastructure
- Attakcs on your website and in case of compromise, tracing what was done (forensics)
- Failing database
- Failing api server
- Traffic message broker

Different groups, differend insights needed

Developers:
- Debug logs: providing stack traces and exceptions

Sysadmins:
- See if everything is working as expected
- Logins outside of normal working hours

Security team:
- Authentication activity
- Resource access
- Malware activity
- Recognize security problems and respond to them

Log and analysis solutions have the following capabilities:
- Aggregation - the ability to collect and ship logs from multiple data sources
- Processing - the ability to transform log messages into meaningful data for easier analysis
- Storage - the ability to store data for extended time periods to allow for monitoring, trend analysis, and security use cases
- Analysis - the ability to dissect the data by quering it and creating visulizations and dashboards on top of it.

## Log monitors
Opening many log files manually can be cumbersome:
- Different log files, different log formats, different locations, ...
- Couldn't we just centralize all useful data and one location?
- Can we avoid logging into the server to view our log files?

# ElasticStack
The ELK Stack began as a collection of three open-source products - Elasticsearch, Logstash, and Kibana - all developed, managed and maintained by Elastic.

The introduction and subsequent addition of Beats turned the stack into a four legged project.

It allows:
- Deploy and manage logs
- Get insights for structured and unstructured logs
- Search across everything with search that scales
- Real-time troubleshooting with live tail
- Detect patterns and outliers with log categorization and anomaly

## Elasticsearch
Elasticsearch is a full-text search and analysuis engine, based on the Apache Lucene open source search engine

## Logstash
Logstash is a log aggregator that collects data from various input sources, executes different transformations and enhancements and then ships the data to various supported output destinations.

## Kibana
It is a visualization layer that works on top of Elasticsearch, providing users with the ability to analyze and visualize the data

## Beats
Beats are lightweight agents taht are installed on edge hosts to collect different types of data for forwarding into the stack.

