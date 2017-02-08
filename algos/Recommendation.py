'''
Created on Feb 1, 2017

@author: Pragya
comment: based on person similarity scores
'''
from math import sqrt, pow
from numpy import sum

def pearson_similarity(critics, person1, person2):
#     find commonly rated items in critics array
    si = {}
    for item in critics[person1]:
        if item in critics[person2]: si[item] = 1
        
    n = len(si)
#     find sum of each person ratings for common movies in 2 fetch_lfw_people
    sum1 = sum(critics[person1][item] for item in si)
    sum2 = sum(critics[person2][item] for item in si)
    
#     sum of squares
    sum1sq = sum(pow(critics[person1][item], 2) for item in si )
    sum2sq = sum(pow(critics[person2][item], 2) for item in si )
    
#     sum of products of ratings
    pSum = sum(critics[person1][item] * critics[person2][item] for item in si)
    
#     pearson similarity formula
    num = pSum - (sum1 * sum2)/n
    den = sqrt((sum1sq - pow(sum1, 2)/n) * (sum2sq - pow(sum2, 2)/n))
    return num/den

def top_matches(critics, person1, rankCount):
    scores = [(pearson_similarity(critics, person1, other),other) for other in critics if other!=person1]
    scores.sort()
    scores.reverse()
    return scores[0:rankCount]

def getRecommendations(critics, recoForPerson):
    simSum = {}
    totals = {}
    for other in critics:
        if other != recoForPerson:
            similaity = pearson_similarity(critics, recoForPerson, other)
            if similaity <= 0: continue
            for item in critics[other]:
                if item not in critics[recoForPerson]:
                    totals.setdefault(item, 0)
                    simSum.setdefault(item, 0)
                    totals[item] += similaity * critics[other][item]
                    simSum[item] += similaity
    
    rankings = [(total/simSum[item], item) for item,total in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings     