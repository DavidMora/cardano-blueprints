import unittest
from app.modules.command_protocol import CommandProtocol


class CommandProtocolTestCase(unittest.TestCase):

    def test_ProtocolStartsInInitGrid(self):
        protocol = CommandProtocol()
        self.assertEqual(protocol.current, 'grid_init')

    def test_ProtocolChangesStatusAppropiately(self):
        protocol = CommandProtocol()
        self.assertEqual(protocol.next(), 'rover_init')

        self.assertEqual(protocol.next(), 'rover_move')
        self.assertEqual(protocol.next(), 'rover_move')
        protocol.abortMovement()
        self.assertEqual(protocol.current, 'rover_move_end')
        self.assertEqual(protocol.next(), 'rover_init')
