# 🛡️ Privacy Statement

It is the explicit aim of this project to store the absolute minimal amount of information,
for the minimum time functionally required by the application.

This is done by omitting account registration, only keeping functional logs
and storing all possible information exclusively within the session state. 

## Data included
- Any/all data uploaded by the user via file uploads.
- Any/all data requested from the user server via HTTP requests.
- Any/all data resulting from internal data transformations.

## Data removal
The session state, and therefore all available data, is immediately cleared upon:
- App refresh
- Page refresh
- Tab close
