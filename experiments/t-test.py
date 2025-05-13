from scipy import stats
import numpy as np

loanword_perplexity = [97.44, 142.11, 133.79, 186.01, 281.69, 151.45, 189.47, 154.83, 161.99, 169.19]
native_perplexity = [102.91, 143.14, 136.44, 187.52, 285.73, 153.78, 197.30, 160.09, 171.11, 168.78]

# Perform paired t-test
t_statistic, p_value = stats.ttest_rel(loanword_perplexity, native_perplexity)

print(f"t-statistic: {t_statistic}")
print(f"p-value: {p_value}")