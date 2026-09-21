# # def total_expense (exp):
# #     total = 0
# #     for item in exp:
# #         total = total + item
# #     return total
# #
# # tom_exp_list = [2100,3200,4100]
# # joe_exp_list = [200,320,430]
# #
# # tom_total = total_expense(tom_exp_list)
# # joe_total = total_expense(joe_exp_list)
# #
# # print(tom_total)
# # print(joe_total)
#
# def calculate_area(b,h,s='triangle'):
#     if s == 'triangle':
#         area = (1 / 2) * b * h
#         return area
#     elif s == 'rectangle':
#         area = b*h
#         return area
#
# Result = calculate_area(12,6)
# print(Result)

def print_pattern(n):
    for i in range(n):
        s=" "
        for j in range(i+1):
            s = s + "*"
        print(s)


print_pattern(5)


