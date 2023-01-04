pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-])(?=.{8,})"
# ?=
# The ?= is the syntax for a positive lookahead assertion, 
# which means that it looks ahead in the string to check if #the
# pattern following it is present, but it does not actually #consume
#  any characters in the string

# .*[a-z]
# The .* preceding the character class [a-z] matches any #number of characters,
#  including zero, and the character class [a-z] matches any #lowercase letter.


# (?=.*[a-z])
# So, the overall expression will match a position in the #string that is immediately followed by a string containing at least one 
# lowercase letter.
