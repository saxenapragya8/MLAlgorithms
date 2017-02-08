'''
Created on Feb 7, 2017

@author: Pragya
'''
from algos.Recommendation import top_matches

def transformToProductData(movies):
    result = {}
    for person in movies:
        for item in movies[person]:
            result.setdefault(item,{})
            result[item][person] = movies[person][item]  
    return result

def calculateItemSimilars(itemData):
    results = {}
    for item in itemData:
        scores = top_matches(itemData, item, 4)
        results[item] = scores
    return results

def getItemRecommendations(critics, itemSimilarItems, person):
    usersRatings = critics[person]
    scores={}
    totalSim={}
    for (item, rating) in  usersRatings.items():
        for (similarity, similarItem) in itemSimilarItems[item]:
            if similarItem in usersRatings: continue
            scores.setdefault(similarItem, 0)
            scores[similarItem] +=similarity * rating
            totalSim.setdefault(similarItem, 0)
            totalSim[similarItem] += similarity
    
    rankings = [(score/totalSim[item], item) for item,score in scores.items()]
    rankings.sort()
    rankings.reverse()
    return rankings