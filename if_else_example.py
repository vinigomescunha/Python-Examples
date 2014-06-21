var = raw_input('Enter with command: ')
while var != 'exit':
    if str(var).isalpha() == False:
        print 'Please command only string'
        variavel = raw_input('Entre with command: ')
    else:
        print 'the command is', var
    var = raw_input('Enter with command: ')
