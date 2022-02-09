states = ["Washington", "Oregon", "California"]
""""
for state in states:
    state = state.lower()
    print(state)

print("Washington" in states)
print("Tennessee" in states)
print("washington" not in states)
"""
states2 = ["Idaho", "Alaska", "Florida"]
best_states = states + states2
print(best_states[1:3])
print(best_states[:2])
print(best_states[4:])
print(best_states)
