'''
Created on Feb 1, 2017

@author: Pragya
'''

from algos import Recommendation
from algos.Recommendation import pearson_similarity, top_matches, getRecommendations
from algos.ItemBasedRecommendation import transformToProductData,\
    calculateItemSimilars, getItemRecommendations

critics = {
    'Rose':{'Lady in the water': 2.5, 'Snakes on a plane': 3.5, 'Just my luck': 3.0, 'Superman Returns': 3.5, 'You me and dupree': 2.5, 'The night listener':3.0},
    'Gene':{'Lady in the water': 3.0, 'Snakes on a plane': 3.5, 'Just my luck': 1.5, 'Superman Returns': 5, 'You me and dupree': 3, 'The night listener':3.5},
    'Michael':{'Lady in the water': 2.5, 'Snakes on a plane': 3, 'Superman Returns': 3.5, 'The night listener':4},
    'Claudia':{'Snakes on a plane': 3.5, 'Just my luck': 3, 'Superman Returns': 4, 'You me and dupree': 2.5, 'The night listener':4.5},
    'Mick':{'Lady in the water': 3.0, 'Snakes on a plane': 4, 'Just my luck': 2, 'Superman Returns': 3, 'You me and dupree': 2, 'The night listener': 3},
    'Jack':{'Lady in the water': 3.0, 'Superman Returns': 5, 'You me and dupree': 3.5},
    'Toby':{'Snakes on a plane': 4.5, 'Superman Returns': 4, 'You me and dupree': 1}
    }

# print(pearson_similarity(critics, 'Rose', 'Toby'))
# print(pearson_similarity(critics, 'Gene', 'Toby'))
print("top matches for Rose")
print(top_matches(critics, 'Rose', 5))
print("get recommendations for Toby")
print(getRecommendations(critics, "Toby"))

print("transform to a item based list")
result = transformToProductData(critics)
print(result)

print("calculate item similarities")
itemSimilars = calculateItemSimilars(result)
print(itemSimilars)

print("get item recommendations")
print(getItemRecommendations(critics, itemSimilars, "Toby"))