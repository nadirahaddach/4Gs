import base64
import random


img_list = ["/static/assets/map/dnfield.png",
            "/static/assets/map/dngym.png",
            "/static/assets/map/dnoffice.png",
            "/static/assets/map/dnpool.png",
            "/static/assets/map/dnquad.png"]
img_choice = random.choice(img_list)
''''with open(img_choice, "rb") as img_file:
    my_string = base64.b64encode(img_file.read())'''''
print(img_choice)


if __name__ == "__main__":
    app.run(debug=True)
