# AWS Services

## Storages

### S3 (Simple Storage Service)

- At its core is object storage.
- Storage and protection of large sums of data for various use cases, such as websites, applications, backup, and more.

### EFS (Elastic File System)

- A simple, scalable, fully managed elastic NFS file system.
- EFS provides massively shared access to thousands of Amazon EC2 instances.
- Used whenever you need a shared file storage option for multiple EC2 instances with automatic, high-performance scaling.

### EBS (Elastic Block Store)

- It is a block storage solution.
- Used within Amazon EC2 for throughput and transaction workloads of any size, at any time.
- It handles a diverse range of workloads, such as relational and non-relational databases, and enterprise applications.
- EBS used to be accessible to a single EC2 instance only, making it almost like your physical hard drive.
- EBS Instances can be either general-purpose SSDs (for general use) or Provisioned IOPS SSDs, for mission-critical workloads.
- When you need high-performance storage service for a single instance, use EBS.

### ECR (Elastic Container Registry)

- Is an AWS-managed container image registry service that is secure, scalable, and reliable.
- Supports private repositories with resource-based permissions using AWS IAM.

## Servers

### EC2 (Elastic Compute Cloud)

- Offers secure, and resizable computing capacity.
- Is for web-scale cloud computing.
- Allowing total control of your computing resources.

### ECS (Elastic Container Service)

- Used primarily to orchestrate Docker containers.

### EKS (Elastic Kubernetes Service)

- It is a managed Kubernetes service that makes it easy for you to run Kubernetes on AWS and on-premises.

### Lambda

- Run code without owning or managing servers.
- Only pay for the computing time consumed.
- Just upload the code, and Lambda does the rest, which provides precise software scaling and extensive availability.

## Databases

### RDS (Relational Database Services)

- It makes database configuration, management, and scaling easy.
- RDS is available on various database instances:

   - Amazon Aurora

   - PostgreSQL

   - MySQL

   - MariaDB

   - Oracle

   - SQL Server

### DynamoDB

- NoSQL database service that supports key–value and document data structures.
- Dynamo has built-in security with a fully managed, multi-master, multi-region, durable database, backup and restore, and in-memory archiving for web-scale applications.

## Caches

### Glacier

- It is for data caching and prolonged backup.

### ElastiCache

- Runs, and scales popular open-source in-memory data storage.
- It is a popular option for real-time use cases including caching, session stores, gaming, geospatial services, live analytics, and queuing.
- Offers fully managed Redis and Memcached applications.

## Other

### CodeBuild

- Is a fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy.

### Kinesis

- Offer timely insights.
- Collect, process, and analyze data in real-time.
- Ingest real-time data, including video, audio, application records, and website activity..

### SQS (Simple Queue Service)

- It is a fully managed message queuing facility.
- Can send, store, and receive messages between multiple software parts.

### Route 53

- It is a scalable and highly available Domain Name System (DNS) service.

### SES (Simple Email Service)

- It is an email tool that also supports a variety of deployments including dedicated, shared, or owned IP addresses.
- Supports SMTP protocol.
