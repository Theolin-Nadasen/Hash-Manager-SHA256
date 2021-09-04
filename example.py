import hashmanager

h = hashmanager.hasher("list.txt")
h.checkfile()

result = h.checkword("cat")
print(result)

result = h.gethashes()
print(result)

result = h.printfile()
print(result)

result = h.findhash("77af778b51abd4a3c51c5ddd97204a9c3ae614ebccb75a606c3b6865aed6744e")
print(result)
