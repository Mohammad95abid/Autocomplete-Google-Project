import string


allowed_chars = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ','\n' ]
for ch in string.ascii_lowercase:
    allowed_chars.append( ch )

class LeaveTreeNode:
    def __init__(self):
        self.data = [ ]

class TreeNode:
    def __init__(self):
        self.childs = { }
    
    def add( self, sentence: str, sentence_id: str  = None):
        for ch in sentence:
            if ch not in allowed_chars:
                return False
        temp = self
        i = 0
        ch = sentence[ i ]
        pref_len = len( sentence )
        while ch in temp.childs.keys() and i < pref_len - 1:
            temp = temp.childs[ ch ]
            i += 1
            ch = sentence[ i ]
        
        while i < pref_len - 1:
            temp.childs[ch] = TreeNode()
            i += 1
            temp = temp.childs[ch]
            ch = sentence[i]

        if i == pref_len - 1 and ch == '\n':
          temp.childs[ch] = LeaveTreeNode()
          temp.childs[ ch ].data.append( sentence_id )

