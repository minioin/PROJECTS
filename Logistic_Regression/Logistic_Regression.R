#Data statistics:
Dt<-read.csv(file="C:\\Users\\tejve\\Desktop\\Arrowsmith.csv",head=TRUE,sep=",",skip = 4)
attach(Dt)
summary(Dt)

# Summary Statistics:

#1.
#Literature sizes should be comparable.
y_equals_x <- function(x) {x}
y_equals_x_by_2 <- function(x) {x/2}
# Plot literature C size vs literature A size.
lit_A_size <- tapply(A.lit.size, Arrowsmith.search, mean)
lit_C_size <- tapply(C.lit.size, Arrowsmith.search, mean)
plot(lit_A_size,lit_C_size,xlim = c(0,7000), ylim = c(0,7000), xlab = "Literature A size", ylab= "Literature C size",pch = 16, main = "Literature A size vs Literature C size")
curve(y_equals_x,from = 0, to = 7000, add = TRUE)
curve(y_equals_x_by_2,from = 0, to = 7000, add = TRUE)
#The literature ( A and C) sizes are not comparable as we can see

#2.
#Number of B terms for each standard:
barplot(tapply(B.term,Arrowsmith.search,length),main="Number of B terms for each standard")

#There is quite a deep variation in number of B-terms for each standard

#3.
#Nof Mesh Terms in common:


hist(nof.MeSH.in.common,probability = TRUE, main = "Density histogram for number of common MeSH terms",xlab = "Number of common Mesh terms")
hist(log10(nof.MeSH.in.common),probability = TRUE, main = "Density histogram for number of common MeSH terms log10 scaled.",xlab = "log10(Number of common Mesh terms)")
boxplot(nof.MeSH.in.common,ylab="nof.MeSH.in.common")
#From the Box-plot we see that term has outliers.(points which outside the 1.5 times the Interquartile Range)
# It also has missing values(99999)

#4.
boxplot(nof.semantic.categories,ylab="nof.semantic.categories")
#From the boxplot The variable nof.semantic.Categories has outliers.(points which outside the 1.5 times the Interquartile Range)


# 5. Exploring cohesion score
hist(cohesion.score, main = "Cohesion score histogram",xlab = "Cohesion score")
# As seen in the histogram, number of values above 0.3 is very few. Hence, that might be the motive choosing 0.3 as the upper limit.
boxplot(cohesion.score,ylab="cohesion.score")
#From the boxplot we see that the variable has significant outliers.(points which outside the 1.5 times the Interquartile Range)
# The variable cohesion.score has missing values(0.99990)

#6.
boxplot(n.in.MEDLINE,ylab="n.in.MEDLINE")
# From the boxplot we see the variable n.in.MEDLINE has outlier.(points which outside the 1.5 times the Interquartile Range)

#7.
#Pairwise scatter plots.
plot(Dt[1:13])

#There was no relation found among any pairs of variables, but just literature A and literature C size. However, these two are not used to calculate two different features.

#8
boxplot(nA,ylab="nA")
# From the boxplot the "nA" variable has outlier.(points which outside the 1.5 times the Interquartile Range)

#9

boxplot(nC,ylab="nC")
# From the boxplot the "nC" variable has outlier.(points which outside the 1.5 times the Interquartile Range)


# 9. A new feature. x_new

x_new <- -abs((nA/A.lit.size) -(nC/C.lit.size))
# I think that none of the features capture intuition that if a B-term occurs a lot frequently in A but not in C or vice-versa, then it is less relevant. In other words, number of articles containing B-term should be in both literatures should be comparable.
# The number of occurences in MEDLINE is a similar feature but that only captures that very common and very rare words in MEDLINE are less relevant. It doesn't capture the intuition that a B-term very frequent in one literature but very rare in other literature will mostly likely be irrelevant.
# I am not sure if this will prove to be a useful parameter. It is even difficult to test because we are not provided with any test data. The best evaluation I can do is check for statistical significance based on the p-value




#After Transformation:


#X1 = 1 if (nA > 1 or A-lit size < 1000) and (nC > 1 or C-lit size < 1000), 0 otherwise

X1<-ifelse((nA > 1 | A.lit.size < 1000) & (nC > 1 | C.lit.size < 1000),1,0)


#X2 = 1 if nof MeSH > 0 and < 99999, 0.5 if nof MeSH = 99999, 0 otherwise


X2<-c()
for (i in 1:length(nof.MeSH.in.common)) {
if (nof.MeSH.in.common[i] >0 & nof.MeSH.in.common[i] < 99999) {
  X2<-append(X2,1)
} else if (nof.MeSH.in.common[i] == 99999) {
  X2<-append(X2,0.5)
} else {  X2<-append(X2,0) }
}
# The variable nof.mesh.in.common has missing values before transformation,after transformation(X2) there are no missing values.
boxplot(X2,ylab="nof.mesh.in.common")
#From the boxplot we see that there are no outliers.(points which outside the 1.5 times the Interquartile Range)


#X3 = 1 if nof semantic categories > 0, 0 otherwise

X3<-ifelse(nof.semantic.categories>0,1,0)

## The variable nof.semantic.categories have outliers before transformation but after transformation it does not have. 
boxplot(X3,ylab="nof.semantic.categories")
#From the boxplot we see that there are  outliers.(points which outside the 1.5 times the Interquartile Range)


#X4 = cohesion score if cohesion score < 0.3, 0.3 otherwise

X4<-ifelse(cohesion.score<0.3,cohesion.score,0.3)
##The variable cohesion.score has missing values before transformation but after transformation there are no missing values.
boxplot(X4,ylab="cohesion.score")
#From the box plot we see that it does not have outliers.(points which outside the 1.5 times the Interquartile Range)


#X5 = -|log10(n in MEDLINE) - 3|

X5<--abs(log10(n.in.MEDLINE)-3)
boxplot(X5,ylab="n.in.MEDLINE")
#From the box plot we see that n.in.MEDILINE has outliers.(points which outside the 1.5 times the Interquartile Range)



#X6 = max(min(1st year in MEDLINE,2005),1950)

X6<- pmax(pmin(X1st.year.in.MEDLINE,2005),1950)
boxplot(X6,ylab="1st year in MEDLINE")
#From the boxplot we see that it has too many outliers.(points which outside the 1.5 times the Interquartile Range)


#X7 = min(8,-log10(pAC+0.000000001))

X7<-pmin(8,-log10(pAC+0.000000001))
boxplot(X7,ylab="pAC")
#From the box plot we see that X7 does not have any outliers.(points which outside the 1.5 times the Interquartile Range)


#I1 = 1 if Arrowsmith search = 'retinal detachment', 0 otherwise

I1<-ifelse(Arrowsmith.search=='retinal detachment vs aortic aneurysm',1,0)
I2<-ifelse(Arrowsmith.search=='NO and mitochondria vs PSD',1,0)
I3<-ifelse(Arrowsmith.search=='mGluR5 vs lewy bodies',1,0)
I4<-ifelse(Arrowsmith.search=='magnesium vs migraine',1,0)
I5<-ifelse(Arrowsmith.search=='Calpain vs PSD',1,0)
I6<-ifelse(Arrowsmith.search=='APP vs reelin',1,0)

#Y = 1 if target = 0 or 2, 0 otherwise

Y<-ifelse(target==0 | target==2 ,1,0)

new_frame<-data.frame(X1=X1,X2=X2,X3=X3,X4=X4,X5=X5,X6=X6,X7=X7,I1=I1,I2=I2,I3=I3,I4=I4,I5=I5,I6=I6,Y=Y)
summary(new_frame)



#Logistic Regression


## Checking for assumptions:
# Independence: As sample size is quite large, assuming that all observations are independent from each other.
# Multicollinearity: I checked for corelation by pairs command (Scatter plot). There was none found.Hence, it can be concluded that there is no multicollinearity.



# Weights' interpretation:
# All weights are interpreted as how much would log(odds) change with one unit change in that feature provided everything else is constant.
# For binary features, weight is interpreted as how much log(odds) will change if that feature is true.

# Model evalation techniques used:
# 1. Check p-values of all estimates.
# 2. Check null deviance of the model

fit_model<-glm(formula=Y~X1+X2+X3+X4+X5+X6+X7+I1+I2+I3+I4+I5+I6,family=binomial,data=new_frame)
summary(fit_model)
plot(fit_model)
#The null deviance decrease from 2853.9 to 1997.5 ,so the model is better fitted by logistic regression.
#I saw from the summary(fit_model) command all the weights related to my feature (x1 to x7) are related to  the model described in Table
#S2 (in the supplemental data file) in the research  paper.
# All the P -values of the features(estimate) (X1 to X7) is less than 0.05 ,so the model is statistically significant .There is a relationship between output (Y) and the features ( X1 to X7).
# The estimate(Weight) of X1 is "0.73220"->binary feature, weight is interpreted as how much log(odds) will change if that feature is true 
#The estimate (Weight) of X2 is "0.98770"->log(odds) change with one unit change in that feature provided everything else is constant.
#The estimate (Weight) of X3 is "1,31738"->binary feature, weight is interpreted as how much log(odds) will change if that feature is true 
#The estimate (Weight) of X4 is "13.76594"->log(odds) change with one unit change in that feature provided everything else is constant.
#The estimate (Weight) of X5 is "0.58621"->log(odds) change with one unit change in that feature provided everything else is constant.
#The estimate (Weight) of X6 is "0.03957"->log(odds) change with one unit change in that feature provided everything else is constant.
#The estimate (weight) of X7 is "0.18873"->log(odds) change with one unit change in that feature provided everything else is constant.
#The intercept is (-86.14907) ,it means when the features predicting the output has zero value , then we will get this output(log(odds))




