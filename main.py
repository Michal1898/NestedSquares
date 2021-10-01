def nested_squares(n):
    for square_index in range(n - 1, -1, -1):
        # print(square_index)
        print(
            (n - square_index - 1) * "# "
            + (4 * square_index + 1) * "#"
            + (n - square_index - 1) * " #"
        )
        if square_index:
            print(
                (n - square_index - 1) * "# "
                + "#"
                + (4 * square_index - 1) * " "
                + "#"
                + (n - square_index - 1) * " #"
            )

    for square_index in range(1, n):
        # print(square_index)

        if square_index:
            print(
                (n - square_index - 1) * "# "
                + "#"
                + (4 * square_index - 1) * " "
                + "#"
                + (n - square_index - 1) * " #"
            )

        print(
            (n - square_index - 1) * "# "
            + (4 * square_index + 1) * "#"
            + (n - square_index - 1) * " #"
        )


if __name__ == "__main__":
    for n in range (1,10):
        print(f"n= {n}:")
        nested_squares(n)
