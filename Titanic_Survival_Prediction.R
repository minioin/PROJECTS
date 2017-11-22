titanic.train<-read.csv("C:/Users/tejve/Downloads/train.csv",stringsAsFactors = FALSE,header = TRUE)
titanic.test<-read.csv("C:/Users/tejve/Downloads/test.csv",stringsAsFactors = FALSE,header = TRUE)

titanic.train$isTrainset<-TRUE
titanic.test$isTrainset<-FALSE

titanic.test$Survived<-NA

titanic.full<-rbind(titanic.train,titanic.test)

titanic.full[titanic.full$Embarked=="","Embarked"]<-"S"

#fare.median<-median(titanic.full$Fare,na.rm=TRUE)
#titanic.full[is.na(titanic.full$Fare),"Fare"]<-fare.median

upper.whisker<-boxplot(titanic.full$Fare)$stats[5]
outlier.filter<-titanic.full$Fare<upper.whisker


fare.equation<-"Fare~Pclass+Sex+Age+SibSp+Parch+Embarked"
fare.model<-lm( formula=fare.equation,data=titanic.full[outlier.filter,])

fare.row<-titanic.full[is.na(titanic.full$Fare),c("Pclass","Sex","Age","SibSp","Parch","Embarked")]

fare.predictions<-predict(fare.model,newdata = fare.row)
titanic.full[is.na(titanic.full$Fare),"Fare"]<-fare.predictions


#median.age<-median(titanic.full$Age,na.rm=TRUE)
#titanic.full[is.na(titanic.full$Age),"Age"]<-median.age

upper.whisker<-boxplot(titanic.full$Age)$stats[5]
lower.whisker<-boxplot(titanic.full$Age)$stats[1]
outlier.filter.Age<-titanic.full$Age>lower.whisker & titanic.full$Age<upper.whisker
Age.equation<-"Age~Pclass+Sex+SibSp+Parch+Fare+Embarked"
Age.model<-lm(formula=Age.equation,data=titanic.full[outlier.filter.Age,])
Age.row<-titanic.full[is.na(titanic.full$Age),c("Pclass","Sex","Fare","SibSp","Parch","Embarked")]

Age.predictions<-predict(Age.model,newdata = Age.row)
titanic.full[is.na(titanic.full$Age),"Age"]<-Age.predictions


#categorical

titanic.full$Pclass<-as.factor(titanic.full$Pclass)
titanic.full$Sex<-as.factor(titanic.full$Sex)
titanic.full$Embarked<-as.factor(titanic.full$Embarked)



titanic.train<-titanic.full[titanic.full$isTrainset==TRUE,]
titanic.test<-titanic.full[titanic.full$isTrainset==FALSE,]

titanic.train$Survived<-as.factor(titanic.train$Survived)


Survived.equation<-"Survived~Pclass+Sex+Age+SibSp+Parch+Fare+Embarked"
Survived.formula<-as.formula(Survived.equation)
#install.packages("randomForest")
library(randomForest)
titanic.model<-randomForest(formula=Survived.formula,data=titanic.train,ntree=500,mtry=3,nodesize=0.01*nrow(titanic.train))



feature.equation<-"Pclass+Sex+Age+SibSp+Parch+Fare+Embarked"
Survived<-predict(titanic.model,newdata=titanic.test)


PassengerID<-titanic.test$PassengerId
output<-as.data.frame(PassengerID)
output$Survived<-Survived
write.csv(output,"C:/Users/tejve/Desktop/kaggle2.csv",row.names=FALSE)


