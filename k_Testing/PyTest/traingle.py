"""
we want to draw
take a character

@
@@
@@@
@@@@ and so on
"""

def main():
    line = int(input("Enter how many lines you wanna print: "))
    element = input("Enter a single character u wanna use for prinitng triangle: ")
    print("\nTriangle Printing\n")
    for row in tri(line):
        print(row)

# # wrong version
# def tri(n):
#     for i in range(n):
#         yield '@' * i

# correct version
def tri(n):
    for i in range(1, n+1):
        yield '@' * i



def draw_traingle(line, element):
    for i in range(line):
        for _ in range(i+1):
            print(element, end = "")
        print()


    
if __name__ == "__main__":
    main()