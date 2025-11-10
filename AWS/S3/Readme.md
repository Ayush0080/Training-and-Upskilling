### Amazon S3 – Lifecycle Rules
| Feature / Concept                     | Description                                                                                     | Key Actions / Options                                                    | Example Use Case                                                             |
| ------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| **Lifecycle Rules**                   | Automated rules in S3 to manage objects over time, reducing cost and maintaining data lifecycle | Transition, Expiration, AbortIncompleteMultipartUpload                   | Automatically move old logs to cheaper storage, delete temp files after time |
| **Scope**                             | Specify which objects the rule applies to                                                       | Prefix (folder/object key) or Tag-based filters                          | Apply rule only to objects with prefix `logs/` or tag `Project=Analytics`    |
| **Transition**                        | Move objects to a different storage class after a specified time                                | S3 Standard → S3 Standard-IA → S3 Glacier → S3 Glacier Deep Archive      | Move monthly backups to Glacier after 30 days to save cost                   |
| **Expiration**                        | Permanently delete objects after a certain period                                               | Specify days since creation or a specific date                           | Delete temporary upload files after 7 days                                   |
| **Abort Incomplete Multipart Upload** | Deletes unfinished multipart uploads after a set number of days                                 | Number of days after initiation                                          | Remove multipart uploads that never completed within 7 days                  |
| **Storage Classes Supported**         | Standard, Intelligent-Tiering, Standard-IA, One Zone-IA, Glacier, Glacier Deep Archive          | Can transition between storage classes using lifecycle rules             | Move infrequently accessed data to cheaper storage automatically             |
| **Rule Status**                       | Lifecycle rules can be active or disabled                                                       | `Enabled` or `Disabled`                                                  | Disable old rules during testing or policy change                            |
| **Cost Optimization**                 | Main purpose is to reduce storage costs while maintaining data availability                     | Automated transition to cheaper classes + expiration                     | Move old logs to Glacier → reduces S3 cost without manual intervention       |
| **Combination**                       | Multiple rules can be applied to the same bucket                                                | Rules can overlap, S3 evaluates each object against all applicable rules | Logs older than 30 days → Glacier, older than 365 days → Delete              |


| Storage Class                           | Durability / Availability         | Cost     | Access / Retrieval | Use Case / Description                                                                |
| --------------------------------------- | --------------------------------- | -------- | ------------------ | ------------------------------------------------------------------------------------- |
| **S3 Standard**                         | 99.999999999% (11 9’s) / 99.99%   | High     | Immediate          | Frequently accessed data, dynamic content, websites, applications                     |
| **S3 Intelligent-Tiering**              | 99.999999999% / 99.9–99.99%       | Medium   | Immediate          | Automatically moves data between frequent & infrequent tiers based on access patterns |
| **S3 Standard-IA** (Infrequent Access)  | 99.999999999% / 99.9%             | Lower    | Immediate          | Data accessed less often, but requires rapid access (e.g., backups, logs)             |
| **S3 One Zone-IA**                      | 99.999999999% / 99.5% (single AZ) | Low      | Immediate          | Infrequently accessed data, lower cost, single AZ (non-critical)                      |
| **S3 Glacier**                          | 99.999999999% / N/A               | Very Low | Minutes to hours   | Archival data, long-term backups, compliance data                                     |
| **S3 Glacier Deep Archive**             | 99.999999999% / N/A               | Lowest   | Up to 12 hours     | Long-term archival, rarely accessed data (years), lowest storage cost                 |
| **S3 Reduced Redundancy Storage (RRS)** | 99.99% / 99.99%                   | Lower    | Immediate          | Legacy option for non-critical, easily reproducible data (not recommended today)      |


### Amazon S3 Batch Operations

| Feature / Concept          | Description                                                                                                                                                                                  |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Scope**                  | Operates on objects in a **bucket** specified by a **manifest** (list of object keys, usually in CSV or S3 inventory).                                                                       |
| **Supported Actions**      | - Copy objects to another bucket or storage class<br>- Replace object tags<br>- Modify ACLs (permissions)<br>- Invoke AWS Lambda on objects<br>- Restore Glacier objects<br>- Delete objects |
| **Manifest File**          | List of S3 object keys to apply the operation to. Can come from:<br>- S3 Inventory reports<br>- Custom CSV files                                                                             |
| **Scalability**            | Can handle **billions of objects** in a single job.                                                                                                                                          |
| **Monitoring & Reporting** | Provides detailed **job reports** including success/failure for each object.                                                                                                                 |
| **Security**               | Can use **IAM roles** to control permissions and encrypt objects during operations.                    |                                               

### Storage Lens – Metrics
                                       
| Metric Category       | Metric Name / Description                                                                               | Type           | Applicable Scope / Notes | Use Case / Example                                                |
| --------------------- | ------------------------------------------------------------------------------------------------------- | -------------- | ------------------------ | ----------------------------------------------------------------- |
| **Storage Metrics**   | **Total Storage Bytes** – Total size of objects in bytes                                                | Usage          | Bucket, prefix, account  | Track total data usage, growth trends                             |
|                       | **Object Count** – Number of objects in the bucket                                                      | Usage          | Bucket, prefix, account  | Monitor bucket size and object growth                             |
|                       | **Object Size Distribution** – Number of objects by size ranges (0–128 KB, 128 KB–1 MB, etc.)           | Usage          | Bucket, prefix, account  | Identify storage pattern; optimize lifecycle or storage class     |
|                       | **Number of Multipart Uploads** – Incomplete multipart uploads                                          | Usage          | Bucket, prefix, account  | Cleanup old multipart uploads                                     |
|                       | **Average Object Size** – Average size per object                                                       | Usage          | Bucket, prefix, account  | Assess storage patterns for cost optimization                     |
| **Activity Metrics**  | **Number of Requests** – Total PUT, GET, COPY, POST, LIST, DELETE requests                              | Activity       | Bucket, prefix, account  | Monitor usage, detect spikes or unusual activity                  |
|                       | **Bytes Uploaded** – Data uploaded to S3                                                                | Activity       | Bucket, prefix, account  | Track upload activity, data growth                                |
|                       | **Bytes Downloaded** – Data retrieved from S3                                                           | Activity       | Bucket, prefix, account  | Detect heavy read activity, potential cost impact                 |
|                       | **4xx Errors** – Client errors                                                                          | Activity       | Bucket, prefix, account  | Troubleshoot application or access issues                         |
|                       | **5xx Errors** – Server errors                                                                          | Activity       | Bucket, prefix, account  | Identify service or configuration issues                          |
|                       | **Number of Requests per Operation Type** – PUT, GET, POST, LIST, COPY, DELETE                          | Activity       | Bucket, prefix, account  | Detailed analysis of operations per bucket                        |
| **Advanced Metrics**  | **Number of Objects with Intelligent-Tiering Transition** – Objects automatically moved to another tier | Advanced Usage | Bucket, prefix, account  | Track cost-saving transitions                                     |
|                       | **Number of Encrypted Objects** – Objects encrypted via SSE-S3, SSE-KMS, SSE-C                          | Advanced Usage | Bucket, prefix, account  | Compliance and security monitoring                                |
|                       | **Number of Replicated Objects** – Objects replicated across buckets (Cross-Region Replication)         | Advanced Usage | Bucket, prefix, account  | Track replication and disaster recovery coverage                  |
|                       | **Number of Public Objects** – Objects accessible publicly                                              | Advanced Usage | Bucket, prefix, account  | Security audit, ensure no sensitive data is public                |
|                       | **Number of Objects with Tags** – Objects that have tags                                                | Advanced Usage | Bucket, prefix, account  | Policy enforcement and lifecycle rules targeting tagged objects   |
| **Cost Metrics**      | **Estimated Storage Cost per Bucket / Storage Class** – Approximate cost per month                      | Cost           | Bucket, storage class    | Identify high-cost buckets, optimize storage class usage          |
|                       | **Estimated Cost per Account** – Aggregated estimated storage cost                                      | Cost           | Account level            | Track overall storage spend                                       |
| **Optional / Export** | Metrics can be exported to CSV or Parquet for further analysis                                          | Reporting      | Bucket, prefix, account  | Integrate with Athena, QuickSight, or custom analytics dashboards |



### Access Point
- S3 Access Point is basically a customized access entry (like a virtual endpoint) to an S3 bucket, each with its own:

    - Unique name and ARN

    - Custom permissions (IAM or resource-based policy)

    - Network configuration (public internet or VPC-only)