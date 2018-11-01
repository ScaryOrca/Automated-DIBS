# Automated-DIBS
Python script to automatically reserve a Volpe Library study room at 4:00 PM. Uses Tennessee Tech's DIBS API. This script can run daily with the use of crontab.
There is no documentation for DIBS API, so packet analysis was done with Chrome's network inspect tool in order to determine the POST API URL, parameters, and headers required.

Run requirements:

1. Use python3 dibs.py (or just python Main.py, but make sure python version is 3.6+ and not 2.7)
2. Needs requests package installed (use python3 -m pip install X)
