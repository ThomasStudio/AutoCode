from functools import wraps


def log(fun):
    @wraps(fun)
    def new_fun(*args, **kwargs):
        '''
        @wraps(fun) can help to return real fun name when call fun.__name__
        '''
        funName = fun.__name__

        argList = [str(x) for x in args]
        kwargsList = [f'{x} = {str(kwargs[x])}' for x in kwargs]

        if len(argList) > 0:
            argList = f'{", ".join(argList)}'
        else:
            argList = ""

        if len(kwargsList) > 0:
            kwargsList = f' , {", ".join(kwargsList)}'
        else:
            kwargsList = ""

        print(f'{funName}( {argList}{kwargsList} )')

        return fun(*args, **kwargs)

    return new_fun
