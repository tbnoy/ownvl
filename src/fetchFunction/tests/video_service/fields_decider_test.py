import unittest
from src.fetchFunction.video_service.fields_decider import fieldsDecider

class FieldsDeciderTest(unittest.TestCase):

    def test_get_single(self):
        fieldsIn = ['metadata']
        fieldsOut = fieldsDecider(fieldsIn)
        self.assertEqual(fieldsIn, fieldsOut)

    def test_get_several(self):
        fieldsIn = ['metadata', 'urls', 'rays']
        fieldsOut = fieldsDecider(fieldsIn)
        self.assertEqual(fieldsIn.sort(), fieldsOut.sort())

    def test_get_default(self):
        fieldsIn = ['default']
        expectedDefault = ['urls', 'captions', 'modifiers', 'metadata']
        fieldsOut = fieldsDecider(fieldsIn)
        self.assertEqual(expectedDefault.sort(), fieldsOut.sort())

    def test_get_all(self):
        fieldsIn = ['all']
        expectedAll = [
            'metadata',
            'links',
            'cons',
            'another',
            'urls',
            'modifiers',
            'captions',
            'rays',
            'auth',
            'waivers',
            'thumbnail',
            'audio',
            'ads'
        ]
        fieldsOut = fieldsDecider(fieldsIn)
        self.assertEqual(expectedAll.sort(), fieldsOut.sort())