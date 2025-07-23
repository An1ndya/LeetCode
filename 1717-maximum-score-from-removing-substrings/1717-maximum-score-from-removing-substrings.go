func maximumGain(s string, x int, y int) int {
    // Decide which substring to remove first
    // If x >= y, remove "ab" first (x points), else remove "ba" first
    first, firstScore := "ab", x
    second, secondScore := "ba", y
    if y > x {
        first, firstScore, second, secondScore = "ba", y, "ab", x
    }

    // stack simulation using a slice of runes
    var stack []rune
    score := 0

    // First pass: remove all `first` substrings greedily
    for _, c := range s {
        if len(stack) > 0 &&
           string(stack[len(stack)-1]) + string(c) == first {
            stack = stack[:len(stack)-1]
            score += firstScore
        } else {
            stack = append(stack, c)
        }
    }

    // Prepare for second pass: reuse stack to collect remainders
    rem := stack
    stack = stack[:0]

    // Second pass: remove all `second` substrings greedily
    for _, c := range rem {
        if len(stack) > 0 &&
           string(stack[len(stack)-1]) + string(c) == second {
            stack = stack[:len(stack)-1]
            score += secondScore
        } else {
            stack = append(stack, c)
        }
    }

    return score
}
