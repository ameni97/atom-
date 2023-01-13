from typing import Generic, TypeVar


class Meta(type):
  def __getitem__(cls,key):
     return key

T= TypeVar("T",  bound=object)

class A(Generic[T], metaclass=Meta):
  def __init__(self,  T) -> None:
       self.T =T
class B(A[float]):
  pass

#Meta.__getitem__(A,  T)
#a = A(T)
#a.T=""  
b = B(T)
b.T = ""



       # __getitem__(self, k: In) -> Out:
      #return self._dct[k]



  #A[int]


