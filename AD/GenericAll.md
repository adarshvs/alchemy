# GenericAll
---
## GenericAll on Group
If the user we have has GenericAll permissions on a group, this allows us to add the current owned user to that group.
```
net group "Domain Admins" cbbn /add /domain
```

## GenericAll on User
If our user has GenericAll rights over a user, we can reset the user password without knowing the current password.
