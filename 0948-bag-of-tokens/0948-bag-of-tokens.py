class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        #sorted; so faceup from less and facedown from most value most profitable
        tokens.sort()
        # faceup index from least value
        faceup = 0
        # facedown index from largest value
        facedown = n-1
        #intial score 
        score = 0
        maxscore = 0
        #faceup should not be more than facedown
        #note faceup = facedown accepted
        #cause facedown index is not get actioned yet so it can be used as faceup
        while faceup <= facedown: 
            #print(power,faceup, facedown)
            #take face up first so we get maximum
            if power >= tokens[faceup]:
                score+=1
                power -= tokens[faceup]
                faceup+=1
                maxscore = max(score, maxscore)
            #As power less to do face up do a facedown
            # so it might lead to future greater score
            elif score >= 1:
                score -= 1
                power += tokens[facedown]
                facedown -= 1
            else:
                #if no case possible there is no way to proceed 
                break
        return maxscore