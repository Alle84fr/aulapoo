prod = dict()

prod["cavalo"]=12000.54
prod.update({"egua": 20410.00, "burro": 8040.54, "potro":10500.56, "mula":7450.65})

print(prod)

for i in prod.values():
          print(i)
for i in prod.keys():
          print(i)
for anim, val in prod.items():
          if val > 10600:
                    print(f"animal {anim} vale {val}")
  