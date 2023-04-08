from util import TestCase

class TestCommon(TestCase):
    def test_common_empty(self):
        self.assertEqual(self.submission.common('', ''), '')

    def test_common_single(self):
        self.assertEqual(self.submission.common('a', 'a'), 'a')

    def test_common_consecutive(self):
        self.assertEqual(self.submission.common('abcde', 'bcdef'), 'bcde')

    def test_common_nonconsecutive(self):
        self.assertEqual(self.submission.common('abcde', 'aceg'), 'ace')

    def test_common_many(self):
        cases = [
            ("355827f2d1083fb6", "c921eaa106033a35", "2103"),
            ("b495f40010ada653", "1f37e9239d1e103a", "910a"),
            ("f562d38569be44c3", "4b9cd246c00f5c25", "f525"),
            ("a79e90609ed6935d", "75b492cc19c557d2", "7995d"),
            ("dc1d68a3ba123930", "82f30b742c61b621", "83b12"),
            ("63f78f01657ce85a", "cf8fb858d296a2be", "f8f58a"),
            ("4e15305f0adeed13", "e5b3f6c73656db3a", "e535d3"),
            ("72503e4ec3ab0125", "4efad3b754b121ba", "754b12"),
            ("aea7f63d5e649a81", "0fde4d482cbdc624", "fde64"),
            ("095f8d0344d3a359", "f6e4b1bc5db85fc5", "f4d5"),
            ("dfb086e923c00c2d", "5834cbd6ed8bc454", "d6ec"),
            ("5beafda4e9f76e1a", "f37d85d4de5c67d6", "5d4e76"),
            ("daeef23439647446", "84b18fc903b2e59c", "f29"),
            ("3329d2c20fff4d5b", "c3f6248dcd430525", "32dc25"),
            ("777fef636c0b6762", "8a0654dfdd50c98d", "fc"),
            ("4ac52f89a7a40a4f", "38ca6769b793f09f", "a970f"),
            ("f8675e7a6a8188cb", "2a5d18f4c7a8ff24", "f7a8"),
            ("1e4bd482867f03bb", "9cf5e1a290ffdf88", "1d88"),
            ("35a81cd502f45353", "2c1eccd166a43b83", "1cd433"),
            ("b35e375e222f6344", "29cb2df768f036dd", "b2f63"),
            ("9582a6adb4a9d5f7", "ffe985514d284977", "958497"),
            ("f359c79c556ef971", "bc28beecbb691a86", "cc691"),
            ("4ad16dc4a8bc81e1", "bd3920a71b9a4921", "a141"),
            ("874cd7563d1006d1", "cdfc77b7033505bc", "cd750"),
            ("69226156a167c7b5", "ab8650718b298cec", "651c"),
            ("dc45e4c9daebe522", "4c1b0b91811618a7", "4c9a"),
            ("c800a69628897901", "52787a6dae5918a0", "8a6980"),
            ("f2e6f31c9bf87ecd", "e099ca53adf26214", "f261"),
            ("c116787e90655130", "2b230bb9a128c5eb", "18e"),
            ("ac8b2a756f7ee75d", "cbf117d1e19637f4", "cbf7e7"),
            ("45c7d478f0b4e37e", "4eaf4293ad03067e", "4d037e"),
            ("5cdeab9601e18532", "4fc5406ee8d340de", "5ee83"),
            ("29e221c524bf08d0", "6d8d138a3d041718", "18d0"),
            ("883ce51cfdccc519", "decf05768d384c8e", "ecfdc"),
            ("5080938befa033c0", "06318fc4e9671df2", "038ef"),
            ("76fe7c2a2d6f49c9", "e2ef006e146ad37d", "6e7d"),
            ("9cac5395cf2ae6ea", "94b8aa96ef6a75dd", "9a9f6a"),
            ("f52c022bfe97e0eb", "018a98aa9fe421a3", "0fe"),
            ("b1f9ff5d77b99802", "ff5d866f4414a779", "ff5d779"),
            ("3d398c21ab648f85", "71fec1a0c9f35771", "c1af5"),
            ("6f525a4044530cf3", "3e336f4406d60f7b", "6f400f"),
            ("580c651f3421cc08", "557414df44dd8eb0", "551f40"),
            ("6233bc2ff442a914", "4fe24a8b67933c31", "633c1"),
            ("95285dce3f8c432e", "c3f2aadf439f5b8a", "2d3f8"),
            ("f55e5cd0f3d00eae", "56ca7877f75ab9de", "5cfde"),
            ("19fd5a88e901a590", "3dcf53bac106bcca", "f5a0a"),
            ("46641e31f73198a2", "c603bfbf2f012b5f", "63f12"),
            ("13690812521d3cae", "90737cb295e9ea81", "90251"),
            ("72c2cd81f9ddb79d", "6a5eed10aec7df28", "d17d"),
            ("d0fcdb29431571bd", "4b1df5e78cdbcc1f", "dfcdb1"),
            ("eed0913062ea5b32", "d01b0f4ecba71545", "d010ea5"),
            ("8765176cbc72abd6", "32bd6d58a19a41e3", "651a"),
            ("637d5f60e1a8832b", "9c8d113293e2bb1e", "d132b"),
            ("89ca66986cbfcc06", "ae85dbc84654eb58", "8c86b"),
            ("09b9c74ee4d66123", "636c3bb652d6340b", "bd63"),
            ("21ab0e6897303150", "dfb4d87537e43e8c", "b8733"),
            ("8765672ad2e5d4e3", "b950f2df03a6150c", "52a5"),
            ("aba01ee4037e2449", "19b7d6353153c920", "b132"),
            ("43669a2b33bd8f5f", "e4a6f23e93ed35cc", "46233d5"),
            ("5ad4a3b93a56bdd4", "d1a2966a3be5c9f0", "aa3b9"),
            ("1fdcc151aee1166f", "7622abfd5e8e5c1b", "fd5ee1"),
            ("18a783fd51311fd8", "4fe9ef2f82dfac25", "8a5"),
            ("11e2244b6ea5760a", "6980ec87c4922079", "e227"),
            ("7aa1e033326fd89a", "299a35ecc44cc15a", "a1a"),
            ("a009d3440b5ff9b8", "990c328b950b2994", "090b9"),
            ("0ff141dc1ae7c528", "20cf5676ba43e2ca", "0f4ca"),
            ("275b85129fba8f4b", "a1134c6625d7ae82", "2782"),
            ("196b4d240c0d34d4", "da4609b13927d36f", "192d3"),
            ("e3b01e35956dfbc6", "72f0f297587aafbe", "095fb"),
            ("823fcba162aa46e8", "fea78d9a72b1e1a9", "82b1a"),
            ("168bbea07645191d", "db22cd9a54085d10", "ba051"),
            ("3a5f12ba3ea2661c", "960f7085bd6afb88", "afb"),
            ("fe93d48ff0ed019e", "c7d3f0816080b723", "f800"),
            ("f53a09b4004a36c1", "6f88557163d26089", "f5309"),
            ("36c2fcf1f8f6b2e3", "42a9019fac307d15", "2fc1"),
            ("274d565c05b25d08", "9e46588e160fc7ac", "456c"),
            ("706dded9a15ba8c6", "3b16c2e3c2595d66", "6e956"),
            ("365249815f1e5fbe", "2e6523c9a693a00d", "6529"),
            ("971fc1204b1dde98", "a5128b2a042202c3", "1204"),
            ("b37ee0d219044969", "b6cc123e85c7d471", "b37d1"),
            ("f79ed439b6cbecd5", "e2121d0789bebae0", "ed9bbe"),
            ("68a4f3db60050aa6", "cc8c9ed279aee141", "8a4"),
            ("a5bc0eeb94913e35", "b938c2eab7c87907", "bceb9"),
            ("18efaf1772188f3e", "ef5b6ad4309013d4", "efa13"),
            ("391e12fedf835e70", "df17ca8c417edd77", "11ed7"),
            ("0f61421c1287f2dc", "975da42e93effe4c", "42fc"),
            ("ba8ebfe8a982fb96", "143c088b1111ca95", "8ba9"),
            ("50e5cc194d1f1b99", "a693d740b35d9c2b", "05cb"),
            ("0e9ff5f95f6597a2", "03b27b9f164f8af2", "09fff2"),
            ("ecb7c339c61fe261", "5fa4bb60b9692821", "b9621"),
            ("93f6ac2e8424c3d2", "18672f4143e455cf", "62e4c"),
            ("32148330f093ab7b", "70c2d381a2f97727", "32f97"),
            ("9c689fb1376e10d0", "57393bbcb4f025eb", "9cfb"),
            ("edb190934d71a7ab", "baacb0852756759f", "b077"),
            ("a8d3dc2dd082614d", "46f96ee2822ac7f0", "ac0"),
            ("ff3c4dec59274c4b", "77a448caafbbced3", "44cb"),
            ("8978d8acc393a6b9", "a5a1aaea04456603", "aa6"),
            ("2e6fb3a9ca700835", "a9d76e3d4ed09364", "a9703"),
            ("c4b00d98fdf292e7", "1e4b31d015006dbb", "4b00d"),
            ("a0e10ae5a1421e17", "a18619714c3a2c42", "a1a42"),
        ]
        for a, b, c in cases:
            self.assertEqual(self.submission.common(a, b), c)
