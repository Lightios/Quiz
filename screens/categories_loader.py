class CategoryQuestion:
    def __init__( self, contents: str, category: str ):
        self.contents = contents
        self.category = category

    def __repr__( self ):
        return f"{self.category}: {self.contents}"


questions = []
categories = []

with open( "categories.txt", encoding="utf-8" ) as file:
    file_content = file.readlines()

for line in file_content:
    line = line.split( ":" )
    category = line[0]
    contents = line[1]

    for content in contents.split( "," ):
        content = content.strip()
        questions.append(CategoryQuestion(content, category))

    categories.append(category)

