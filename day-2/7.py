#find index value of item in array
def find_needle(haystack):
    index=haystack.index("needle")
    return f"fount the needle position at {index}"
print(find_needle(["hay", "junk", "hay", "hay", "moreJunk","junk", "needle", "randomJunk"]))