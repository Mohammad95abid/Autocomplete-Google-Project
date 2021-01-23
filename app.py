from termcolor import colored
import pickle
import string
import json
import os
import re
import time
def load_files_pathes( file_path: str ):
  if os.path.isfile( file_path ):
        with open( file_path, 'r', encoding = "utf-8" ) as fp:
            return json.load( fp )["Pathes"]
  return []
def convert_id_to_filePath():
    file_paths = load_files_pathes("files_directories.json")
    ids_to_paths = {}
    for i,file_path in enumerate(file_paths):
        ids_to_paths[str(i)] = file_path

    with open('id_file_path.json', 'w') as fp:
        json.dump(ids_to_paths, fp, indent = 2)


def get_alphanumerc( sentence: str ):
    result = ""
    for ch in sentence:
        if ch in string.ascii_lowercase or ch in string.ascii_uppercase or ch in string.digits or ch == ' ':
            result += ch
    return result


def unpickle_tree(file_path: str) -> dict:
  infile = open(file_path,'rb')
  tree = pickle.load(infile)
  infile.close()
  return tree



def get_end_sentence(cur_node, max_number, letter, suitable_sentences, sentence ):
    if len(suitable_sentences) >= max_number:
        return suitable_sentences

    if letter == '\n' and len( suitable_sentences ) < max_number :
        suitable_sentences.add( ( sentence, cur_node[0] ) )
        return suitable_sentences

    for letter in cur_node:
        temp = sentence
        if letter != '\n':
            temp = sentence + letter
        get_end_sentence( cur_node[letter], max_number, letter, suitable_sentences, temp)

        if( len( suitable_sentences ) >= max_number):
            break

    return suitable_sentences


def search_complete_sentence( tree_index: dict, prefix: str ):
    if tree_index is None:
        return [ ]
    cur_node = tree_index
    sentence_results = set()
    sentence_result = ""
    for ch in prefix:
        if ch in cur_node:
            sentence_result += ch
            cur_node = cur_node[ ch ]
        else:
            return []

    if '\n' in cur_node:
        file_id = cur_node['\n'][0]
        sentence_results.add( ( sentence_result, file_id ) )

    if ('\n' in cur_node and len(cur_node) > 1) or ('\n' not in cur_node):
        for letter in cur_node:
            if letter == '\n':
                continue
            results = get_end_sentence( cur_node[letter], 5 - len(sentence_results), letter, set(),sentence_result + letter )
            for res in results:
                sentence_results.add( res )
            if len( sentence_results ) >= 5:
                break

    return (list(sentence_results))[:5]


def search( prefix: str ):
    if prefix is None:
        return [ ]
    
    first_char = prefix[0]
    if first_char == 'i':
        first_char = "i0"
    index_path = "pkl_files/{}.pkl".format( first_char )
    root = unpickle_tree( index_path )
    return search_complete_sentence( root, prefix )
def get_alphanumeric( line: str ):
  result = ""
  allowed_chars = list(string.ascii_lowercase) + list(string.ascii_uppercase)
  allowed_chars += [str(d) for d in range(10)] + [' ']
  for ch in line:
    if ch in allowed_chars:
      result += ch
  result = re.sub(' +', ' ', result)
  return result.casefold( )
def test():
    with open("pandas.txt",'r', encoding="utf-8") as fp:
        lines = fp.readlines()
        for line in lines:
            #line = get_alphanumeric(line)
            print(line)
            if line == "of":
                print(line)
def get_converter():
    with open("id_file_path.json",'r', encoding="utf-8") as fp:
        return json.load(fp)

def run_search_engine():
    id_path = get_converter()
    while True:
        print( colored( "Enter a search sentence:", 'red' ) )
        prefix = input()
        start_time = time.time()
        if prefix == "#":
            print( colored( "Thank you for using our search engine, have a nice day!", 'Green' ) )
            break
        prefix = get_alphanumerc( prefix.casefold() )
        autocomplete_sentences = search( prefix )
        for sentence in autocomplete_sentences:
            print( colored( sentence[0], 'blue' ), "    ==>  File name: " , colored( id_path[sentence[1]], 'green' ))

        end_time = time.time()
        print(colored("the search takes {} secondes.".format(round(end_time - start_time,2)),'yellow'))



if __name__ == "__main__":
    #convert_id_to_filePath()
    #run_search_engine( )
    test()