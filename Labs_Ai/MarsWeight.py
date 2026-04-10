# Constant - Mars weight is 37.8% of Earth weight
MARS_MULTIPLE = 0.378

def main():
    # Step 1: Get input from user (comes as STRING)
    earth_weight_str = input('Enter a weight on earth: ')

    # Step 2: CAST string → float so we can do math
    earth_weight = float(earth_weight_str)

    # Step 3: Calculate Mars weight (float * float = float)
    mars_weight = earth_weight * MARS_MULTIPLE #earth_weight*0.378

    # Step 4: Print result — CAST float → str for concatenation
    print('The equivalent weight on Mars: ' + str(mars_weight))

if __name__ == '__main__':
    main()
