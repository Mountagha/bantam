# bantam
** Bantam ** is a tiny little language used to demonstrate Pratt parsing from [this blog of Bob Nystrom](http://journal.stuffwithstuff.com/2011/03/19/pratt-parsers-expression-parsing-made-easy/). I ported the toy language
to Python since the article uses Java and not everyone including me (*sarcasm*) is fan of Java. I tried to make it look as much as possible to the original implementation from [the original repository](https://github.com/munificent/bantam).
Instead of reimplementing a testing function as done in java I used the python [pytest library](https://pytest.org). 
After installing pytest you can run all the tests using the following command. 
` pytest main.py `
