from random import randrange

class TableConversion:
    alfabet = "qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLzZxXcCvVbBnNmM"
    def create_key()->str:
        
        code = []

        for i in range(len(TableConversion.alfabet)):
            while True: 
                index = randrange(0,len(TableConversion.alfabet))
                if index == i or TableConversion.alfabet[index] in code:
                    continue
                else:
                    break
            code.append(TableConversion.alfabet[index])
        
        return ''.join(code)