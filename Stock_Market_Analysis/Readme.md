
##Compare Major Stock Tickers of US Market

## Uses these	representative	major	stock	indexes:

  a. NASDAQ	Composite:	Yahoo!	ticker:	“^IXIC”

  b. NYSE	Composite:	Yahoo!	ticker:	“^NYA ”

  c. Dow	Jones	Industrial	Average:	Yahoo!	ticker:	“^DJI”

  d. S&P	500:	Yahoo!	ticker:	“^GSPC”

  e. 'Shanghai	Composite':	'000001.SS'

  f. Euro	STOXX	50:	Yahoo!	ticker:	“^STOXX50E”

2. Ask	the	user	to	type	in a	list	of	any other individual stock	tickers.		For	example,	they	
might	enter	“IBM,	MSFT,	ORCL,	CSCO,	XOM”.

3. Automatically	download	the	stock	data	(including	the	indexes)	for	the	past	24 months	
(up	to	current	date),	from	Yahoo	(as	shown	in	the	examples) for	all	listed	tickers.
Note:	You	may	find	that	sometimes	when	we	query	Yahoo!	using	the	datareader,	it	
can	fail	and	has	to	be	retried.		Make	your	program	automatically	handle	this	instead	
of	crashing.

4. Your	program	should	load	all	those stock	price	histories	into	one	or	more Pandas	
DataFrame. Specifically,	we’ll	use	the	“adjusted	close”	prices and	ignore	the	other	price	
data.

5. Then,	calculate	the	correlations	between	each	of	the	user-specified tickers	against	each	
Index.

6. Output	a	result	that	shows	which	index	correlates	most	strongly	with	each	individual	
stock	and vice	versa.

7. Make	use	of	the	Pandas	shift()	method	to	help	calculate	whether	any	of	the	stocks	
correlate	more	strongly	with	an	index	when	shifted	anywhere	in	the	range	up	to	5 days	
earlier	or	later.		Output	the	strongest	finding	for	each	combination,	only	if	they	exceed	
the	date-aligned	ones	calculated	previously.	Although	such	a	finding	does	not prove	any	
predictive	causation	between	the	prices,	it’s	an	interesting	conjecture	to	explore
further,	if	any	high	correlation	is	discovered.
