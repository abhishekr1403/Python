# #
# # # ----------------Problem 1-------------------
# #
# # info={
# #     "china" : 143,
# #     "india" : 136,
# #     "usa" : 32,
# #     "pakistan" : 21,
# # }
# #
# # def printall():
# #     for key, value in info.items():
# #         print(f"{key}==>{value}")
# #
# # def add():
# #     country = input("Enter a Country to be added:").lower()
# #     print(country)
# #     if country in info:
# #         print("This country is already exist")
# #     else:
# #         population = input("Enter a population:")
# #         info[country] = population
# #         printall()
# #
# # def remove():
# #     country = input("Enter a Country to be removed:").lower()
# #     if country in info:
# #         del info[country]
# #         printall()
# #     else:
# #         print("This country is not exist")
# #
# # def query():
# #     country = input("Enter a Country to be queried:").lower()
# #     if country in info:
# #         print(f'Population of {country} ==> {info[country]}')
# #     else:
# #         print("This country is not exist")
# #
# # user_choice = input("Enter your  choice (add, remove, query, print): ")
# # if user_choice == 'add':
# #     add()
# # elif user_choice == 'remove':
# #     remove()
# # elif user_choice == 'query':
# #     query()
# # elif user_choice == 'print':
# #     printall()
# # else:
# #     print("Please enter a valid choice")
# #
# # # -----------Problem 2--------------------
#
# import statistics as st
#
# stocks = {
#     "info" : [600,630,620],
#     "ril"  : [1430,1490,1567],
#     "mtl"  : [234,180,160]
# }
#
# def print_all():
#     for stock,prices_list in stocks.items():
#         avg = st.mean(prices_list)
#         print(f"{stock} ==> {prices_list} ==> avg: {round(avg,2)}")
# def add():
#     stock_ticker = input("Enter stock ticker: ").lower()
#     price = float(input("Enter price: "))
#     if stock_ticker in stocks:
#         stocks[stock_ticker].append(price)
#     else:
#         stocks[stock_ticker] = [price]
#     print_all()
#
# def main():
#     choice = input("Enter choice: ").lower()
#     if choice == "add":
#         add()
#     elif choice == "print":
#         print_all()
#     else:
#         print("Invalid choice")
#
# if __name__ == "__main__":
#     main()

# ---------------Problem 3 ---------------
import math
def circ_calc(r):
    area = math.pi * r ** 2
    circumference = 2 * math.pi * r
    return area,circumference
def main():
    radius = float(input("Enter the radius of the circle: "))
    area, circumference = circ_calc(radius)
    print("The area and circumference of the circle is: ",area,circumference)
if __name__ == "__main__":
    main()