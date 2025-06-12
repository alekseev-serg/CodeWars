def validate_hello(greetings):
    words = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    return any(greet in greetings.lower() for greet in words)