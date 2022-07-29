import re

m = input("Input: ").strip()
new_m = re.sub("[aeiouAEIOU]", "", m)
print(f"Output: {new_m}")