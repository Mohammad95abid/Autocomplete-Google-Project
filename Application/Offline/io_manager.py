
import json
import string
import re
import os

SLASH = "\\"

# A function to read the hole given file and return it as string.
def load_text_file( file_path: str ):
    return open( file_path, "r" ).read( )


# A generator to read the given file line by line.
def read_file_by_generator( file_path: str ):
    file_data = open( file_path , "r", encoding = "utf8" )
    while True:
        line = file_data.readline()
        if not line:
            break
        yield line


def load_json_file( file_path ):
    if os.path.isfile( file_path ):
        with open( file_path, 'r', encoding = "utf-8" ) as fp:
            return json.load( fp )


def make_json_file( root_directory, file_name, data: dict ):
    file_path = "D:\\Google-Project\\Autocomplete-Google-Project\\Application\\indexes\\" +  file_name
    prev_data = load_json_file( file_path )
    data.update( prev_data )
    with open( file_path , 'w', encoding = "utf-8" ) as fp:
        json.dump( data, fp, indent = 4 )
    

def get_alphanumerc( sentence: str ):
    result = ""
    for ch in sentence:
        if ch in string.ascii_lowercase or ch in string.ascii_uppercase or ch in string.digits or ch == ' ':
            result += ch
    return result


def remove_multiple_spaces_in_sentence( text ):
    return re.sub(' +', ' ', text )


def load_all_sub_directories_in_directory( root ):
    return [ os.path.join( root, dI ) for dI in os.listdir( root ) if os.path.isdir( os.path.join( root, dI ) ) ]


def get_all_subdirectores_in_resources( root = "resources", result = [ "resources" + SLASH ] ):
    temp = load_all_sub_directories_in_directory( root )
    for dir_ in temp:
        if not dir_.endswith( SLASH ):
                dir_ += SLASH
        result.append( dir_ )
        get_all_subdirectores_in_resources( dir_, result )
    return result

def get_all_files_in_dir( ):
    result = set( )
    pathes = get_all_subdirectores_in_resources( )
    for path in pathes:
        files_pathes = os.listdir( path + SLASH )
        for file_path in files_pathes:
            if not file_path.endswith( SLASH ):
                file_path += SLASH
            result.add(  path + file_path )
    return result


def read_directory_files( directory_name: str ):
    all_directories = get_all_subdirectores_in_resources( )
    for dir in all_directories:
        yield load_text_file( dir )