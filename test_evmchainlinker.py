# test_evmchainlinker.py
"""
Tests for EvmChainLinker module.
"""

import unittest
from evmchainlinker import EvmChainLinker

class TestEvmChainLinker(unittest.TestCase):
    """Test cases for EvmChainLinker class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EvmChainLinker()
        self.assertIsInstance(instance, EvmChainLinker)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EvmChainLinker()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
