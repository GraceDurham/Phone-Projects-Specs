import collections 
import operator
import string 


def read_entire_file(file_name):
    with open(file_name) as my_file:
        output=my_file.read()
    return output 
     


def main():

    file_returned_as_string=read_entire_file("LoremIpsum.txt")
    file_returned_as_string=file_returned_as_string.lower().decode("utf-8-sig").encode("utf-8")
    print file_returned_as_string
    file_split_into_array=file_returned_as_string.split(" ")
    print file_split_into_array

    file_set=set (file_split_into_array)
    print len(file_set)
    word_count={}
    for word in file_split_into_array:
        word_no_punc=word.strip(string.punctuation)
        if word_no_punc not in word_count:
            word_count[word_no_punc]=1
        else:
            word_count[word_no_punc]+=1

    write_word_counts(word_count, "wordcountresults.txt",sort_count=False)       
    # return word_count  


def write_word_counts(word_count, file_name,sort_count=False):
    with open(file_name,'w') as my_file:
        sort_key = operator.itemgetter(0)
        if sort_count:
            sort_key = operator.itemgetter(1)
        sorted_word_count = sorted(word_count.items(),key=sort_key) 


        for word, count in sorted_word_count:
            my_file.write(word)
            my_file.write('\t')
            my_file.write(str(count)) 
            my_file.write('\n')  




if __name__ == '__main__':
    main()