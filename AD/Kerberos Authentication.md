# Kerberos Authentication 
--------------------------------------

- Kerberos is an alternative to NTLM 
- Kerberos only works with hostnames & not IPs
- IPs will still use NTLM

## Authentication Process
-----------------------------


1.  When a user wants to login, they request a ticket from DC (User ticket or TGT) which is used for the entire session.  **AS - REQ**
	1. The user doesnt send their password but the timestamp encrypted with their password (known as Pre-Auth data).



2. The DC decrypts the data w the user's password and if the time is the current time it hands out the Ticket Granting Ticket (TGT) and the Session Key.  **AS - REP**
	1. The Session Key is inside the TGT (E1) and  also sent seperately (E2) and will be encrypted differently each time.
		

3. Using these tickets the user now requests access to a Service Ticket. **TGS - REQ**
	1. These tickets contain the user ticket (TGT) along with the timestamp encrypted with the Session Key (Authenticator).
	2. We can get the session key only if we have the password of the user.
	
 
4. The DC now sends back a Service Ticket (Ticket Granting Service ticekt) which has a Session Key inside of it (E3) encrypted w the Service Account password & a new Session Key (E2) encrypted w user password. **TGS - REP** 


5. The Service Ticket is sent to the Hosted Service and works as an authentication mechanism here.  **AP - REQ**

6.  The ticket  is decrypted using Service Account's password and validated. <br> </br>

E1 - Encrypted w Krbtgt Account Password (only DC is aware of this password)
E2 - Encrypted w User Password
E3 - Encrypted w Service Account Password


![[Kerberos_2.png]]

