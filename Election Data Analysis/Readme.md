Single-file queries:
List all individuals who donated a TOTAL of over 100,000 dollars. Show name, city, state, employer, occupation, and total amount. [Tip: You must groupby name+city+state or by name+zipcode]
List top 10 cities by total individual donations. Try creating a visual barchart with matplotlib.


Data Set: Federal Elections Commission
http://classic.fec.gov/finance/disclosure/ftpdet.shtml files for download and the metadata.


Multi-file queries (needing merge or join). Some of these are good ways to see corruption in action:

Find people who donated over 5000 directly to a Senate or House candidate who's not even in their own state, and show the details. [Tip: You'll need to compare the candidate's state to the individual donor's state after you get them joined.] http://classic.fec.gov/finance/disclosure/metadata/DataDictionaryPartyCodeDescriptions.shtml]
Download all 3 individual donations files (itcont.txt) from 2014, 2016, and 2018. Figure out how to concatenate them (just the columns you need) into a single DataFrame covering that whole range from 2013-2018. Then use that to compute an analysis of questions such as:
Political activity is much higher for Presidential elections than in other years. Find out whether the level of donations to Senate and House campaigns goes up or down at that time compared to other years.
Find out how many and what percentage of individual donors have contributed to BOTH a Democratic and a Republican candidate at some point.
