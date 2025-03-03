import colorgram

colors = colorgram.extract('image.jpg', 35)
pallet = []

for _ in range(35):
    pallet.append((colors[_].rgb.r, colors[_].rgb.b, colors[_].rgb.b))

print(pallet)