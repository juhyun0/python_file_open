#줄 단위로 텍스트를 읽는 readline(), readlines()메소드

with open('movie_quotes.txt','r') as file:
    lines=file.readlines()
    line=''
    for line in lines:
        print(line,end='')