a = "apple is red"
# Replace
# returns a copy of a string were all occurences of the substring is replaced with another substrig
rep = a.replace("red", "apple")  # string_var.replace(old_string, new_string)
low = a.lower()  # Convert to lower case
upp = a.upper()  # Convert to upper case
case = a.casefold()  # Convert all characters to lower case
swap = a.swapcase()  # Convert all characters to upper case
cap = a.capitalize()  # Capitalize all lower case
stp = a.strip()  # Remove Spaces in left and right
spl = a.split()  # Seprate Words with spaces(default) -- a.split(e) Seprate Words 'e'
con = a.count("e")  # Count


print(rep, low, upp, case, swap, cap, stp, spl, con, sep="\r")
