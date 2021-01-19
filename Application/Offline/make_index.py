
from Application.Offline import io_manager as iom


main_index = { }


def get_sentence_prefixes( sentence: str ):
    for i in range( len(sentence) ):
        yield iom.get_alphanumerc( sentence[ : i + 1 ].casefold( ) ).strip()


def prepare_main_index( file_path: str ):
    if not file_path.endswith( ".txt" ):
        return
    # for sentence in iom.read_file_by_generator( file_path ):
    for sentence in iom.read_file_by_generator( file_path ):
        sentence = sentence.rstrip( "\n" ).strip( )
        sentence = iom.remove_multiple_spaces_in_sentence( sentence )
        for prefix in get_sentence_prefixes( sentence ):
            prefix = iom.remove_multiple_spaces_in_sentence( prefix )
            if prefix not in main_index.keys():
                main_index[ prefix ] = [ ]
            main_index[ prefix ].append( sentence )
            # if file_path not in main_index[ prefix ].keys():
            #     main_index[ prefix ][ file_path ] = [ ]
            # if line_num not in main_index[ prefix ][ file_path ]:
            #     main_index[ prefix ][ file_path ].append( line_num )


# def prepare_main_index( file_path: str ):
#     if not file_path.endswith( ".txt" ):
#         return
#     # for sentence in iom.read_file_by_generator( file_path ):
#     for sentence in iom.read_file_by_generator( file_path ):
#         src_sentence = sentence
#         sentence = sentence.rstrip( "\n" ).strip( )
#         sentence = iom.get_alphanumerc( sentence.casefold( ) ).strip()
#         if sentence not in main_index.keys():
#             main_index[ sentence ] = [ ]
#         if file_path not in main_index[ sentence ]:
#             main_index[ sentence ].append( src_sentence )


def convert_lists_to_lists_in_main_index( ):
    for key, set_ in main_index.items():
        main_index[ key ] = list( set_ )


if __name__ == "__main__":
    pass
    
