with open('test.txt', 'r') as reader:
    content = reader.readlines()
    reversed_content = reversed(content)

    with open('test.txt', 'w') as writer:
        n = 1
        for line in reversed(content):
            print (f"Write line {n} in progress: {line}")
            n +=1
            writer.write(line)
