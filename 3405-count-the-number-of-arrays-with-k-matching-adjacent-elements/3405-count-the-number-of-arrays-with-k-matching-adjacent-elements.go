const MOD = 1e9 + 7
const MAX = 200005  // Adjust based on problem constraints for n

var fact [MAX]int64
var invFact [MAX]int64

func countGoodArrays(n int, m int, k int) int {
   	precompute()
	m64 := int64(m)
	part1 := m64 % MOD
	part2 := nCr(n-1, k)
	part3 := power(m64-1, int64(n-1-k))
	result := part1 * part2 % MOD * part3 % MOD
	return int(result)
}
// Fast exponentiation (a^b % MOD)
func power(a, b int64) int64 {
	result := int64(1)
	a = a % MOD
	for b > 0 {
		if b%2 == 1 {
			result = result * a % MOD
		}
		a = a * a % MOD
		b /= 2
	}
	return result
}

// Precompute factorials and inverse factorials
func precompute() {
	fact[0] = 1
	for i := 1; i < MAX; i++ {
		fact[i] = fact[i-1] * int64(i) % MOD
	}
	invFact[MAX-1] = power(fact[MAX-1], MOD-2)
	for i := MAX - 2; i >= 0; i-- {
		invFact[i] = invFact[i+1] * int64(i+1) % MOD
	}
}

// nCr modulo MOD
func nCr(n, r int) int64 {
	if r < 0 || r > n {
		return 0
	}
	return fact[n] * invFact[r] % MOD * invFact[n-r] % MOD
}