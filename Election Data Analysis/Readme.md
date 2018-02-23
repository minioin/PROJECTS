Single-file queries:

Data Set: Federal Elections Commission
http://classic.fec.gov/finance/disclosure/ftpdet.shtml files for download and the metadata.


List all individuals who donated a TOTAL of over 100,000 dollars. Show name, city, state, employer, occupation, and total amount. [Tip: You must groupby name+city+state or by name+zipcode]

List top 10 cities by total individual donations. Try creating a visual barchart with matplotlib.

<img width="473" alt="capture" src="https://user-images.githubusercontent.com/31773426/36612930-92a79c3e-189d-11e8-85c8-ee2fa2fd0abc.PNG">

<img width="459" alt="capture_1" src="https://user-images.githubusercontent.com/31773426/36613094-1016267c-189e-11e8-95f7-9a2336d1029f.PNG">





List the top 5 organisation which donated the maximum amount. ORG = Organization (not a committee and not a person)

<img width="494" alt="0capture" src="https://user-images.githubusercontent.com/31773426/36618481-e2b31a6a-18b0-11e8-8d8e-686f1c49ff08.PNG">



Multi-file queries (needing merge or join). Some of these are good ways to see corruption in action:

Find people who donated over 5000 directly to a Senate or House candidate who's not even in their own state, and show the details. [Tip: You'll need to compare the candidate's state to the individual donor's state after you get them joined.] http://classic.fec.gov/finance/disclosure/metadata/DataDictionaryPartyCodeDescriptions.shtml]
Download all 3 individual donations files (itcont.txt) from 2014, 2016, and 2018. Figure out how to concatenate them (just the columns you need) into a single DataFrame covering that whole range from 2013-2018. Then use that to compute an analysis of questions such as:
Political activity is much higher for Presidential elections than in other years. Find out whether the level of donations to Senate and House campaigns goes up or down at that time compared to other years.

<img width="471" alt="1capture" src="https://user-images.githubusercontent.com/31773426/36618653-9941ee82-18b1-11e8-8d7a-c1190e50d80e.PNG">


