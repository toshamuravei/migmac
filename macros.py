import ast
import astpretty



def parse_revision_file(rev_file: str):
    with open(rev_file, 'r') as file:
        raw_file = file.read()
        astpretty.pprint(ast.parse(raw_file))


if __name__ == "__main__":
    MIGRATION_FILE = "example_migro.py"
    parse_revision_file(MIGRATION_FILE)
