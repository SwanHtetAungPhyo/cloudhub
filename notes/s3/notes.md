
---

### 🧠 **Amazon S3 – DVA-C02 Style Questions**

#### 1️⃣ Which of the following is **NOT** a valid Amazon S3 storage class?

* S3 Standard
* S3 Glacier
* S3 Intelligent-Tiering
* S3 Magnetic

<details>
<summary>🔽 Reveal Answer</summary>

✅ **Correct Answer:** `S3 Magnetic`
❌ *S3 Magnetic* is not an S3 storage class — it's associated with Amazon EBS (Elastic Block Store).

</details>

---

#### 2️⃣ What feature of Amazon S3 protects against **accidental overwrites or deletions**?

* S3 Object Lock
* Versioning
* S3 Lifecycle Policies
* MFA Delete

<details>
<summary>🔽 Reveal Answer</summary>

✅ **Correct Answer:** `Versioning`
📝 Versioning stores multiple versions of an object and allows you to restore deleted or overwritten versions.

</details>

---

#### 3️⃣ Which of the following services **can be directly notified by S3 event notifications**?

* EC2
* SQS
* SNS
* Lambda

<details>
<summary>🔽 Reveal Answer</summary>

✅ **Correct Answers:** `SQS`, `SNS`, `Lambda`
❌ `EC2` cannot receive S3 events directly.

</details>

---

#### 4️⃣ How is data **encrypted at rest** in Amazon S3?

* AWS KMS (SSE-KMS)
* SSE-S3 (Managed Keys)
* Client-Side Encryption
* RSA Key Pairs

<details>
<summary>🔽 Reveal Answer</summary>

✅ **Correct Answers:**

* SSE-S3
* SSE-KMS
* Client-Side Encryption

❌ RSA Key Pairs are not used directly by S3 encryption services.

</details>

---

#### 5️⃣ What access control method should you use to restrict access to a **specific IP address**?

* Bucket Policy
* IAM Role
* ACL (Access Control List)
* CORS Configuration

<details>
<summary>🔽 Reveal Answer</summary>

✅ **Correct Answer:** `Bucket Policy`
🛡️ Bucket policies allow conditions like `IpAddress` to restrict access to specific IPs.

</details>

---

### 🧠 Amazon S3, Lambda & AWS Services – DVA Quiz

#### 6️⃣ A developer needs to securely serve private website content stored in S3 through CloudFront so users **cannot bypass** CloudFront. How should this be implemented?

* Use CloudFront Origin Access Control (OAC) + update S3 bucket policy
* Enable S3 static website hosting + point CloudFront at bucket website endpoint
* Make the S3 bucket public and set CloudFront header to restrict
* Add a custom header to CloudFront origin + bucket policy with `aws:RequestTag`

<details>
<summary>🔽 Reveal Answer</summary>

✅ **Correct Answer:** Use CloudFront Origin Access Control (OAC) + update S3 bucket policy
This ensures content is served **only** via CloudFront, without exposing the S3 bucket directly ([examtopics.com][1], [examtopics.com][2], [examtopics.com][3], [jayendrapatil.com][4], [examtopics.com][5]).

</details>

---

#### 7️⃣ A company has multiple branches uploading daily sales reports to an S3 bucket. A single Lambda processes all reports at the same time every day. What’s the **most cost-effective** trigger?

* S3 Event Notification on each upload
* Step Functions state machine scheduled
* Always-running Lambda waiting for time
* EventBridge scheduled rule at specified time

<details>
<summary>🔽 Reveal Answer</summary>

✅ **Correct Answer:** EventBridge scheduled rule
EventBridge cron rule triggers the Lambda **once per day**, avoiding unnecessary invocations ([tutorialsdojo.com][6]).

</details>

---

#### 8️⃣ What is the **recommended way** for on-premises applications to securely access AWS services?

* Assign IAM role to on-prem server
* Create IAM user + store credentials in `~/.aws/credentials`
* Use STS AssumeRole from on-prem
* Use IAM user + hashed password in credentials file

<details>
<summary>🔽 Reveal Answer</summary>

✅ **Correct Answer:** Create IAM user + store credentials in `~/.aws/credentials`
On-prem apps can't use IAM roles natively, so using long-term credentials in AWS credentials files is correct .

</details>

---

#### 9️⃣ Which solution ensures **automatic rotation** of database credentials for an RDS MySQL instance?

* Store credentials in environment variables and rotate AMIs
* Store credentials in Parameter Store with rotation
* Store credentials in Secrets Manager with rotation
* Store credentials in env vars and relaunch EC2s

<details>
<summary>🔽 Reveal Answer</summary>

✅ **Correct Answer:** Store credentials in AWS Secrets Manager with rotation
Secrets Manager manages and rotates credentials for RDS automatically ([examtopics.com][3]).

</details>

---

#### 🔟 Which S3 storage class is **NOT valid**?

* S3 Intelligent-Tiering
* S3 Glacier
* S3 Magnetic
* S3 Standard

<details>
<summary>🔽 Reveal Answer</summary>

✅ **Correct Answer:** S3 Magnetic
That's an EBS volume type, not an S3 storage class.

</details>

---

#### 1️⃣1️⃣ What solution requires the **least development effort** to enrich messages from SQS before sending them to fulfillment?

* Lambda polls SQS → enrich → SNS → Lambda
* Step Functions triggered by EventBridge → Lambda → completion
* EMR cluster to enrich → upload to S3
* Use EventBridge Pipes to filter & enrich from SQS to fulfillment

<details>
<summary>🔽 Reveal Answer</summary>

✅ **Correct Answer:** Use EventBridge Pipes
Pipes streamline SQS → enrichment → target flow with minimal code ([serverlessland.com][7], [examtopics.com][3]).

</details>

---

#### 1️⃣2️⃣ In EventBridge Pipes, what built-in step lets you add data to events before sending them to the target?

* Filter
* Input Transformer
* Enrichment
* Target Transformer

<details>
<summary>🔽 Reveal Answer</summary>

✅ **Correct Answer:** Enrichment
EventBridge Pipes supports enrichment steps—e.g., calling a Lambda to add data to incoming events ([docs.aws.amazon.com][8]).

</details>



[1]: https://www.examtopics.com/discussions/amazon/view/4172-exam-aws-certified-security-specialty-topic-1-question-74/?utm_source=chatgpt.com "Exam AWS Certified Security - Specialty topic 1 question 74 ..."
[2]: https://www.examtopics.com/discussions/amazon/view/87524-exam-aws-certified-solutions-architect-associate-saa-c03/?utm_source=chatgpt.com "Exam AWS Certified Solutions Architect - Associate SAA-C03 topic 1 ..."
[3]: https://www.examtopics.com/discussions/amazon/view/153146-exam-aws-certified-developer-associate-dva-c02-topic-1/?utm_source=chatgpt.com "Associate DVA-C02 topic 1 question 476 discussion - ExamTopics"
[4]: https://jayendrapatil.com/aws-cloudfront-with-s3/?utm_source=chatgpt.com "AWS CloudFront with S3 - Jayendra's Cloud Certification Blog"
[5]: https://www.examtopics.com/discussions/amazon/view/127068-exam-aws-certified-security-specialty-scs-c02-topic-1/?utm_source=chatgpt.com "Exam AWS Certified Security - Specialty SCS-C02 topic 1 question ..."
[6]: https://tutorialsdojo.com/amazon-eventbridge/?utm_source=chatgpt.com "Amazon EventBridge Cheat Sheet - Tutorials Dojo"
[7]: https://serverlessland.com/patterns/eventbridge-pipes-sqs-to-sqs-with-lambda-enrichment-dotnet?utm_source=chatgpt.com "SQS to SQS with EventBridge Pipes and Lambda Enrichment"
[8]: https://docs.aws.amazon.com/eventbridge/latest/userguide/pipes-enrichment.html?utm_source=chatgpt.com "Event enrichment in Amazon EventBridge Pipes"
