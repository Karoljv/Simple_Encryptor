from random import randrange
from json import dump
class TableConversion:
    alfabet = "qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLzZxXcCvVbBnNmM"
    def create_key()->str:  
        code = []
        dic = {}
        for i in range(len(TableConversion.alfabet)):
            while True: 
                index = randrange(0,len(TableConversion.alfabet))
                if TableConversion.alfabet[index] in code:
                    continue
                else:
                    break
            
            dic[TableConversion.alfabet[i]] = TableConversion.alfabet[index]
            code.append(TableConversion.alfabet[index])
        
        with open("conversion_table.json","w") as json_file:
            dump(dic,json_file,indent=4)

        return ''.join(code)
