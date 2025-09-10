#!/usr/bin/env python3


class HelloWorld:
  def hello(self) -> str:
      """Return a friendly greeting."""
      return f"Hello, {self.name}!"
  
  
  def __init__(self, name: str = "World") -> None:
      """Entry point for `python -m helloworld.main`."""
      self.name = name
      print(self.hello())
  
  
if __name__ == "__main__":
  main = HelloWorld()

