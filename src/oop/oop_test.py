import abc

class Effable(object,metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __str__(self):
        raise NotImplementedError('users must define __str__ to use this base class')


class EffableImpl(Effable):
    #pass
    def __str__(self):
        return 'expressable'


impl = EffableImpl()
print(impl)