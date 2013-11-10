k = 26.to_f
m = 26.to_f
n = 30.to_f

total = k + m + n
second_total = total - 1

p_homozygous_dom = (k / total) * ((k-1.0)/second_total + m/second_total + n/second_total)
p_hetero_dom = (m / total) * (k / second_total + 0.75 * (m-1.0) / second_total + 0.5 * n / second_total)
p_homozygous_rec = (n / total) * (k / second_total + 0.5 * m / second_total)

prob = p_homozygous_dom + p_hetero_dom + p_homozygous_rec
puts prob
