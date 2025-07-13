func matchPlayersAndTrainers(players []int, trainers []int) int {
    sort.Ints(players)
    sort.Ints(trainers)
    
    i, j, count := 0, 0, 0
    
    for i < len(players) && j < len(trainers) {
        if players[i] <= trainers[j] {
            count++
            i++
            j++
        } else {
            j++  // trainer too weak, move to next trainer
        }
    }
    
    return count
}