# [sync lotus notes calendar with google calendar](http://lngooglecalsync.sourceforge.net/index.html)


## Setup Info:

Google now requires applications like LNGS to use an OAuth 2.0 Client ID to sign into Google Calendar.

You must create your own Client ID as follows:

1. Go to <https://cloud.google.com/console/project>.

2. Click Create Project.

3. Set Project Name to something like "LN Cal Sync". You can leave Project ID alone.

4. Click Create.

5. On the left side, click APIs & Auth.

6. Turn the Calendar API to ON and everything else OFF.

7. On the left side, click Credentials.

8. Click Create New Client ID.

9. Click Installed Application then select Other.

10. Click Create Client ID.

11. Click Download JSON.

12. Save the file into the same dir as lngsync.jar. It will have a long name like client_secret_760911730022-0nbs07o6o6qqc3ru4guooasalmrvbo89.apps.googleusercontent.com.json.
Note: This file may be renamed to a shorter name because LNGS will look for any file named client_secret*.json.

13. Run LNGS and do a sync. A web browser window will open asking you to authorize Google Calendar access. After the authorization is complete, LNGS should be able to connect to Google Calendar automatically. If the web browser doesn't open, try deleting the credential file which is in the main LNGS directory and is named client_credential.
