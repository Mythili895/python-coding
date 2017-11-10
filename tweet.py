from collections import defaultdict

def getRecommendedTweets(followGraph_edges, likeGraph_edges, targetUser, minLikeThreshold):
        a=0
        answer = []
        targetUserFollows = []
        for t in followGraph_edges:
            if t[a] is targetUser:
                targetUserFollows.append(t[1])

        
        recommendedTweets = defaultdict(lambda:a)
        #print recommendedTweets.items()
        
        for like in likeGraph_edges:
                if like[a] in targetUserFollows:
                    recommendedTweets[like[1]] = recommendedTweets[like[1]] + 1
        for tweet in recommendedTweets:
            if recommendedTweets[tweet] >= minLikeThreshold:
                answer.append(tweet)

        return answer        
            
        
        

followGraph_edges = [(4 , 3) , 
                     (1 , 2) ,
                     (1 , 3) ,
                     (1 , 4) ,
                     (5 , 6)]

likeGraph_edges = [(2 , 10),
                   (3 , 10),
                   (4 , 10),
                   (2 , 11),
                   (3 , 12),
                   (4 , 11)]


print getRecommendedTweets(followGraph_edges, likeGraph_edges,1,3)   
