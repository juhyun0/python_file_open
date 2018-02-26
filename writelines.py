lines=["we'll find a way we always have - Interstellar\n","I'll find you and I'll kill you - Taken\n", "I'll be back - Terminator 2\n"]


#문자열을담은리스트를 파일에 쓰는 writelines()메소드
with open('movie_quotes.txt','w') as file:
    file.writelines(lines)