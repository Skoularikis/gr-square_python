import sys


if len(sys.argv) == 2:
    input_file = sys.argv[1]
    array = []
    with open(input_file) as graph_input:
        for size, line in enumerate(graph_input):

            array.append(line.split())

    print(array)


    print(array[0][5:])
    print([ x for x in range(len(array))])
    o = [ [x[0]] for x in array]
    print(o)

    def findTraversals(array,counter, k):

        # if k == 0:
        #     return findTraversals(array, counter, k + 1)
        if k == len(array):
            print('this is the k in the', k, 'iteration')
            return o
        else:


            # o.append()
            # for i in range(len(array[counter])):
            if array[counter][k] not in o[counter] and array[k][counter] not in o[counter]:
              print(array[counter][k], k)
              o[counter].append(array[counter][k])
        return findTraversals(array,counter, k + 1)

    a = []
    for i in range(len(array[0])):
      a.append(findTraversals(array,i, k = 0))
    print(a)



else:
    # print (sys.argv[0])
    print("Please enter arguments to make the algorithm work properly")
    print ("Try again")

    # # Python function to print permutations of a given list
    # def permutation(lst):
    #     # print(lst)
    #     print('this is the starting list')
    #     print(lst)
    #     # If lst is empty then there are no permutations
    #     if len(lst) == 0:
    #         return []
    #
    #     # If there is only one element in lst then, only
    #     # one permuatation is possible
    #     if len(lst) == 1:
    #         return [lst]
    #
    #     # Find the permutations for lst if there are
    #     # more than 1 characters
    #
    #     l = []  # empty list that will store current permutation
    #
    #     # Iterate the input(lst) and calculate the permutation
    #     for i in range(len(lst)):
    #         m = lst[i]
    #
    #         # Extract lst[i] or m from the list.  remLst is
    #         # remaining list
    #         remLst = lst[:i] + lst[i + 1:]
    #         print('this is the list')
    #         print(remLst, m)
    #         # Generating all permutations where m is first
    #         # element
    #         for p in permutation(remLst):
    #             l.append([m] + p)
    #             print('this is each item ?')
    #             print(l)
    #     return l
    #
    #
    # for p in permutation([ x for x in range(len(array)-1)]):
    #     print(p)