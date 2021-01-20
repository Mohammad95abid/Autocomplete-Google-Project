from termcolor import colored
import pickle
import string


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



def get_end_sentence(cur_node, max_number, letter, sentence = "", suitable_sentences = set() ):
    if letter == '\n' and len( suitable_sentences ) < max_number :
        suitable_sentences.add( ( sentence, cur_node[0] ) )
        return suitable_sentences

    for letter in cur_node:
        temp = sentence
        if letter != '\n':
            temp = sentence + letter
        get_end_sentence( cur_node[letter], max_number, letter, temp, suitable_sentences)

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
            results = get_end_sentence( cur_node[letter], 5 - len(sentence_results), letter, sentence_result )
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



def run_search_engine():
    while True:
        print( colored( "Enter a search sentence:", 'red' ) )
        prefix = input()
        if prefix == "#":
            print( colored( "Thank you for using our search engine, have a nice day!", 'Green' ) )
            break
        prefix = get_alphanumerc( prefix.casefold() )
        autocomplete_sentences = search( prefix )
        for sentence in autocomplete_sentences:
            print( colored( sentence[0], 'blue' ), "    ==>  File Number: " , colored( sentence[1], 'green' ))



if __name__ == "__main__":
    run_search_engine( )