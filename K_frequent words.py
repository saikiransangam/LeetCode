import heapq
def topKFrequent(words):
        
        #words = [for w in words]
        
        
        result = []
        
        heapq.heapify(words)
        
        #while len(words) > 1:
            
        for i in range(len(words)):
                
                if words[i] == words[i + 1]:
                    
                    result.append(i)
                    
                else:
                    i + 1
                    
        return result