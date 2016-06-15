li = ["Simba", "Nala", "Nala", "Skaza", "Kovu", "Kiara", "Zira"]
print [elem for elem in li if len(elem) > 4]
print [elem for elem in li if elem != "Simba"]
print [elem for elem in li if li.count(elem) == 1]
