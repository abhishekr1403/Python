import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--physics" , type=int, help="physics marks")
    parser.add_argument("--chemistry", type=int, help="chemistry marks")
    parser.add_argument("--maths", type=int, help="maths marks")

    args = parser.parse_args()

    print(args.physics)
    print(args.chemistry)
    print(args.maths)

    print("Result:", (
        args.physics + args.chemistry + args.maths
    ) / 3)