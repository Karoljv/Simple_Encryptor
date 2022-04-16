from table_conversion import TableConversion
from wikipedia import summary

class Coder:

    def __init__(self,alfabet = TableConversion.alfabet,table_conversion=TableConversion.create_key()) -> None:
        
        self.alfabet = alfabet
        self.table_conversion = table_conversion
    
    def coder(self) -> None:
        converted_data = ''
        with open("text.txt","w",encoding='utf-8') as f1:
            f1.write(summary("Python (programming language)"))

        with open("text.txt","r",encoding='utf-8') as f1:
            text = f1.read()
            for i in range(len(text)):
                if text[i] in set(self.table_conversion): 
                    converted_data += self.table_conversion[self.alfabet.index(text[i])] 
                else: 
                    converted_data += text[i]

        with open("coded.txt","w",encoding="utf-8") as f2:
            f2.write(converted_data)


    def decoding(self):
        decoded_data = ''
        with open("coded.txt","r",encoding="utf-8") as f:
            text = f.read()
            for i in range(len(text)):
                if text[i] in set(self.table_conversion):
                    decoded_data += self.alfabet[self.table_conversion.index(text[i])]
                else:
                    decoded_data += text[i]


        with open("decoded.txt","w",encoding="utf-8") as f1:
            f1.write(decoded_data)
                


koder = Coder()
koder.coder()
koder.decoding()


            

    
