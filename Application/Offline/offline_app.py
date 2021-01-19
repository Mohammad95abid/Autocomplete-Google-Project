import make_index as mindx
from io_manager import *
import time
import tree_index


#  Offline part
SLASH = "\\"
file_path = "Offline" + SLASH + "files_directories.json"


def store_subdirectories_in_json():
   all_files = list( get_all_files_in_dir( ) )
   mindx.iom.make_json_file( "Offline" + SLASH, "files_directories.json", { "Pathes": all_files, "Length": len( all_files ) } )


def load_subdirectories_from_json():
   if os.path.isfile( file_path ):
        with open( file_path, 'r' ) as fp:
            data = json.load( fp )
            return data["Pathes"]


def make_files_ids():
   files_ids = { }
   for i, file_path in enumerate( all_files ):
      files_ids[ i ] = file_path
   return files_ids

all_files = load_subdirectories_from_json( )
files_ids = make_files_ids()


def make_main_index( start: int, end: int ):
   for i, file_path in enumerate( all_files[ start: end ], start ):
      print( "Iteration: ", i )
      if file_path.endswith( SLASH ):
         file_path = file_path[ : -1 ]
      mindx.prepare_main_index( file_path )
   keys_length = len( mindx.main_index.keys( ) )
   for i, key in enumerate( mindx.main_index.keys( ) ):
      print( " key {} from {} keys".format( i, keys_length ) )
      if len( key ) > 0 and key[ 0 ] != '"':
         make_json_file( "indexes" , "{}.json".format( key[ 0 ] if key[ 0 ] != 'i' else ( key[ 0 ] + "0") ), { key: mindx.main_index[ key ] } )
    
