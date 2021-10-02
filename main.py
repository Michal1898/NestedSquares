def nested_squares(n):
    # create kernel (:-)
    picture_of_squares = (n-1)*"# " + "#" + (n-1)*" #"+"\n"
    for square_index in range(n-1 , 0, -1):
        square_part1 =  (square_index)*"# "+(4* (n-square_index)-3 )*" "+(square_index)*" #"+"\n"
        square_part2 = (square_index-1) * "# " + (4 * (n-square_index) +1) * "#" + (square_index-1) * " #" + "\n"
        # Wrap kernel with next layers
        picture_of_squares=square_part2+square_part1+picture_of_squares+square_part1+square_part2
    print(picture_of_squares)

if __name__ == "__main__":
    for n in range (1,7):
        print ("n=",n)
        nested_squares(n)
