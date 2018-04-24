def fastsqrt(n):
	a = n.bit_length()
	kek = n
	if a < 32:
		s = int(n**0.5)
		r = n - s*s
		return (s, r)
	flag = False
	if(a % 4 != 0):
		if(a % 4 == 1 or a % 4 == 2):
			n <<= 2
			flag = True
			a += 2
		b = a // 4 + 1
	else:
		b = a // 4
	ed = 1 << b
	ed -= 1
	a0 = n & ed
	n >>= b
	a1 = n & ed
	n >>= b
	a2 = n & ed
	n >>= b
	a3 = n & ed
	s0, r0 = fastsqrt((a3 << b) + a2)
	q, u = divmod((r0 << b) + a1, 2*s0)
	s = (s0 << b) + q
	r = (u << b) + a0 - q*q
	if r < 0:
		r = r + 2*s - 1
		s -= 1
	if flag:
		s >>= 1
		r = kek - s*s
	return (s, r)
