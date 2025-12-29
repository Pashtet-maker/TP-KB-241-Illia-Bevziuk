party={
    "date":"01.01.2026",
    "name":"Apocalypse",
    "dress_code":"costumes"
}

print(party)

party.update({"Where":"NewVegasFallout"})
print(party)

del party["date"]
print (party)

party.clear()
print(party)

party={
    "date":"01.01.2026",
    "name":"Apocalypse",
    "dress_code":"costumes"
}

print(party.keys())

print(party.values())

print(party.items()
      )
