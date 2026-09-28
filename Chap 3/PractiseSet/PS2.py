## Write a program to fill in a letter template given below with name and date.
## letter = '''
##        Dear <|Name|>,
##        You are Selected!
##        <|Date|>
##         '''

letter = ''' Dear <|Name|>
        You are Selected!
        <|Date|> '''
print(letter.replace("<|Name|>", "Prabhu").replace("<|Date|>", "10-08-2025"))