from Offline.offline_app import *



def run( ):
   start_time = time.time( )
   start_range = 0
   end_range = 2
   make_main_index( start_range, end_range )
   mindx.convert_lists_to_lists_in_main_index()
   end_time = time.time( )
   val = ( end_time - start_time ) / 60 
   key = "{} - {}".format( start_range, end_range)

   mindx.iom.make_json_file( "indexes" + SLASH, "time_execution.json", { key: str( round( val, 4 ) ) + " minutes." } )



if __name__ == "__main__":
   run( )


   
