func makeFancyString(s string) string {
    var result []byte

    for i := 0; i < len(s); i++ {
        n := len(result)
        if n >= 2 && result[n-1] == result[n-2] && result[n-1] == s[i] {
            continue
        }
        result = append(result, s[i])
    }

    return string(result)
}
