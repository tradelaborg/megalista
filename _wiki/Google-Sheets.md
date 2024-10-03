**Using Google Sheets:**
 - Make a copy of the [Sheets template](https://docs.google.com/spreadsheets/d/1Mu0yj7RWw_cr3bevWCnjXyODlCbdmabWDLsBvPv2EVY/copy?resourcekey=0-ZqbZ72FJVIa8X4YgelHUHA#gid=0)
 - In the "Intro" sheet provide Account IDs for Google Ads, Analytics, CM360, etc.
 - Configure source/input data in the "Sources" sheet
 - Configure destinations in the "Destinations" sheet
  + The "Help" sheet has a chart to document the required metadata for each use case.
 - Configure connections from Sources to Destinations in the "Connect" sheet
 - Make note of the Sheet's ID in the URL: `docs.google.com/spreadsheets/d/`**EXAMPLEIDHERE**`/edit`

***
**Spreadsheet Configuration** 
   - All data upload rules are defined in a single configuration spreadsheet. 
   The trix contains four tabs: Intro, Sources, Destinations,  Connector:

1. **Intro Tab:** Holds basic, common information across upload rules

2. **Sources tab:** 
  Holds the bigQuery location of each data source. **Important**: The schema of each bigQuery source table needs to perfectly match the expected schema of the destination type that will be used with:
  - **Source Name:** A friendly name for that source
  - **Dataset:** BigQuery dataset name
  - **Table:** BigQuery table name
![image](https://user-images.githubusercontent.com/6962758/191812503-4e394696-ea28-4671-9efc-fcfd13771cd1.png)

3. **Destinations Tab:** Defines where the data should be send to - according to the destination type and expected metadata information
 - **Destination Name:** Friendly name of each destination
 - **Type:** The type of upload, limited to supported upload destinations
 - **Metadata[1-6]:** Additional required pieces of information expected by each destination type (details can be found at the corresponding destination type's wiki page)
![image](https://user-images.githubusercontent.com/6962758/191812938-e07caf8f-f71c-409a-a3d2-8a6b1f3096ca.png)

4. **Connect Tab:** Responsible for mapping a source to a destination
 - **Enabled (Yes/No):** Disabled lines are ignored at runtime
 - **Source:** The friendly name of a Megalista source
 - **Destination:** The friendly name of a Megalista destination
![image](https://user-images.githubusercontent.com/6962758/191820347-9ba625fa-c585-404e-a3ab-15862d388ad3.png)

