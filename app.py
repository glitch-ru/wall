from PIL import Image, ImageDraw, ImageFont

W, H = 2772, 1280

with open("counter.txt", "r") as f:
    n = int(f.read().strip())

n += 1

img = Image.new("RGB", (W, H), "black")
draw = ImageDraw.Draw(img)

font = ImageFont.truetype("Barsilliago.ttf", 600)
text = str(n)

bbox = draw.textbbox((0, 0), text, font=font)
x = (W - (bbox[2] - bbox[0])) // 2
y = (H - (bbox[3] - bbox[1])) // 2

draw.text((x, y), text, fill="white", font=font)
img.save("wall.png")

with open("counter.txt", "w") as f:
    f.write(str(n))
