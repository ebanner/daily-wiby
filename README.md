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

### Create lambda function

![image](https://github.com/ebanner/daily-wiby/assets/2068912/85686d83-0119-4900-a1d3-7f26eea25fad)

### Zip code

```
$ make zip
rm -rf .venv
rm -rf python python.zip
rm -rf lambda.zip
zip -r lambda.zip *
  adding: Makefile (deflated 43%)
  adding: README.md (deflated 35%)
  adding: lambda_function.py (deflated 51%)
  adding: requirements.txt (stored 0%)
  adding: s3_daily_cache.py (deflated 62%)
```

### Upload as zip

<img width="1092" alt="image" src="https://github.com/ebanner/daily-wiby/assets/2068912/67b48c71-c548-4486-80bd-4e130f6eb39d">

### Create S3 bucket

<img width="1296" alt="image" src="https://github.com/ebanner/daily-wiby/assets/2068912/b87d05fd-83ca-4569-b8e0-245d75cc3257">

### Create a IAM Policy

<img width="1296" alt="image" src="https://github.com/ebanner/daily-wiby/assets/2068912/24935bc8-9116-4175-a1a8-7ee999ef3557">

### Add `GetObject` and `PutObject` permissions

<img width="1296" alt="image" src="https://github.com/ebanner/daily-wiby/assets/2068912/ed837e9f-08e2-4442-907f-e15dff27baea">

<img width="1252" alt="image" src="https://github.com/ebanner/daily-wiby/assets/2068912/0d1346a6-1617-4340-8603-ffc467db4b61">

### Specify bucket

<img width="1296" alt="image" src="https://github.com/ebanner/daily-wiby/assets/2068912/636bd3b4-0583-4c81-af91-9cd2bf222f6c">

### Create a role and add the policy

<img width="1296" alt="image" src="https://github.com/ebanner/daily-wiby/assets/2068912/b978f071-b9e2-4e89-80c6-04f73e6e6069">

## Resources

[Upload to S3 From Lambda Tutorial | Step by Step Guide (YouTube)](https://www.youtube.com/watch?v=vXiZO1c5Sk0)
