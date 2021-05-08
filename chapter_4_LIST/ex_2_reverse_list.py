def reverse_list(l):
    reversed_list = []
    for i in range(len(l)):
       popped_item = l.pop()
       reversed_list.append(popped_item)
    return reversed_list

List = list(input("Enter contents of strings(with ',' in between): ").split(","))

print(reverse_list(List))

    
