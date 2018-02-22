import pandas_datareader.data as web    #Import pandas data reader for reading data from the web
import datetime                         #Import datetime module
from datetime import date


start_date = datetime.datetime(2015,10,10)   #defining start date
end_date=date.today()                        #defining the end date


def reading_indexes():
    """
        This below block of code will fetch data of all the tickers from the yahoo website
       :return:
    """
    tickers=['^IXIC','^NYA','^DJI','^GSPC','^STOXX50E','000001.SS']
    #create a list of tickers (Indexes)
    dic={}
    #create a empty dictionary
    index_ticker={}
    #create a empty dictionary
    for ticker in tickers:
    #loop for iteration on tickers
        while True:
         #This loop will fetch data unless it is captured properly without an error

            try:
            #This is a try block
                dic[ticker] = web.DataReader(ticker, 'yahoo', start_date, end_date)
                #This will read the data from the web
                print(ticker)
                #print ticker name
                print("Data contains {} rows and {} columns".format(*dic[ticker].shape))
                #Print the dimension of ticker
                print("Start date: {}\nEnd date: {}".format(start_date, end_date))
                #Print the start and end date of the ticker
                print()
                #for space
                index_ticker[ticker]=dic[ticker]["Adj Close"].pct_change()
                #extracting column from the data frame by making percentage changes
                print (index_ticker[ticker])
                #print the ticker
                print()

                break
            except:
            #executes when we are unable to download from the website
                print("Remote Error")


def correlation_max():
    """
     This below block will create correlation between company stocks ( input by user) and tickers specified in the above program
     For example stock input by user ="IBM" then this will be correlated with tickers=['^IXIC','^NYA','^DJI','^GSPC','^STOXX50E','000001.SS']
     Then  stock( input by user) & ticker will be printed based on the maximum value of correlation
    :return:
    """

    tickers = ['^IXIC', '^NYA', '^DJI', '^GSPC', '^STOXX50E', '000001.SS']
    # create a list of tickers (Indexes)
    dic = {}
    # create a empty dictionary
    index_ticker = {}
    # create a empty dictionary
    for ticker in tickers:
        # loop for iteration on tickers
        while True:
            # This loop will fetch data unless it is captured properly without an error

            try:
                # This is a try block
                dic[ticker] = web.DataReader(ticker, 'yahoo', start_date, end_date)
                # This will read the data from the web
                index_ticker[ticker] = dic[ticker]["Adj Close"].pct_change()
                # extracting column from the data frame by making percentage changes
                break
            except:
                # executes when we are unable to download from the website
                print("Remote Error")


    global max_values_correlation
    #creating the global variable so that it can be accessed by other functions
    max_values_correlation=[]
    #Create the empty list for storing the maximum values of the correlation
    dic_stock_correlation={}
    #create the empty dictionary for storing the correlation
    for i in range(len(input_tickers)):
    #loop for iteration on the length of tickers specified by the user
        for j in tickers:
        #loop for iteration on tickers
            dic_stock_correlation[j]=(stock_ticker[input_tickers[i]].corr(index_ticker[j]))
            #creating dictionary with key as tickers and correlation as values
        q=max(dic_stock_correlation.values())
        #print the maximum value of correlation
        max_values_correlation.append(q)
        #appending maximum value of correlation in the list
        print(dic_stock_correlation)
        #print the dictionary correlation
        for key in dic_stock_correlation.keys():
        #loop for printing the ticker associated with maximum value
            if dic_stock_correlation[key]==q:
            #checking the key where we find the maximum value
                print ("The",input_tickers[i],"stock correlates most strongly with",key,"index")
                #print which stock correlates maximum with which index
                print()




def index_correlation():
    """
    This below block will correlate the tickers=['^IXIC','^NYA','^DJI','^GSPC','^STOXX50E','000001.SS'] with the company stock specified by the user input like IBM,MSFT

    :return:
    """


    tickers = ['^IXIC', '^NYA', '^DJI', '^GSPC', '^STOXX50E', '000001.SS']
    # create a list of tickers (Indexes)
    dic = {}
    # create a empty dictionary
    index_ticker = {}
    # create a empty dictionary
    for ticker in tickers:
        # loop for iteration on tickers
        while True:
            # This loop will fetch data unless it is captured properly without an error

            try:
                # This is a try block
                dic[ticker] = web.DataReader(ticker, 'yahoo', start_date, end_date)
                # This will read the data from the web
                index_ticker[ticker] = dic[ticker]["Adj Close"].pct_change()
                # extracting column from the data frame by making percentage changes
                break
            except:
                # executes when we are unable to download from the website
                print("Remote Error")


    dic_index_correlation = {}
    #create the empty dictionary for storing correlation
    for i in range(len(tickers)):
    #loop for calculating the maximum correlation
        for j in input_tickers:
        #loop for iteration on input tickers specified by user
            dic_index_correlation[j] = (stock_ticker[j].corr(index_ticker[tickers[i]]))
            #dictionary for storing the correlation
            q = max(dic_index_correlation.values())
            #print the maximum valueso of the dictionary
            print()
            print(dic_index_correlation)
            #print the dictionary
            for key in dic_index_correlation.keys():
                #loop for printing the ticker associated with maximum values
                if dic_index_correlation[key] == q:
                #condition for checking the key associated with maximum values
                    print("The", tickers[i], "index correlates most strongly with",key, "stock")
                    #Print the index maximum correalted with the stock





def shifted_correlation():
    """
     Part 7 of the assignment
     This below block of code will fix the stock ticker input by the user and will shift the index ticker ( 5 places up and 5 places down), then calculating the maximum correlation with each combination.
     Then we will compare this maximum correlation with the correlation calculated earlier.

     :return:
    """

    tickers = ['^IXIC', '^NYA', '^DJI', '^GSPC', '^STOXX50E', '000001.SS']
    # create a list of tickers (Indexes)
    dic = {}
    # create a empty dictionary
    index_ticker = {}
    # create a empty dictionary
    for ticker in tickers:
            # loop for iteration on tickers
            while True:
                # This loop will fetch data unless it is captured properly without an error

                try:
                    # This is a try block
                    dic[ticker] = web.DataReader(ticker, 'yahoo', start_date, end_date)
                    # This will read the data from the web
                    index_ticker[ticker] = dic[ticker]["Adj Close"].pct_change()
                    # extracting column from the data frame by making percentage changes
                    break
                except:
                    # executes when we are unable to download from the website
                    print("Remote Error")


    z={}
    #create dictionary for storing the maximum correlation values
    list_stock_shift_correlation=[]
    #create the empty list for storing  correlation values
    for i in range(len(input_tickers)):
                #loop for calulating the maximum value of correlation when the index ticker shifted upwards and downwards
                for j in tickers:
                #loop for iteration onto each tickers
                    for h in range(-5,6):
                    #loop for shifting the index ticker upwards and downwards
                        if h!=0:
                        #condition for not calucating the correlation when there is no shift
                         list_stock_shift_correlation.append((stock_ticker[input_tickers[i]].corr(index_ticker[j].shift(h))))
                        #appending the values in list for each correlation

                        else:
                            continue
                            #go to the starting of the loop

                    z[j]=max(list_stock_shift_correlation)
                    #founding the maximum correlation and storing it in the dictionary
                    list_stock_shift_correlation=[]
                    #emptying the list so that correlation can stored again for different values
                shifted_correlation=max(z.values())
                #storing the maximum value in dictionary in the shifted_correlation variable
                if shifted_correlation>max_values_correlation[i]:
                    #checking if the shifted correlation calculated above is different when compared with correlation calcuated when there is no shift
                  for f in z:
                  #loop for printing the stock and ticket if there is any change in the maximum correlation calculated above in the program
                    if z[f]==shifted_correlation:
                    #condition for printing the index associated with maximum value of correlation
                        print("The", input_tickers[i], "stock correlates most strongly with the shifted index up or down five days", f, "index")
                        #print which stock correlated most with the tickers
                else:
                  pass
                #pass the program if there is no change




reading_indexes()


#This below block will print the stock ticker entered by the user

input_tickers=input("Enter the ticker").split(",")
#Enter the company ticker
stock={}
#create the empty dictionary
stock_ticker={}
#create the empty dictionary
for ticker in input_tickers:
#loop for iteration through input tickers
        while True:
        #loop will continue until the data is published

            try:
            #this block will fetch data from website
                stock[ticker] = web.DataReader(ticker, 'yahoo', start_date, end_date)
                #fetch data from the website as a ticker enter by user
                print(ticker)
                #print the ticker
                print("Data contains {} rows and {} columns".format(*stock[ticker].shape))
                #print  the row and column of the company stock tickers
                print("Start date: {}\nEnd date: {}".format(start_date, end_date))
                #print the start and end date
                print()
                #print the space
                stock_ticker[ticker]=stock[ticker]["Adj Close"].pct_change()
                #create the stock ticker by selecting column from the data frame and then computing percentage changes
                print (stock_ticker[ticker])
                #print the stock ticker
                print()
                #print the space
                break
            except:
            #this will execute when we are unable to fetch data from website
                print("Remote Error")

correlation_max()
index_correlation()
shifted_correlation()