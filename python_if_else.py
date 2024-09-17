if __name__ == "__main__":
    n = int(input().strip())

    if n % 2 != 0: print("Curious!")
    elif n % 2 == 0 and 2 <= n <= 5: print("Not Curious.")
    elif n % 2 == 0 and 6 <= n <= 20: print("Curious!")
    else: print("Not Curious!")