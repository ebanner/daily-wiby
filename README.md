# daily-wiby

Fetch today's daily random [wiby.me](https://wiby.me) site

## Description

[wiby.me](https://wiby.me) is a search engine for old school web 1.0 websites. They have a "surpise me" button which will take you to a random site.

I wanted to have a "daily" random wiby website. And that's what this does.

## Architecture

- Lambda
- Lambda Layer (requests + boto3)
- S3 (cache)
- IAM role + policy (for accessing S3 from Lambda)

## Setting up

Here's some instructions for how to deploy this thing

### Create S3 bucket

<img width="1296" alt="image" src="https://github.com/ebanner/daily-wiby/assets/2068912/b87d05fd-83ca-4569-b8e0-245d75cc3257">

### Create a IAM Policy

You need to create a new IAM policy for each lambda with S3 permissions and access to a specific bucket.

<img width="1296" alt="image" src="https://github.com/ebanner/daily-wiby/assets/2068912/24935bc8-9116-4175-a1a8-7ee999ef3557">

### Add `GetObject` and `PutObject` permissions

<img width="1296" alt="image" src="https://github.com/ebanner/daily-wiby/assets/2068912/ed837e9f-08e2-4442-907f-e15dff27baea">

<img width="1252" alt="image" src="https://github.com/ebanner/daily-wiby/assets/2068912/0d1346a6-1617-4340-8603-ffc467db4b61">

### Specify bucket

<img width="1296" alt="image" src="https://github.com/ebanner/daily-wiby/assets/2068912/636bd3b4-0583-4c81-af91-9cd2bf222f6c">

### Create a role and add the policy

<img width="1296" alt="image" src="https://github.com/ebanner/daily-wiby/assets/2068912/b978f071-b9e2-4e89-80c6-04f73e6e6069">

### Create the lambda function with the role

<img width="1445" alt="image" src="https://github.com/user-attachments/assets/54eaa295-4bfd-4bbf-9d1f-ee67d8e7d765">

## Resources

[Upload to S3 From Lambda Tutorial | Step by Step Guide (YouTube)](https://www.youtube.com/watch?v=vXiZO1c5Sk0)
