{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':'TNS Switcher',
          'size':(292, 261),
          'icon':'icon-oracle.ico',
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit',
                   'command':'exit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'StaticText', 
    'name':'txtStatus', 
    'position':(4, 0), 
    'size':(168, -1), 
    'foregroundColor':(0, 0, 198, 255), 
    'text':u'Current environment is rocky', 
    },

{'type':'RadioGroup', 
    'name':'radEnv', 
    'position':(68, 40), 
    'size':(142, 87), 
    'items':['rocky', 'xps'], 
    'label':u'TNS Environment', 
    'layout':'vertical', 
    'max':1, 
    'stringSelection':u'rocky', 
    },

{'type':'Button', 
    'name':'btnExit', 
    'position':(94, 152), 
    'command':'exit', 
    'label':u'OK', 
    },

] # end components
} # end background
] # end backgrounds
} }
