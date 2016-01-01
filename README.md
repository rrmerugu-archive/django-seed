# rsquarelabs-xyz api



## Technical Stack
- Django
- Django Restframework
- PostgreSQL (Primary Database)
- MongoDB (Secondary Database)


## Installation

brew install postgresql
pip install psycopg2


```

To have launchd start postgresql at login:
  mkdir -p ~/Library/LaunchAgents
  ln -sfv /usr/local/opt/postgresql/*.plist ~/Library/LaunchAgents
Then to load postgresql now:
  launchctl load ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist
Or, if you don't want/need launchctl, you can just run:
  postgres -D /usr/local/var/postgres
==> Summary

```

## Reasons why I moved from MongoDB to PostgreSQL as Primary Database
1. MongoEngine support was removed recently(from 0.9) and don't know when they will be back, currently it is 0.10.5
2. MongoEngine support pymongo2.7, where as the latest is pymongo3.2
3. MongoEngine support djangorestframework till 3.0.5, where as currently it is 3.3.2
4. In PostgreSQL 9.4 more efficient  JSONB type is added, so **we can have a mix of relational and document data** (which is very likely).
5. https://www.quora.com/Which-database-should-I-use-for-a-killer-web-application-MongoDB-PostgreSQL-or-MySQL
6. http://www.aptuz.com/blog/is-postgres-nosql-database-better-than-mongodb/
7. http://thebuild.com/presentations/json2015-pgconfus.pdf

## Reference

https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn
