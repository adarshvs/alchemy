# Mongo 
------

In a linux machine, if a mongo db runs internally:
```bash
ss -lntp | grep '27017'
```

Use `mongo` to drop into a mongo shell:
```bash
>show databases

>use backup

>show collections

>db.user.find()
```

