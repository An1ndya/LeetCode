# @param {Integer[]} values
# @return {Integer}
def max_score_sightseeing_pair(values)
    n=values.length()
    maxi=0
    prevmax=values[0]
    mx=0
    for i in 1..n-1
        if values[i] + values[maxi] + maxi - i > mx
            mx = values[i] + values[maxi] + maxi - i 
        end
        if values[i]> prevmax -i+maxi
            prevmax = values[i]
            maxi=i
        end
    end       
    return mx
end