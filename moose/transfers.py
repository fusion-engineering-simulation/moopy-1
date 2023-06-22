#!/usr/env/python3

from enum import IntEnum, auto

class TransferType(IntEnum):
    MultiAppCloneReporterTransfer = auto()
    MultiAppCopyTransfer = auto()
    MultiAppGeometricInterpolationTransfer = auto()
    MultiAppInterpolationTransfer = auto()
    MultiAppMeshFunctionTransfer = auto()
    MultiAppNearestNodeTransfer = auto()
    MultiAppPostprocessorInterpolationTransfer = auto()
    MultiAppPostprocessorToAuxScalarTransfer = auto()
    MultiAppPostprocessorTransfer = auto()
    MultiAppProjectionTransfer = auto()
    MultiAppReporterTransfer = auto()
    MultiAppScalarToAuxScalarTransfer = auto()
    MultiAppShapeEvaluationTransfer = auto()
    MultiAppUserObjectTransfer = auto()
    MultiAppVariableValueSamplePostprocessorTransfer = auto()
    MultiAppVariableValueSampleTransfer = auto()
    MultiAppVectorPostprocessorTransfer = auto()
    MoabMeshTransfer = auto()

class Transfer:
    def __init__(self, name="", **kwargs):
        self.name = name
        self.type = None

        # Set the kwargs into attributes
        for arg in kwargs.keys():
            self.__setattr__(arg, kwargs[arg])

    def __str__(self):
        string = f'[{self.name}]\n'
        string += f'type={self.type.name}\n'

        objects = ["name", "type"]

        for key in self.__dict__.keys():
            if key not in objects:
                data = self.__dict__[key]
                if isinstance(data, list):
                    if hasattr(data[0], '__dict__'):
                        data = [x.name for x in data]
                    else:
                        data = [str(x) for x in data]
                    data = ' '.join(data)
                if hasattr(data, '__dict__'):
                    data = data.name
                string += f'{key}="{data}"\n'

        string += '[]\n'
        return string

class MultiAppNearestNodeTransfer(Transfer):
    def __init__(self, name="", source_variable = "", aux_variable = "", \
        **kwargs):
        super().__init__(name,source_variable,aux_variable,**kwargs)
        self.type = TransferType.MultiAppNearestNodeTransfer

class Transfers:
    def __init__(self):
        self.name = "Transfers"
        self.transfers = {}

    def __str__(self):
        string =  f'[{self.name}]\n'
        for transfer in self.transfers.keys():
            string += self.transfers[transfer].__str__()
        string += '[]\n'
        return string
