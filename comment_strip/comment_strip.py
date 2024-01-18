def strip_comments(input_text, markers):
    lines = input_text.split('\n')
    for i, line in enumerate(lines):
        min_index = len(line)  
        for marker in markers:
            idx = line.find(marker)
            if idx != -1 and idx < min_index:
                min_index = idx  
        line = line[:min_index].rstrip()  
        lines[i] = line
    return '\n'.join(lines)

input_text = "hello world! #this is comment\nbanana #another comment\ncherry % one more"
markers = ["!", "#", "%"]
result = strip_comments(input_text, markers)
print(result)  
