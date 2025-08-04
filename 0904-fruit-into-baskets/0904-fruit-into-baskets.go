func totalFruit(fruits []int) int {
    fruitCount := make(map[int]int)
    left, maxFruits := 0, 0

    for right := 0; right < len(fruits); right++ {
        fruitCount[fruits[right]]++

        for len(fruitCount) > 2 {
            fruitCount[fruits[left]]--
            if fruitCount[fruits[left]] == 0 {
                delete(fruitCount, fruits[left])
            }
            left++
        }

        if maxFruits < right-left+1 {
            maxFruits = right - left + 1
        }
    }

    return maxFruits
}