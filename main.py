from parser import Parser
from string_feeder import StringFeeder

def main():
    parser = Parser("( 4 + 5 * 9)"
    print(parser.parse()) # 7

    parser = Parser("3 - 4")
    print(parser.parse()) # -1
    
    parser = Parser("(3 - (2+  2))")
    print(parser.parse()) # -1

    parser = Parser("(3 * (2 + (1-6))))")
    print(parser.parse()) # -9

    
main()