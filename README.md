# GenAPI for Warren.io

## Create an article for SEO purposes
[x] Favourite articles of FreshRSS from an iOS app or web interface.
[x] Fetch favourite articles from FreshRSS and insert to Baserow database table.
[] Fetch RACE prompting instructions from Baserow table.
[] Fetch unpublished articles from Baserow table.
[] Inject original unpublished article into RACE prompt instructions.
[] Send RACE prompt to Gemini Pro 1.5 to return Warren version.
[] Populate Warren oriented article into Baserow database.
[] N8N will publish on Warren.io every day.
[] N8N will notify Slack channel to review and unpublish in case doesn't meet quality standards.
[] Create Linkedin post for manual posting
[] Create Tweets to post automatically to X





## Deploy with docker compose
```
$ chmod +x ./restart.sh
$ ./restart.sh
```

## Shutdown services
Stop and remove the containers
```
$ docker compose down
```

## Expected behavior 

