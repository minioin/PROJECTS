import re


class WordMath():
    """A silly OO class to parse and compute simple integer mathematical expressions
    written as words. Note it does NOT use standard order of precedence rules, but
    simply proceeds from left to right.
    >>> WordMath('eighty one').compute()
    81
    >>> WordMath('nine multiplied by nine').compute()
    81
    >>> wm = WordMath('ninety seven plus two divided by three')
    >>> print(wm)
    ninety seven plus two divided by three
    >>> wm.compute()
    33
    >>> WordMath('two exponent three').compute()
    8
    >>> WordMath('five ni plus').compute()
    Traceback (most recent call last):
    ...
    ValueError

    >>> WordMath('one minus exponent two').compute()
    Traceback (most recent call last):
    ...
    ValueError
    >>> WordMath('nine equals nine').compute()
    Traceback (most recent call last):
     ...
    ValueError
    >>> WordMath('minus abc').compute()
    Traceback (most recent call last):
     ...
    ValueError
    >>> WordMath('twenty eight minus two plus one').compute()
    27
    >>> WordMath('twenty two multiplied by two').compute()
    44
    >>> WordMath('add').compute()
    Traceback (most recent call last):
    ...
    ValueError
    >>> WordMath('six fi six').compute()
    Traceback (most recent call last):
     ...
    ValueError
    >>> WordMath('six add plus nine').compute()
    Traceback (most recent call last):
    ...
    ValueError
    """

    # Declare the strings we recognize as tokens:
    digit_words = 'zero one two three four five six seven eight nine'.split()
    tens_words = 'ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
    decades_words = 'ten twenty thirty forty fifty sixty seventy eighty ninety'.split()

    number_words = digit_words + tens_words + decades_words

    operator_words = {'add': '+', 'plus': '+', 'minus': '-', 'subtract': '-',
                      'times': '*', 'multiplied by': '*', 'divide': '/', 'divided by': '/',
                      'modulo': '%','exponent':'**','power of':'**'}

    def __init__(self, expression=''):
        self.expression = expression
        self.symbols = None
        self.answer = None

    @staticmethod
    def symbolize_one_token(token: str) -> str:
        """Given a single string token, return its symbolic equivalent.

        :param token: string(s), each representing a token
        :return: a symbolic value

        >>> WordMath.symbolize_one_token('five')
        5
        >>> WordMath.symbolize('hundred')
        'hundred'

        """
        if token in WordMath.operator_words.keys():
            return WordMath.operator_words[token]

        elif token in WordMath.digit_words:
            return WordMath.digit_words.index(token)

        elif token in WordMath.tens_words:
            return WordMath.tens_words.index(token) + 10

        elif token=="hundred":
            return token


        elif token in WordMath.decades_words:
            return (WordMath.decades_words.index(token) + 1) * 10


    @staticmethod
    def symbolize(tokens):
        """Given a single string token or a list of tokens, replace them all with 
        their symbolic equivalents.
        
        :param tokens: a string or a list of strings, each representing a token
        :type tokens: list of str|str
        :return: same as tokens except with words replaced as symbols.

        
        >>> WordMath.symbolize("five")
        5
        >>> WordMath.symbolize(['fifteen'])
        [15]
        >>> WordMath.symbolize(['three', 'times', 'five'])
        [3, '*', 5]
        >>> WordMath.symbolize(['add', 'plus', 'minus', 'subtract', 'times', 'divide', 'modulo'])
        ['+', '+', '-', '-', '*', '/', '%']
        >>> WordMath.symbolize(43)
        Traceback (most recent call last):
        ...
        ValueError
        >>> WordMath.symbolize('hundred')
        'hundred'
        >>> WordMath.symbolize('minus')
        '-'

        """
        

        if isinstance(tokens, str):
            return WordMath.symbolize_one_token(tokens)

        elif isinstance(tokens, list):
            token_list = []
            for t in tokens:
                token_list.append(WordMath.symbolize_one_token(t))
        elif tokens == "hundred":
            return "hundred"
        else:
            raise ValueError  # tokens is an unsupported data type
        return token_list

    @staticmethod
    def tokenize(s: str) -> list:
        """Convert a text phrase into a list of strings tokens (words and symbols). A complication
        is that some tokens (e.g. 'divided by') have spaces in them because they're multi-word.

        :param s: string containing a math phrase 
        :return: list of strings (the tokens created)

        >>> WordMath.tokenize('three plus five minus two')
        ['three', 'plus', 'five', 'minus', 'two']
        >>> WordMath.tokenize('six')
        ['six']
        >>> WordMath.tokenize('four times eight')
        ['four', 'times', 'eight']
        >>> WordMath.tokenize('one divide seven')
        ['one', 'divide', 'seven']
        >>> WordMath.tokenize('two divided by nine')
        ['two', 'divided by', 'nine']
        >>> WordMath.tokenize('ten multiplied by zero')
        ['ten', 'multiplied by', 'zero']
        >>> WordMath.tokenize(6)
        Traceback (most recent call last):
        ...
        AttributeError: 'int' object has no attribute 'strip'
        >>> WordMath.tokenize("+- one seven")
        Traceback (most recent call last):
        ...
        ValueError
        """

        tokens = []  # accumulate tokens in a list
        s = s.strip()

        # Scan from left to right in s, matching tokens.
        while len(s):
            t = False

            # get the first word in s:
            result = re.search(r'^(\S+)', s)
            if result:
                fw = result.group(1)
                if fw in WordMath.number_words or fw in WordMath.operator_words or fw=="hundred":
                    t = fw  # found a valid 1-word token.
                else:
                    # Look for a 2-word token instead:
                    result = re.search(r'^(\S+\s+\S+)', s)
                    if result:
                        tw = result.group(1)
                        if tw in WordMath.operator_words:
                            t = tw  # found a valid 2-word token.
            if t:
                # remove that match from the beginning of s:
                s = s.replace(t, '', 1).strip()
                tokens.append(t)
            else:
                print('unrecognized token in: ', s)
                raise ValueError  # raise exception, couldn't recognize the token

        return tokens

    @staticmethod
    def merge_symbols(symbols: list) -> list:
        """Given a list of symbols, look for successive numeric symbols that should be merged.
        
        :param symbols: a list of symbols, such as comes from WordMath.symbolize()
        :return: a new list of symbols, possibly with some merged.
        
        >>> WordMath.merge_symbols([30, 5, '*', 200, 50, 4])
        [35, '*', 254]
        >>> WordMath.merge_symbols([70, 5, '+', 90, 4])
        [75, '+', 94]
        >>> WordMath.merge_symbols([7,'hundred','+',7,4])
        [700, '+', 11]
        """
        new_list = []

        # read through the symbols in order. Successive numbers should be merged.
        last_type = None
        last_item = None
        while len(symbols):
            item = symbols.pop(0)  # pop off FIRST item
            this_type = type(item)
            if this_type == int and last_type == int:
                # merge this item into the previous one (by adding their values):
                new_value = last_item + item
                last_item = new_value
                new_list.pop()  # remove the old last item
                new_list.append(new_value)  # store the new computed value in list

            elif item == "hundred".strip():
                # merge this item into the previous one (by adding their values):
                new_value = last_item * 100
                last_item = new_value
                new_list.pop()  # remove the old last item
                new_list.append(new_value)  # store the new computed value in list
                this_type = int
            else:
                new_list.append(item)  # store the new item
                last_item = item
            # update the other "short-term memory" variable:
            last_type = this_type
        return new_list

    def compute(self):
        """Given the expression stored, parse, compute, and store the result."""

        tokens = WordMath.tokenize(self.expression)
        symbols = WordMath.symbolize(tokens)
        symbols = WordMath.merge_symbols(symbols)
        self.symbols = symbols.copy()  # Copy symbols list so we don't destroy it below.

        # Now go through the sequence of symbols to evaluate them without using
        # the potentially unsafe eval() function.

        current_value = symbols.pop(0)  # start with first number value.
        if not isinstance(current_value, int):
            raise ValueError  # we can't start with an operator in INFIX notation

        operator = None
        for s in symbols:
            if isinstance(s, str):
                if operator is None:
                    # we found an operator
                    operator = s
                else:
                    raise ValueError  # we don't allow two operators in a row
            elif isinstance(s, int):
                current_value = WordMath.calc_operation(current_value, operator, s)
                operator = None
        self.answer = current_value
        return current_value
    @staticmethod
    def calc_operation(v1, operator: str, v2):
        """Given two numeric values and a numeric operator (as a string), compute the
        result and return it.
         >>> WordMath.calc_operation(30, "-", 10)
         20
         >>> WordMath.calc_operation(2, "**", 5)
         32
         >>> WordMath.calc_operation(2, "-*", 5)
         Traceback (most recent call last):
         ...
         ValueError

        :param v1: first numeric value
        :param operator: arithmetic operation to perform (as a string symbol)
        :param v2: second numeric value
        :return: a number
        """
        if operator == '+':
            return v1 + v2
        elif operator == '-':
            return v1 - v2
        elif operator == '*':
            return v1 * v2
        elif operator == '/':
            return v1 // v2
        elif operator == '**':
            return v1 ** v2

        # default fall-through case:
        raise ValueError

    def __repr__(self) -> str:
        """Override __repr__ to give better string representations of the class."""
        if self.answer is not None:
            return str(self.answer)
        else:
            return self.expression


# the conditional below determines whether we are running this "word_math.py" script
# directly vs. it being imported into another script.  If directly, it will compute
# the example below.
if __name__ == '__main__':
    wm = WordMath('nine plus five minus twelve')
    print(wm)
    wm.compute()
    print(wm)
    print(WordMath('two exponent three').compute())
    print(WordMath('two power of three').compute())
    print(WordMath('two hundred eight minus three').compute())
    print(WordMath('ninety nine divide three times eleven').compute())
