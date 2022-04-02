#Importing KMeans from sklearn

from sklearn.cluster import KMeans

# Now we calculate the Within Cluster Sum of Squared Errors (WSS) for different values of k. 
# Next, we choose the k for which WSS first starts to diminish.

wcss=[]

for i in range(1,11):
    km=KMeans(n_clusters=i)
    km.fit(X)
    wcss.append(km.inertia_)

#The elbow curve

plt.figure(figsize=(12,6))

plt.plot(range(1,11),wcss)

plt.plot(range(1,11),wcss, linewidth=2, color="red", marker ="8")

plt.xlabel("K Value")
plt.xticks(np.arange(1,11,1))
plt.ylabel("WCSS")

plt.show()

#this is known as the elbow graph , the x axis being the number of clusters
#the number of clusters is taken at the elbow joint point
#this point is the point where making clusters is most relevant
#the numbers of clusters is kept at maximum


#Taking 4 clusters

km1=KMeans(n_clusters=4, random_state=44)

#Fitting the input data

km1.fit(X)


#predicting the labels of the input data

y=km1.predict(X)


#adding the labels to a column named label

data_join["label"] = y

#The new dataframe with the clustering done

data_join = data_join.reset_index(drop=True)

data_join['label'] = data_join['label'].replace([0,1,2,3],['medium crime','high crime','highest crime','lowest crime'])


print(data_join)
