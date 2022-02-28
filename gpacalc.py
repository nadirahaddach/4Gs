num = int(input('How many classes: '))
total_sum = 0
for n in range(num):
    numbers = float(input('Enter grade % : '))
    total_sum = numbers
avg = total_sum/num
print('Average of ', num, ' classes :', avg)

if __name__ == "__main__":
    app.run(debug=True)    