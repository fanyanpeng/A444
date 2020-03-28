import unittest
import sys
from src import word_count


class Testwordcount(unittest.TestCase):
    def setUp(self):
        self.stream_out = MyStream()
        self.stream_in = MyStream()
        self.out_stream = sys.stdout
        self.in_stream = sys.stdin
        sys.stdout = self.stream_out
        sys.stdin = self.stream_in
        pass

    def test_word_count_one(self):
        word_count.wordcount('./files/test1')
        expect = (  'Elizabeth: *******' + '\n'
                  + 'Linda:     *****' + '\n'
                  + 'Barbara:   ****' + '\n'
                  + 'Mary:      ****' + '\n'
                  + 'Patricia:  ****'+'\n')
        result = ''
        for i in range(0, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_word_count_two(self):
        word_count.wordcount('./files/test2')
        expect = (    'Elizabeth: ********' + '\n'
                    + 'Barbara:   *****' + '\n'
                    + 'Mary:      *****' + '\n'
                    + 'Patricia:  *****' + '\n'
                    + 'Linda:     *'+'\n')
        result = ''
        for i in range(0, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_word_count_three(self):
        word_count.wordcount('./files/test3')
        expect = (      'Susan:    ******' + '\n'
                      + 'Jennifer: *****' + '\n'
                      + 'Margaret: ****' + '\n'
                      + 'Maria:    ****' + '\n'
                      + 'Dorothy:  ***'+'\n'
                      + 'Lisa:     **'+'\n')
        result = ''
        for i in range(0, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_word_count_four(self):
        word_count.wordcount('./files/test4')
        expect = (        'Jennifer: *******' + '\n'
						+ 'Lisa:     ****' + '\n'
                        + 'Margaret: ****' + '\n'
                        + 'Susan:    ****' + '\n'
                        + 'Maria:    ***'+'\n'
                        + 'Dorothy:  **'+'\n')
        result = ''
        for i in range(0, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_word_count_five(self):
        word_count.wordcount('./files/test5')
        expect = (          'Lisa:     ******' + '\n'
                          + 'Margaret: ******' + '\n'
                          + 'Susan:    ****' + '\n'
                          + 'Dorothy:  ***' + '\n'
                          + 'Maria:    ***'+'\n'
                          + 'Jennifer: **'+'\n')
        result = ''
        for i in range(0, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def tearDown(self):
        sys.stdout = self.out_stream
        sys.stdin = self.in_stream
        pass

class MyStream:

    def __init__(self):
        self.buff = []
        self.write_count = 0

    def write(self, output_stream):
        self.buff.append(output_stream)

    def readline(self):
        if len(self.buff) > 0:
            cur = self.buff[0]
            del self.buff[0]
            return cur


unittest.main()
