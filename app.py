from Application.Online import search_engine
from Application.Offline import io_manager
from termcolor import colored



def run():
    while True:
        print( colored( "Enter a search sentence:", 'red' ) )
        prefix = input()
        if prefix == "#":
            print( colored( "Thank you for using our search engine, have a nice day!", 'Green' ) )
            break
        prefix = io_manager.get_alphanumerc( prefix.casefold() )
        autocomplete_sentences = search_engine.get_best_k_completions( prefix )
        for sentence in autocomplete_sentences:
            print( colored( sentence, 'blue' ) )



if __name__ == "__main__":
    run( )