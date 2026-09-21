# # # f =  open("E://Python//Sample//Funny.txt",'a')
# # # f.write("\nHello World")
# # # f.close()
# #
# # f =  open("E://Python//Sample//Funny.txt",'r')
# # f_out = open("E://Python/Sample//Funny_wc.txt","w")
# # for line in f:
# #     tokens = line.split(' ')
# #     f_out.write("Wordcount: "+str(len(tokens))+ '\t' + line)
# #     print(len(tokens))
# #
# # f.close()
# # f_out.close()
# word_count = {}
# with open("E://Python//Sample//poem.txt",'r') as f:
#     for line in f:
#         words = line.split(" ")
#         # print(len(words))
#         for word in words:
#             if word in word_count:
#                 word_count[word] += 1
#             else:
#                 word_count[word] = 1
# # print(word_count)
#
# word_occur = list(word_count.values())
# max_count = max(word_occur)
# print("Words with maximum occurence are:\n")
# for word,count in word_count.items():
#     if count == max_count:
#         print(f"'{word}' with {count} counts.")

# ------------------Problem 2---------------

with open('E://Python//Sample//stocks.csv','r') as f, open("E://Python//Sample//output.csv",'w') as out:
    out.write("Company Name,PE Ratio, PB Ratio\n")
    next(f)  # This will skip first line in the file which is a header
    # print(f.read())
    for line in f:
        tokens = line.split(',')
        # print(tokens)
        stocks = tokens[0]
        price = float(tokens[1])
        eps = float(tokens[2])
        bv = float(tokens[3])
        pe = round(price/eps,2)
        pbr = round(price/bv,2)
        out.write(f'{stocks},{pe},{pbr}\n')
