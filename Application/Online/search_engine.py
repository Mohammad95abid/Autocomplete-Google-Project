from Application.Offline import make_index as mindx


ascii_lower_letters = mindx.iom.string.ascii_lowercase

#  Online Part
def search( prefix: str ):
   if len( prefix ) <= 0:
      return None
   first_ch = prefix[ 0 ]
   index_name = "i0" if first_ch == 'i' else first_ch
   index_path = "Application\\indexes\\{}.json".format( index_name )
   index_data = mindx.iom.load_json_file( index_path )
   if index_data is None or prefix not in index_data:
      return []
   sentences = list(index_data[ prefix ])
   return sentences[ : 5 ] 


def replace_a_letter( prefix: str ):
   result = set( )
   count = 5
   for prefix_letter in prefix:
      for letter in ascii_lower_letters:
         if count <= 0:
            return result
         new_prefix = prefix.replace( prefix_letter, letter, 1 )
         current_search_results = search( new_prefix )
         result.update( current_search_results )
         count -= len( result )
   return result


def add_a_letter( prefix:str ):
   result = set( )
   count = 5
   for i in range(len(prefix )):
      for letter in ascii_lower_letters:
         if count <= 0:
            return result
         new_prefix = prefix[ :i ] + letter + prefix[ i: ]
         current_search_results = search( new_prefix )
         result.update( current_search_results )
         count -= len( result )
   return result


def remove_a_letter( prefix: str ):
   result = set( )
   count = 5
   for i in range(len(prefix )):
      if count <= 0:
            return result
      new_prefix = prefix[ :i ] + prefix[ i + 1: ]
      current_search_results = search( new_prefix )
      result.update( current_search_results )
      count -= len( result )
   return result


def spelling_correction( prefix: str ):
   result = set()
   
   # get autocompletion sentences after replacing a letter
   results_after_replacing_a_letter = replace_a_letter( prefix )
   results_len = len( results_after_replacing_a_letter )
   if results_len >= 5:
      return list(results_after_replacing_a_letter)[ :5 ]
   result.update( results_after_replacing_a_letter )

   # get autocompletion sentences after adding a letter
   results_after_adding_a_letter = add_a_letter( prefix )
   temp = len( results_after_adding_a_letter )
   if (temp + results_len) >= 5:
      return list(results_after_replacing_a_letter.update( results_after_adding_a_letter[ :( 5 - results_len ) ] ))
   result.update( results_after_adding_a_letter )
   results_len += temp

   # get autocompletion sentences after removing a letter
   results_after_removing_a_letter = remove_a_letter( prefix )
   result.update(results_after_removing_a_letter)

   # return top 5 sentences
   return list(result)[:5]



def get_best_k_completions( prefix: str ):
   result = search( prefix )
   if len(result) >= 5:
      return result[:5]
   spelling_correction_results = spelling_correction( prefix )
   result = result + spelling_correction_results
   result = list( set(result) )
   return result[:5]
